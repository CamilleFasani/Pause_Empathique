# Prochaine session — Objectifs

> Source de vérité pour la prochaine étape de travail. À mettre à jour à la fin de
> chaque session.

## Session #17 — objectifs révisés pour finaliser la branche en cours

### Contexte

La reprise du suivi de la session #17, le 10 juillet 2026, confirme que les vues de
connexion et d'inscription et leur branchement au store sont terminés. Le layout
des vues d'authentification est réalisé, mais l'objectif global sur les layouts
n'est que partiellement terminé.

La branche front active est `feat/-base-layout-and-auth-views`. Elle contient aussi
une première gestion JWT fonctionnelle avec refresh token dans `localStorage`.
Cette stratégie est explicitement transitoire : la sécurisation par cookies fera
l'objet de la branche suivante.

### Objectif 1 — Page intermédiaire avant la pratique

- [ ] Créer une page intermédiaire accessible depuis le bouton « Commencer » de
  `WelcomeView`.
- [ ] Ajouter une route dédiée à cette page.
- [ ] Proposer deux parcours clairement identifiables :
  - aller vers `AuthView` pour se connecter ou créer un compte ;
  - démarrer directement une pratique anonyme.
- [ ] Relier le bouton « Commencer » de `WelcomeView` à cette nouvelle route.
- [ ] Vérifier le comportement de navigation sur mobile et desktop.

### Objectif 2 — Finaliser et merger la branche

- [ ] Relire les changements de `feat/-base-layout-and-auth-views` et vérifier
  qu'aucun travail incomplet non prévu n'est embarqué silencieusement.
- [ ] Exécuter `npm run type-check`, `npm run lint` et `npm run build`.
- [ ] Corriger les éventuelles erreurs détectées.
- [ ] Merger la branche dans `dev` et vérifier la CI.

### Limites de cette session

- Ne pas commencer la migration vers les cookies sur la branche actuelle.
- Ne pas reprendre le Dashboard ni les pages du parcours avant la session dédiée.
- Ne pas considérer tous les layouts applicatifs comme terminés : seuls ceux liés
  à l'authentification sont validés à ce stade.

---

## Étapes planifiées après le merge

### Session #18 — 17 juillet 2026 — Authentification sécurisée

Créer une nouvelle branche dédiée, puis :

- définir le contrat de cookies entre Django/DRF et Vue ;
- remplacer le stockage persistant du refresh token dans `localStorage` par une
  stratégie fondée sur des cookies sécurisés ;
- traiter explicitement `HttpOnly`, `Secure`, `SameSite`, CSRF, refresh, rotation,
  expiration et logout ;
- adapter le back-end, le client Axios et le store auth ;
- écrire ou mettre à jour les tests back et front pertinents ;
- vérifier le fonctionnement de bout en bout avant merge.

La solution exacte devra être conçue et validée avant l'implémentation : « utiliser
des cookies » ne suffit pas, à lui seul, à garantir une authentification sûre.

### Objectif suivant — Dashboard et parcours de pratique

Après sécurisation de l'authentification, créer une branche commune pour :

- reprendre et finaliser le Dashboard ;
- finaliser le layout des pages applicatives ;
- construire le parcours « vide ton sac » → observation → sentiments → besoins ;
- définir les données et transitions entre les étapes ;
- intégrer progressivement les endpoints API correspondants.
