# Recruitment Screening System

A web-based recruitment screening system. Backend built with **Django** and **MySQL**.

## Tech stack

- Python 3.12+
- Django 5.2+/6.x
- MySQL 8.x
- Django REST Framework (for the API layer)
- GitHub Actions (CI/CD)

## Project structure

```
recruitment-screening-system/
├── config/              # Django project settings, URLs, WSGI/ASGI
├── screening/           # Main app (models, views, tests)
├── requirements.txt     # Production dependencies
├── requirements-dev.txt # + linting/testing tools
├── .env.example         # Template for local environment variables
├── pytest.ini           # pytest-django config
├── setup.cfg            # flake8 config
└── .github/workflows/   # CI pipeline
```

## Local setup

### 1. Clone and create a virtual environment

```bash
git clone <your-repo-url>
cd recruitment-screening-system

python3 -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
```

### 2. Install dependencies

```bash
pip install -r requirements-dev.txt   # includes prod deps + lint/test tools
```

### 3. Configure environment variables

```bash
cp .env.example .env
```

Edit `.env` and fill in your local MySQL credentials and a real `DJANGO_SECRET_KEY`.

### 4. Set up MySQL

Create the database (adjust user/password as needed):

```sql
CREATE DATABASE recruitment_screening CHARACTER SET utf8mb4;
```

> Tip: if you don't want to install MySQL locally yet, set `DB_ENGINE=sqlite` in `.env`
> to fall back to SQLite for quick local development.

### 5. Run migrations and start the server

```bash
python manage.py migrate
python manage.py createsuperuser   # optional, for /admin access
python manage.py runserver
```

Visit `http://127.0.0.1:8000/`.

## Running tests

```bash
python manage.py test
# or, with coverage:
coverage run manage.py test && coverage report
```

## Linting & formatting

```bash
flake8 .
black .
isort .
```

## Setting up the GitHub repository

1. Create a new, empty repository on GitHub (do **not** initialize it with a
   README/.gitignore/license there, since this project already has them).
2. From this project folder:

   ```bash
   git init
   git add .
   git commit -m "Initial commit: Django project scaffold"
   git branch -M main
   git remote add origin https://github.com/<your-username>/<your-repo>.git
   git push -u origin main
   ```

3. (Recommended) Create a `develop` branch for ongoing work and protect `main`:

   ```bash
   git checkout -b develop
   git push -u origin develop
   ```

   In GitHub → Settings → Branches, add a branch protection rule for `main`
   requiring the CI checks (`lint`, `test`) to pass before merging.

## CI/CD pipeline

A GitHub Actions workflow is included at `.github/workflows/ci.yml`. It runs
automatically on every push/PR to `main` or `develop` and:

1. **Lint job** — runs `flake8` and `black --check`.
2. **Test job** — spins up a real MySQL 8.4 service container, runs
   migrations, and runs the Django test suite with coverage.

No secrets are required for CI as-is (it uses a throwaway MySQL container).

### Adding deployment later

The workflow has a commented-out placeholder `deploy` job. Once you pick a
hosting target, come back and let me know — I can fill in the deploy steps for:

- **Docker + VPS** (build & push image, SSH deploy)
- **Render / Railway** (deploy via their GitHub integration or CLI)
- **AWS** (ECS, Elastic Beanstalk, or Lambda via SAM/Zappa)

## Environment variables reference

See `.env.example` for the full list. Key ones:

| Variable | Purpose |
|---|---|
| `DJANGO_SECRET_KEY` | Django cryptographic signing key — keep secret |
| `DJANGO_DEBUG` | `True`/`False` |
| `DJANGO_ALLOWED_HOSTS` | Comma-separated list of allowed hostnames |
| `DB_ENGINE` | `mysql` (default) or `sqlite` for quick local dev |
| `DB_NAME`, `DB_USER`, `DB_PASSWORD`, `DB_HOST`, `DB_PORT` | MySQL connection details |
