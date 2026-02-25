from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_response import APIResponse
from ...models.reorder_payment_schedule_blocks import ReorderPaymentScheduleBlocks
from ...models.reorder_payment_schedule_blocks_response import (
    ReorderPaymentScheduleBlocksResponse,
)
from ...types import Response


def _get_kwargs(
    tenant_path: str,
    proposal_id: str,
    *,
    body: ReorderPaymentScheduleBlocks,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/{tenant_path}/payment_schedule_blocks/{proposal_id}/reorder".format(
            tenant_path=quote(str(tenant_path), safe=""),
            proposal_id=quote(str(proposal_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> APIResponse | ReorderPaymentScheduleBlocksResponse | None:
    if response.status_code == 200:
        response_200 = APIResponse.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = APIResponse.from_dict(response.json())

        return response_400

    if response.status_code == 422:
        response_422 = ReorderPaymentScheduleBlocksResponse.from_dict(response.json())

        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[APIResponse | ReorderPaymentScheduleBlocksResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    tenant_path: str,
    proposal_id: str,
    *,
    client: AuthenticatedClient,
    body: ReorderPaymentScheduleBlocks,
) -> Response[APIResponse | ReorderPaymentScheduleBlocksResponse]:
    """Reorder Payment Schedule Blocks

     Adjust payment milestone sequence to match revised project timelines or priorities.
    Reordering affects payment due dates and cash flow projections. Ensure customer
    agreement before changing established payment sequences. Maintain logical flow
    aligned with project deliverables for clear expectations.

    Args:
        tenant_path (str):
        proposal_id (str):
        body (ReorderPaymentScheduleBlocks):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[APIResponse | ReorderPaymentScheduleBlocksResponse]
    """

    kwargs = _get_kwargs(
        tenant_path=tenant_path,
        proposal_id=proposal_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    tenant_path: str,
    proposal_id: str,
    *,
    client: AuthenticatedClient,
    body: ReorderPaymentScheduleBlocks,
) -> APIResponse | ReorderPaymentScheduleBlocksResponse | None:
    """Reorder Payment Schedule Blocks

     Adjust payment milestone sequence to match revised project timelines or priorities.
    Reordering affects payment due dates and cash flow projections. Ensure customer
    agreement before changing established payment sequences. Maintain logical flow
    aligned with project deliverables for clear expectations.

    Args:
        tenant_path (str):
        proposal_id (str):
        body (ReorderPaymentScheduleBlocks):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        APIResponse | ReorderPaymentScheduleBlocksResponse
    """

    return sync_detailed(
        tenant_path=tenant_path,
        proposal_id=proposal_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    tenant_path: str,
    proposal_id: str,
    *,
    client: AuthenticatedClient,
    body: ReorderPaymentScheduleBlocks,
) -> Response[APIResponse | ReorderPaymentScheduleBlocksResponse]:
    """Reorder Payment Schedule Blocks

     Adjust payment milestone sequence to match revised project timelines or priorities.
    Reordering affects payment due dates and cash flow projections. Ensure customer
    agreement before changing established payment sequences. Maintain logical flow
    aligned with project deliverables for clear expectations.

    Args:
        tenant_path (str):
        proposal_id (str):
        body (ReorderPaymentScheduleBlocks):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[APIResponse | ReorderPaymentScheduleBlocksResponse]
    """

    kwargs = _get_kwargs(
        tenant_path=tenant_path,
        proposal_id=proposal_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    tenant_path: str,
    proposal_id: str,
    *,
    client: AuthenticatedClient,
    body: ReorderPaymentScheduleBlocks,
) -> APIResponse | ReorderPaymentScheduleBlocksResponse | None:
    """Reorder Payment Schedule Blocks

     Adjust payment milestone sequence to match revised project timelines or priorities.
    Reordering affects payment due dates and cash flow projections. Ensure customer
    agreement before changing established payment sequences. Maintain logical flow
    aligned with project deliverables for clear expectations.

    Args:
        tenant_path (str):
        proposal_id (str):
        body (ReorderPaymentScheduleBlocks):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        APIResponse | ReorderPaymentScheduleBlocksResponse
    """

    return (
        await asyncio_detailed(
            tenant_path=tenant_path,
            proposal_id=proposal_id,
            client=client,
            body=body,
        )
    ).parsed
