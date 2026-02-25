from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_response import APIResponse
from ...models.partner_portal_support_requests import PartnerPortalSupportRequests
from ...types import Response


def _get_kwargs(
    tenant_path: str,
    bridge_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/{tenant_path}/partner_portal/{bridge_id}/closed_support_requests".format(
            tenant_path=quote(str(tenant_path), safe=""),
            bridge_id=quote(str(bridge_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> APIResponse | PartnerPortalSupportRequests | None:
    if response.status_code == 200:
        response_200 = PartnerPortalSupportRequests.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = APIResponse.from_dict(response.json())

        return response_400

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[APIResponse | PartnerPortalSupportRequests]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    tenant_path: str,
    bridge_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[APIResponse | PartnerPortalSupportRequests]:
    """Partner Portal Closed Support Requests

     Get closed support requests for this specific bridge/partner (last 100, newest first).

    Args:
        tenant_path (str):
        bridge_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[APIResponse | PartnerPortalSupportRequests]
    """

    kwargs = _get_kwargs(
        tenant_path=tenant_path,
        bridge_id=bridge_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    tenant_path: str,
    bridge_id: str,
    *,
    client: AuthenticatedClient,
) -> APIResponse | PartnerPortalSupportRequests | None:
    """Partner Portal Closed Support Requests

     Get closed support requests for this specific bridge/partner (last 100, newest first).

    Args:
        tenant_path (str):
        bridge_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        APIResponse | PartnerPortalSupportRequests
    """

    return sync_detailed(
        tenant_path=tenant_path,
        bridge_id=bridge_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    tenant_path: str,
    bridge_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[APIResponse | PartnerPortalSupportRequests]:
    """Partner Portal Closed Support Requests

     Get closed support requests for this specific bridge/partner (last 100, newest first).

    Args:
        tenant_path (str):
        bridge_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[APIResponse | PartnerPortalSupportRequests]
    """

    kwargs = _get_kwargs(
        tenant_path=tenant_path,
        bridge_id=bridge_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    tenant_path: str,
    bridge_id: str,
    *,
    client: AuthenticatedClient,
) -> APIResponse | PartnerPortalSupportRequests | None:
    """Partner Portal Closed Support Requests

     Get closed support requests for this specific bridge/partner (last 100, newest first).

    Args:
        tenant_path (str):
        bridge_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        APIResponse | PartnerPortalSupportRequests
    """

    return (
        await asyncio_detailed(
            tenant_path=tenant_path,
            bridge_id=bridge_id,
            client=client,
        )
    ).parsed
