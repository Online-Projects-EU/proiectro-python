from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.output_customer_asset_tickets import OutputCustomerAssetTickets
from ...types import Response


def _get_kwargs(
    tenant_path: str,
    asset_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/{tenant_path}/list_customer_asset_tickets/{asset_id}".format(
            tenant_path=quote(str(tenant_path), safe=""),
            asset_id=quote(str(asset_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> OutputCustomerAssetTickets | None:
    if response.status_code == 200:
        response_200 = OutputCustomerAssetTickets.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[OutputCustomerAssetTickets]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    tenant_path: str,
    asset_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[OutputCustomerAssetTickets]:
    """List Customer Asset Tickets

     View all support tickets linked to a specific customer asset.
    Shows both ISR and ESR where this asset is the reported asset or root cause asset.

    Args:
        tenant_path (str):
        asset_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OutputCustomerAssetTickets]
    """

    kwargs = _get_kwargs(
        tenant_path=tenant_path,
        asset_id=asset_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    tenant_path: str,
    asset_id: str,
    *,
    client: AuthenticatedClient,
) -> OutputCustomerAssetTickets | None:
    """List Customer Asset Tickets

     View all support tickets linked to a specific customer asset.
    Shows both ISR and ESR where this asset is the reported asset or root cause asset.

    Args:
        tenant_path (str):
        asset_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OutputCustomerAssetTickets
    """

    return sync_detailed(
        tenant_path=tenant_path,
        asset_id=asset_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    tenant_path: str,
    asset_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[OutputCustomerAssetTickets]:
    """List Customer Asset Tickets

     View all support tickets linked to a specific customer asset.
    Shows both ISR and ESR where this asset is the reported asset or root cause asset.

    Args:
        tenant_path (str):
        asset_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OutputCustomerAssetTickets]
    """

    kwargs = _get_kwargs(
        tenant_path=tenant_path,
        asset_id=asset_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    tenant_path: str,
    asset_id: str,
    *,
    client: AuthenticatedClient,
) -> OutputCustomerAssetTickets | None:
    """List Customer Asset Tickets

     View all support tickets linked to a specific customer asset.
    Shows both ISR and ESR where this asset is the reported asset or root cause asset.

    Args:
        tenant_path (str):
        asset_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OutputCustomerAssetTickets
    """

    return (
        await asyncio_detailed(
            tenant_path=tenant_path,
            asset_id=asset_id,
            client=client,
        )
    ).parsed
