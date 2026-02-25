from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.permissions import Permissions
from ...types import Response


def _get_kwargs(
    tenant_path: str,
    role_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/{tenant_path}/role_permissions/{role_id}".format(
            tenant_path=quote(str(tenant_path), safe=""),
            role_id=quote(str(role_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Permissions | None:
    if response.status_code == 200:
        response_200 = Permissions.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Permissions]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    tenant_path: str,
    role_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Permissions]:
    """Tenant Role Permissions

     Examine all permissions granted by a role to understand its access scope. Shows
    granular permissions for each feature area and data domain. Essential before
    assigning roles to new members or modifying role definitions. Review regularly
    to ensure roles align with job functions and security requirements.

    Args:
        tenant_path (str):
        role_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Permissions]
    """

    kwargs = _get_kwargs(
        tenant_path=tenant_path,
        role_id=role_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    tenant_path: str,
    role_id: str,
    *,
    client: AuthenticatedClient,
) -> Permissions | None:
    """Tenant Role Permissions

     Examine all permissions granted by a role to understand its access scope. Shows
    granular permissions for each feature area and data domain. Essential before
    assigning roles to new members or modifying role definitions. Review regularly
    to ensure roles align with job functions and security requirements.

    Args:
        tenant_path (str):
        role_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Permissions
    """

    return sync_detailed(
        tenant_path=tenant_path,
        role_id=role_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    tenant_path: str,
    role_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Permissions]:
    """Tenant Role Permissions

     Examine all permissions granted by a role to understand its access scope. Shows
    granular permissions for each feature area and data domain. Essential before
    assigning roles to new members or modifying role definitions. Review regularly
    to ensure roles align with job functions and security requirements.

    Args:
        tenant_path (str):
        role_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Permissions]
    """

    kwargs = _get_kwargs(
        tenant_path=tenant_path,
        role_id=role_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    tenant_path: str,
    role_id: str,
    *,
    client: AuthenticatedClient,
) -> Permissions | None:
    """Tenant Role Permissions

     Examine all permissions granted by a role to understand its access scope. Shows
    granular permissions for each feature area and data domain. Essential before
    assigning roles to new members or modifying role definitions. Review regularly
    to ensure roles align with job functions and security requirements.

    Args:
        tenant_path (str):
        role_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Permissions
    """

    return (
        await asyncio_detailed(
            tenant_path=tenant_path,
            role_id=role_id,
            client=client,
        )
    ).parsed
