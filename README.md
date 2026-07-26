# Pause Empathique — Back-end

> Projet conçu et développé en solo dans le cadre du titre RNCP6 Concepteur Développeur d'Applications.

API REST Django permettant de pratiquer l'auto-empathie de façon guidée, inspirée par la Communication Non Violente (CNV). Les utilisateurs peuvent créer et gérer des pauses empathiques en identifiant leurs sentiments et besoins.

## Stack technique

- **Python 3.13** / **Django 5.2** / **Django REST Framework**
- **PostgreSQL 17**
- **Simple JWT** — authentification par tokens
- **Poetry** — gestion des dépendances
- **Docker & Docker Compose** — environnement de développement
- **pytest + pytest-cov** — tests et couverture
- **Ruff** — linting et formatage
- **GitHub Actions** — CI (lint, tests, audit sécurité)

## Lancer le projet en local

**Prérequis :** Docker, Docker Compose, Poetry

```bash
# 1. Copier et remplir les variables d'environnement
cp .env.example .env

# 2. Démarrer les conteneurs
docker compose up -d

# 3. Appliquer les migrations
docker compose exec web python manage.py migrate

# 4. (Optionnel) Charger les données de base
docker compose exec web python manage.py loaddata pauses/fixtures/feelings.json
docker compose exec web python manage.py loaddata pauses/fixtures/needs.json
```

L'API est accessible sur `http://localhost:8000`.
La documentation interactive (Swagger) est disponible sur `http://localhost:8000/api/docs/`.

## Tests

```bash
# Lancer tous les tests
docker compose exec web pytest

# Avec rapport de couverture
docker compose exec web pytest --cov
```

## Endpoints principaux

| Méthode            | URL                             | Description                 |
| ------------------ | ------------------------------- | --------------------------- |
| `GET`              | `/api/v1/health/`               | Santé de l'API              |
| `POST`             | `/api/v1/users/`                | Inscription                 |
| `POST`             | `/api/v1/auth/token/`           | Connexion (JWT)             |
| `POST`             | `/api/v1/auth/token/refresh/`   | Rafraîchir le token         |
| `POST`             | `/api/v1/auth/token/blacklist/` | Déconnexion                 |
| `GET/PATCH/DELETE` | `/api/v1/users/me/`             | Profil utilisateur          |
| `GET/POST`         | `/api/v1/pauses/`               | Liste et création de pauses |
| `GET`              | `/api/v1/feelings/`             | Liste des sentiments        |
| `GET`              | `/api/v1/needs/`                | Liste des besoins           |

## Front-end

Le front-end Vue.js est dans un repo séparé : [`pause_empathique_front`](../pause_empathique_front/).
