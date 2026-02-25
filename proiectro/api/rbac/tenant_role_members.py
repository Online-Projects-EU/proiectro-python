from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.team_members_role import TeamMembersRole
from ...types import Response


def _get_kwargs(
    tenant_path: str,
    role_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/{tenant_path}/role_members/{role_id}".format(
            tenant_path=quote(str(tenant_path), safe=""),
            role_id=quote(str(role_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> TeamMembersRole | None:
    if response.status_code == 200:
        response_200 = TeamMembersRole.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[TeamMembersRole]:
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
) -> Response[TeamMembersRole]:
    """Tenant Role Members

     List all team members assigned to a specific security role for access auditing.
    Critical for compliance reviews and understanding who has elevated privileges.
    Shows direct assignments only - members may have additional permissions through
    other roles. Regular review prevents permission creep and maintains security.

    Args:
        tenant_path (str):
        role_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TeamMembersRole]
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
) -> TeamMembersRole | None:
    """Tenant Role Members

     List all team members assigned to a specific security role for access auditing.
    Critical for compliance reviews and understanding who has elevated privileges.
    Shows direct assignments only - members may have additional permissions through
    other roles. Regular review prevents permission creep and maintains security.

    Args:
        tenant_path (str):
        role_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        TeamMembersRole
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
) -> Response[TeamMembersRole]:
    """Tenant Role Members

     List all team members assigned to a specific security role for access auditing.
    Critical for compliance reviews and understanding who has elevated privileges.
    Shows direct assignments only - members may have additional permissions through
    other roles. Regular review prevents permission creep and maintains security.

    Args:
        tenant_path (str):
        role_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TeamMembersRole]
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
) -> TeamMembersRole | None:
    """Tenant Role Members

     List all team members assigned to a specific security role for access auditing.
    Critical for compliance reviews and understanding who has elevated privileges.
    Shows direct assignments only - members may have additional permissions through
    other roles. Regular review prevents permission creep and maintains security.

    Args:
        tenant_path (str):
        role_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        TeamMembersRole
    """

    return (
        await asyncio_detailed(
            tenant_path=tenant_path,
            role_id=role_id,
            client=client,
        )
    ).parsed
