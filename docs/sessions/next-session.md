# Prochaine session — Objectifs

> Ce fichier est lu en priorité par Copilot au démarrage de chaque session.
> Mis à jour en fin de session avec les objectifs suivants.

---

## Session #3 — Date prévue : 13 mars 2026

### Contexte

Session #2 (6 mars) : debugging infra Railway + DNS.

- Dockerfile corrigé (Node 20 + build Tailwind)
- `start-django.sh` corrigé (gunicorn bind sur `0.0.0.0:$PORT`, staging utilise gunicorn)
- TXT `_railway-verify.staging` et `_railway-verify.www` ajoutés dans OVH
- En attente de propagation DNS et validation Railway au moment de clore la session

---

### Objectifs de la session

#### Objectif 1 — Valider que prod et staging sont en ligne

- [x] Vérifier que Railway a validé les deux domaines (plus de "Waiting for DNS update")
- [x] Vérifier que `www.pause-empathique.fr` et `staging.pause-empathique.fr` répondent (SSL OK, pas de 404)
- [x] Vérifier que le déploiement automatique sur la branche `dev` fonctionne (webhook Railway)
- [x] Si encore bloqué : supprimer/recréer les domaines dans Railway pour forcer la re-vérification

#### Objectif 2 — Migration vers pytest + mesure de couverture (Phase 0.2)

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

---

### Rappels du chef de projet

- ⚠️ La Phase 1 (charte graphique) ne démarre pas tant que la Phase 0 n'est pas validée
- 📋 Penser à définir la charte graphique (couleurs, typos) pour ne pas bloquer la Phase 1
- 🔒 Aucune dépendance DRF ni Vue.js pour l'instant — on consolide la base
