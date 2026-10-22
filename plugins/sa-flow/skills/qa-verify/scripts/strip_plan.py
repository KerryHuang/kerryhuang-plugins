#!/usr/bin/env python3
"""從 plan.yml 抽出 runner 能看的部分：id／欄位（實機名）／步驟／寫入／畫面斷言目標。**不含 預期**——預期是答案，會錨定；
畫面斷言只給 目標（要讀什麼），不給 期望／比對。"""
import sys, yaml
from validate import STALE_NOTE_RE

def strip(plan):
    real = {m["規格"]: m["實機"] for m in plan["meta"]["欄位對照"]}
    cases = []
    for c in plan["cases"]:
        for s in c["步驟"]:
            for key in ("注意", "目標"):
                val = s.get(key)
                if val and STALE_NOTE_RE.search(str(val)):
                    raise SystemExit(f"步驟 {key} 含結論性文字：{c['id']} {val}")
        cases.append({"id": c["id"], "實機欄位": real.get(c["欄位"]), "步驟": c["步驟"], "寫入": c["寫入"],
                      "畫面斷言目標": [a["目標"] for a in c["預期"].get("畫面斷言", [])]})
    return {"meta": {"功能": plan["meta"]["功能"], "功能碼": plan["meta"]["功能碼"]}, "cases": cases}

if __name__ == "__main__":
    plan = yaml.safe_load(open(sys.argv[1], encoding="utf-8"))
    out = strip(plan)
    assert "預期" not in yaml.safe_dump(out, allow_unicode=True), "預期 洩漏"
    with open(sys.argv[2], "w", encoding="utf-8") as f:
        yaml.safe_dump(out, f, allow_unicode=True, sort_keys=False)
    print(f"OK {len(out['cases'])} cases → {sys.argv[2]}")
