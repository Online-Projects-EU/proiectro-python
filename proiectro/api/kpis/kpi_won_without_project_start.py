from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.output_kpi_won_without_project_start import (
    OutputKPIWonWithoutProjectStart,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    tenant_path: str,
    *,
    days_since_won_gte: int | Unset = 7,
    include_items: bool | Unset = False,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["days_since_won_gte"] = days_since_won_gte

    params["include_items"] = include_items

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/{tenant_path}/kpi/won_without_project_start".format(
            tenant_path=quote(str(tenant_path), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> OutputKPIWonWithoutProjectStart | None:
    if response.status_code == 200:
        response_200 = OutputKPIWonWithoutProjectStart.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[OutputKPIWonWithoutProjectStart]:
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
    days_since_won_gte: int | Unset = 7,
    include_items: bool | Unset = False,
) -> Response[OutputKPIWonWithoutProjectStart]:
    """Kpi Won Without Project Start

    Args:
        tenant_path (str):
        days_since_won_gte (int | Unset):  Default: 7.
        include_items (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OutputKPIWonWithoutProjectStart]
    """

    kwargs = _get_kwargs(
        tenant_path=tenant_path,
        days_since_won_gte=days_since_won_gte,
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
    days_since_won_gte: int | Unset = 7,
    include_items: bool | Unset = False,
) -> OutputKPIWonWithoutProjectStart | None:
    """Kpi Won Without Project Start

    Args:
        tenant_path (str):
        days_since_won_gte (int | Unset):  Default: 7.
        include_items (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OutputKPIWonWithoutProjectStart
    """

    return sync_detailed(
        tenant_path=tenant_path,
        client=client,
        days_since_won_gte=days_since_won_gte,
        include_items=include_items,
    ).parsed


async def asyncio_detailed(
    tenant_path: str,
    *,
    client: AuthenticatedClient,
    days_since_won_gte: int | Unset = 7,
    include_items: bool | Unset = False,
) -> Response[OutputKPIWonWithoutProjectStart]:
    """Kpi Won Without Project Start

    Args:
        tenant_path (str):
        days_since_won_gte (int | Unset):  Default: 7.
        include_items (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OutputKPIWonWithoutProjectStart]
    """

    kwargs = _get_kwargs(
        tenant_path=tenant_path,
        days_since_won_gte=days_since_won_gte,
        include_items=include_items,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    tenant_path: str,
    *,
    client: AuthenticatedClient,
    days_since_won_gte: int | Unset = 7,
    include_items: bool | Unset = False,
) -> OutputKPIWonWithoutProjectStart | None:
    """Kpi Won Without Project Start

    Args:
        tenant_path (str):
        days_since_won_gte (int | Unset):  Default: 7.
        include_items (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OutputKPIWonWithoutProjectStart
    """

    return (
        await asyncio_detailed(
            tenant_path=tenant_path,
            client=client,
            days_since_won_gte=days_since_won_gte,
            include_items=include_items,
        )
    ).parsed
