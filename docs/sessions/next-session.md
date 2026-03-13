# Prochaine session — Objectifs

> Ce fichier est lu en priorité par Copilot au démarrage de chaque session.
> Mis à jour en fin de session avec les objectifs suivants.

---

## Session #4 — Date prévue : 20 mars 2026

### Contexte

Session #3 (13 mars) : validation infra + préparation qualité.

- Production et staging validés sur Railway (DNS + SSL + disponibilité)
- Déploiement auto de la branche `dev` confirmé sur staging
- Job CI `security` avec `pip-audit` en place
- Priorité suivante validée : migration tests vers pytest + mise en place pre-commit

---

### Objectifs de la session

#### Objectif 1 — Migration vers pytest + mesure de couverture (Phase 0.2)

- [ ] Installer `pytest`, `pytest-django`, `pytest-cov` (via Poetry)
- [ ] Configurer `[tool.pytest.ini_options]` dans `pyproject.toml`
- [ ] Vérifier que les tests existants passent avec pytest
- [ ] Mesurer la couverture actuelle : `pytest --cov=. --cov-report=term-missing`
- [ ] Identifier les zones non couvertes (modèles, vues, forms)
- [ ] Mettre à jour le job CI `test` pour utiliser pytest

#### Objectif 2 bis — Audit sécurité des dépendances (Phase 0.3)

- [x] Ajouter un job CI `security` avec `pip-audit`
- [x] Exécuter l'audit sur PR et sur push `main` / `dev`
- [x] Traiter les vulnérabilités critiques détectées (si présentes)

#### Objectif 3 — Pre-commit hooks (Phase 0.4) (si le temps le permet)

- [ ] Installer `pre-commit` localement
- [ ] Créer `.pre-commit-config.yaml` avec `ruff check` + `ruff format`
- [ ] Tester sur un commit fictif

#### Objectif 4 — Préparer la documentation API Swagger (Phase 2)

- [ ] Valider l'outil retenu : `drf-spectacular` (OpenAPI 3 + Swagger UI + Redoc)
- [ ] Planifier l'installation dès le démarrage de la phase DRF (setup technique de la phase 2.1)
- [ ] Prévoir la validation finale de la doc sur staging (phase 2.4)

---

### Rappels du chef de projet

- ⚠️ La Phase 1 (charte graphique) ne démarre pas tant que la Phase 0 n'est pas validée
- 📋 Penser à définir la charte graphique (couleurs, typos) pour ne pas bloquer la Phase 1
- 🔒 Aucune dépendance DRF (hors doc Swagger préparatoire) ni Vue.js pour l'instant — on consolide la base
