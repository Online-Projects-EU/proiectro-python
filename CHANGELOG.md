# Changelog

## 0.4.0

980 operations across 42 namespaces (`proiectro.api.<namespace>`).

### New namespaces

- `shares` - show a customer organisation the proposals, documents and files you choose: assemble a
  share (`add_share`, `add_share_proposal`, `add_share_org_document`, `add_share_org_file`, ...),
  publish and unpublish it, see who opened what (`share_accesses`).
- `sales_targets` - target schemes and their bands, and per-person sales targets
  (`add_target_scheme`, `add_target_band`, `add_sales_target`, ...).

### Orders and quote requests

- Customer portal: `portal_order_catalog`, `add_order`, `portal_orders`, `portal_order`,
  `portal_closed_orders`, `portal_cancel_order`, `portal_confirm_order_receipt`; quote requests with
  `portal_quote_catalog`, `add_quote_request`, `portal_quote_requests`, `portal_quote_request`,
  `portal_withdraw_quote_request`.
- Partner portal: the same flow towards a partner, from `partner_portal_order_catalog` and
  `add_partner_order` to `partner_portal_confirm_order_receipt`, and `add_partner_quote_request`.
- Supplier side: `accept_portal_order`, `reject_portal_order`, `mark_portal_order_delivered`.
- Price lists decide which catalog items each customer and partner sees, and at what price:
  `add_price_list`, `edit_price_list`, `edit_price_list_items`, `delete_price_list`,
  `set_org_price_lists`, `set_bridge_price_lists`.
- Catalog items carry `available_in_customer_portal`, `available_in_partner_portals` and
  `price_lists`; customers carry `portal_ordering_enabled` and `portal_quote_requests_enabled`;
  funnels carry `used_for_orders` and `used_for_quote_requests`.

### Other new operations

- Customer portal shares: `portal_shares`, `portal_share`, `portal_share_proposal`, PDF downloads.
- Coordinates for locations, customer locations and assets (`set_location_coordinates`,
  `set_customer_location_coordinates`, `set_customer_asset_coordinates`); `get_customer_asset`,
  `tenant_customer_assets`.
- Notification preferences, for the workspace and for yourself.
- Sales: `my_pipeline`, `my_stage_proposals`, `my_sales`, `salesperson_sales`,
  `list_sale_activity_types`, `product_details`; leads: `fast_proposal`, `lead_owner_candidates`.
- `my_profile` / `edit_my_profile`, `tenant_my_work_items`, `tenant_my_bookings`,
  `my_permissions_explain`.

### Breaking changes

- Work logs are in minutes. `add_work_log` and `edit_work_log` take `duration` (`2`, `1h30m`, `45m`
  or `3:45`; a bare number is hours) instead of `hours`; work log responses carry `minutes`,
  `total_minutes` and `total_logged_minutes` instead of the hour fields, and delivery KPIs carry
  `minutes_logged_period` / `minutes_logged_total`.
- `project_product_details` is removed; use `product_details`.
- `delete_lead_list` takes no request body.
- Member preferences no longer carry `preference_mentions`, `preference_my_number`,
  `preference_my_string` or `preference_theme`.
- Model renames: `NotificationItemTenantType0` is now `NotificationTenant`, and
  `EditOperationalItemPriority` is now `EditOperationalItemPriorityType0`.

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
