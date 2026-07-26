# Back-end Instructions — Django and REST API

These instructions extend the workspace root `AGENTS.md` for all work in this
repository.

## Current transition

The repository is migrating incrementally from a classic server-rendered Django
application to a Django REST Framework API consumed by a separate Vue SPA. Django
templates and session-based flows may coexist temporarily with `/api/v1/`
endpoints. Do not remove or break the legacy flow until the equivalent SPA flow is
implemented, tested, validated in staging, and its removal is planned.

New application-facing capabilities should normally expose an API contract rather
than add new template behavior. When touching legacy code, distinguish clearly
between:

- behavior that must remain compatible during the transition;
- behavior already owned by the API;
- code that can only be removed after front-end parity is confirmed.

Consult `docs/project-management.md` for migration status rather than assuming a
phase is complete.

## API architecture

- Keep versioned endpoints under `/api/v1/` and preserve a consistent REST
  contract.
- Use serializers for input validation and representation, permissions for access
  control, and views/viewsets for HTTP orchestration. Keep domain rules close to
  models or focused services when they do not belong to HTTP handling.
- Enforce authentication, object ownership, authorization, and data validation on
  the server for every relevant endpoint. Never rely on the SPA to enforce them.
- Return deliberate HTTP status codes and stable, useful error bodies. Do not leak
  secrets, tokens, stack traces, or sensitive personal data through errors or logs.
- Avoid inefficient query patterns. Use `select_related`/`prefetch_related` when
  justified by measured or evident access patterns, without speculative tuning.
- Keep authentication and JWT behavior centralized in the auth/API layer. Treat
  token storage and cookie strategy as an explicit cross-repository security
  decision, not a component-level implementation detail.
- Configure CORS, CSRF, cookies, hosts, and environment-specific security settings
  narrowly. Development convenience must not weaken staging or production.
- Describe public endpoints and errors with `drf-spectacular`; update and validate
  the OpenAPI schema whenever an API contract changes.

## Data and privacy

Pause content and profile information are personal and potentially sensitive.
Apply least privilege, ownership checks, data minimization, and safe logging.
Schema changes require migrations. Review destructive or irreversible migrations
explicitly and provide a safe rollout path when existing data is involved.

Gender-dependent API representations must follow the documented shared contract.
Do not silently move presentation-only label selection back into Django if the
front-end composable owns that choice.

## Tests and quality

- Prefer pytest and pytest-django, following the existing test organization.
- For API work, cover serializer validation and endpoint behavior as appropriate:
  success, invalid input, unauthenticated/unauthorized access, ownership boundaries,
  and meaningful edge cases.
- Reproduce bugs with a failing regression test before fixing them when practical.
- Run the narrowest relevant tests during development, then the broader impacted
  suite. Run Ruff checks/formatting for changed Python code.
- Keep the OpenAPI schema generation valid when contracts change.
- Do not weaken assertions or coverage merely to make CI pass.

Use the commands and environment already documented by the repository. Inspect
`pyproject.toml`, Docker configuration, and CI workflows before inventing a new
tooling path.

## Migration completion criteria

A legacy Django page can be considered replaceable only when its API contract,
authorization, automated tests, SPA equivalent, relevant error states, and staging
validation are complete. Remove templates and front-only Django dependencies in a
separate, reviewable cleanup step after that evidence exists.
