from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.output_tenant_resource_types import OutputTenantResourceTypes
from ...types import UNSET, Response, Unset


def _get_kwargs(
    tenant_path: str,
    *,
    exclude_mode: bool | None | Unset = UNSET,
    search: None | str | Unset = UNSET,
    name: None | str | Unset = UNSET,
    internal_code: None | str | Unset = UNSET,
    timezone: None | str | Unset = UNSET,
    is_bookable: bool | None | Unset = UNSET,
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

    json_internal_code: None | str | Unset
    if isinstance(internal_code, Unset):
        json_internal_code = UNSET
    else:
        json_internal_code = internal_code
    params["internal_code"] = json_internal_code

    json_timezone: None | str | Unset
    if isinstance(timezone, Unset):
        json_timezone = UNSET
    else:
        json_timezone = timezone
    params["timezone"] = json_timezone

    json_is_bookable: bool | None | Unset
    if isinstance(is_bookable, Unset):
        json_is_bookable = UNSET
    else:
        json_is_bookable = is_bookable
    params["is_bookable"] = json_is_bookable

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
        "url": "/api/v1/{tenant_path}/resource_types".format(
            tenant_path=quote(str(tenant_path), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> OutputTenantResourceTypes | None:
    if response.status_code == 200:
        response_200 = OutputTenantResourceTypes.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[OutputTenantResourceTypes]:
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
    internal_code: None | str | Unset = UNSET,
    timezone: None | str | Unset = UNSET,
    is_bookable: bool | None | Unset = UNSET,
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
) -> Response[OutputTenantResourceTypes]:
    """Tenant Resources

     View your complete resource hierarchy organized by type and category. Returns the
    entire resource tree from departments to individual assets. Essential for resource
    planning, capacity analysis, and organizational structure visualization. Use to
    identify resource gaps and optimization opportunities. Supports filtering by name,
    internal code, bookability status, and timezone.

    Args:
        tenant_path (str):
        exclude_mode (bool | None | Unset): Invert filter logic to exclude matching results
        search (None | str | Unset): Search by name or internal code
        name (None | str | Unset): Filter by resource name
        internal_code (None | str | Unset): Filter by exact internal code
        timezone (None | str | Unset): Filter by timezone
        is_bookable (bool | None | Unset): Filter bookable resources (leaf nodes)
        tags1 (list[str] | None | Unset): Filter by tags (first set)
        tags2 (list[str] | None | Unset): Filter by tags (second set)
        tags3 (list[str] | None | Unset): Filter by tags (third set)
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
        Response[OutputTenantResourceTypes]
    """

    kwargs = _get_kwargs(
        tenant_path=tenant_path,
        exclude_mode=exclude_mode,
        search=search,
        name=name,
        internal_code=internal_code,
        timezone=timezone,
        is_bookable=is_bookable,
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
    internal_code: None | str | Unset = UNSET,
    timezone: None | str | Unset = UNSET,
    is_bookable: bool | None | Unset = UNSET,
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
) -> OutputTenantResourceTypes | None:
    """Tenant Resources

     View your complete resource hierarchy organized by type and category. Returns the
    entire resource tree from departments to individual assets. Essential for resource
    planning, capacity analysis, and organizational structure visualization. Use to
    identify resource gaps and optimization opportunities. Supports filtering by name,
    internal code, bookability status, and timezone.

    Args:
        tenant_path (str):
        exclude_mode (bool | None | Unset): Invert filter logic to exclude matching results
        search (None | str | Unset): Search by name or internal code
        name (None | str | Unset): Filter by resource name
        internal_code (None | str | Unset): Filter by exact internal code
        timezone (None | str | Unset): Filter by timezone
        is_bookable (bool | None | Unset): Filter bookable resources (leaf nodes)
        tags1 (list[str] | None | Unset): Filter by tags (first set)
        tags2 (list[str] | None | Unset): Filter by tags (second set)
        tags3 (list[str] | None | Unset): Filter by tags (third set)
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
        OutputTenantResourceTypes
    """

    return sync_detailed(
        tenant_path=tenant_path,
        client=client,
        exclude_mode=exclude_mode,
        search=search,
        name=name,
        internal_code=internal_code,
        timezone=timezone,
        is_bookable=is_bookable,
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
    internal_code: None | str | Unset = UNSET,
    timezone: None | str | Unset = UNSET,
    is_bookable: bool | None | Unset = UNSET,
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
) -> Response[OutputTenantResourceTypes]:
    """Tenant Resources

     View your complete resource hierarchy organized by type and category. Returns the
    entire resource tree from departments to individual assets. Essential for resource
    planning, capacity analysis, and organizational structure visualization. Use to
    identify resource gaps and optimization opportunities. Supports filtering by name,
    internal code, bookability status, and timezone.

    Args:
        tenant_path (str):
        exclude_mode (bool | None | Unset): Invert filter logic to exclude matching results
        search (None | str | Unset): Search by name or internal code
        name (None | str | Unset): Filter by resource name
        internal_code (None | str | Unset): Filter by exact internal code
        timezone (None | str | Unset): Filter by timezone
        is_bookable (bool | None | Unset): Filter bookable resources (leaf nodes)
        tags1 (list[str] | None | Unset): Filter by tags (first set)
        tags2 (list[str] | None | Unset): Filter by tags (second set)
        tags3 (list[str] | None | Unset): Filter by tags (third set)
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
        Response[OutputTenantResourceTypes]
    """

    kwargs = _get_kwargs(
        tenant_path=tenant_path,
        exclude_mode=exclude_mode,
        search=search,
        name=name,
        internal_code=internal_code,
        timezone=timezone,
        is_bookable=is_bookable,
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
    internal_code: None | str | Unset = UNSET,
    timezone: None | str | Unset = UNSET,
    is_bookable: bool | None | Unset = UNSET,
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
) -> OutputTenantResourceTypes | None:
    """Tenant Resources

     View your complete resource hierarchy organized by type and category. Returns the
    entire resource tree from departments to individual assets. Essential for resource
    planning, capacity analysis, and organizational structure visualization. Use to
    identify resource gaps and optimization opportunities. Supports filtering by name,
    internal code, bookability status, and timezone.

    Args:
        tenant_path (str):
        exclude_mode (bool | None | Unset): Invert filter logic to exclude matching results
        search (None | str | Unset): Search by name or internal code
        name (None | str | Unset): Filter by resource name
        internal_code (None | str | Unset): Filter by exact internal code
        timezone (None | str | Unset): Filter by timezone
        is_bookable (bool | None | Unset): Filter bookable resources (leaf nodes)
        tags1 (list[str] | None | Unset): Filter by tags (first set)
        tags2 (list[str] | None | Unset): Filter by tags (second set)
        tags3 (list[str] | None | Unset): Filter by tags (third set)
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
        OutputTenantResourceTypes
    """

    return (
        await asyncio_detailed(
            tenant_path=tenant_path,
            client=client,
            exclude_mode=exclude_mode,
            search=search,
            name=name,
            internal_code=internal_code,
            timezone=timezone,
            is_bookable=is_bookable,
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
