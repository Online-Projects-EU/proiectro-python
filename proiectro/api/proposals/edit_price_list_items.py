from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_response import APIResponse
from ...models.edit_price_list_items import EditPriceListItems
from ...models.pydantic_detail import PydanticDetail
from ...types import Response


def _get_kwargs(
    tenant_path: str,
    price_list_id: str,
    *,
    body: EditPriceListItems,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/api/v1/{tenant_path}/edit_price_list_items/{price_list_id}".format(
            tenant_path=quote(str(tenant_path), safe=""),
            price_list_id=quote(str(price_list_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> APIResponse | PydanticDetail | None:
    if response.status_code == 200:
        response_200 = APIResponse.from_dict(response.json())

        return response_200

    if response.status_code == 404:
        response_404 = APIResponse.from_dict(response.json())

        return response_404

    if response.status_code == 422:
        response_422 = PydanticDetail.from_dict(response.json())

        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[APIResponse | PydanticDetail]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    tenant_path: str,
    price_list_id: str,
    *,
    client: AuthenticatedClient,
    body: EditPriceListItems,
) -> Response[APIResponse | PydanticDetail]:
    """Edit Price List Items

     Set a price list's items, each at its catalog price or at a custom price.
    An item can have a custom price in only one of the price lists a customer or partner holds.

    Args:
        tenant_path (str):
        price_list_id (str):
        body (EditPriceListItems): The list's items, as a whole: items left out leave the list.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[APIResponse | PydanticDetail]
    """

    kwargs = _get_kwargs(
        tenant_path=tenant_path,
        price_list_id=price_list_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    tenant_path: str,
    price_list_id: str,
    *,
    client: AuthenticatedClient,
    body: EditPriceListItems,
) -> APIResponse | PydanticDetail | None:
    """Edit Price List Items

     Set a price list's items, each at its catalog price or at a custom price.
    An item can have a custom price in only one of the price lists a customer or partner holds.

    Args:
        tenant_path (str):
        price_list_id (str):
        body (EditPriceListItems): The list's items, as a whole: items left out leave the list.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        APIResponse | PydanticDetail
    """

    return sync_detailed(
        tenant_path=tenant_path,
        price_list_id=price_list_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    tenant_path: str,
    price_list_id: str,
    *,
    client: AuthenticatedClient,
    body: EditPriceListItems,
) -> Response[APIResponse | PydanticDetail]:
    """Edit Price List Items

     Set a price list's items, each at its catalog price or at a custom price.
    An item can have a custom price in only one of the price lists a customer or partner holds.

    Args:
        tenant_path (str):
        price_list_id (str):
        body (EditPriceListItems): The list's items, as a whole: items left out leave the list.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[APIResponse | PydanticDetail]
    """

    kwargs = _get_kwargs(
        tenant_path=tenant_path,
        price_list_id=price_list_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    tenant_path: str,
    price_list_id: str,
    *,
    client: AuthenticatedClient,
    body: EditPriceListItems,
) -> APIResponse | PydanticDetail | None:
    """Edit Price List Items

     Set a price list's items, each at its catalog price or at a custom price.
    An item can have a custom price in only one of the price lists a customer or partner holds.

    Args:
        tenant_path (str):
        price_list_id (str):
        body (EditPriceListItems): The list's items, as a whole: items left out leave the list.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        APIResponse | PydanticDetail
    """

    return (
        await asyncio_detailed(
            tenant_path=tenant_path,
            price_list_id=price_list_id,
            client=client,
            body=body,
        )
    ).parsed
