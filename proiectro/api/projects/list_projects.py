from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.output_projects_list import OutputProjectsList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    tenant_path: str,
    *,
    exclude_mode: bool | None | Unset = UNSET,
    search: None | str | Unset = UNSET,
    name: None | str | Unset = UNSET,
    customer: None | str | Unset = UNSET,
    owner: None | str | Unset = UNSET,
    manager: None | str | Unset = UNSET,
    created_after: None | str | Unset = UNSET,
    created_before: None | str | Unset = UNSET,
    closed_won_after: None | str | Unset = UNSET,
    closed_won_before: None | str | Unset = UNSET,
    has_products: bool | None | Unset = UNSET,
    tags1: list[str] | None | Unset = UNSET,
    tags2: list[str] | None | Unset = UNSET,
    tags3: list[str] | None | Unset = UNSET,
    label_id1: None | str | Unset = UNSET,
    label_op1: None | str | Unset = UNSET,
    label_val1: None | str | Unset = UNSET,
    label_id2: None | str | Unset = UNSET,
    label_op2: None | str | Unset = UNSET,
    label_val2: None | str | Unset = UNSET,
    label_id3: None | str | Unset = UNSET,
    label_op3: None | str | Unset = UNSET,
    label_val3: None | str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_exclude_mode: bool | None | Unset
    if isinstance(exclude_mode, Unset):
        json_exclude_mode = UNSET
    else:
        json_exclude_mode = exclude_mode
    params["exclude_mode"] = json_exclude_mode

    json_search: None | str | Unset
    if isinstance(search, Unset):
        json_search = UNSET
    else:
        json_search = search
    params["search"] = json_search

    json_name: None | str | Unset
    if isinstance(name, Unset):
        json_name = UNSET
    else:
        json_name = name
    params["name"] = json_name

    json_customer: None | str | Unset
    if isinstance(customer, Unset):
        json_customer = UNSET
    else:
        json_customer = customer
    params["customer"] = json_customer

    json_owner: None | str | Unset
    if isinstance(owner, Unset):
        json_owner = UNSET
    else:
        json_owner = owner
    params["owner"] = json_owner

    json_manager: None | str | Unset
    if isinstance(manager, Unset):
        json_manager = UNSET
    else:
        json_manager = manager
    params["manager"] = json_manager

    json_created_after: None | str | Unset
    if isinstance(created_after, Unset):
        json_created_after = UNSET
    else:
        json_created_after = created_after
    params["created_after"] = json_created_after

    json_created_before: None | str | Unset
    if isinstance(created_before, Unset):
        json_created_before = UNSET
    else:
        json_created_before = created_before
    params["created_before"] = json_created_before

    json_closed_won_after: None | str | Unset
    if isinstance(closed_won_after, Unset):
        json_closed_won_after = UNSET
    else:
        json_closed_won_after = closed_won_after
    params["closed_won_after"] = json_closed_won_after

    json_closed_won_before: None | str | Unset
    if isinstance(closed_won_before, Unset):
        json_closed_won_before = UNSET
    else:
        json_closed_won_before = closed_won_before
    params["closed_won_before"] = json_closed_won_before

    json_has_products: bool | None | Unset
    if isinstance(has_products, Unset):
        json_has_products = UNSET
    else:
        json_has_products = has_products
    params["has_products"] = json_has_products

    json_tags1: list[str] | None | Unset
    if isinstance(tags1, Unset):
        json_tags1 = UNSET
    elif isinstance(tags1, list):
        json_tags1 = tags1

    else:
        json_tags1 = tags1
    params["tags1"] = json_tags1

    json_tags2: list[str] | None | Unset
    if isinstance(tags2, Unset):
        json_tags2 = UNSET
    elif isinstance(tags2, list):
        json_tags2 = tags2

    else:
        json_tags2 = tags2
    params["tags2"] = json_tags2

    json_tags3: list[str] | None | Unset
    if isinstance(tags3, Unset):
        json_tags3 = UNSET
    elif isinstance(tags3, list):
        json_tags3 = tags3

    else:
        json_tags3 = tags3
    params["tags3"] = json_tags3

    json_label_id1: None | str | Unset
    if isinstance(label_id1, Unset):
        json_label_id1 = UNSET
    else:
        json_label_id1 = label_id1
    params["label_id1"] = json_label_id1

    json_label_op1: None | str | Unset
    if isinstance(label_op1, Unset):
        json_label_op1 = UNSET
    else:
        json_label_op1 = label_op1
    params["label_op1"] = json_label_op1

    json_label_val1: None | str | Unset
    if isinstance(label_val1, Unset):
        json_label_val1 = UNSET
    else:
        json_label_val1 = label_val1
    params["label_val1"] = json_label_val1

    json_label_id2: None | str | Unset
    if isinstance(label_id2, Unset):
        json_label_id2 = UNSET
    else:
        json_label_id2 = label_id2
    params["label_id2"] = json_label_id2

    json_label_op2: None | str | Unset
    if isinstance(label_op2, Unset):
        json_label_op2 = UNSET
    else:
        json_label_op2 = label_op2
    params["label_op2"] = json_label_op2

    json_label_val2: None | str | Unset
    if isinstance(label_val2, Unset):
        json_label_val2 = UNSET
    else:
        json_label_val2 = label_val2
    params["label_val2"] = json_label_val2

    json_label_id3: None | str | Unset
    if isinstance(label_id3, Unset):
        json_label_id3 = UNSET
    else:
        json_label_id3 = label_id3
    params["label_id3"] = json_label_id3

    json_label_op3: None | str | Unset
    if isinstance(label_op3, Unset):
        json_label_op3 = UNSET
    else:
        json_label_op3 = label_op3
    params["label_op3"] = json_label_op3

    json_label_val3: None | str | Unset
    if isinstance(label_val3, Unset):
        json_label_val3 = UNSET
    else:
        json_label_val3 = label_val3
    params["label_val3"] = json_label_val3

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/{tenant_path}/projects".format(
            tenant_path=quote(str(tenant_path), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> OutputProjectsList | None:
    if response.status_code == 200:
        response_200 = OutputProjectsList.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[OutputProjectsList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    tenant_path: str,
    *,
    client: AuthenticatedClient,
    exclude_mode: bool | None | Unset = UNSET,
    search: None | str | Unset = UNSET,
    name: None | str | Unset = UNSET,
    customer: None | str | Unset = UNSET,
    owner: None | str | Unset = UNSET,
    manager: None | str | Unset = UNSET,
    created_after: None | str | Unset = UNSET,
    created_before: None | str | Unset = UNSET,
    closed_won_after: None | str | Unset = UNSET,
    closed_won_before: None | str | Unset = UNSET,
    has_products: bool | None | Unset = UNSET,
    tags1: list[str] | None | Unset = UNSET,
    tags2: list[str] | None | Unset = UNSET,
    tags3: list[str] | None | Unset = UNSET,
    label_id1: None | str | Unset = UNSET,
    label_op1: None | str | Unset = UNSET,
    label_val1: None | str | Unset = UNSET,
    label_id2: None | str | Unset = UNSET,
    label_op2: None | str | Unset = UNSET,
    label_val2: None | str | Unset = UNSET,
    label_id3: None | str | Unset = UNSET,
    label_op3: None | str | Unset = UNSET,
    label_val3: None | str | Unset = UNSET,
) -> Response[OutputProjectsList]:
    """List Projects

     List all active projects (proposals in closed_won stage) in the tenant.
    Shows completed deals that are now active projects with project details.
    Supports filtering by various criteria including tags, labels, dates, and more.

    Args:
        tenant_path (str):
        exclude_mode (bool | None | Unset): Invert filter logic to exclude matching results
        search (None | str | Unset): Search by project name, description, or customer name
        name (None | str | Unset): Filter by project name
        customer (None | str | Unset): Filter by customer external ID
        owner (None | str | Unset): Filter by project owner external ID
        manager (None | str | Unset): Filter by project manager external ID
        created_after (None | str | Unset): Show projects created after this date (YYYY-MM-DD)
        created_before (None | str | Unset): Show projects created before this date (YYYY-MM-DD)
        closed_won_after (None | str | Unset): Show projects that moved to closed_won after this
            date (YYYY-MM-DD)
        closed_won_before (None | str | Unset): Show projects that moved to closed_won before this
            date (YYYY-MM-DD)
        has_products (bool | None | Unset): Filter projects that have products attached
        tags1 (list[str] | None | Unset): Filter by tags (first set - match ANY tag in this set)
        tags2 (list[str] | None | Unset): Filter by tags (second set - match ANY tag in this set)
        tags3 (list[str] | None | Unset): Filter by tags (third set - match ANY tag in this set)
        label_id1 (None | str | Unset): Filter by label (first set - select which label)
        label_op1 (None | str | Unset): Label comparison operator (first set)
        label_val1 (None | str | Unset): Label value to compare against (first set)
        label_id2 (None | str | Unset): Filter by label (second set - select which label)
        label_op2 (None | str | Unset): Label comparison operator (second set)
        label_val2 (None | str | Unset): Label value to compare against (second set)
        label_id3 (None | str | Unset): Filter by label (third set - select which label)
        label_op3 (None | str | Unset): Label comparison operator (third set)
        label_val3 (None | str | Unset): Label value to compare against (third set)

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OutputProjectsList]
    """

    kwargs = _get_kwargs(
        tenant_path=tenant_path,
        exclude_mode=exclude_mode,
        search=search,
        name=name,
        customer=customer,
        owner=owner,
        manager=manager,
        created_after=created_after,
        created_before=created_before,
        closed_won_after=closed_won_after,
        closed_won_before=closed_won_before,
        has_products=has_products,
        tags1=tags1,
        tags2=tags2,
        tags3=tags3,
        label_id1=label_id1,
        label_op1=label_op1,
        label_val1=label_val1,
        label_id2=label_id2,
        label_op2=label_op2,
        label_val2=label_val2,
        label_id3=label_id3,
        label_op3=label_op3,
        label_val3=label_val3,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    tenant_path: str,
    *,
    client: AuthenticatedClient,
    exclude_mode: bool | None | Unset = UNSET,
    search: None | str | Unset = UNSET,
    name: None | str | Unset = UNSET,
    customer: None | str | Unset = UNSET,
    owner: None | str | Unset = UNSET,
    manager: None | str | Unset = UNSET,
    created_after: None | str | Unset = UNSET,
    created_before: None | str | Unset = UNSET,
    closed_won_after: None | str | Unset = UNSET,
    closed_won_before: None | str | Unset = UNSET,
    has_products: bool | None | Unset = UNSET,
    tags1: list[str] | None | Unset = UNSET,
    tags2: list[str] | None | Unset = UNSET,
    tags3: list[str] | None | Unset = UNSET,
    label_id1: None | str | Unset = UNSET,
    label_op1: None | str | Unset = UNSET,
    label_val1: None | str | Unset = UNSET,
    label_id2: None | str | Unset = UNSET,
    label_op2: None | str | Unset = UNSET,
    label_val2: None | str | Unset = UNSET,
    label_id3: None | str | Unset = UNSET,
    label_op3: None | str | Unset = UNSET,
    label_val3: None | str | Unset = UNSET,
) -> OutputProjectsList | None:
    """List Projects

     List all active projects (proposals in closed_won stage) in the tenant.
    Shows completed deals that are now active projects with project details.
    Supports filtering by various criteria including tags, labels, dates, and more.

    Args:
        tenant_path (str):
        exclude_mode (bool | None | Unset): Invert filter logic to exclude matching results
        search (None | str | Unset): Search by project name, description, or customer name
        name (None | str | Unset): Filter by project name
        customer (None | str | Unset): Filter by customer external ID
        owner (None | str | Unset): Filter by project owner external ID
        manager (None | str | Unset): Filter by project manager external ID
        created_after (None | str | Unset): Show projects created after this date (YYYY-MM-DD)
        created_before (None | str | Unset): Show projects created before this date (YYYY-MM-DD)
        closed_won_after (None | str | Unset): Show projects that moved to closed_won after this
            date (YYYY-MM-DD)
        closed_won_before (None | str | Unset): Show projects that moved to closed_won before this
            date (YYYY-MM-DD)
        has_products (bool | None | Unset): Filter projects that have products attached
        tags1 (list[str] | None | Unset): Filter by tags (first set - match ANY tag in this set)
        tags2 (list[str] | None | Unset): Filter by tags (second set - match ANY tag in this set)
        tags3 (list[str] | None | Unset): Filter by tags (third set - match ANY tag in this set)
        label_id1 (None | str | Unset): Filter by label (first set - select which label)
        label_op1 (None | str | Unset): Label comparison operator (first set)
        label_val1 (None | str | Unset): Label value to compare against (first set)
        label_id2 (None | str | Unset): Filter by label (second set - select which label)
        label_op2 (None | str | Unset): Label comparison operator (second set)
        label_val2 (None | str | Unset): Label value to compare against (second set)
        label_id3 (None | str | Unset): Filter by label (third set - select which label)
        label_op3 (None | str | Unset): Label comparison operator (third set)
        label_val3 (None | str | Unset): Label value to compare against (third set)

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OutputProjectsList
    """

    return sync_detailed(
        tenant_path=tenant_path,
        client=client,
        exclude_mode=exclude_mode,
        search=search,
        name=name,
        customer=customer,
        owner=owner,
        manager=manager,
        created_after=created_after,
        created_before=created_before,
        closed_won_after=closed_won_after,
        closed_won_before=closed_won_before,
        has_products=has_products,
        tags1=tags1,
        tags2=tags2,
        tags3=tags3,
        label_id1=label_id1,
        label_op1=label_op1,
        label_val1=label_val1,
        label_id2=label_id2,
        label_op2=label_op2,
        label_val2=label_val2,
        label_id3=label_id3,
        label_op3=label_op3,
        label_val3=label_val3,
    ).parsed


async def asyncio_detailed(
    tenant_path: str,
    *,
    client: AuthenticatedClient,
    exclude_mode: bool | None | Unset = UNSET,
    search: None | str | Unset = UNSET,
    name: None | str | Unset = UNSET,
    customer: None | str | Unset = UNSET,
    owner: None | str | Unset = UNSET,
    manager: None | str | Unset = UNSET,
    created_after: None | str | Unset = UNSET,
    created_before: None | str | Unset = UNSET,
    closed_won_after: None | str | Unset = UNSET,
    closed_won_before: None | str | Unset = UNSET,
    has_products: bool | None | Unset = UNSET,
    tags1: list[str] | None | Unset = UNSET,
    tags2: list[str] | None | Unset = UNSET,
    tags3: list[str] | None | Unset = UNSET,
    label_id1: None | str | Unset = UNSET,
    label_op1: None | str | Unset = UNSET,
    label_val1: None | str | Unset = UNSET,
    label_id2: None | str | Unset = UNSET,
    label_op2: None | str | Unset = UNSET,
    label_val2: None | str | Unset = UNSET,
    label_id3: None | str | Unset = UNSET,
    label_op3: None | str | Unset = UNSET,
    label_val3: None | str | Unset = UNSET,
) -> Response[OutputProjectsList]:
    """List Projects

     List all active projects (proposals in closed_won stage) in the tenant.
    Shows completed deals that are now active projects with project details.
    Supports filtering by various criteria including tags, labels, dates, and more.

    Args:
        tenant_path (str):
        exclude_mode (bool | None | Unset): Invert filter logic to exclude matching results
        search (None | str | Unset): Search by project name, description, or customer name
        name (None | str | Unset): Filter by project name
        customer (None | str | Unset): Filter by customer external ID
        owner (None | str | Unset): Filter by project owner external ID
        manager (None | str | Unset): Filter by project manager external ID
        created_after (None | str | Unset): Show projects created after this date (YYYY-MM-DD)
        created_before (None | str | Unset): Show projects created before this date (YYYY-MM-DD)
        closed_won_after (None | str | Unset): Show projects that moved to closed_won after this
            date (YYYY-MM-DD)
        closed_won_before (None | str | Unset): Show projects that moved to closed_won before this
            date (YYYY-MM-DD)
        has_products (bool | None | Unset): Filter projects that have products attached
        tags1 (list[str] | None | Unset): Filter by tags (first set - match ANY tag in this set)
        tags2 (list[str] | None | Unset): Filter by tags (second set - match ANY tag in this set)
        tags3 (list[str] | None | Unset): Filter by tags (third set - match ANY tag in this set)
        label_id1 (None | str | Unset): Filter by label (first set - select which label)
        label_op1 (None | str | Unset): Label comparison operator (first set)
        label_val1 (None | str | Unset): Label value to compare against (first set)
        label_id2 (None | str | Unset): Filter by label (second set - select which label)
        label_op2 (None | str | Unset): Label comparison operator (second set)
        label_val2 (None | str | Unset): Label value to compare against (second set)
        label_id3 (None | str | Unset): Filter by label (third set - select which label)
        label_op3 (None | str | Unset): Label comparison operator (third set)
        label_val3 (None | str | Unset): Label value to compare against (third set)

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OutputProjectsList]
    """

    kwargs = _get_kwargs(
        tenant_path=tenant_path,
        exclude_mode=exclude_mode,
        search=search,
        name=name,
        customer=customer,
        owner=owner,
        manager=manager,
        created_after=created_after,
        created_before=created_before,
        closed_won_after=closed_won_after,
        closed_won_before=closed_won_before,
        has_products=has_products,
        tags1=tags1,
        tags2=tags2,
        tags3=tags3,
        label_id1=label_id1,
        label_op1=label_op1,
        label_val1=label_val1,
        label_id2=label_id2,
        label_op2=label_op2,
        label_val2=label_val2,
        label_id3=label_id3,
        label_op3=label_op3,
        label_val3=label_val3,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    tenant_path: str,
    *,
    client: AuthenticatedClient,
    exclude_mode: bool | None | Unset = UNSET,
    search: None | str | Unset = UNSET,
    name: None | str | Unset = UNSET,
    customer: None | str | Unset = UNSET,
    owner: None | str | Unset = UNSET,
    manager: None | str | Unset = UNSET,
    created_after: None | str | Unset = UNSET,
    created_before: None | str | Unset = UNSET,
    closed_won_after: None | str | Unset = UNSET,
    closed_won_before: None | str | Unset = UNSET,
    has_products: bool | None | Unset = UNSET,
    tags1: list[str] | None | Unset = UNSET,
    tags2: list[str] | None | Unset = UNSET,
    tags3: list[str] | None | Unset = UNSET,
    label_id1: None | str | Unset = UNSET,
    label_op1: None | str | Unset = UNSET,
    label_val1: None | str | Unset = UNSET,
    label_id2: None | str | Unset = UNSET,
    label_op2: None | str | Unset = UNSET,
    label_val2: None | str | Unset = UNSET,
    label_id3: None | str | Unset = UNSET,
    label_op3: None | str | Unset = UNSET,
    label_val3: None | str | Unset = UNSET,
) -> OutputProjectsList | None:
    """List Projects

     List all active projects (proposals in closed_won stage) in the tenant.
    Shows completed deals that are now active projects with project details.
    Supports filtering by various criteria including tags, labels, dates, and more.

    Args:
        tenant_path (str):
        exclude_mode (bool | None | Unset): Invert filter logic to exclude matching results
        search (None | str | Unset): Search by project name, description, or customer name
        name (None | str | Unset): Filter by project name
        customer (None | str | Unset): Filter by customer external ID
        owner (None | str | Unset): Filter by project owner external ID
        manager (None | str | Unset): Filter by project manager external ID
        created_after (None | str | Unset): Show projects created after this date (YYYY-MM-DD)
        created_before (None | str | Unset): Show projects created before this date (YYYY-MM-DD)
        closed_won_after (None | str | Unset): Show projects that moved to closed_won after this
            date (YYYY-MM-DD)
        closed_won_before (None | str | Unset): Show projects that moved to closed_won before this
            date (YYYY-MM-DD)
        has_products (bool | None | Unset): Filter projects that have products attached
        tags1 (list[str] | None | Unset): Filter by tags (first set - match ANY tag in this set)
        tags2 (list[str] | None | Unset): Filter by tags (second set - match ANY tag in this set)
        tags3 (list[str] | None | Unset): Filter by tags (third set - match ANY tag in this set)
        label_id1 (None | str | Unset): Filter by label (first set - select which label)
        label_op1 (None | str | Unset): Label comparison operator (first set)
        label_val1 (None | str | Unset): Label value to compare against (first set)
        label_id2 (None | str | Unset): Filter by label (second set - select which label)
        label_op2 (None | str | Unset): Label comparison operator (second set)
        label_val2 (None | str | Unset): Label value to compare against (second set)
        label_id3 (None | str | Unset): Filter by label (third set - select which label)
        label_op3 (None | str | Unset): Label comparison operator (third set)
        label_val3 (None | str | Unset): Label value to compare against (third set)

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OutputProjectsList
    """

    return (
        await asyncio_detailed(
            tenant_path=tenant_path,
            client=client,
            exclude_mode=exclude_mode,
            search=search,
            name=name,
            customer=customer,
            owner=owner,
            manager=manager,
            created_after=created_after,
            created_before=created_before,
            closed_won_after=closed_won_after,
            closed_won_before=closed_won_before,
            has_products=has_products,
            tags1=tags1,
            tags2=tags2,
            tags3=tags3,
            label_id1=label_id1,
            label_op1=label_op1,
            label_val1=label_val1,
            label_id2=label_id2,
            label_op2=label_op2,
            label_val2=label_val2,
            label_id3=label_id3,
            label_op3=label_op3,
            label_val3=label_val3,
        )
    ).parsed
