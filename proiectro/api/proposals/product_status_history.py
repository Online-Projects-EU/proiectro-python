from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.product_status_history_output import ProductStatusHistoryOutput
from ...types import Response


def _get_kwargs(
    tenant_path: str,
    product_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/{tenant_path}/product_status_history/{product_id}".format(
            tenant_path=quote(str(tenant_path), safe=""),
            product_id=quote(str(product_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ProductStatusHistoryOutput | None:
    if response.status_code == 200:
        response_200 = ProductStatusHistoryOutput.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ProductStatusHistoryOutput]:
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
) -> Response[ProductStatusHistoryOutput]:
    """Product Status History

     View complete status history for a product showing progression through lifecycle stages.
    Displays chronological timeline of status changes with timestamps, reasons, and responsible
    team members. Essential for understanding product delivery progress, audit compliance,
    and workflow analysis.

    Args:
        tenant_path (str):
        product_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ProductStatusHistoryOutput]
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
) -> ProductStatusHistoryOutput | None:
    """Product Status History

     View complete status history for a product showing progression through lifecycle stages.
    Displays chronological timeline of status changes with timestamps, reasons, and responsible
    team members. Essential for understanding product delivery progress, audit compliance,
    and workflow analysis.

    Args:
        tenant_path (str):
        product_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ProductStatusHistoryOutput
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
) -> Response[ProductStatusHistoryOutput]:
    """Product Status History

     View complete status history for a product showing progression through lifecycle stages.
    Displays chronological timeline of status changes with timestamps, reasons, and responsible
    team members. Essential for understanding product delivery progress, audit compliance,
    and workflow analysis.

    Args:
        tenant_path (str):
        product_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ProductStatusHistoryOutput]
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
) -> ProductStatusHistoryOutput | None:
    """Product Status History

     View complete status history for a product showing progression through lifecycle stages.
    Displays chronological timeline of status changes with timestamps, reasons, and responsible
    team members. Essential for understanding product delivery progress, audit compliance,
    and workflow analysis.

    Args:
        tenant_path (str):
        product_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ProductStatusHistoryOutput
    """

    return (
        await asyncio_detailed(
            tenant_path=tenant_path,
            product_id=product_id,
            client=client,
        )
    ).parsed
