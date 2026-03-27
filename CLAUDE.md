# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

---

## Project Overview

**Pause Empathique** is a Django web app for Nonviolent Communication (NVC) self-empathy guidance. It walks users through a 3-step process: Observation → Feelings → Needs. Texts adapt grammatically to the user's declared gender (F/M). The project is also a certification training base (RNCP5-DWWM → RNCP6-CDA).

**Project management** is described and documented in `docs/project_management.md`.

**Session workflow:** At the start of each session, read `docs/sessions/next-session.md` for planned objectives. At the end, update `docs/sessions/session-log.md`, `docs/sessions/next-session.md`and `docs/project_management.md`.

---

## Role of Claude Code in this project

This project is both a production app and a **CDA (RNCP6) certification training ground**. Claude Code must adopt two complementary roles:

### Technical mentor

- Justify every technical decision: why this choice, what alternatives exist, what trade-offs are involved.
- Provide theoretical background on concepts being implemented (architecture patterns, security, etc.).
- Always reference official documentation (Django, DRF, Vue.js, TypeScript…) rather than personal opinion.
- Ask comprehension questions regularly — before moving to the next step, verify understanding.
- Proactively flag antipatterns and technical debt.

### Technical project manager

- Keep track of the roadmap in `docs/project_management.md` and session files (`docs/sessions/`).
- Recall priorities and flag when a decision deviates from the plan.
- Stay agile: adjust the plan when needed, but maintain the overall direction.
- End of session: propose a summary (done / remaining / blockers) and update the session docs.

---

## Development Commands

### Python environment (Poetry)

```bash
poetry install          # Install dependencies
poetry shell            # Activate virtualenv
```

### Local development (Docker)

```bash
docker compose up       # Start DB (postgres:17) + Django on localhost:8000
docker compose up -d    # Detached mode
docker compose down     # Stop services
```

### Django management

```bash
python manage.py migrate
python manage.py collectstatic
python manage.py runserver 0.0.0.0:8000
python manage.py loaddata pauses/fixtures/feelings.json pauses/fixtures/needs.json
```

### Frontend CSS (Tailwind)

```bash
npm install
npm run dev:css    # Watch mode during development
npm run build:css  # One-time production build
```

### Testing

```bash
pytest                                                    # Run all tests
pytest tests/test_models.py                               # Single test file
pytest -k "test_name"                                     # Single test by name
pytest --cov=pause_empathique --cov=pauses --cov=users --cov-report=term-missing  # With coverage
```

### Linting & formatting

```bash
ruff check .        # Lint
ruff check . --fix  # Lint + auto-fix
ruff format .       # Format (line length 88)
```

### CI (GitHub Actions — `.github/workflows/ci.yml`)

Triggered on push to `main` and `dev`: Ruff lint → pip-audit security scan → pytest with coverage.

---

## Architecture

### Stack

- **Backend:** Python 3.13, Django 5.2, PostgreSQL 17 (psycopg v3), Gunicorn, WhiteNoise
- **Frontend:** Django templates (server-side rendered), Tailwind CSS 4.1 (compiled via npm), vanilla JS
- **API layer (emerging):** Django REST Framework, drf-spectacular (OpenAPI), simplejwt
- **Dev tooling:** Poetry, Docker Compose, Ruff, pre-commit, django-browser-reload

**Planned evolution:** Decouple to DRF API + Vue.js 3 + TypeScript SPA.

### App structure

```
pause_empathique/      # Django project config
│   settings.py        # ENV-based config (python-decouple)
│   urls.py            # Root router: includes pauses/, users/, api/v1/, api/docs/
│   api/               # REST endpoints (currently: HealthCheckView only)
pauses/                # Core domain
│   models.py          # Pause, Feeling (12 families), Need (7 families)
│   views.py           # Mix of CBV (CreateView, ListView…) and FBV
│   fixtures/          # feelings.json, needs.json — load on first deploy
│   templatetags/      # Custom template filters
users/                 # Auth & profiles
│   models.py          # Custom AbstractBaseUser (email login, gender field)
│   managers.py        # UserManager
templates/             # base.html + partials per app
static/                # css/input.css (Tailwind source), js/, icons/ (SVG)
staticfiles/           # collectstatic output (served by WhiteNoise)
tests/                 # Centralized: test_models.py, test_views.py
docs/                  # sessions/, project-management.md, architecture
```

### Data model essentials

- **User:** email as `USERNAME_FIELD`, `gender` (F/M) drives all gender-aware text rendering.
- **Pause:** FK to User, auto-generated title ("Pause du JJ Mois AAAA"), M2M to Feeling and Need.
- **Feeling:** `feeling_family` (12 codes: AF/SE/JO/IN/EN/PE/CO/TR/CF/FA/SI/TE), `feminine_name`, `masculine_name`. Use `feeling.get_label(user)` to get the correct gendered label.
- **Need:** same structure as Feeling, 7 family codes.

### Environment & deployment

| Environment | Branch | Platform | Domain                      |
| ----------- | ------ | -------- | --------------------------- |
| Production  | main   | Railway  | pause-empathique.fr         |
| Staging     | dev    | Railway  | staging.pause-empathique.fr |
| Local       | —      | Docker   | localhost:8000              |

Key env vars: `ENV_STATE` (`production`/`staging`/`development`), `SECRET_KEY`, `DEBUG`, `DATABASE_URL`, `ADMIN_URL` (custom admin path for security).

Settings branch on `ENV_STATE`: production/staging share most config (DEBUG=False, WhiteNoise, etc.); development enables `django-browser-reload` and `DEBUG=True`.

### Conventional commits

This project uses `conventional-pre-commit` hooks. Commit messages must follow Conventional Commits format (e.g., `feat:`, `fix:`, `refactor:`, `test:`).
