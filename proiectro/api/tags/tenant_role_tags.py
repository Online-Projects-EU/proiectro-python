from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.output_role_tags import OutputRoleTags
from ...types import Response


def _get_kwargs(
    tenant_path: str,
    role_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/{tenant_path}/role_tags/{role_id}".format(
            tenant_path=quote(str(tenant_path), safe=""),
            role_id=quote(str(role_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> OutputRoleTags | None:
    if response.status_code == 200:
        response_200 = OutputRoleTags.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[OutputRoleTags]:
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
) -> Response[OutputRoleTags]:
    """Tenant Role Tags

     View tags assigned to a security role for categorization understanding.
    Shows how roles fit into organizational structure and permission hierarchy.
    Essential for role review and access control documentation.

    Args:
        tenant_path (str):
        role_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OutputRoleTags]
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
) -> OutputRoleTags | None:
    """Tenant Role Tags

     View tags assigned to a security role for categorization understanding.
    Shows how roles fit into organizational structure and permission hierarchy.
    Essential for role review and access control documentation.

    Args:
        tenant_path (str):
        role_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OutputRoleTags
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
) -> Response[OutputRoleTags]:
    """Tenant Role Tags

     View tags assigned to a security role for categorization understanding.
    Shows how roles fit into organizational structure and permission hierarchy.
    Essential for role review and access control documentation.

    Args:
        tenant_path (str):
        role_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OutputRoleTags]
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
) -> OutputRoleTags | None:
    """Tenant Role Tags

     View tags assigned to a security role for categorization understanding.
    Shows how roles fit into organizational structure and permission hierarchy.
    Essential for role review and access control documentation.

    Args:
        tenant_path (str):
        role_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OutputRoleTags
    """

    return (
        await asyncio_detailed(
            tenant_path=tenant_path,
            role_id=role_id,
            client=client,
        )
    ).parsed
