# Prochaine session — Objectifs

> Ce fichier est lu en priorité par Copilot au démarrage de chaque session.
> Mis à jour en fin de session avec les objectifs suivants.

---

## Session #5 — Date prévue : 17 mars 2026

### Contexte

Session #4 (16 mars) : consolidation qualité terminée.

- Migration vers `pytest` effectuée et job CI `test` mis à jour
- `pre-commit` local validé avec Ruff (hooks opérationnels)
- Préparation Swagger validée (`drf-spectacular` retenu)
- Prochaine priorité : démarrer la Phase 1 (charte graphique) avec contrôle accessibilité

---

### Objectifs de la session

#### Objectif 1 — Démarrer la Phase 1 : charte graphique (priorité)

- [ ] Formaliser la charte visuelle cible (palette, typographies, composants de base)
- [ ] Mettre en place les variables CSS de charte dans `static/css/input.css`
- [ ] Appliquer la charte sur 1 à 2 vues prioritaires pour valider la direction

#### Objectif 2 — Accessibilité (à vérifier dès le début)

- [ ] Définir une checklist accessibilité minimale (contrastes, focus visible, labels, hiérarchie titres)
- [ ] Vérifier les contrastes des nouvelles couleurs avant application globale
- [ ] Contrôler la navigation clavier sur les vues modifiées
- [ ] Corriger les problèmes bloquants détectés avant généralisation de la charte

#### Objectif 3 — Suivi qualité restant (Phase 0)

- [ ] Relever le niveau de couverture et planifier les tests manquants pour viser 80 %
- [ ] Confirmer qu'aucune régression n'est introduite par les modifications UI

---

### Rappels du chef de projet

- 🎨 La session suivante démarre la Phase 1 avec une approche incrémentale (vue par vue)
- ♿ L'accessibilité est un critère bloquant de validation UI dès la première itération
- 🔒 Aucun démarrage DRF/Vue.js avant d'avoir une base qualité suffisante et stable
