from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.product_menu_items import ProductMenuItems
from ...types import Response


def _get_kwargs(
    tenant_path: str,
    product_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/{tenant_path}/product_menu_items/{product_id}".format(
            tenant_path=quote(str(tenant_path), safe=""),
            product_id=quote(str(product_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ProductMenuItems | None:
    if response.status_code == 200:
        response_200 = ProductMenuItems.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ProductMenuItems]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    tenant_path: str,
    product_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[ProductMenuItems]:
    """Product Menu Items

     Get product menu items for dynamic UI updates. Returns current state to determine
    which menu actions should be displayed. Used for real-time menu updates
    after state changes without full page reload.

    Args:
        tenant_path (str):
        product_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ProductMenuItems]
    """

    kwargs = _get_kwargs(
        tenant_path=tenant_path,
        product_id=product_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    tenant_path: str,
    product_id: str,
    *,
    client: AuthenticatedClient,
) -> ProductMenuItems | None:
    """Product Menu Items

     Get product menu items for dynamic UI updates. Returns current state to determine
    which menu actions should be displayed. Used for real-time menu updates
    after state changes without full page reload.

    Args:
        tenant_path (str):
        product_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ProductMenuItems
    """

    return sync_detailed(
        tenant_path=tenant_path,
        product_id=product_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    tenant_path: str,
    product_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[ProductMenuItems]:
    """Product Menu Items

     Get product menu items for dynamic UI updates. Returns current state to determine
    which menu actions should be displayed. Used for real-time menu updates
    after state changes without full page reload.

    Args:
        tenant_path (str):
        product_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ProductMenuItems]
    """

    kwargs = _get_kwargs(
        tenant_path=tenant_path,
        product_id=product_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    tenant_path: str,
    product_id: str,
    *,
    client: AuthenticatedClient,
) -> ProductMenuItems | None:
    """Product Menu Items

     Get product menu items for dynamic UI updates. Returns current state to determine
    which menu actions should be displayed. Used for real-time menu updates
    after state changes without full page reload.

    Args:
        tenant_path (str):
        product_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ProductMenuItems
    """

    return (
        await asyncio_detailed(
            tenant_path=tenant_path,
            product_id=product_id,
            client=client,
        )
    ).parsed
