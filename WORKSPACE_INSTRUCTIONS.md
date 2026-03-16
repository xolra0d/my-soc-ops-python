# Workspace Instructions

**Soc Ops** — A social bingo game for in-person mixers. Python + FastAPI + Jinja2.

## ✅ Mandatory Development Checklist

Before committing, **always run**:
```bash
uv run ruff check . --fix    # Lint & auto-fix
uv run ruff format .         # Format code
uv run pytest                # Run all tests
```

---

## 📋 Quick Start

| Task | Command |
|------|---------|
| **Setup** | `uv sync` |
| **Run** | `uv run uvicorn app.main:app --reload` |
| **Test** | `uv run pytest` |
| **Lint** | `uv run ruff check .` |
| **Format** | `uv run ruff format .` |

**Prerequisites**: Python 3.13+, [uv](https://docs.astral.sh/uv/)

---

## 📁 Key Files

| File | Purpose |
|------|---------|
| `app/main.py` | FastAPI routes & app setup |
| `app/game_logic.py` | Bingo validation, card generation |
| `app/game_service.py` | Game state management |
| `app/models.py` | Pydantic data models |
| `app/data.py` | Questions & fixtures |
| `app/templates/` | Jinja2 HTML |
| `app/static/` | CSS, JavaScript, images |
| `tests/` | Pytest test suite |

---

## 🎨 Styling

Custom CSS utilities in `app/static/css/app.css` (Tailwind-like approach):
- **Layout**: `.flex`, `.flex-col`, `.grid`, `.items-center`, `.justify-center`
- **Spacing**: `.p-1` to `.p-6`, `.mb-2` to `.mb-8`, `.gap-1`
- **Colors**: `.bg-white`, `.bg-gray-50`, `.text-gray-500`, `.text-green-600`
- **Typography**: `.text-xs` to `.text-5xl`, `.font-semibold`, `.font-bold`
- **Borders**: `.rounded`, `.shadow-sm`, `.shadow-xl`
- **Animation**: `.transition-all`, `.duration-150`

All HTML uses Jinja2 templates in `app/templates/`.

---

## 🧪 Testing & Code Quality

```bash
# Run all tests
uv run pytest

# Verbose output
uv run pytest -v

# Auto-fix linting issues
uv run ruff check . --fix

# Format code
uv run ruff format .
```

**Code Style**: Python 3.13, 88-char line length, rules: E, F, I, N, W
