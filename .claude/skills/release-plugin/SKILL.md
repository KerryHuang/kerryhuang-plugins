---
name: release-plugin
description: Use when bumping a plugin version, releasing a new plugin version, or syncing version numbers across plugin.json, marketplace.json, and README.md.
---

# Release Plugin

Sync version numbers across all three locations when releasing a plugin update.

## Input

```
$ARGUMENTS
```

- `release-plugin <name> <bump>` — release with specified bump (patch/minor/major)
- `release-plugin <name>` — prompt for bump type
- `release-plugin` — prompt for plugin and bump type

## Steps

### 1. Select Plugin

If not specified, list available plugins from `.claude-plugin/marketplace.json` and ask user to choose.

### 2. Read Current Version

Read `plugins/<name>/.claude-plugin/plugin.json` → extract current `version`.

### 3. Calculate New Version

| Bump | Example |
|------|---------|
| patch | 1.2.0 → 1.2.1 (bug fixes) |
| minor | 1.2.0 → 1.3.0 (new skills/features) |
| major | 1.2.0 → 2.0.0 (breaking changes) |

Confirm with user: "版本 `<current>` → `<new>`，確認？"

### 4. Update All Three Locations

1. `plugins/<name>/.claude-plugin/plugin.json` → update `version`
2. `.claude-plugin/marketplace.json` → update matching plugin `version`
3. `README.md` → update version in plugin table row

### 5. Verify Consistency

Read all three files and confirm versions match.

- [ ] plugin.json version = new version
- [ ] marketplace.json version = new version
- [ ] README.md table version = new version

### 6. Summary

List all files modified and the version change:

```
<name>: <old> → <new>
  - plugins/<name>/.claude-plugin/plugin.json
  - .claude-plugin/marketplace.json
  - README.md
```
