from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.output_customer_portal_asset_tickets import (
    OutputCustomerPortalAssetTickets,
)
from ...types import Response


def _get_kwargs(
    customer_org_id: str,
    asset_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/portal/{customer_org_id}/asset_closed_tickets/{asset_id}".format(
            customer_org_id=quote(str(customer_org_id), safe=""),
            asset_id=quote(str(asset_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> OutputCustomerPortalAssetTickets | None:
    if response.status_code == 200:
        response_200 = OutputCustomerPortalAssetTickets.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[OutputCustomerPortalAssetTickets]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    customer_org_id: str,
    asset_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[OutputCustomerPortalAssetTickets]:
    """Portal Asset Closed Tickets

     Get closed support requests linked to an asset (reported_asset only).
    Returns closed ESRs where this asset was reported as the issue source.

    Args:
        customer_org_id (str):
        asset_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OutputCustomerPortalAssetTickets]
    """

    kwargs = _get_kwargs(
        customer_org_id=customer_org_id,
        asset_id=asset_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    customer_org_id: str,
    asset_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> OutputCustomerPortalAssetTickets | None:
    """Portal Asset Closed Tickets

     Get closed support requests linked to an asset (reported_asset only).
    Returns closed ESRs where this asset was reported as the issue source.

    Args:
        customer_org_id (str):
        asset_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OutputCustomerPortalAssetTickets
    """

    return sync_detailed(
        customer_org_id=customer_org_id,
        asset_id=asset_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    customer_org_id: str,
    asset_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[OutputCustomerPortalAssetTickets]:
    """Portal Asset Closed Tickets

     Get closed support requests linked to an asset (reported_asset only).
    Returns closed ESRs where this asset was reported as the issue source.

    Args:
        customer_org_id (str):
        asset_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OutputCustomerPortalAssetTickets]
    """

    kwargs = _get_kwargs(
        customer_org_id=customer_org_id,
        asset_id=asset_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    customer_org_id: str,
    asset_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> OutputCustomerPortalAssetTickets | None:
    """Portal Asset Closed Tickets

     Get closed support requests linked to an asset (reported_asset only).
    Returns closed ESRs where this asset was reported as the issue source.

    Args:
        customer_org_id (str):
        asset_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OutputCustomerPortalAssetTickets
    """

    return (
        await asyncio_detailed(
            customer_org_id=customer_org_id,
            asset_id=asset_id,
            client=client,
        )
    ).parsed
