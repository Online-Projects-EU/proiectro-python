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
    tenant_path: str,
    customer_org_external_id: str,
    asset_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/{tenant_path}/portal/{customer_org_external_id}/asset_tickets/{asset_id}".format(
            tenant_path=quote(str(tenant_path), safe=""),
            customer_org_external_id=quote(str(customer_org_external_id), safe=""),
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
    tenant_path: str,
    customer_org_external_id: str,
    asset_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[OutputCustomerPortalAssetTickets]:
    """Team Preview Portal Asset Tickets

     Preview customer portal asset tickets as team member.
    Returns ESRs linked to a specific asset of a customer organization.

    Args:
        tenant_path (str):
        customer_org_external_id (str):
        asset_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OutputCustomerPortalAssetTickets]
    """

    kwargs = _get_kwargs(
        tenant_path=tenant_path,
        customer_org_external_id=customer_org_external_id,
        asset_id=asset_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    tenant_path: str,
    customer_org_external_id: str,
    asset_id: str,
    *,
    client: AuthenticatedClient,
) -> OutputCustomerPortalAssetTickets | None:
    """Team Preview Portal Asset Tickets

     Preview customer portal asset tickets as team member.
    Returns ESRs linked to a specific asset of a customer organization.

    Args:
        tenant_path (str):
        customer_org_external_id (str):
        asset_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OutputCustomerPortalAssetTickets
    """

    return sync_detailed(
        tenant_path=tenant_path,
        customer_org_external_id=customer_org_external_id,
        asset_id=asset_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    tenant_path: str,
    customer_org_external_id: str,
    asset_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[OutputCustomerPortalAssetTickets]:
    """Team Preview Portal Asset Tickets

     Preview customer portal asset tickets as team member.
    Returns ESRs linked to a specific asset of a customer organization.

    Args:
        tenant_path (str):
        customer_org_external_id (str):
        asset_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OutputCustomerPortalAssetTickets]
    """

    kwargs = _get_kwargs(
        tenant_path=tenant_path,
        customer_org_external_id=customer_org_external_id,
        asset_id=asset_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    tenant_path: str,
    customer_org_external_id: str,
    asset_id: str,
    *,
    client: AuthenticatedClient,
) -> OutputCustomerPortalAssetTickets | None:
    """Team Preview Portal Asset Tickets

     Preview customer portal asset tickets as team member.
    Returns ESRs linked to a specific asset of a customer organization.

    Args:
        tenant_path (str):
        customer_org_external_id (str):
        asset_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OutputCustomerPortalAssetTickets
    """

    return (
        await asyncio_detailed(
            tenant_path=tenant_path,
            customer_org_external_id=customer_org_external_id,
            asset_id=asset_id,
            client=client,
        )
    ).parsed
