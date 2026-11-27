# Changelog

## 0.8.0

1041 operations across 45 namespaces (`proiectro.api.<namespace>`).

### Changes

- `edit_tenant` takes `intake_owner`, `intake_role` and `intake_lead_list`: who owns a new lead from
  the public page or a public form, which role is told and which list it goes to, unless that page or
  form has its own. It answers 422 when one of them is not an active member, role or open list of the
  workspace.
- `edit_tenant_public_page_settings` takes `lead_role` and `inherits_default`, and `lead_owner: ''` now
  clears the owner; leave the key out to keep it.
- `add_public_form` and `edit_public_form` take `role` and `inherits_default`. `owner` is optional on
  `add_public_form`: a form added without choices uses the workspace's. `owner: ''` clears it.

## 0.7.0

1041 operations across 45 namespaces (`proiectro.api.<namespace>`).

### Changes

- A lead carries `company_domain` (the domain of its email or of its website), and `tenant_lead`
  returns `company`: the customer and the other open leads at the same company, as far as the caller
  may see them (`leads`, `more`, `hidden`).
- `import_leads_preview` and `import_leads` report `company_matches`, the rows at a company that
  already has a lead or is already a customer.
- `tenant_business_process` returns `dependencies` and `enabled` (the processes it depends on and the
  ones it enables) and takes `back`, the process it was opened from. An artifact lists its `sources`.
- `edit_tenant` takes `llm_may_change_data`.

### Removed

- `add_subtenant` no longer takes `parent_id`, and `add_member_availability`,
  `add_resource_availability` and `edit_subtenant_legal_info` no longer take `tenant`: the workspace
  in the path already says it.

## 0.6.0

1041 operations across 45 namespaces (`proiectro.api.<namespace>`).

### New namespaces

- `meetings` - accept, decline or cancel a meeting request, and edit your own meeting page
  (`accept_meeting_request`, `decline_meeting_request`, `cancel_meeting_request`,
  `edit_my_meeting_page`).
- `experiments` - beliefs and how they changed over time (`tenant_beliefs`, `tenant_belief`,
  `tenant_belief_over_time`, `add_belief`, `edit_belief`, `delete_belief`, `tenant_chain`).

### Other new operations

- Feed posts: `feed_post`, `add_feed_post`, `edit_own_feed_post`, `delete_own_feed_post`, and for feed
  moderators `edit_feed_post`, `delete_feed_post`.
- Feed post comments: `list_feed_post_comments`, `add_feed_post_comment`, `edit_own_feed_post_comment`,
  `delete_own_feed_post_comment`, and for feed moderators `edit_feed_post_comment`,
  `delete_feed_post_comment`.
- Public page: `edit_tenant_public_page_settings`, `publish_public_pages`, web links
  (`add_web_link`, `edit_web_link`, `delete_web_link`, `reorder_web_links`), public forms
  (`add_public_form`, `edit_public_form`, `delete_public_form`), `add_public_share`, and the brand
  cover (`generate_upload_url_brand_cover`, `edit_brand_cover_focus`, `mark_brand_cover_as_deleted`).
- `edit_tenant_meetings_settings`.
- Messages sent about a record: `customer_asset_messages`, `location_messages`,
  `operational_work_item_messages`, `external_support_request_messages`,
  `internal_support_request_messages`.
- `email_template_defaults`, `set_email_template_default`.
- `lead_history`, `proposal_lead_history`, `analytics_sales_leads`.

### Changes

- `send_email` on accepting, rejecting and delivering portal orders, on changing or closing an external
  support request and on its comments; `mark_project_delivered` takes an optional body with
  `send_email`.
- `record_activity` when sending a document or a proposal by email.
- Processes have `allow_take_over`, and task `actions` report `can_claim`.
- Feed events carry `comment_count`, `edited`, `can_edit` and `can_delete`; the feed says `can_post`.
- Catalog items have `available_on_public_page`; legal info has `legal_brand_name`,
  `legal_contact_email` and `legal_contact_phone`.
- Sales analytics report deals and value slower than usual and what the forecast is waiting on.
  `probability_percent` on a pipeline stage can be fractional or empty.
- `EditLead.status` may be left empty.

## 0.5.0

990 operations across 43 namespaces (`proiectro.api.<namespace>`).

### New namespace

- `time_off` - members ask for time off, change or withdraw it, and approvers list, approve or reject
  it (`add_my_time_off`, `list_my_time_off`, `list_time_off_requests`, `approve_time_off`,
  `reject_time_off`).

### Other new operations

- `import_orgs`, `import_orgs_preview`, `import_catalog`, `import_catalog_preview` - import customers
  and catalog items, with a preview first.
- `tenant_messages_list`, `org_messages`, `proposal_messages` - the messages your workspace sent.
- `generate_upload_url_catalog_picture`, `mark_catalog_picture_as_deleted` - catalog pictures.

### Changes

- `finalize_document`: `series_id` is optional; a document from a template with no series finalizes
  without a number.
- Task lists carry `actions` and `source_*`; assets accept `next_service_date`; payments accept
  `invoiced_date`.

### Breaking changes

- Removed: `generate_download_url_member_avatar`, `generate_download_url_org_branding`,
  `generate_download_url_tenant_branding`, `generate_download_url_user_avatar`,
  `generate_upload_url_org_branding`, `mark_org_branding_as_deleted`.
- `generate_upload_url_*` no longer take `attachmentNodeId` or `attachmentNodeType`.
- `mark_member_avatar_as_deleted`, `mark_tenant_branding_as_deleted` and `mark_user_avatar_as_deleted`
  no longer take a body.
- `partner_approve_product` and `partner_reject_product` take their ids from the path only.
- `list_work_item_comments` and `list_operational_work_item_comments` no longer return `attachments`.

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
