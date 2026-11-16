# SC4J mod catalog

**English** | [한국어](README.ko.md)

`mods.json` is the list of mods that the [SC4J](https://github.com/fogofwarlabs/sc4j) launcher offers when you install a mod. The launcher reads it from the `main` branch of this repository and shows each entry by its name; it installs the mod from the GitHub releases of the entry's repository. A mod that is not listed can still be installed by typing its repository in the launcher.

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
| `mods` | the entries, in the order the launcher lists them |
| `name` | the name the launcher shows, one line |
| `repository` | the GitHub repository of the mod as `owner/repo` |
| `description` | one line about the mod |

Every field is required; no two entries share a name or a repository (without case).

## Adding a mod

1. The mod's repository publishes each release as a GitHub release `vX.Y.Z` with the mod jar `<id>.jar` (`<id>` is the mod id of its `sc4j-mod.json`) and its checksum `<id>.jar.sha256` in the `sha256sum` format (the hash, two spaces, the file name).
2. Open a pull request that adds the entry to `mods.json`.
3. The check `validate` must pass; run it locally with `python3 scripts/validate_mods.py`.

## Licence

The catalog is licensed under the [Apache License 2.0](LICENSE). Each listed mod has its own licence in its repository.
