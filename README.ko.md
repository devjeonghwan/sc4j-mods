# SC4J 모드 목록

[English](README.md) | **한국어**

`mods.json`은 [SC4J](https://github.com/fogofwarlabs/sc4j/blob/main/README.ko.md) 런처가 설치용으로 보여 주는 모드 목록입니다. 런처는 `main`에서 이 파일을 읽고, 모드를 그 저장소의 GitHub 릴리즈에서 설치합니다. 목록에 없는 모드는 저장소를 입력해 설치할 수 있습니다.

## 형식

```json
{
  "format": 1,
  "mods": [
    {"name": "SC:R", "repository": "fogofwarlabs/sc4j-scr", "description": "..."}
  ]
}
```

| 필드 | 값 |
|---|---|
| `format` | `1` |
| `mods` | 항목, 런처에 보이는 순서 |
| `name` | 보이는 이름, 한 줄 |
| `repository` | GitHub `owner/repo` |
| `description` | 한 줄 |

모든 필드가 필요합니다. 이름과 저장소는 대소문자 구분 없이 중복될 수 없습니다.

## 모드 추가

1. 모드의 릴리즈마다 `<id>.jar`(`<id>`는 그 `sc4j-mod.json`의 id)와 `sha256sum` 형식의 `<id>.jar.sha256`이 있는 GitHub 릴리즈 `vX.Y.Z`가 있어야 합니다.
2. 항목을 추가하는 풀 리퀘스트를 엽니다.
3. `validate` 검사를 통과해야 합니다: `python3 scripts/validate_mods.py`.

## 라이선스

[Apache License 2.0](LICENSE). 목록의 각 모드는 자기 라이선스를 따릅니다.
