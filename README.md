# proiectro

Official Python SDK for the [Proiect.ro](https://proiect.ro) API.

Fully typed with sync and async support via httpx.

## Installation

```bash
pip install proiectro
```

## Quick Start

```python
from proiectro.client import AuthenticatedClient
from proiectro.api.orgs import tenant_orgs

# Authenticate (base_url defaults to https://proiect.ro)
client = AuthenticatedClient(
    base_url="https://proiect.ro",
    token="your_api_key_here",
)

# List customers
response = tenant_orgs.sync_detailed(
    tenant_path="my-workspace",
    client=client,
)

if response.status_code == 200:
    print(response.parsed)
```

## Authentication

Create an API key in your workspace under **Settings > API Keys**. The SDK sends it as a Bearer token automatically.

```python
from proiectro.client import AuthenticatedClient

client = AuthenticatedClient(
    base_url="https://proiect.ro",
    token="your_api_key_here",
)
```

## Sync and Async

Every endpoint has four variants:

```python
from proiectro.api.orgs import tenant_orgs

# Sync — returns parsed model or None
data = tenant_orgs.sync(tenant_path="my-workspace", client=client)

# Sync — returns full httpx.Response with .parsed, .status_code, .headers
response = tenant_orgs.sync_detailed(tenant_path="my-workspace", client=client)

# Async
data = await tenant_orgs.asyncio(tenant_path="my-workspace", client=client)

# Async — detailed
response = await tenant_orgs.asyncio_detailed(tenant_path="my-workspace", client=client)
```

## Usage Examples

### Customers

```python
from proiectro.api.orgs import tenant_orgs, add_subtenant, edit_subtenant, delete_subtenant
from proiectro.models import AddSubtenant, EditSubtenant

# List all customers
customers = tenant_orgs.sync(tenant_path="my-workspace", client=client)

# Create a customer
add_subtenant.sync_detailed(
    tenant_path="my-workspace",
    client=client,
    body=AddSubtenant(
        name="Acme Corp",
        parent_id="org-uuid",
        timezone="Europe/Berlin",
        default_currency="EUR",
        country="DE",
        manager="member-uuid",
    ),
)

# Update a customer
edit_subtenant.sync_detailed(
    tenant_path="my-workspace",
    subtenant_id="customer-uuid",
    client=client,
    body=EditSubtenant(
        name="Acme Corporation",
        timezone="Europe/Berlin",
        default_currency="EUR",
        country="DE",
        manager="member-uuid",
    ),
)

# Delete a customer
delete_subtenant.sync_detailed(
    tenant_path="my-workspace",
    subtenant_id="customer-uuid",
    client=client,
)
```

### Leads

```python
from datetime import datetime, timezone
from proiectro.api.leads import add_lead, tenant_all_leads, update_lead_status, mark_lead_converted
from proiectro.models import AddLead, AddLeadSource, UpdateLeadStatus, UpdateLeadStatusStatus, MarkLeadConverted

# Capture an inbound lead
add_lead.sync_detailed(
    tenant_path="my-workspace",
    client=client,
    body=AddLead(
        name="Jane Doe",
        company_name="Acme Corp",
        email="jane@acme.example",
        source=AddLeadSource.WEB_FORM,
    ),
)

# List leads, filtered
leads = tenant_all_leads.sync(tenant_path="my-workspace", client=client, status="new", has_email=True)

# Move a lead through the pipeline. `updated_at` is the value you last read —
# the API rejects the write if someone else changed the lead in between.
update_lead_status.sync_detailed(
    tenant_path="my-workspace",
    lead_id="lead-uuid",
    client=client,
    body=UpdateLeadStatus(
        status=UpdateLeadStatusStatus.QUALIFIED,
        updated_at=datetime(2026, 3, 15, 10, 0, tzinfo=timezone.utc),
    ),
)

# Convert it into a customer
mark_lead_converted.sync_detailed(
    tenant_path="my-workspace",
    lead_id="lead-uuid",
    client=client,
    body=MarkLeadConverted(
        updated_at=datetime(2026, 3, 15, 10, 5, tzinfo=timezone.utc),
        new_org_name="Acme Corp",
    ),
)
```

### Proposals

```python
from proiectro.api.proposals import add_proposal, org_proposals, change_proposal_stage
from proiectro.models import AddProposal, ChangeProposalStage

# List proposals for a customer
proposals = org_proposals.sync(
    tenant_path="my-workspace",
    org_id="customer-uuid",
    client=client,
)

# Create a proposal
add_proposal.sync_detailed(
    tenant_path="my-workspace",
    client=client,
    body=AddProposal(
        name="Q1 Consulting",
        description="Consulting engagement for Q1",
        customer="customer-uuid",
        owner="member-uuid",
        manager="member-uuid",
        sales_stage="stage-uuid",
        proposal_currency="EUR",
        wbsconfiguration="wbs-uuid",
    ),
)

# Move a proposal to the next stage
change_proposal_stage.sync_detailed(
    tenant_path="my-workspace",
    proposal_id="proposal-uuid",
    stage_id="next-stage-uuid",
    client=client,
    body=ChangeProposalStage(),
)
```

### Projects

```python
from proiectro.api.projects import list_projects, project_work_items, add_work_item, update_work_item_status
from proiectro.api.comments import add_work_item_comment
from proiectro.models import AddWorkItem, UpdateWorkItemStatus, AddWorkItemComment

# List all projects
projects = list_projects.sync(tenant_path="my-workspace", client=client)

# Get work items for a project
work_items = project_work_items.sync(
    tenant_path="my-workspace",
    project_id="project-uuid",
    client=client,
)

# Create a work item
add_work_item.sync_detailed(
    tenant_path="my-workspace",
    client=client,
    body=AddWorkItem(
        name="Design mockups",
        project_id="project-uuid",
        work_item_type_id="type-uuid",
    ),
)

# Report progress, then finish it
update_work_item_status.sync_detailed(
    tenant_path="my-workspace",
    work_item_id="work-item-uuid",
    client=client,
    body=UpdateWorkItemStatus(percent_complete=60),
)
update_work_item_status.sync_detailed(
    tenant_path="my-workspace",
    work_item_id="work-item-uuid",
    client=client,
    body=UpdateWorkItemStatus(finished_at="2026-03-10T16:00:00Z"),
)

# Comment on it
add_work_item_comment.sync_detailed(
    tenant_path="my-workspace",
    client=client,
    body=AddWorkItemComment(work_item_id="work-item-uuid", content="Mockups approved by the customer."),
)
```

### Payments

```python
from proiectro.api.proposals import add_payment, mark_payment_paid
from proiectro.models import AddPayment, MarkPaymentPaid

# Create a payment
add_payment.sync_detailed(
    tenant_path="my-workspace",
    client=client,
    body=AddPayment(
        payment_schedule_block_id="block-uuid",
        name="First milestone",
        due_date="2026-03-15",
        amount="5000.00",
    ),
)

# Mark a payment as paid
mark_payment_paid.sync_detailed(
    tenant_path="my-workspace",
    payment_id="payment-uuid",
    client=client,
    body=MarkPaymentPaid(paid_date="2026-03-15"),
)
```

### Documents

```python
from proiectro.api.documents import tenant_document_templates_list, generate_proposal_document, tenant_documents_list
from proiectro.models import GenerateDocument

# Templates available in the workspace
templates = tenant_document_templates_list.sync(tenant_path="my-workspace", client=client)

# Generate a numbered document for a proposal
generate_proposal_document.sync_detailed(
    tenant_path="my-workspace",
    proposal_id="proposal-uuid",
    client=client,
    body=GenerateDocument(template_id="template-uuid"),
)

# Documents, filtered
documents = tenant_documents_list.sync(tenant_path="my-workspace", client=client, org_id="customer-uuid")
```

### Tags

```python
from proiectro.api.tags import tenant_tags, add_tag, tag_org, untag_org
from proiectro.models import AddTag

# List all tags
tags = tenant_tags.sync(tenant_path="my-workspace", client=client)

# Create a tag
add_tag.sync_detailed(
    tenant_path="my-workspace",
    client=client,
    body=AddTag(name="VIP", color="#ff0000"),
)

# Tag a customer
tag_org.sync_detailed(
    tenant_path="my-workspace",
    org_id="customer-uuid",
    tag_id="tag-uuid",
    client=client,
)
```

### Team

```python
from proiectro.api.team import tenant_team, invite_to_team
from proiectro.models import InviteMemberToTenant

# List team members
team = tenant_team.sync(tenant_path="my-workspace", client=client)

# Invite someone to the team
invite_to_team.sync_detailed(
    tenant_path="my-workspace",
    client=client,
    body=InviteMemberToTenant(email="colleague@example.com"),
)
```

### Webhooks

Subscribe to platform events instead of polling:

```python
from proiectro.api.webhooks import add_webhook, tenant_webhooks
from proiectro.models import AddWebhook

add_webhook.sync_detailed(
    tenant_path="my-workspace",
    client=client,
    body=AddWebhook(
        name="CRM sync",
        target_url="https://example.com/hooks/proiectro",
        event_types=["changeProposalStage", "markPaymentPaid"],
        is_active=True,
        is_secure=True,
    ),
)

hooks = tenant_webhooks.sync(tenant_path="my-workspace", client=client)
```

## Namespaces

Operations live under `proiectro.api.<namespace>`, one module per operation:

| Area | Namespaces |
|---|---|
| Sales | `leads`, `proposals`, `orgs`, `rfp`, `bridge` (partnerships), `partnerportal` |
| Delivery | `projects`, `work`, `operations`, `comments`, `timers`, `booking`, `capacity`, `resources`, `holidays`, `calendar` |
| Money | `costs`, `exchange`, `analytics`, `kpis` |
| Support & assets | `support`, `assets`, `locations`, `custom_forms` |
| Documents & files | `documents`, `files`, `cdn` |
| Workspace | `tenant`, `team`, `rbac`, `tags`, `labels`, `notifications`, `feed`, `welcome`, `auth` |
| Automation | `webhooks`, `automation`, `integrations`, `portal` |

## Error Handling

Use `sync_detailed` / `asyncio_detailed` to inspect status codes:

```python
response = tenant_orgs.sync_detailed(
    tenant_path="my-workspace",
    client=client,
)

if response.status_code == 200:
    print("Success:", response.parsed)
else:
    print("Error:", response.status_code, response.content)
```

Or enable automatic exceptions for unexpected status codes:

```python
client = AuthenticatedClient(
    base_url="https://proiect.ro",
    token="your_api_key_here",
    raise_on_unexpected_status=True,
)
```

## Context Manager

The client can be used as a context manager to ensure connections are properly closed:

```python
with AuthenticatedClient(
    base_url="https://proiect.ro",
    token="your_api_key_here",
) as client:
    data = tenant_orgs.sync(tenant_path="my-workspace", client=client)
```

Async:

```python
async with AuthenticatedClient(
    base_url="https://proiect.ro",
    token="your_api_key_here",
) as client:
    data = await tenant_orgs.asyncio(tenant_path="my-workspace", client=client)
```

## Requirements

- Python >= 3.10
- httpx >= 0.23.0

## API Documentation

Full API reference is available at [proiect.ro/api/v1/docs](https://proiect.ro/api/v1/docs).

## Changelog

See [CHANGELOG.md](CHANGELOG.md).

## License

MIT
