from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.org_contacts import OrgContacts
from ...types import Response


def _get_kwargs(
    tenant_path: str,
    org_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/{tenant_path}/contacts/{org_id}".format(
            tenant_path=quote(str(tenant_path), safe=""),
            org_id=quote(str(org_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> OrgContacts | None:
    if response.status_code == 200:
        response_200 = OrgContacts.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[OrgContacts]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    tenant_path: str,
    org_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[OrgContacts]:
    """Tenant Org Contacts

     Access customer organization contacts for relationship management and portal access control.
    Shows contacts with and without portal access, including invitation status. Essential for
    customer communication, project stakeholder tracking, and portal access management.
    Includes job titles and contact details for effective engagement.

    Args:
        tenant_path (str):
        org_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OrgContacts]
    """

    kwargs = _get_kwargs(
        tenant_path=tenant_path,
        org_id=org_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    tenant_path: str,
    org_id: str,
    *,
    client: AuthenticatedClient,
) -> OrgContacts | None:
    """Tenant Org Contacts

     Access customer organization contacts for relationship management and portal access control.
    Shows contacts with and without portal access, including invitation status. Essential for
    customer communication, project stakeholder tracking, and portal access management.
    Includes job titles and contact details for effective engagement.

    Args:
        tenant_path (str):
        org_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OrgContacts
    """

    return sync_detailed(
        tenant_path=tenant_path,
        org_id=org_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    tenant_path: str,
    org_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[OrgContacts]:
    """Tenant Org Contacts

     Access customer organization contacts for relationship management and portal access control.
    Shows contacts with and without portal access, including invitation status. Essential for
    customer communication, project stakeholder tracking, and portal access management.
    Includes job titles and contact details for effective engagement.

    Args:
        tenant_path (str):
        org_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OrgContacts]
    """

    kwargs = _get_kwargs(
        tenant_path=tenant_path,
        org_id=org_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    tenant_path: str,
    org_id: str,
    *,
    client: AuthenticatedClient,
) -> OrgContacts | None:
    """Tenant Org Contacts

     Access customer organization contacts for relationship management and portal access control.
    Shows contacts with and without portal access, including invitation status. Essential for
    customer communication, project stakeholder tracking, and portal access management.
    Includes job titles and contact details for effective engagement.

    Args:
        tenant_path (str):
        org_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OrgContacts
    """

    return (
        await asyncio_detailed(
            tenant_path=tenant_path,
            org_id=org_id,
            client=client,
        )
    ).parsed
