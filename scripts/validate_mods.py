"""Checks the mod catalog mods.json: JSON, format 1, the fields of every entry, the repository pattern and duplicates."""

import json
import re
import sys

CATALOG_FORMAT = 1
CATALOG_KEYS = {"format", "mods"}
ENTRY_KEYS = {"name", "repository", "description"}
# A GitHub owner (letters, digits, inner hyphens, at most 39 characters) and a repository name.
REPOSITORY_PATTERN = re.compile(r"^[A-Za-z0-9](?:[A-Za-z0-9]|-(?=[A-Za-z0-9])){0,38}/(?!\.{1,2}$)[A-Za-z0-9._-]{1,100}$")


def reject_duplicate_keys(pairs):
    keys = [key for key, _ in pairs]
    duplicates = sorted({key for key in keys if keys.count(key) > 1})
    if duplicates:
        raise ValueError("duplicate keys " + ", ".join(duplicates))
    return dict(pairs)


def check_text(problems, where, entry, key):
    value = entry.get(key)
    if not isinstance(value, str) or not value.strip():
        problems.append(f"{where}: {key} must be a non-empty string")
        return None
    if value != value.strip() or "\n" in value or "\r" in value:
        problems.append(f"{where}: {key} must be one line without leading or trailing spaces")
    return value


def check_catalog(catalog):
    problems = []
    if not isinstance(catalog, dict):
        return ["the catalog must be a JSON object"]
    for key in sorted(set(catalog) - CATALOG_KEYS):
        problems.append(f"unknown key {key}")
    if type(catalog.get("format")) is not int or catalog["format"] != CATALOG_FORMAT:
        problems.append(f"format must be {CATALOG_FORMAT}")
    mods = catalog.get("mods")
    if not isinstance(mods, list):
        problems.append("mods must be a list")
        return problems
    names = {}
    repositories = {}
    for index, entry in enumerate(mods):
        where = f"mods[{index}]"
        if not isinstance(entry, dict):
            problems.append(f"{where}: an entry must be a JSON object")
            continue
        for key in sorted(set(entry) - ENTRY_KEYS):
            problems.append(f"{where}: unknown key {key}")
        name = check_text(problems, where, entry, "name")
        repository = check_text(problems, where, entry, "repository")
        check_text(problems, where, entry, "description")
        if repository is not None and not REPOSITORY_PATTERN.match(repository):
            problems.append(f"{where}: repository {repository} is not owner/repo")
        # Names and repositories compare without case, as GitHub names do.
        if name is not None:
            other = names.setdefault(name.casefold(), index)
            if other != index:
                problems.append(f"{where}: the name {name} is also the name of mods[{other}]")
        if repository is not None:
            other = repositories.setdefault(repository.casefold(), index)
            if other != index:
                problems.append(f"{where}: the repository {repository} is also the repository of mods[{other}]")
    return problems


def main():
    path = sys.argv[1] if len(sys.argv) > 1 else "mods.json"
    try:
        with open(path, encoding="utf-8") as file:
            catalog = json.load(file, object_pairs_hook=reject_duplicate_keys)
    except (OSError, ValueError) as error:
        print(f"{path}: {error}", file=sys.stderr)
        return 1
    problems = check_catalog(catalog)
    for problem in problems:
        print(f"{path}: {problem}", file=sys.stderr)
    if problems:
        return 1
    print(f"{path}: {len(catalog['mods'])} mods, no problems")
    return 0


if __name__ == "__main__":
    sys.exit(main())
