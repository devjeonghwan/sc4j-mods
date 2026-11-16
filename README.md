# SC4J mod catalog

**English** | [한국어](README.ko.md)

`mods.json` lists the mods the [SC4J](https://github.com/fogofwarlabs/sc4j) launcher offers for install. The launcher reads it from `main` and installs a mod from the GitHub releases of its repository. An unlisted mod can be installed by typing its repository.

## Format

```json
{
  "format": 1,
  "mods": [
    {"name": "SC:R", "repository": "fogofwarlabs/sc4j-scr", "description": "..."}
  ]
}
```

| Field | Value |
|---|---|
| `format` | `1` |
| `mods` | entries, in launcher order |
| `name` | name shown, one line |
| `repository` | GitHub `owner/repo` |
| `description` | one line |

All fields are required. Names and repositories are unique, ignoring case.

## Adding a mod

1. Each release of the mod is a GitHub release `vX.Y.Z` with `<id>.jar` (`<id>` from its `sc4j-mod.json`) and `<id>.jar.sha256` in `sha256sum` format.
2. Open a pull request that adds the entry.
3. The `validate` check must pass: `python3 scripts/validate_mods.py`.

## Licence

[Apache License 2.0](LICENSE). Each listed mod has its own licence.
