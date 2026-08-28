# Prochaine session — Objectifs

> Source de vérité pour la prochaine étape de travail. À mettre à jour à la fin de
> chaque session.

## Session #24 — 31 août 2026 — Journal, navigation et fin de branche

### Contexte

Les sessions #21 à #23 ont stabilisé le parcours de pratique et posé les
premiers accès au Journal :

- `EmptyYourBagView` et `ObservationView` sont reliées au brouillon Pinia ;
- `FeelingsView` et `NeedsView` chargent leurs catalogues via l'API front ;
- les sentiments et besoins utilisent une sélection multiple par familles ;
- seules les listes d'identifiants `feelingIds` et `needIds` sont stockées dans
  Pinia ;
- les états de chargement, d'erreur et d'absence de données sont affichés ;
- la progression est bloquée tant qu'aucune sélection n'a été faite dans l'étape
  courante ;
- `useGender()` choisit le libellé genré des sentiments ;
- le parcours anonyme demande le genre grammatical au premier démarrage et le
  conserve dans `sessionStorage` via `ANONYMOUS_GENDER_STORAGE_KEY` ;
- `PauseView` affiche le résumé du brouillon et gère les fins de parcours
  authentifiée et anonyme ;
- une première version visuelle de `HomeView` prépare l'accès au Journal, à la
  pratique, aux dernières pauses et à la future timeline statistique.
- `PauseDetailView` permet de consulter et supprimer une pause ;
- après création authentifiée, `PauseView` redirige vers le Journal.

Clarification produit actée en session #23 :

- `HomeView` est le point d'entrée synthétique : salutation, accès à la
  pratique, trois dernières pauses et timeline statistique.
- `DiaryView` est l'espace d'exploration de l'historique complet : liste
  chronologique détaillée, filtres, accès aux détails.

La prochaine session doit trancher la navigation entre Accueil, Journal,
pratique et détail de pause, vérifier la logique du parcours utilisateur, puis
terminer le Journal. Une fois les objectifs ci-dessous validés, la branche
pourra être mergée. La suite prévue est une branche dédiée aux vues du compte
utilisateur, puis le déploiement front en préproduction, le back étant déjà
déployé.

### Objectif 1 — Trancher la navigation et vérifier le parcours

- [ ] Trancher les liens entre `HomeView`, `DiaryView`, `PauseDetailView` et le
      démarrage de pratique.
- [ ] Vérifier les libellés et intentions : Accueil = point d'entrée, Journal =
      exploration complète.
- [ ] Vérifier les retours depuis le détail de pause après consultation et après
      suppression.
- [ ] Vérifier la cohérence des redirections après création réussie,
      authentification depuis le parcours et fin sans enregistrement.
- [ ] Ajuster les composants ou routes si une incohérence produit apparaît.

### Objectif 2 — Terminer le Journal

- [ ] Implémenter la liste complète des pauses dans `DiaryView`.
- [ ] Afficher les pauses en ordre chronologique clair.
- [ ] Ajouter un filtre par famille de sentiments.
- [ ] Ajouter un filtre par famille de besoins.
- [ ] Conserver les états chargement, erreur et liste vide.
- [ ] Garder les trois dernières pauses sur `HomeView`, au-dessus de la
      timeline.
- [ ] Vérifier que chaque pause listée mène au détail.

### Objectif 3 — Prévenir la perte du brouillon

- [ ] Ajouter `beforeunload` uniquement lorsqu'un brouillon contient des données.
- [ ] Vérifier le comportement sur un rechargement mobile et desktop.
- [ ] Ne pas ajouter de persistance `localStorage` ou `sessionStorage` dans cette
      étape.

### Objectif 4 — Vérifications et fin de branche

- [ ] Ajouter les tests ciblés du store : sélection, validation, réinitialisation,
      soumission authentifiée, soumission anonyme et conservation après erreur.
- [ ] Ajouter des tests ciblés pour les comportements directs de vues si un outil
      de test front adapté est déjà en place.
- [ ] Lancer `npm run type-check`.
- [ ] Lancer `npm run lint`.
- [ ] Lancer `npm run build`.
- [ ] Vérifier manuellement le parcours anonyme sur mobile.
- [ ] Vérifier manuellement le parcours création de compte → sauvegarde → Journal.
- [ ] Mettre à jour les documents de session en fin de travail.
- [ ] Préparer le merge de cette branche après validation.

### Suite prévue après merge

- Créer une branche dédiée aux vues liées au compte : visualiser, modifier et
  supprimer son compte.
- Déployer le front en préproduction après finalisation de ces vues, le back
  étant déjà déployé.

### Limites de la prochaine session

- Ne pas finaliser le Dashboard détaillé avant la stabilisation du Journal.
- Ne pas ajouter de logique métier durable côté front si elle appartient au back.
- Ne pas persister le brouillon dans `localStorage` ou `sessionStorage`.
- Ne pas viser l'adaptation desktop complète au-delà de la vérification du
  parcours.
- Ne pas créer d'abstraction générique sans besoin observé dans plusieurs vues.
