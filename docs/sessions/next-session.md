# Prochaine session — Objectifs

> Ce fichier est lu en priorité par Copilot au démarrage de chaque session.
> Mis à jour en fin de session avec les objectifs suivants.

---

## Session #10 — 10 avril 2026 ✅ COMPLÉTÉE

### Bilan

- [x] Objectif 1 — Ruff S106 débloqué : `per-file-ignores` dans `pyproject.toml`
- [x] Objectif 2 — `UserMeAPITest` relu et validé (40 tests passent)
- [x] Objectif 3 — `LoginAPITest` + `LogoutAPITest` écrits avec vrais tokens JWT
- [x] Objectif 4 — Couverture 87% (seuil 80% atteint)
- [x] Merge `feature/authentication` → `dev` (CI verte requise)
- [x] Branche `feature/pauses-api` créée

---

## Session #11 — prochaine session

### Contexte

Session #10 (10 avril) : socle auth API complet, testé, mergé dans `dev`.

- `LoginAPITest` + `LogoutAPITest` écrits avec vrais tokens JWT ✅
- Couverture `users` : 87% (40 tests) ✅
- `feature/authentication` mergée dans `dev` ✅
- Branche `feature/pauses-api` créée ✅

---

### Objectifs de la session

#### Objectif 1 — Rédiger le plan de tests Pauses (dossier CDA)

- [ ] Rédiger le plan de tests formalisé avant d'écrire le code
- [ ] Couvrir : cas nominaux, cas limites, cas d'erreur pour list/create/retrieve/update/delete
- [ ] Valider le plan avant implémentation

#### Objectif 2 — Serializer Pause

- [ ] Créer `PauseSerializer` dans `pauses/api/serializers.py`
- [ ] Champs : `id`, `title`, `created_at`, `feelings`, `needs`
- [ ] Écrire les tests unitaires du serializer

#### Objectif 3 — Endpoints Pauses

- [ ] `GET /api/v1/pauses/` — liste des pauses de l'utilisateur connecté
- [ ] `POST /api/v1/pauses/` — créer une pause
- [ ] `GET /api/v1/pauses/<id>/` — détail d'une pause
- [ ] `PATCH /api/v1/pauses/<id>/` — modifier une pause
- [ ] `DELETE /api/v1/pauses/<id>/` — supprimer une pause
- [ ] Vérifier l'isolation : un utilisateur ne peut pas accéder aux pauses d'un autre

#### Objectif 4 — Tests d'intégration Pauses

- [ ] Tests CRUD complets selon le plan de tests rédigé en Objectif 1
- [ ] Couverture `pauses` maintenue ≥ 80%

---

### Rappels du chef de projet

- Le plan de tests doit être rédigé **avant** le code (pas après)
- Toujours tester l'isolation des données entre utilisateurs
- CI verte obligatoire avant merge `feature/pauses-api` → `dev`
