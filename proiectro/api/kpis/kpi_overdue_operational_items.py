from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.output_kpi_overdue_operational_items import (
    OutputKPIOverdueOperationalItems,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    tenant_path: str,
    *,
    days_overdue_gte: int | None | Unset = UNSET,
    process_id: None | str | Unset = UNSET,
    priority: None | str | Unset = UNSET,
    include_items: bool | Unset = False,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_days_overdue_gte: int | None | Unset
    if isinstance(days_overdue_gte, Unset):
        json_days_overdue_gte = UNSET
    else:
        json_days_overdue_gte = days_overdue_gte
    params["days_overdue_gte"] = json_days_overdue_gte

    json_process_id: None | str | Unset
    if isinstance(process_id, Unset):
        json_process_id = UNSET
    else:
        json_process_id = process_id
    params["process_id"] = json_process_id

    json_priority: None | str | Unset
    if isinstance(priority, Unset):
        json_priority = UNSET
    else:
        json_priority = priority
    params["priority"] = json_priority

    params["include_items"] = include_items

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/{tenant_path}/kpi/overdue_operational_items".format(
            tenant_path=quote(str(tenant_path), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> OutputKPIOverdueOperationalItems | None:
    if response.status_code == 200:
        response_200 = OutputKPIOverdueOperationalItems.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[OutputKPIOverdueOperationalItems]:
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
    days_overdue_gte: int | None | Unset = UNSET,
    process_id: None | str | Unset = UNSET,
    priority: None | str | Unset = UNSET,
    include_items: bool | Unset = False,
) -> Response[OutputKPIOverdueOperationalItems]:
    """Kpi Overdue Operational Items

    Args:
        tenant_path (str):
        days_overdue_gte (int | None | Unset):
        process_id (None | str | Unset):
        priority (None | str | Unset):
        include_items (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OutputKPIOverdueOperationalItems]
    """

    kwargs = _get_kwargs(
        tenant_path=tenant_path,
        days_overdue_gte=days_overdue_gte,
        process_id=process_id,
        priority=priority,
        include_items=include_items,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    tenant_path: str,
    *,
    client: AuthenticatedClient,
    days_overdue_gte: int | None | Unset = UNSET,
    process_id: None | str | Unset = UNSET,
    priority: None | str | Unset = UNSET,
    include_items: bool | Unset = False,
) -> OutputKPIOverdueOperationalItems | None:
    """Kpi Overdue Operational Items

    Args:
        tenant_path (str):
        days_overdue_gte (int | None | Unset):
        process_id (None | str | Unset):
        priority (None | str | Unset):
        include_items (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OutputKPIOverdueOperationalItems
    """

    return sync_detailed(
        tenant_path=tenant_path,
        client=client,
        days_overdue_gte=days_overdue_gte,
        process_id=process_id,
        priority=priority,
        include_items=include_items,
    ).parsed


async def asyncio_detailed(
    tenant_path: str,
    *,
    client: AuthenticatedClient,
    days_overdue_gte: int | None | Unset = UNSET,
    process_id: None | str | Unset = UNSET,
    priority: None | str | Unset = UNSET,
    include_items: bool | Unset = False,
) -> Response[OutputKPIOverdueOperationalItems]:
    """Kpi Overdue Operational Items

    Args:
        tenant_path (str):
        days_overdue_gte (int | None | Unset):
        process_id (None | str | Unset):
        priority (None | str | Unset):
        include_items (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OutputKPIOverdueOperationalItems]
    """

    kwargs = _get_kwargs(
        tenant_path=tenant_path,
        days_overdue_gte=days_overdue_gte,
        process_id=process_id,
        priority=priority,
        include_items=include_items,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    tenant_path: str,
    *,
    client: AuthenticatedClient,
    days_overdue_gte: int | None | Unset = UNSET,
    process_id: None | str | Unset = UNSET,
    priority: None | str | Unset = UNSET,
    include_items: bool | Unset = False,
) -> OutputKPIOverdueOperationalItems | None:
    """Kpi Overdue Operational Items

    Args:
        tenant_path (str):
        days_overdue_gte (int | None | Unset):
        process_id (None | str | Unset):
        priority (None | str | Unset):
        include_items (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OutputKPIOverdueOperationalItems
    """

    return (
        await asyncio_detailed(
            tenant_path=tenant_path,
            client=client,
            days_overdue_gte=days_overdue_gte,
            process_id=process_id,
            priority=priority,
            include_items=include_items,
        )
    ).parsed
