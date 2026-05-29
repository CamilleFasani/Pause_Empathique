# Prochaine session — Objectifs

> Ce fichier est lu en priorité par Copilot au démarrage de chaque session.
> Mis à jour en fin de session avec les objectifs suivants.

## Session #15 — à planifier

### Contexte

Session #14 (29 mai) : compteur anonyme conçu, implémenté, testé. Tous les tests passent au vert. Reste la validation finale et le merge.

- Compteur anonyme `AnonymousPauseCounter` (singleton) ✅
- Permission `IsAnonymousOnly` ✅
- Endpoint `POST /api/v1/pauses/anonymous` → 204 ✅
- Tests ANO-01 + ANO-02 au vert ✅
- `conftest.py` — désactivation throttle en test ✅
- Couverture `pauses` ≥ 80 % **non vérifiée** ❌
- Merge `feat/add-pauses-endpoints` → `dev` **en attente** ❌

---

### Objectifs de la session

#### Objectif 1 — Validation

- [ ] Vérifier la couverture `pauses` ≥ 80 % (`pytest --cov=pauses`)
- [ ] Ruff + pip-audit verts en local
- [ ] CI verte sur `feat/add-pauses-endpoints`

#### Objectif 2 — Merge

- [ ] Merge `feat/add-pauses-endpoints` → `dev`

---

### Rappels du chef de projet

- TDD strict : ne pas modifier un test pour qu'il passe sans en comprendre la raison
- CI verte obligatoire avant merge vers `dev`
