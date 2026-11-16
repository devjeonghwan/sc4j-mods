# SC4J 모드 목록

[English](README.md) | **한국어**

`mods.json`은 [SC4J](https://github.com/fogofwarlabs/sc4j/blob/main/README.ko.md) 런처가 모드를 설치할 때 보여 주는 모드 목록입니다. 런처는 이 저장소의 `main` 브랜치에서 파일을 읽어 항목마다 이름을 보여 주고, 항목의 저장소에 있는 GitHub 릴리스에서 모드를 설치합니다. 목록에 없는 모드도 런처에 저장소를 입력하면 설치할 수 있습니다.

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
| `mods` | 항목들. 런처가 이 순서로 보여 줌 |
| `name` | 런처에 보이는 이름, 한 줄 |
| `repository` | 모드의 GitHub 저장소, `owner/repo` 형식 |
| `description` | 모드 소개 한 줄 |

모든 필드는 꼭 있어야 하며, 이름이나 저장소가 같은 항목은 둘 수 없습니다(대소문자 구분 없음).

## 모드 추가

1. 모드 저장소는 릴리스마다 GitHub 릴리스 `vX.Y.Z`에 모드 jar `<id>.jar`(`<id>`는 그 `sc4j-mod.json`의 모드 id)와 체크섬 `<id>.jar.sha256`을 올립니다. 체크섬은 `sha256sum` 형식(해시, 공백 두 칸, 파일 이름)입니다.
2. `mods.json`에 항목을 추가하는 풀 리퀘스트를 엽니다.
3. `validate` 검사를 통과해야 합니다. 로컬에서는 `python3 scripts/validate_mods.py`로 실행합니다.

## 라이선스

이 목록은 [Apache License 2.0](LICENSE)으로 배포됩니다. 목록의 각 모드는 자기 저장소의 라이선스를 따릅니다.
