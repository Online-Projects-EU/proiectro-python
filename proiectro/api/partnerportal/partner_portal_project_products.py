from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_response import APIResponse
from ...models.partner_portal_project_products import PartnerPortalProjectProducts
from ...types import Response


def _get_kwargs(
    tenant_path: str,
    bridge_id: str,
    project_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/{tenant_path}/partner_portal/{bridge_id}/projects/{project_id}/products".format(
            tenant_path=quote(str(tenant_path), safe=""),
            bridge_id=quote(str(bridge_id), safe=""),
            project_id=quote(str(project_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> APIResponse | PartnerPortalProjectProducts | None:
    if response.status_code == 200:
        response_200 = PartnerPortalProjectProducts.from_dict(response.json())

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
) -> Response[APIResponse | PartnerPortalProjectProducts]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    tenant_path: str,
    bridge_id: str,
    project_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[APIResponse | PartnerPortalProjectProducts]:
    """Partner Portal Project Products

     Get detailed project view for a specific project in partner portal.
    Returns product deliverables with status badges, payment schedule, and escalation contacts.

    Args:
        tenant_path (str):
        bridge_id (str):
        project_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[APIResponse | PartnerPortalProjectProducts]
    """

    kwargs = _get_kwargs(
        tenant_path=tenant_path,
        bridge_id=bridge_id,
        project_id=project_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    tenant_path: str,
    bridge_id: str,
    project_id: str,
    *,
    client: AuthenticatedClient,
) -> APIResponse | PartnerPortalProjectProducts | None:
    """Partner Portal Project Products

     Get detailed project view for a specific project in partner portal.
    Returns product deliverables with status badges, payment schedule, and escalation contacts.

    Args:
        tenant_path (str):
        bridge_id (str):
        project_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        APIResponse | PartnerPortalProjectProducts
    """

    return sync_detailed(
        tenant_path=tenant_path,
        bridge_id=bridge_id,
        project_id=project_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    tenant_path: str,
    bridge_id: str,
    project_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[APIResponse | PartnerPortalProjectProducts]:
    """Partner Portal Project Products

     Get detailed project view for a specific project in partner portal.
    Returns product deliverables with status badges, payment schedule, and escalation contacts.

    Args:
        tenant_path (str):
        bridge_id (str):
        project_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[APIResponse | PartnerPortalProjectProducts]
    """

    kwargs = _get_kwargs(
        tenant_path=tenant_path,
        bridge_id=bridge_id,
        project_id=project_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    tenant_path: str,
    bridge_id: str,
    project_id: str,
    *,
    client: AuthenticatedClient,
) -> APIResponse | PartnerPortalProjectProducts | None:
    """Partner Portal Project Products

     Get detailed project view for a specific project in partner portal.
    Returns product deliverables with status badges, payment schedule, and escalation contacts.

    Args:
        tenant_path (str):
        bridge_id (str):
        project_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        APIResponse | PartnerPortalProjectProducts
    """

    return (
        await asyncio_detailed(
            tenant_path=tenant_path,
            bridge_id=bridge_id,
            project_id=project_id,
            client=client,
        )
    ).parsed
