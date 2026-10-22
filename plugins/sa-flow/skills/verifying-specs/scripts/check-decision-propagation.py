#!/usr/bin/env python3
"""決策傳播比對：decisions.md 的每條 D-xxx 是否已回寫到該出現的規格文件 §D。

用法：
    python3 check-decision-propagation.py <功能目錄> [--json]

規則（任一不成立即列為 CRITICAL，退出碼 1）：
  R1  正文引用了「本階段」D-xxx 的文件，其 §D 決策紀錄必須列出該 D。
      （上游階段的 D 在下游正文被引用是正常的 ref，不算；只抓本階段拍板卻沒進 §D 的）
  R2  decisions.md 中「階段」為 FRD／SAD／BFS／FFS 的 D，必須出現在該階段文件的 §D。
  R3  「階段」為 dev-readiness／verifying-specs／CR 的 D（回寫型決策），
      必須出現在至少一份規格文件的 §D——回寫了正文卻沒列 §D 是最常見的漏。
  R4  decisions.md 的 D 編號必須連號無斷、無重號。

不做的事：不比對決策內容是否被正確落實（那是 verifying-specs 各維度 agent 的工作），
只比對「編號有沒有傳播」。這是機械閘門，不是語意檢查。

緣起：立下「決策回寫的掃描義務」後，某案 verifying-specs --cross
首輪 9 CRITICAL 仍有 7 筆屬「BFS 階段決策未回寫 SAD」——
規則寫在散文裡擋不住人，改成腳本。
"""
import json
import re
import sys
from pathlib import Path

DOC_PATTERNS = {
    "FRD": "*_需求文件.md",
    "SAD": "*_系統分析文件.md",
    "BFS": "*_後端功能規格書.md",
    "FFS": "*_前端功能規格書.md",
}
STAGE_TO_DOC = {
    "frd": "FRD", "requirement": "FRD", "需求": "FRD", "分析": "FRD",
    "sad": "SAD", "system-analysis": "SAD",
    "bfs": "BFS", "specify-backend": "BFS",
    "ffs": "FFS", "specify-frontend": "FFS",
}
WRITEBACK_STAGES = ("dev-readiness", "verifying-specs", "cr", "回寫")
D_RE = re.compile(r"\bD-(\d{3})\b")


def find_doc(feature_dir: Path, pattern: str):
    hits = [p for p in feature_dir.glob(pattern) if "附錄" not in p.name]
    return hits[0] if hits else None


def section_d_ids(text: str) -> set:
    """取 `## D.` 決策紀錄章到下一個 `## ` 之間出現的 D 編號。"""
    m = re.search(r"^## D\.[^\n]*\n(.*?)(?=^## |\Z)", text, re.S | re.M)
    if not m:
        return set()
    return set(D_RE.findall(m.group(1)))


def body_ids(text: str) -> set:
    """§D 章以外的全文（含 §0、附錄引用）出現的 D 編號。"""
    without_d = re.sub(r"^## D\.[^\n]*\n.*?(?=^## |\Z)", "", text, flags=re.S | re.M)
    without_changelog = re.sub(r"<!-- CHANGELOG -->.*", "", without_d, flags=re.S)
    return set(D_RE.findall(without_changelog))


def parse_decisions(text: str):
    """回傳 [(id, stage)]，只取決策表列（`| D-xxx |` 起頭）。"""
    rows = []
    for line in text.splitlines():
        if not line.startswith("| D-"):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) < 7:
            continue
        did = cells[0].replace("D-", "")
        stage = cells[6].lower()  # 表頭：# | 決策 | 選定 | 否決 | 依據 | 拍板 | 階段 | 日期
        rows.append((did, stage))
    return rows


def main(argv):
    if len(argv) < 2:
        print(__doc__)
        return 2
    feature_dir = Path(argv[1]).expanduser().resolve()
    as_json = "--json" in argv
    dec_path = feature_dir / "decisions.md"
    if not dec_path.exists():
        print(f"decisions.md 不存在：{dec_path}")
        return 2

    docs = {}
    for key, pat in DOC_PATTERNS.items():
        p = find_doc(feature_dir, pat)
        if p:
            t = p.read_text(encoding="utf-8")
            docs[key] = {"path": p.name, "sectionD": section_d_ids(t), "body": body_ids(t)}

    decisions = parse_decisions(dec_path.read_text(encoding="utf-8"))
    findings = []

    # R4 連號
    ids = sorted(int(d) for d, _ in decisions)
    if ids:
        missing = sorted(set(range(1, ids[-1] + 1)) - set(ids))
        dups = sorted({i for i in ids if ids.count(i) > 1})
        if missing:
            findings.append({"rule": "R4", "id": None, "doc": "decisions.md",
                             "msg": f"D 編號斷號：{['D-%03d' % i for i in missing]}"})
        if dups:
            findings.append({"rule": "R4", "id": None, "doc": "decisions.md",
                             "msg": f"D 編號重號：{['D-%03d' % i for i in dups]}"})

    # R1 本階段引用必列
    stage_of = {did: STAGE_TO_DOC.get(stage) for did, stage in decisions}
    for key, d in docs.items():
        for did in sorted(d["body"] - d["sectionD"]):
            if stage_of.get(did) == key:
                findings.append({"rule": "R1", "id": f"D-{did}", "doc": d["path"],
                                 "msg": "本階段決策：正文引用但 §D 未列"})

    # R2 / R3 階段傳播
    all_section_ids = set().union(*(d["sectionD"] for d in docs.values())) if docs else set()
    for did, stage in decisions:
        target = STAGE_TO_DOC.get(stage)
        if target:
            if target in docs and did not in docs[target]["sectionD"]:
                findings.append({"rule": "R2", "id": f"D-{did}", "doc": docs[target]["path"],
                                 "msg": f"階段={stage} 但該文件 §D 未列"})
        elif any(s in stage for s in WRITEBACK_STAGES):
            if did not in all_section_ids:
                findings.append({"rule": "R3", "id": f"D-{did}", "doc": "（任一規格文件）",
                                 "msg": f"回寫型決策（階段={stage}）未出現在任何文件 §D"})

    summary = {"feature_dir": str(feature_dir), "docs": {k: v["path"] for k, v in docs.items()},
               "decisions": len(decisions), "critical": len(findings), "findings": findings}
    if as_json:
        print(json.dumps(summary, ensure_ascii=False, indent=2))
    else:
        print(f"決策傳播比對：{feature_dir.name}｜文件 {len(docs)} 份｜決策 {len(decisions)} 條｜CRITICAL {len(findings)}")
        for f in findings:
            print(f"  [{f['rule']}] {f['id'] or '-':<6} {f['doc']}：{f['msg']}")
    return 1 if findings else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
