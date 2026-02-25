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

To point at a different server (e.g. staging or self-hosted), override the `base_url`:

```python
client = AuthenticatedClient(
    base_url="https://staging.proiect.ro",
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
from proiectro.api.projects import list_projects, project_work_items, add_work_item
from proiectro.models import AddWorkItem

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

## License

MIT
