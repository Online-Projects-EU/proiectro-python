from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_response import APIResponse
from ...models.edit_payment_schedule_block import EditPaymentScheduleBlock
from ...models.edit_payment_schedule_block_response import (
    EditPaymentScheduleBlockResponse,
)
from ...types import Response


def _get_kwargs(
    tenant_path: str,
    proposal_id: str,
    block_id: str,
    *,
    body: EditPaymentScheduleBlock,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/api/v1/{tenant_path}/payment_schedule_block/{proposal_id}/{block_id}".format(
            tenant_path=quote(str(tenant_path), safe=""),
            proposal_id=quote(str(proposal_id), safe=""),
            block_id=quote(str(block_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> APIResponse | EditPaymentScheduleBlockResponse | None:
    if response.status_code == 200:
        response_200 = APIResponse.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = APIResponse.from_dict(response.json())

        return response_400

    if response.status_code == 422:
        response_422 = EditPaymentScheduleBlockResponse.from_dict(response.json())

        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[APIResponse | EditPaymentScheduleBlockResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    tenant_path: str,
    proposal_id: str,
    block_id: str,
    *,
    client: AuthenticatedClient,
    body: EditPaymentScheduleBlock,
) -> Response[APIResponse | EditPaymentScheduleBlockResponse]:
    """Edit Payment Schedule Block

     Modify payment milestone terms as negotiations evolve or project scope changes.
    Updates cascade to all payments within the block maintaining proportional relationships.
    Changes require careful review as they affect cash flow forecasts and customer
    expectations. Document reasons for schedule modifications for audit purposes.

    Args:
        tenant_path (str):
        proposal_id (str):
        block_id (str):
        body (EditPaymentScheduleBlock):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[APIResponse | EditPaymentScheduleBlockResponse]
    """

    kwargs = _get_kwargs(
        tenant_path=tenant_path,
        proposal_id=proposal_id,
        block_id=block_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    tenant_path: str,
    proposal_id: str,
    block_id: str,
    *,
    client: AuthenticatedClient,
    body: EditPaymentScheduleBlock,
) -> APIResponse | EditPaymentScheduleBlockResponse | None:
    """Edit Payment Schedule Block

     Modify payment milestone terms as negotiations evolve or project scope changes.
    Updates cascade to all payments within the block maintaining proportional relationships.
    Changes require careful review as they affect cash flow forecasts and customer
    expectations. Document reasons for schedule modifications for audit purposes.

    Args:
        tenant_path (str):
        proposal_id (str):
        block_id (str):
        body (EditPaymentScheduleBlock):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        APIResponse | EditPaymentScheduleBlockResponse
    """

    return sync_detailed(
        tenant_path=tenant_path,
        proposal_id=proposal_id,
        block_id=block_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    tenant_path: str,
    proposal_id: str,
    block_id: str,
    *,
    client: AuthenticatedClient,
    body: EditPaymentScheduleBlock,
) -> Response[APIResponse | EditPaymentScheduleBlockResponse]:
    """Edit Payment Schedule Block

     Modify payment milestone terms as negotiations evolve or project scope changes.
    Updates cascade to all payments within the block maintaining proportional relationships.
    Changes require careful review as they affect cash flow forecasts and customer
    expectations. Document reasons for schedule modifications for audit purposes.

    Args:
        tenant_path (str):
        proposal_id (str):
        block_id (str):
        body (EditPaymentScheduleBlock):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[APIResponse | EditPaymentScheduleBlockResponse]
    """

    kwargs = _get_kwargs(
        tenant_path=tenant_path,
        proposal_id=proposal_id,
        block_id=block_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    tenant_path: str,
    proposal_id: str,
    block_id: str,
    *,
    client: AuthenticatedClient,
    body: EditPaymentScheduleBlock,
) -> APIResponse | EditPaymentScheduleBlockResponse | None:
    """Edit Payment Schedule Block

     Modify payment milestone terms as negotiations evolve or project scope changes.
    Updates cascade to all payments within the block maintaining proportional relationships.
    Changes require careful review as they affect cash flow forecasts and customer
    expectations. Document reasons for schedule modifications for audit purposes.

    Args:
        tenant_path (str):
        proposal_id (str):
        block_id (str):
        body (EditPaymentScheduleBlock):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        APIResponse | EditPaymentScheduleBlockResponse
    """

    return (
        await asyncio_detailed(
            tenant_path=tenant_path,
            proposal_id=proposal_id,
            block_id=block_id,
            client=client,
            body=body,
        )
    ).parsed
