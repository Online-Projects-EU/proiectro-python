from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.output_customer_portal_asset_detail import (
    OutputCustomerPortalAssetDetail,
)
from ...types import Response


def _get_kwargs(
    customer_org_id: str,
    asset_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/portal/{customer_org_id}/asset_detail/{asset_id}".format(
            customer_org_id=quote(str(customer_org_id), safe=""),
            asset_id=quote(str(asset_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> OutputCustomerPortalAssetDetail | None:
    if response.status_code == 200:
        response_200 = OutputCustomerPortalAssetDetail.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[OutputCustomerPortalAssetDetail]:
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
) -> Response[OutputCustomerPortalAssetDetail]:
    """Portal Asset Detail

     Get asset detail for customer portal.
    Returns asset properties including category, status, location, and dates.

    Args:
        customer_org_id (str):
        asset_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OutputCustomerPortalAssetDetail]
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
) -> OutputCustomerPortalAssetDetail | None:
    """Portal Asset Detail

     Get asset detail for customer portal.
    Returns asset properties including category, status, location, and dates.

    Args:
        customer_org_id (str):
        asset_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OutputCustomerPortalAssetDetail
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
) -> Response[OutputCustomerPortalAssetDetail]:
    """Portal Asset Detail

     Get asset detail for customer portal.
    Returns asset properties including category, status, location, and dates.

    Args:
        customer_org_id (str):
        asset_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OutputCustomerPortalAssetDetail]
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
) -> OutputCustomerPortalAssetDetail | None:
    """Portal Asset Detail

     Get asset detail for customer portal.
    Returns asset properties including category, status, location, and dates.

    Args:
        customer_org_id (str):
        asset_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OutputCustomerPortalAssetDetail
    """

    return (
        await asyncio_detailed(
            customer_org_id=customer_org_id,
            asset_id=asset_id,
            client=client,
        )
    ).parsed
