from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.output_block_payments import OutputBlockPayments
from ...types import Response


def _get_kwargs(
    tenant_path: str,
    block_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/{tenant_path}/block_payments/{block_id}".format(
            tenant_path=quote(str(tenant_path), safe=""),
            block_id=quote(str(block_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> OutputBlockPayments | None:
    if response.status_code == 200:
        response_200 = OutputBlockPayments.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[OutputBlockPayments]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    tenant_path: str,
    block_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[OutputBlockPayments]:
    """Block Payments

     List all payment components within a milestone block including amounts, due dates,
    and collection status. Shows payment breakdown for customer invoicing and internal
    tracking. Essential for accounts receivable management and collection follow-up.
    Includes payment history and any adjustments made.

    Args:
        tenant_path (str):
        block_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OutputBlockPayments]
    """

    kwargs = _get_kwargs(
        tenant_path=tenant_path,
        block_id=block_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    tenant_path: str,
    block_id: str,
    *,
    client: AuthenticatedClient,
) -> OutputBlockPayments | None:
    """Block Payments

     List all payment components within a milestone block including amounts, due dates,
    and collection status. Shows payment breakdown for customer invoicing and internal
    tracking. Essential for accounts receivable management and collection follow-up.
    Includes payment history and any adjustments made.

    Args:
        tenant_path (str):
        block_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OutputBlockPayments
    """

    return sync_detailed(
        tenant_path=tenant_path,
        block_id=block_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    tenant_path: str,
    block_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[OutputBlockPayments]:
    """Block Payments

     List all payment components within a milestone block including amounts, due dates,
    and collection status. Shows payment breakdown for customer invoicing and internal
    tracking. Essential for accounts receivable management and collection follow-up.
    Includes payment history and any adjustments made.

    Args:
        tenant_path (str):
        block_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OutputBlockPayments]
    """

    kwargs = _get_kwargs(
        tenant_path=tenant_path,
        block_id=block_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    tenant_path: str,
    block_id: str,
    *,
    client: AuthenticatedClient,
) -> OutputBlockPayments | None:
    """Block Payments

     List all payment components within a milestone block including amounts, due dates,
    and collection status. Shows payment breakdown for customer invoicing and internal
    tracking. Essential for accounts receivable management and collection follow-up.
    Includes payment history and any adjustments made.

    Args:
        tenant_path (str):
        block_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OutputBlockPayments
    """

    return (
        await asyncio_detailed(
            tenant_path=tenant_path,
            block_id=block_id,
            client=client,
        )
    ).parsed
