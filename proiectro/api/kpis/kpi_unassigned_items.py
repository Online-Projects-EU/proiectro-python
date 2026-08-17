from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.output_kpi_unassigned_items import OutputKPIUnassignedItems
from ...types import UNSET, Response, Unset


def _get_kwargs(
    tenant_path: str,
    *,
    older_than_hours: int | None | Unset = UNSET,
    include_items: bool | Unset = False,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_older_than_hours: int | None | Unset
    if isinstance(older_than_hours, Unset):
        json_older_than_hours = UNSET
    else:
        json_older_than_hours = older_than_hours
    params["older_than_hours"] = json_older_than_hours

    params["include_items"] = include_items

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/{tenant_path}/kpi/unassigned_items".format(
            tenant_path=quote(str(tenant_path), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> OutputKPIUnassignedItems | None:
    if response.status_code == 200:
        response_200 = OutputKPIUnassignedItems.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[OutputKPIUnassignedItems]:
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
    older_than_hours: int | None | Unset = UNSET,
    include_items: bool | Unset = False,
) -> Response[OutputKPIUnassignedItems]:
    """Kpi Unassigned Items

    Args:
        tenant_path (str):
        older_than_hours (int | None | Unset):
        include_items (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OutputKPIUnassignedItems]
    """

    kwargs = _get_kwargs(
        tenant_path=tenant_path,
        older_than_hours=older_than_hours,
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
    older_than_hours: int | None | Unset = UNSET,
    include_items: bool | Unset = False,
) -> OutputKPIUnassignedItems | None:
    """Kpi Unassigned Items

    Args:
        tenant_path (str):
        older_than_hours (int | None | Unset):
        include_items (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OutputKPIUnassignedItems
    """

    return sync_detailed(
        tenant_path=tenant_path,
        client=client,
        older_than_hours=older_than_hours,
        include_items=include_items,
    ).parsed


async def asyncio_detailed(
    tenant_path: str,
    *,
    client: AuthenticatedClient,
    older_than_hours: int | None | Unset = UNSET,
    include_items: bool | Unset = False,
) -> Response[OutputKPIUnassignedItems]:
    """Kpi Unassigned Items

    Args:
        tenant_path (str):
        older_than_hours (int | None | Unset):
        include_items (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OutputKPIUnassignedItems]
    """

    kwargs = _get_kwargs(
        tenant_path=tenant_path,
        older_than_hours=older_than_hours,
        include_items=include_items,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    tenant_path: str,
    *,
    client: AuthenticatedClient,
    older_than_hours: int | None | Unset = UNSET,
    include_items: bool | Unset = False,
) -> OutputKPIUnassignedItems | None:
    """Kpi Unassigned Items

    Args:
        tenant_path (str):
        older_than_hours (int | None | Unset):
        include_items (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OutputKPIUnassignedItems
    """

    return (
        await asyncio_detailed(
            tenant_path=tenant_path,
            client=client,
            older_than_hours=older_than_hours,
            include_items=include_items,
        )
    ).parsed
