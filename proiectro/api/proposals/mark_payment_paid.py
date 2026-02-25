from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_response import APIResponse
from ...models.mark_payment_paid import MarkPaymentPaid
from ...models.mark_payment_paid_response import MarkPaymentPaidResponse
from ...types import Response


def _get_kwargs(
    tenant_path: str,
    payment_id: str,
    *,
    body: MarkPaymentPaid,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/api/v1/{tenant_path}/payment/{payment_id}/mark_paid".format(
            tenant_path=quote(str(tenant_path), safe=""),
            payment_id=quote(str(payment_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> APIResponse | MarkPaymentPaidResponse | None:
    if response.status_code == 200:
        response_200 = APIResponse.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = APIResponse.from_dict(response.json())

        return response_400

    if response.status_code == 422:
        response_422 = MarkPaymentPaidResponse.from_dict(response.json())

        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[APIResponse | MarkPaymentPaidResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    tenant_path: str,
    payment_id: str,
    *,
    client: AuthenticatedClient,
    body: MarkPaymentPaid,
) -> Response[APIResponse | MarkPaymentPaidResponse]:
    """Mark Payment Paid

     Record payment collection for revenue recognition and accounts receivable reconciliation.
    Captures payment date, method, and reference for complete audit trail. Updates
    dashboard metrics and cash position immediately. Triggers notifications for
    dependent workflows like project phase releases.

    Args:
        tenant_path (str):
        payment_id (str):
        body (MarkPaymentPaid):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[APIResponse | MarkPaymentPaidResponse]
    """

    kwargs = _get_kwargs(
        tenant_path=tenant_path,
        payment_id=payment_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    tenant_path: str,
    payment_id: str,
    *,
    client: AuthenticatedClient,
    body: MarkPaymentPaid,
) -> APIResponse | MarkPaymentPaidResponse | None:
    """Mark Payment Paid

     Record payment collection for revenue recognition and accounts receivable reconciliation.
    Captures payment date, method, and reference for complete audit trail. Updates
    dashboard metrics and cash position immediately. Triggers notifications for
    dependent workflows like project phase releases.

    Args:
        tenant_path (str):
        payment_id (str):
        body (MarkPaymentPaid):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        APIResponse | MarkPaymentPaidResponse
    """

    return sync_detailed(
        tenant_path=tenant_path,
        payment_id=payment_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    tenant_path: str,
    payment_id: str,
    *,
    client: AuthenticatedClient,
    body: MarkPaymentPaid,
) -> Response[APIResponse | MarkPaymentPaidResponse]:
    """Mark Payment Paid

     Record payment collection for revenue recognition and accounts receivable reconciliation.
    Captures payment date, method, and reference for complete audit trail. Updates
    dashboard metrics and cash position immediately. Triggers notifications for
    dependent workflows like project phase releases.

    Args:
        tenant_path (str):
        payment_id (str):
        body (MarkPaymentPaid):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[APIResponse | MarkPaymentPaidResponse]
    """

    kwargs = _get_kwargs(
        tenant_path=tenant_path,
        payment_id=payment_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    tenant_path: str,
    payment_id: str,
    *,
    client: AuthenticatedClient,
    body: MarkPaymentPaid,
) -> APIResponse | MarkPaymentPaidResponse | None:
    """Mark Payment Paid

     Record payment collection for revenue recognition and accounts receivable reconciliation.
    Captures payment date, method, and reference for complete audit trail. Updates
    dashboard metrics and cash position immediately. Triggers notifications for
    dependent workflows like project phase releases.

    Args:
        tenant_path (str):
        payment_id (str):
        body (MarkPaymentPaid):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        APIResponse | MarkPaymentPaidResponse
    """

    return (
        await asyncio_detailed(
            tenant_path=tenant_path,
            payment_id=payment_id,
            client=client,
            body=body,
        )
    ).parsed
