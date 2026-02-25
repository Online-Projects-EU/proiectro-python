from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.add_custom_product import AddCustomProduct
from ...models.add_custom_product_response import AddCustomProductResponse
from ...models.api_response import APIResponse
from ...types import Response


def _get_kwargs(
    tenant_path: str,
    *,
    body: AddCustomProduct,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/{tenant_path}/add_custom_product".format(
            tenant_path=quote(str(tenant_path), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> APIResponse | AddCustomProductResponse | None:
    if response.status_code == 200:
        response_200 = APIResponse.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = APIResponse.from_dict(response.json())

        return response_400

    if response.status_code == 422:
        response_422 = AddCustomProductResponse.from_dict(response.json())

        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[APIResponse | AddCustomProductResponse]:
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
    body: AddCustomProduct,
) -> Response[APIResponse | AddCustomProductResponse]:
    """Add Custom Product

     Create one-off products for unique customer requirements not in your standard catalog.
    Allows complete flexibility in specifications, pricing, and terms. Custom products
    require additional approval workflows to ensure profitability. Consider adding
    successful custom products to your catalog for future reuse.

    Args:
        tenant_path (str):
        body (AddCustomProduct):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[APIResponse | AddCustomProductResponse]
    """

    kwargs = _get_kwargs(
        tenant_path=tenant_path,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    tenant_path: str,
    *,
    client: AuthenticatedClient,
    body: AddCustomProduct,
) -> APIResponse | AddCustomProductResponse | None:
    """Add Custom Product

     Create one-off products for unique customer requirements not in your standard catalog.
    Allows complete flexibility in specifications, pricing, and terms. Custom products
    require additional approval workflows to ensure profitability. Consider adding
    successful custom products to your catalog for future reuse.

    Args:
        tenant_path (str):
        body (AddCustomProduct):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        APIResponse | AddCustomProductResponse
    """

    return sync_detailed(
        tenant_path=tenant_path,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    tenant_path: str,
    *,
    client: AuthenticatedClient,
    body: AddCustomProduct,
) -> Response[APIResponse | AddCustomProductResponse]:
    """Add Custom Product

     Create one-off products for unique customer requirements not in your standard catalog.
    Allows complete flexibility in specifications, pricing, and terms. Custom products
    require additional approval workflows to ensure profitability. Consider adding
    successful custom products to your catalog for future reuse.

    Args:
        tenant_path (str):
        body (AddCustomProduct):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[APIResponse | AddCustomProductResponse]
    """

    kwargs = _get_kwargs(
        tenant_path=tenant_path,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    tenant_path: str,
    *,
    client: AuthenticatedClient,
    body: AddCustomProduct,
) -> APIResponse | AddCustomProductResponse | None:
    """Add Custom Product

     Create one-off products for unique customer requirements not in your standard catalog.
    Allows complete flexibility in specifications, pricing, and terms. Custom products
    require additional approval workflows to ensure profitability. Consider adding
    successful custom products to your catalog for future reuse.

    Args:
        tenant_path (str):
        body (AddCustomProduct):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        APIResponse | AddCustomProductResponse
    """

    return (
        await asyncio_detailed(
            tenant_path=tenant_path,
            client=client,
            body=body,
        )
    ).parsed
