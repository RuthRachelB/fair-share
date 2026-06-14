[![CI](https://github.com/RuthRachelB/fair-share/actions/workflows/ci.yml/badge.svg)](https://github.com/RuthRachelB/fair-share/actions/workflows/ci.yml)

# fair-share

No more awkward math or guessing who owes what. `fair-share` is a straightforward expense splitter for friends – clean, fast, and drama-free.

## 🚀 Quick Start

This project uses `uv` for dependency management. To get everything set up and isolated instantly, just run:

```bash
uv sync
```
## 🛠️ Development & QA
To keep the code sharp, stable, and error-free, use these pre-configured checks:

```bash
# Run tests and check coverage
uv run pytest --cov

# Run type checker
uv run ty check

# Run linter for style and formatting
uv run ruff check .
```