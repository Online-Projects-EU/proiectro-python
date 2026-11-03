from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_response import APIResponse
from ...models.output_billable_source_list import OutputBillableSourceList
from ...types import Response


def _get_kwargs(
    tenant_path: str,
    payment_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/{tenant_path}/payment/{payment_id}/billable_external_support_requests".format(
            tenant_path=quote(str(tenant_path), safe=""),
            payment_id=quote(str(payment_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> APIResponse | OutputBillableSourceList | None:
    if response.status_code == 200:
        response_200 = OutputBillableSourceList.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = APIResponse.from_dict(response.json())

        return response_400

    if response.status_code == 422:
        response_422 = APIResponse.from_dict(response.json())

        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[APIResponse | OutputBillableSourceList]:
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
) -> Response[APIResponse | OutputBillableSourceList]:
    """List Billable External Support Requests For Payment

     List support requests closed as fixed or done for this Payment's customer that have
    not yet been billed on any Payment. Used by the consumption picker to attach support work as
    Payment sources. Each row carries the per-source amount suggestion (when rate
    cards exist) so the revenue officer can confirm or override before bulk-saving.

    Args:
        tenant_path (str):
        payment_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[APIResponse | OutputBillableSourceList]
    """

    kwargs = _get_kwargs(
        tenant_path=tenant_path,
        payment_id=payment_id,
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
) -> APIResponse | OutputBillableSourceList | None:
    """List Billable External Support Requests For Payment

     List support requests closed as fixed or done for this Payment's customer that have
    not yet been billed on any Payment. Used by the consumption picker to attach support work as
    Payment sources. Each row carries the per-source amount suggestion (when rate
    cards exist) so the revenue officer can confirm or override before bulk-saving.

    Args:
        tenant_path (str):
        payment_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        APIResponse | OutputBillableSourceList
    """

    return sync_detailed(
        tenant_path=tenant_path,
        payment_id=payment_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    tenant_path: str,
    payment_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[APIResponse | OutputBillableSourceList]:
    """List Billable External Support Requests For Payment

     List support requests closed as fixed or done for this Payment's customer that have
    not yet been billed on any Payment. Used by the consumption picker to attach support work as
    Payment sources. Each row carries the per-source amount suggestion (when rate
    cards exist) so the revenue officer can confirm or override before bulk-saving.

    Args:
        tenant_path (str):
        payment_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[APIResponse | OutputBillableSourceList]
    """

    kwargs = _get_kwargs(
        tenant_path=tenant_path,
        payment_id=payment_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    tenant_path: str,
    payment_id: str,
    *,
    client: AuthenticatedClient,
) -> APIResponse | OutputBillableSourceList | None:
    """List Billable External Support Requests For Payment

     List support requests closed as fixed or done for this Payment's customer that have
    not yet been billed on any Payment. Used by the consumption picker to attach support work as
    Payment sources. Each row carries the per-source amount suggestion (when rate
    cards exist) so the revenue officer can confirm or override before bulk-saving.

    Args:
        tenant_path (str):
        payment_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        APIResponse | OutputBillableSourceList
    """

    return (
        await asyncio_detailed(
            tenant_path=tenant_path,
            payment_id=payment_id,
            client=client,
        )
    ).parsed
