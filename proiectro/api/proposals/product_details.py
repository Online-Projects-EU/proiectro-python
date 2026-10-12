from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.output_product_details import OutputProductDetails
from ...types import Response


def _get_kwargs(
    tenant_path: str,
    product_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/{tenant_path}/product_details/{product_id}".format(
            tenant_path=quote(str(tenant_path), safe=""),
            product_id=quote(str(product_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> OutputProductDetails | None:
    if response.status_code == 200:
        response_200 = OutputProductDetails.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[OutputProductDetails]:
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
) -> Response[OutputProductDetails]:
    """Product Details

     Examine comprehensive product performance including sales history, customer segments,
    and profitability metrics. Shows adoption trends and competitive positioning.
    Essential for product lifecycle management and pricing decisions. Includes customer
    feedback and satisfaction metrics when available.

    Args:
        tenant_path (str):
        product_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OutputProductDetails]
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
) -> OutputProductDetails | None:
    """Product Details

     Examine comprehensive product performance including sales history, customer segments,
    and profitability metrics. Shows adoption trends and competitive positioning.
    Essential for product lifecycle management and pricing decisions. Includes customer
    feedback and satisfaction metrics when available.

    Args:
        tenant_path (str):
        product_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OutputProductDetails
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
) -> Response[OutputProductDetails]:
    """Product Details

     Examine comprehensive product performance including sales history, customer segments,
    and profitability metrics. Shows adoption trends and competitive positioning.
    Essential for product lifecycle management and pricing decisions. Includes customer
    feedback and satisfaction metrics when available.

    Args:
        tenant_path (str):
        product_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OutputProductDetails]
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
) -> OutputProductDetails | None:
    """Product Details

     Examine comprehensive product performance including sales history, customer segments,
    and profitability metrics. Shows adoption trends and competitive positioning.
    Essential for product lifecycle management and pricing decisions. Includes customer
    feedback and satisfaction metrics when available.

    Args:
        tenant_path (str):
        product_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OutputProductDetails
    """

    return (
        await asyncio_detailed(
            tenant_path=tenant_path,
            product_id=product_id,
            client=client,
        )
    ).parsed
