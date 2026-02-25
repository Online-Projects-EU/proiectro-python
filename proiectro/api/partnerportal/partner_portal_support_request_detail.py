from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_response import APIResponse
from ...models.partner_portal_support_request_detail import (
    PartnerPortalSupportRequestDetail,
)
from ...types import Response


def _get_kwargs(
    tenant_path: str,
    bridge_id: str,
    support_request_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/{tenant_path}/partner_portal/{bridge_id}/support/{support_request_id}".format(
            tenant_path=quote(str(tenant_path), safe=""),
            bridge_id=quote(str(bridge_id), safe=""),
            support_request_id=quote(str(support_request_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> APIResponse | PartnerPortalSupportRequestDetail | None:
    if response.status_code == 200:
        response_200 = PartnerPortalSupportRequestDetail.from_dict(response.json())

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
) -> Response[APIResponse | PartnerPortalSupportRequestDetail]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    tenant_path: str,
    bridge_id: str,
    support_request_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[APIResponse | PartnerPortalSupportRequestDetail]:
    """Partner Portal Support Request Detail

     Get detailed view of support request.

    Args:
        tenant_path (str):
        bridge_id (str):
        support_request_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[APIResponse | PartnerPortalSupportRequestDetail]
    """

    kwargs = _get_kwargs(
        tenant_path=tenant_path,
        bridge_id=bridge_id,
        support_request_id=support_request_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    tenant_path: str,
    bridge_id: str,
    support_request_id: str,
    *,
    client: AuthenticatedClient,
) -> APIResponse | PartnerPortalSupportRequestDetail | None:
    """Partner Portal Support Request Detail

     Get detailed view of support request.

    Args:
        tenant_path (str):
        bridge_id (str):
        support_request_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        APIResponse | PartnerPortalSupportRequestDetail
    """

    return sync_detailed(
        tenant_path=tenant_path,
        bridge_id=bridge_id,
        support_request_id=support_request_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    tenant_path: str,
    bridge_id: str,
    support_request_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[APIResponse | PartnerPortalSupportRequestDetail]:
    """Partner Portal Support Request Detail

     Get detailed view of support request.

    Args:
        tenant_path (str):
        bridge_id (str):
        support_request_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[APIResponse | PartnerPortalSupportRequestDetail]
    """

    kwargs = _get_kwargs(
        tenant_path=tenant_path,
        bridge_id=bridge_id,
        support_request_id=support_request_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    tenant_path: str,
    bridge_id: str,
    support_request_id: str,
    *,
    client: AuthenticatedClient,
) -> APIResponse | PartnerPortalSupportRequestDetail | None:
    """Partner Portal Support Request Detail

     Get detailed view of support request.

    Args:
        tenant_path (str):
        bridge_id (str):
        support_request_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        APIResponse | PartnerPortalSupportRequestDetail
    """

    return (
        await asyncio_detailed(
            tenant_path=tenant_path,
            bridge_id=bridge_id,
            support_request_id=support_request_id,
            client=client,
        )
    ).parsed
