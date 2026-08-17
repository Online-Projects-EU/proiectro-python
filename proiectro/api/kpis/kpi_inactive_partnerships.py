from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.output_kpi_inactive_partnerships import OutputKPIInactivePartnerships
from ...types import UNSET, Response, Unset


def _get_kwargs(
    tenant_path: str,
    *,
    days_inactive_gte: int | None | Unset = UNSET,
    include_items: bool | Unset = False,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_days_inactive_gte: int | None | Unset
    if isinstance(days_inactive_gte, Unset):
        json_days_inactive_gte = UNSET
    else:
        json_days_inactive_gte = days_inactive_gte
    params["days_inactive_gte"] = json_days_inactive_gte

    params["include_items"] = include_items

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/{tenant_path}/kpi/inactive_partnerships".format(
            tenant_path=quote(str(tenant_path), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> OutputKPIInactivePartnerships | None:
    if response.status_code == 200:
        response_200 = OutputKPIInactivePartnerships.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[OutputKPIInactivePartnerships]:
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
    days_inactive_gte: int | None | Unset = UNSET,
    include_items: bool | Unset = False,
) -> Response[OutputKPIInactivePartnerships]:
    """Kpi Inactive Partnerships

    Args:
        tenant_path (str):
        days_inactive_gte (int | None | Unset):
        include_items (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OutputKPIInactivePartnerships]
    """

    kwargs = _get_kwargs(
        tenant_path=tenant_path,
        days_inactive_gte=days_inactive_gte,
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
    days_inactive_gte: int | None | Unset = UNSET,
    include_items: bool | Unset = False,
) -> OutputKPIInactivePartnerships | None:
    """Kpi Inactive Partnerships

    Args:
        tenant_path (str):
        days_inactive_gte (int | None | Unset):
        include_items (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OutputKPIInactivePartnerships
    """

    return sync_detailed(
        tenant_path=tenant_path,
        client=client,
        days_inactive_gte=days_inactive_gte,
        include_items=include_items,
    ).parsed


async def asyncio_detailed(
    tenant_path: str,
    *,
    client: AuthenticatedClient,
    days_inactive_gte: int | None | Unset = UNSET,
    include_items: bool | Unset = False,
) -> Response[OutputKPIInactivePartnerships]:
    """Kpi Inactive Partnerships

    Args:
        tenant_path (str):
        days_inactive_gte (int | None | Unset):
        include_items (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OutputKPIInactivePartnerships]
    """

    kwargs = _get_kwargs(
        tenant_path=tenant_path,
        days_inactive_gte=days_inactive_gte,
        include_items=include_items,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    tenant_path: str,
    *,
    client: AuthenticatedClient,
    days_inactive_gte: int | None | Unset = UNSET,
    include_items: bool | Unset = False,
) -> OutputKPIInactivePartnerships | None:
    """Kpi Inactive Partnerships

    Args:
        tenant_path (str):
        days_inactive_gte (int | None | Unset):
        include_items (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OutputKPIInactivePartnerships
    """

    return (
        await asyncio_detailed(
            tenant_path=tenant_path,
            client=client,
            days_inactive_gte=days_inactive_gte,
            include_items=include_items,
        )
    ).parsed
