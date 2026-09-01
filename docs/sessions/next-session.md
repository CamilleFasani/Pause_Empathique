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
- après création authentifiée, `PauseView` redirige vers l'Accueil authentifié.

Clarification produit actée en session #23 :

- `HomeView` est le point d'entrée synthétique : salutation, accès à la
  pratique, trois dernières pauses et timeline statistique.
- `DiaryView` est l'espace d'exploration de l'historique complet : liste
  chronologique détaillée, filtres, accès aux détails.

La session #24 a commencé par trancher la navigation entre Accueil, Journal,
pratique et détail de pause. La suite doit terminer le Journal, puis vérifier la
logique du parcours utilisateur avant merge. Une fois les objectifs ci-dessous
validés, la branche pourra être mergée. La suite prévue est une branche dédiée
aux vues du compte utilisateur, puis le déploiement front en préproduction, le
back étant déjà déployé.

### Objectif 1 — Trancher la navigation et vérifier le parcours

- [x] Trancher les liens entre `HomeView`, `DiaryView`, `PauseDetailView` et le
      démarrage de pratique.
- [x] Vérifier les libellés et intentions : Accueil = point d'entrée, Journal =
      exploration complète.
- [x] Vérifier les retours depuis le détail de pause après consultation et après
      suppression.
- [x] Vérifier la cohérence des redirections après création réussie,
      authentification depuis le parcours et fin sans enregistrement.
- [x] Ajuster les composants ou routes si une incohérence produit apparaît.

Décisions validées :

- un utilisateur connecté qui arrive sur `/` est redirigé vers `/home` ;
- `HomeView` mène au Journal, au démarrage de pratique et aux détails des trois
  dernières pauses ;
- `DiaryView` mène à l'Accueil et au démarrage de pratique ;
- `PauseDetailView` permet de revenir au Journal après consultation, de démarrer
  une nouvelle pratique et redirige vers l'Accueil après suppression ;
- après enregistrement authentifié, `PauseView` redirige vers l'Accueil ;
- après connexion ou inscription lancée depuis le récapitulatif, l'utilisateur
  revient sur `/pause` pour valider explicitement l'enregistrement ;
- après fin anonyme sans enregistrement, l'utilisateur revient sur `/`.

### Objectif 2 — Terminer le Journal

- [x] Implémenter la liste complète des pauses dans `DiaryView`.
- [x] Afficher les pauses en ordre chronologique clair.
- [x] Ajouter un filtre par famille de sentiments.
- [x] Ajouter un filtre par famille de besoins.
- [x] Ajouter un filtre par période/date.
- [x] Conserver les états chargement, erreur et liste vide.
- [x] Garder les trois dernières pauses sur `HomeView`, au-dessus de la
      timeline.
- [x] Vérifier que chaque pause listée mène au détail.

Décisions validées :

- le Journal utilise une présentation “Carnet vivant” mobile-first : timeline
  verticale, cartes simples et pauses les plus récentes en haut ;
- les cartes affichent le titre, l'heure et une icône automatique ;
- la famille de sentiments prédominante donne la couleur de fond ; en cas
  d'ex aequo entre deux familles de sentiments, le fond devient un dégradé entre
  les deux couleurs ;
- la famille de besoins prédominante donne l'icône tracée en noir ; en cas
  d'ex aequo entre besoins, la première famille rencontrée est utilisée ;
- les filtres par familles de sentiments, familles de besoins et période/date
  se combinent en logique `ET`.

### Objectif 3 — Prévenir la perte du brouillon

- [x] Ajouter `beforeunload` uniquement lorsqu'un brouillon contient des données.
- [x] Vérifier le comportement sur un rechargement mobile et desktop.
- [x] Ne pas ajouter de persistance `localStorage` ou `sessionStorage` dans cette
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
- [ ] Vérifier manuellement le parcours création de compte → sauvegarde → Accueil.
- [ ] Mettre à jour les documents de session en fin de travail.
- [ ] Préparer le merge de cette branche après validation.

### Suite prévue après merge

- Créer une branche dédiée aux vues liées au compte : visualiser, modifier et
  supprimer son compte.
- Avant le déploiement front, ajouter rapidement un timestamp au modèle/table du
  compteur de pratiques anonymes pour connaître le moment des pratiques
  anonymes.
- Déployer le front en préproduction après finalisation de ces vues, le back
  étant déjà déployé.

### Limites de la prochaine session

- Ne pas finaliser le Dashboard détaillé avant la stabilisation du Journal.
- Ne pas ajouter de logique métier durable côté front si elle appartient au back.
- Ne pas persister le brouillon dans `localStorage` ou `sessionStorage`.
- Ne pas viser l'adaptation desktop complète au-delà de la vérification du
  parcours.
- Ne pas créer d'abstraction générique sans besoin observé dans plusieurs vues.
