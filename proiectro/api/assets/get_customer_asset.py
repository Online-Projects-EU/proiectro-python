from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.output_customer_asset import OutputCustomerAsset
from ...types import Response


def _get_kwargs(
    tenant_path: str,
    asset_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/{tenant_path}/customer_asset/{asset_id}".format(
            tenant_path=quote(str(tenant_path), safe=""),
            asset_id=quote(str(asset_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> OutputCustomerAsset | None:
    if response.status_code == 200:
        response_200 = OutputCustomerAsset.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[OutputCustomerAsset]:
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
) -> Response[OutputCustomerAsset]:
    """Get Customer Asset

     View a single customer asset by id.
    Returns the same fields as the asset lists, including coordinates,
    for detail consumers such as the mobile app's QR scan flow.

    Args:
        tenant_path (str):
        asset_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OutputCustomerAsset]
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
) -> OutputCustomerAsset | None:
    """Get Customer Asset

     View a single customer asset by id.
    Returns the same fields as the asset lists, including coordinates,
    for detail consumers such as the mobile app's QR scan flow.

    Args:
        tenant_path (str):
        asset_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OutputCustomerAsset
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
) -> Response[OutputCustomerAsset]:
    """Get Customer Asset

     View a single customer asset by id.
    Returns the same fields as the asset lists, including coordinates,
    for detail consumers such as the mobile app's QR scan flow.

    Args:
        tenant_path (str):
        asset_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OutputCustomerAsset]
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
) -> OutputCustomerAsset | None:
    """Get Customer Asset

     View a single customer asset by id.
    Returns the same fields as the asset lists, including coordinates,
    for detail consumers such as the mobile app's QR scan flow.

    Args:
        tenant_path (str):
        asset_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OutputCustomerAsset
    """

    return (
        await asyncio_detailed(
            tenant_path=tenant_path,
            asset_id=asset_id,
            client=client,
        )
    ).parsed
