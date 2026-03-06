# Prochaine session — Objectifs

> Ce fichier est lu en priorité par Copilot au démarrage de chaque session.
> Mis à jour en fin de session avec les objectifs suivants.

---

## Session #2 — 6 mars 2026

### Contexte

Depuis la session #1, les travaux suivants ont été réalisés en autonomie :

- **Phase 0.1** : Environnement staging créé dans le code et déployé sur Railway (branche `dev`)
- **DNS** : Reorganisation des zones DNS OVH — `app.pause-empathique.fr` (prod) et `pause-empathique.fr` (anciennement en redirection permanente, forcé par OVH Cloud qui n'autorisait pas l'enregistrement A sur le domaine nu)

Ces changements sont en place mais **la prod et le staging ne répondent pas correctement**. La priorité absolue de la session est de déboguer et remettre les deux environnements en ligne.

---

### Objectifs de la session

#### Objectif 1 — Déboguer prod et staging Railway (priorité absolue)

- [ ] Vérifier l'état des déploiements Railway (prod + staging) — logs, statuts
- [ ] Vérifier la propagation DNS (`dig`, `nslookup`) pour `app.pause-empathique.fr` et `pause-empathique.fr`
- [ ] Vérifier les enregistrements DNS dans OVH (A, CNAME, redirections actives/supprimées)
- [ ] Vérifier la configuration des domaines personnalisés dans Railway (prod + staging)
- [ ] Vérifier les variables d'environnement (`ALLOWED_HOSTS`, `DJANGO_SETTINGS_MODULE`, etc.)
- [ ] Corriger les erreurs identifiées et valider que les deux sites répondent

#### Objectif 2 — Mesure de couverture et pre-commit hooks (si le temps le permet)

- [ ] Installer `pytest`, `pytest-django`, `pytest-cov` (via Poetry)
- [ ] Configurer `[tool.pytest.ini_options]` dans `pyproject.toml`
- [ ] Mesurer la couverture actuelle : `pytest --cov=. --cov-report=term-missing`
- [ ] Installer `pre-commit`, créer `.pre-commit-config.yaml` avec `ruff check` + `ruff format`

---

### Rappels du chef de projet

- ⚠️ La Phase 1 (charte graphique) ne démarre pas tant que la Phase 0 n'est pas validée
- 📋 Penser à définir la charte graphique (couleurs, typos) pour ne pas bloquer la Phase 1
- 🔒 Aucune dépendance DRF ni Vue.js pour l'instant — on consolide la base
