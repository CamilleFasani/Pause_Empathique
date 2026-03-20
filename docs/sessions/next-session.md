# Prochaine session — Objectifs

> Ce fichier est lu en priorité par Copilot au démarrage de chaque session.
> Mis à jour en fin de session avec les objectifs suivants.

---

## Session #7 — Date prévue : 20 mars 2026

### Contexte

Session #6 (19 mars) : base de charte consolidée et stratégie de transition clarifiée.

- Contraste couleurs vérifié (accessibilité OK)
- Captures d'écran réalisées pour le dossier projet
- Choix stratégique acté : V1 en production, V2 en staging
- Refonte complète des templates Django volontairement mise en pause

---

### Objectifs de la session

#### Objectif 1 — Finaliser les merges de synchronisation (priorité)

- [ ] Merger `dev` vers `main` pour intégrer les changements précédents (dont migration `pytest`)
- [ ] Vérifier CI/CD et stabilité après merge sur `main`
- [ ] Merger ensuite la branche en cours vers `dev`
- [ ] Vérifier le déploiement staging post-merge

#### Objectif 2 — Démarrer la phase DRF

- [ ] Installer `djangorestframework`
- [ ] Préparer la configuration initiale DRF dans le projet
- [ ] Valider qu'aucune régression fonctionnelle n'est introduite

#### Objectif 3 — Préparer la suite design system côté front Vue

- [ ] Définir les états manquants du design system (`hover`, `focus`, `disabled`)
- [ ] Poser les bases des premiers composants Vue
- [ ] Préparer l'ajout des liens/références quand le front sera en place

---

### Rappels du chef de projet

- 🔀 Respecter l'ordre des merges pour sécuriser l'historique et les déploiements
- ✅ Garder la V1 stable en production, travailler la V2 sur staging
- 🔒 Enchaîner rapidement sur l'installation DRF après validation des merges
- 🧩 Continuer le design system en priorité sur les composants Vue plutôt que sur les templates Django amenés à disparaître
