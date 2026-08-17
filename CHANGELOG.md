# Changelog

## 0.3.0

881 operations across 40 namespaces (`proiectro.api.<namespace>`).

### New namespaces

- `leads` — capture leads, organise them in lists, move them through the pipeline
  (`update_lead_status`, `claim_lead`, `reschedule_lead`, `disqualify_lead`), convert them into
  customers (`mark_lead_converted`), import in bulk, log activities.
- `documents` — document templates and numbered series; generate documents for proposals,
  organisations, locations, assets and support requests (`generate_*_document`); list and filter.
- `custom_forms` — form definitions, versions, steps and fields; submissions
  (`submit_custom_form`, `form_submissions`, `edit_submission_status`).
- `timers` — add, edit and delete timers; list them.
- `comments` — one comment surface for work items, operational items and support requests,
  including the `_own_` variants for editing and deleting your own comments.
- `kpis` — 22 KPI endpoints: overdue and upcoming payments, revenue at risk, projects at risk,
  stale and expiring proposals, lead pipeline health, open tickets and queue health, team workload,
  and more.
- `integrations` — `enrich_company`: look up a Romanian company by CUI (name, registration number,
  VAT status, address) to auto-fill legal entity data.

### New operations in existing namespaces

- Projects: `archive_project` / `unarchive_project`; `tenant_my_worklist`.
- Rich query filters on `list_projects`, `org_projects`, `list_tasks` and `project_work_items` —
  `search`, `owner`, `customer`, `manager`, date ranges, `lifecycle_status`, tags and labels.
- Locations carry `latitude` / `longitude`; customers accept `domains`; payments accept
  `show_sources` and expose their `sources`; proposals expose `rejected_at` /
  `rejection_reason`; the workspace has a `lead_visibility` policy.

### Package

- Ships `py.typed`, so type checkers now use the package's annotations.
- Date and datetime fields on responses are parsed into `datetime.date` / `datetime.datetime`.

## 0.2.0

Initial public release.
