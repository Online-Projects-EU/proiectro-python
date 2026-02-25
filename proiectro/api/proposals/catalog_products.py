from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.catalog_products import CatalogProducts
from ...types import Response


def _get_kwargs(
    tenant_path: str,
    pricing_type: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/{tenant_path}/catalog_products/{pricing_type}".format(
            tenant_path=quote(str(tenant_path), safe=""),
            pricing_type=quote(str(pricing_type), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> CatalogProducts | None:
    if response.status_code == 200:
        response_200 = CatalogProducts.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[CatalogProducts]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    tenant_path: str,
    pricing_type: str,
    *,
    client: AuthenticatedClient,
) -> Response[CatalogProducts]:
    """Catalog Products

     Browse available products filtered by pricing model (fixed, hourly, subscription).
    Essential for building proposals with appropriate product mix. Shows product
    details, standard pricing, and availability. Organized for quick selection during
    proposal creation.

    Args:
        tenant_path (str):
        pricing_type (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CatalogProducts]
    """

    kwargs = _get_kwargs(
        tenant_path=tenant_path,
        pricing_type=pricing_type,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    tenant_path: str,
    pricing_type: str,
    *,
    client: AuthenticatedClient,
) -> CatalogProducts | None:
    """Catalog Products

     Browse available products filtered by pricing model (fixed, hourly, subscription).
    Essential for building proposals with appropriate product mix. Shows product
    details, standard pricing, and availability. Organized for quick selection during
    proposal creation.

    Args:
        tenant_path (str):
        pricing_type (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CatalogProducts
    """

    return sync_detailed(
        tenant_path=tenant_path,
        pricing_type=pricing_type,
        client=client,
    ).parsed


async def asyncio_detailed(
    tenant_path: str,
    pricing_type: str,
    *,
    client: AuthenticatedClient,
) -> Response[CatalogProducts]:
    """Catalog Products

     Browse available products filtered by pricing model (fixed, hourly, subscription).
    Essential for building proposals with appropriate product mix. Shows product
    details, standard pricing, and availability. Organized for quick selection during
    proposal creation.

    Args:
        tenant_path (str):
        pricing_type (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CatalogProducts]
    """

    kwargs = _get_kwargs(
        tenant_path=tenant_path,
        pricing_type=pricing_type,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    tenant_path: str,
    pricing_type: str,
    *,
    client: AuthenticatedClient,
) -> CatalogProducts | None:
    """Catalog Products

     Browse available products filtered by pricing model (fixed, hourly, subscription).
    Essential for building proposals with appropriate product mix. Shows product
    details, standard pricing, and availability. Organized for quick selection during
    proposal creation.

    Args:
        tenant_path (str):
        pricing_type (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CatalogProducts
    """

    return (
        await asyncio_detailed(
            tenant_path=tenant_path,
            pricing_type=pricing_type,
            client=client,
        )
    ).parsed
