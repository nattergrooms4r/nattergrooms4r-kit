# nattergrooms4r-kit

Summarize numeric CSV columns (n / min / max / mean).

Small, dependency-free Python utility package generated for day-to-day file chores.
Standard library only — no third-party imports.

## Install

```bash
pip install -e .
```

## Usage

```bash
python -m nattergrooms4r_kit.cli --help
```

```python
from nattergrooms4r_kit.core import Nattergrooms4rTool

tool = Nattergrooms4rTool()
print(tool)
```

## Layout

```
nattergrooms4r_kit/
  __init__.py
  core.py
  cli.py
tests/
  test_core.py
```

## License

MIT © 2026 nattergrooms4r
