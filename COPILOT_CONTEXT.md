# COPILOT_CONTEXT — Pause Empathique

> Fichier de contexte pour GitHub Copilot.
> Mis à jour au fur et à mesure de l'évolution du projet.

---

## 1. Présentation du projet

**Pause Empathique** est une application web d'accompagnement à la Communication NonViolente (CNV).
Elle guide l'utilisateur·ice à travers une "pause empathique" en 3 étapes :

1. **Observation** — vider son sac / décrire la situation
2. **Ressentis** — choisir ses émotions parmi une liste classée par familles
3. **Besoins** — identifier ses besoins sous-jacents

L'application s'adresse à des personnes en apprentissage de la CNV. Les textes s'adaptent au genre grammatical choisi par l'utilisateur·ice (féminin / masculin).

---

## 2. Contexte de formation

| Titre                                       | Statut                                  |
| ------------------------------------------- | --------------------------------------- |
| DWWM (Développeur Web et Web Mobile)        | ✅ Validé — ce projet en est le support |
| CDA (Concepteur Développeur d'Applications) | 🔄 En cours de préparation              |

Ce projet est la base sur laquelle sera préparé le titre CDA. Les évolutions techniques listées ci-dessous sont réalisées dans ce cadre d'apprentissage. **Être pédagogue, expliciter les choix techniques et citer les documentations officielles est une priorité.**

---

## 3. Stack technique actuelle

### Back-end

| Technologie          | Version | Rôle                                                                       |
| -------------------- | ------- | -------------------------------------------------------------------------- |
| Python               | 3.13    | Langage principal                                                          |
| Django               | 5.2.5   | Framework full stack                                                       |
| PostgreSQL           | 17      | Base de données                                                            |
| psycopg              | 3       | Driver PostgreSQL (nouvelle API async-compatible)                          |
| dj-database-url      | 3       | Parse l'URL de BDD depuis les variables d'env                              |
| python-decouple      | 3.8     | Gestion des variables d'environnement (.env)                               |
| gunicorn             | 23      | Serveur WSGI de production                                                 |
| whitenoise[brotli]   | 6       | Servir les fichiers statiques en production (+ compression Brotli)         |
| django-widget-tweaks | 1.5     | Ajouter des attributs HTML aux champs de formulaires dans les templates    |
| user-agents          | 2.2     | Détecter le type d'appareil (mobile/desktop) pour adapter les redirections |

### Front-end (actuel — full stack Django)

| Technologie        | Rôle                                               |
| ------------------ | -------------------------------------------------- |
| Tailwind CSS       | Framework CSS utilitaire (compilé via npm)         |
| Templates Django   | Rendu HTML côté serveur                            |
| JavaScript vanilla | Interactions légères (toggle, password visibility) |

### Dev / Tooling

| Outil                   | Rôle                                        |
| ----------------------- | ------------------------------------------- |
| Poetry                  | Gestionnaire de dépendances Python          |
| Docker + docker-compose | Environnement de développement local        |
| Black                   | Formateur de code Python (ligne = 88 chars) |
| npm                     | Compilation Tailwind (`tailwind watch`)     |
| django-browser-reload   | Hot reload en développement                 |
| GitHub Actions          | CI : lint (Black) + tests Django            |

---

## 4. Architecture du projet (back — repo actuel)

```
pause_empathique/          ← Racine du repo back (deviendra API)
├── .github/workflows/
│   └── ci.yml             ← CI : Black check + Django tests (branches main & dev)
├── pause_empathique/      ← Config Django (settings, urls, wsgi, asgi)
├── pauses/                ← App Django "pauses"
│   ├── models.py          ← Pause, Feeling (FeelingFamily), Need
│   ├── views.py           ← Vues class-based + function-based
│   ├── urls.py            ← Routes pauses
│   ├── fixtures/          ← feelings.json, needs.json (données initiales)
│   └── templatetags/
├── users/                 ← App Django "users"
│   ├── models.py          ← Modèle User personnalisé (email = login, genre)
│   ├── views.py           ← Login, register, profil, suppression
│   ├── forms.py           ← Formulaires d'inscription / mise à jour profil
│   ├── managers.py        ← UserManager personnalisé
│   └── urls.py
├── templates/             ← Templates HTML (base, header, partials, pauses/, users/)
├── static/                ← Sources statiques (css/input.css, js/, icons/)
├── staticfiles/           ← Sortie whitenoise (collectstatic)
├── tests/                 ← Tests centralisés (test_models.py, test_views.py)
├── docker-compose.yml     ← Services : db (postgres:17) + web
├── Dockerfile
├── pyproject.toml         ← Dépendances Poetry
└── manage.py
```

---

## 5. Modèles de données

### `User` (users.User — modèle personnalisé)

```
email         → champ d'authentification (USERNAME_FIELD)
firstname     → prénom
gender        → F (Féminin) | M (Masculin) — adapte les libellés des émotions/besoins
is_active, is_staff, created_at, updated_at
```

### `Pause`

```
user          → ForeignKey → User
title         → auto-généré "Pause du JJ Mois AAAA"
observation   → TextField
empty_your_bag → TextField (optionnel)
feelings      → ManyToMany → Feeling
needs         → ManyToMany → Need
created_at, updated_at
```

### `Feeling`

```
feeling_family → AF/SE/JO/IN/EN/PE/CO/TR/CF/FA/SI/TE (12 familles)
feminine_name  → libellé féminin
masculine_name → libellé masculin
```

`get_label(user)` retourne le libellé selon le genre de l'utilisateur·ice.

### `Need`

(structure similaire à Feeling — données chargées via fixture `needs.json`)

---

## 6. Routes actuelles

| URL                                   | Vue                    | Nom               |
| ------------------------------------- | ---------------------- | ----------------- |
| `/`                                   | CustomLoginView        | `home`            |
| `/users/login/`                       | CustomLoginView        | `login`           |
| `/users/logout/`                      | LogoutView             | `logout`          |
| `/users/register/`                    | register               | `register`        |
| `/users/profile/`                     | UserProfileView        | `profile`         |
| `/users/profile/update/`              | UserProfileUpdateView  | `update_profile`  |
| `/users/profile/delete/`              | UserProfileDeleteView  | `delete_profile`  |
| `/pauses/dashboard/`                  | dashboard              | `dashboard`       |
| `/pauses/observation/`                | PauseCreateView        | `observation`     |
| `/pauses/<pk>/feelings/`              | PauseFeelingCreateView | `feelings`        |
| `/pauses/<pk>/needs/`                 | PauseNeedCreateView    | `needs`           |
| `/pauses/diary/`                      | PauseListView          | `diary`           |
| `/pauses/diary/<pk>/`                 | PauseDetailView        | `pause_details`   |
| `/pauses/diary/<pk>/delete/`          | delete_pause           | `delete_pause`    |
| `/pauses/diary/<pk>/update/`          | PauseUpdateView        | `update_pause`    |
| `/pauses/diary/<pk>/feelings/update/` | PauseFeelingUpdateView | `update_feelings` |
| `/pauses/diary/<pk>/needs/update/`    | PauseNeedUpdateView    | `update_needs`    |

---

## 7. Déploiement

| Environnement     | Plateforme       | Branche | Domaine                     |
| ----------------- | ---------------- | ------- | --------------------------- |
| Production        | Railway          | `main`  | pause-empathique.fr         |
| Staging (à créer) | Railway          | `dev`   | staging.pause-empathique.fr |
| Local             | Docker (compose) | —       | localhost:8000              |

**Variables d'environnement clés :**

```
ENV_STATE       → "production" | "staging" | "development"
SECRET_KEY      → clé secrète Django (différente par env)
DEBUG           → False en production et staging, True en dev
DATABASE_URL    → URL de connexion PostgreSQL
ADMIN_URL       → URL personnalisée de l'admin (sécurité)
CORS_ALLOWED_ORIGINS → à ajouter lors de la phase API (domaine front)
```

**CI/CD (GitHub Actions) :**

- Déclenché sur push/PR vers `main` et `dev`
- Job `lint` : Black formatting check (via Docker)
- Job `test` : Django test runner (via Docker + Postgres)

---

## 8. Feuille de route — Évolutions CDA

### Phase 0 — Staging

- [ ] Créer un environnement Railway pour la branche `dev`
- [ ] Configurer `ENV_STATE=staging` avec ses propres variables
- [ ] Valider le pipeline CI/CD sur staging avant tout merge en `main`

### Phase 1 — Nouvelle charte graphique (Django full stack)

- [ ] Appliquer la nouvelle charte au projet Django existant (Tailwind)
- [ ] Conserver les templates Django pendant la migration progressive

### Phase 2 — Migration progressive vers API REST (DRF)

- [ ] Installer Django Rest Framework dans le projet back
- [ ] Vue par vue : créer l'endpoint API correspondant
- [ ] Stratégie : coexistence temporaire templates Django + API (même projet)
- [ ] À terme : le projet back ne sert plus que l'API (plus de templates)

### Phase 3 — Frontend Vue.js + TypeScript

- [ ] Créer un repo séparé pour le front
- [ ] Vue.js 3 (Composition API) + TypeScript + Vite
- [ ] Vue par vue : migrer depuis le template Django vers le composant Vue
- [ ] Authentification : JWT avec `djangorestframework-simplejwt` ✅ décidé

### Principes directeurs

- Production continue : jamais de coupure, toujours une version stable sur `main`
- Bonnes pratiques : tests, CI/CD, revue de code, gitflow (main / dev / feature branches)
- Documentation officielle comme référence : Django, DRF, Vue.js, TypeScript
- Code sécurisé : CORS configuré, JWT, validation des données côté API

---

## 9. Choix technologiques

### CSS : Tailwind CSS ✅ décidé

Tailwind CSS est conservé pour toute la durée du projet (Django full stack et Vue.js front).

**Approche pour la charte graphique :**
Avec Tailwind v4, la charte s'applique via des variables CSS natives dans le fichier `input.css` :

```css
/* static/css/input.css */
@import "tailwindcss";

@theme {
  --color-primary: #...;
  --color-accent: #...;
  --font-sans: "NomDeLaPolice", sans-serif;
}
```

Ces variables deviennent ensuite utilisables comme classes utilitaires (`bg-primary`, `text-accent`)
ET comme variables CSS standard (`var(--color-primary)`) — le meilleur des deux mondes.

### Authentification API : JWT ✅ décidé

Librairie retenue : **`djangorestframework-simplejwt`** ([doc officielle](https://django-rest-framework-simplejwt.readthedocs.io/))

**Pourquoi JWT pour une SPA Vue.js :**
Django gère nativement l'authentification par **sessions** (un cookie de session est envoyé au navigateur, l'état est stocké côté serveur en base). C'est parfait pour un rendu côté serveur (Django templates).

Pour une SPA (Single Page Application), le front et le back sont sur des domaines différents. Les sessions deviennent complexes à gérer cross-domain. JWT (JSON Web Token) est l'alternative standard :

|              | Sessions Django                | JWT (simplejwt)                      |
| ------------ | ------------------------------ | ------------------------------------ |
| État stocké  | Côté serveur (BDD)             | Côté client (token)                  |
| Cross-domain | Complexe (cookies CSRF)        | Natif (header Authorization)         |
| Adapté pour  | Templates Django               | SPA / API consommée par front JS     |
| Révocation   | Facile (supprimer la session)  | Nécessite une blacklist ou TTL court |
| Scalabilité  | Dépend du stockage de sessions | Stateless, très scalable             |

**Fonctionnement :** Le front envoie email+password → le back retourne un `access_token` (durée courte, ex: 15 min) et un `refresh_token` (durée longue, ex: 7 jours). Le front stocke les tokens (à discuter : `localStorage` vs `httpOnly cookie`), et envoie l'`access_token` dans le header `Authorization: Bearer <token>` à chaque requête API.

**Les autres options qui existaient :**

- **Sessions Django** — rejeté : inadapté cross-domain SPA
- **django-allauth + dj-rest-auth** — surpuissant, gère OAuth/social login, mais complexité inutile pour ce projet
- **Token simple (DRF TokenAuthentication)** — un seul token permanent, pas de refresh, moins sécurisé que JWT
- **Cookie-based JWT** — JWT stocké dans un `httpOnly cookie` (sécurisé contre XSS, problèmes CSRF à gérer) — option à reconsidérer si sécurité renforcée nécessaire

---

## 10. Informations complémentaires à collecter

- [ ] Détails de la nouvelle charte graphique (couleurs, typographies, composants)
- [ ] URL du futur repo front Vue.js
- [x] ~~URL de staging souhaitée~~ → `staging.pause-empathique.fr`
- [x] ~~Choix du mécanisme d'authentification~~ → JWT avec `djangorestframework-simplejwt`
- [ ] Contraintes de délai pour la formation CDA

---

## 11. CI/CD — État actuel et évolutions recommandées

### État actuel

```yaml
# .github/workflows/ci.yml
jobs:
  lint: → Black formatting check (via Docker)
  test: → Django test runner (via Docker + Postgres)
```

**Problème principal :** tout passe par Docker. Construire l'image à chaque run de CI prend du temps (souvent 2-3 min juste pour le build). Pour du lint, c'est du gaspillage.

---

### Recommandation : migrer de Black vers Ruff ✅

**Ruff** ([doc officielle](https://docs.astral.sh/ruff/)) est un linter + formateur Python écrit en Rust.
Il est **10 à 100× plus rapide** que Black + flake8 et peut les remplacer tous les deux.

| Outil       | Ce que Ruff remplace                             |
| ----------- | ------------------------------------------------ |
| `black`     | `ruff format`                                    |
| `flake8`    | `ruff check`                                     |
| `isort`     | `ruff check --select I` (règles isort intégrées) |
| `pyupgrade` | `ruff check --select UP`                         |

**Migration depuis Black :** Ruff format est compatible Black par défaut (`line-length = 88`). Le passage est transparent.

Configuration dans `pyproject.toml` :

```toml
[tool.ruff]
line-length = 88
target-version = "py313"
exclude = ["migrations"]

[tool.ruff.lint]
select = [
    "E",   # pycodestyle errors
    "W",   # pycodestyle warnings
    "F",   # pyflakes
    "I",   # isort
    "UP",  # pyupgrade
    "B",   # flake8-bugbear (bugs potentiels)
    "S",   # flake8-bandit (sécurité)
]
ignore = ["S101"]  # autorise les assert (utiles dans les tests)
```

---

### Améliorations CI recommandées

#### 1. Séparer lint du Docker (quick win majeur)

Le job `lint` n'a pas besoin de Docker ni de Postgres. Avec `actions/setup-python` + cache pip, il tourne en ~20 secondes.

#### 2. Ajouter la couverture de tests (coverage)

Ajouter `pytest` + `pytest-django` + `pytest-cov` pour mesurer la couverture et établir un seuil minimum.

```bash
pytest --cov=. --cov-fail-under=80
```

**Pourquoi pytest plutôt que `manage.py test` ?**

- Meilleure lisibilité des erreurs (diff coloré, rapport détaillé)
- Plugins riches : `pytest-django`, `pytest-cov`, `factory-boy`...
- Fixtures pytest plus puissantes que les fixtures Django dans les tests

#### 3. Audit de sécurité des dépendances

`pip-audit` ([doc](https://pypi.org/project/pip-audit/)) scanne les dépendances contre les CVE connues.
Un job dédié, rapide (~30s), sans Docker.

```bash
pip-audit
```

#### 4. Pre-commit hooks (local)

`pre-commit` ([doc](https://pre-commit.com/)) exécute les checks automatiquement avant chaque commit local.
Évite de pousser du code qui va faire échouer la CI.

```yaml
# .pre-commit-config.yaml
repos:
  - repo: https://github.com/astral-sh/ruff-pre-commit
    rev: v0.9.0
    hooks:
      - id: ruff
      - id: ruff-format
```

---

### Vision cible du workflow CI

```
push / PR
    │
    ├── job: lint (sans Docker, ~20s)
    │       ruff check + ruff format --check
    │
    ├── job: test (avec Docker + Postgres, ~2min)
    │       pytest --cov --cov-fail-under=80
    │
    └── job: security (sans Docker, ~30s)
            pip-audit
```

---

## 12. Conventions du projet

- **Langue :** Français pour les messages utilisateur et les commentaires métier, Anglais pour le code (variables, fonctions, classes)
- **Formatage Python :** Ruff (migration depuis Black — même `line-length = 88`)
- **Branches git :** `main` (prod), `dev` (staging), `feature/<nom>` (fonctionnalités)
- **Tests :** Dossier `tests/` à la racine — migration vers `pytest` + `pytest-django` recommandée
- **Commit message :** conventionnel : `feat:`, `fix:`, `chore:`, `refactor:`, `test:`, `docs:`
