from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.output_my_tenants import OutputMyTenants
from ...types import Response


def _get_kwargs() -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/my_tenants",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> OutputMyTenants | None:
    if response.status_code == 200:
        response_200 = OutputMyTenants.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[OutputMyTenants]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[OutputMyTenants]:
    """My Tenants

     Retrieve the list of workspaces the current user belongs to, with
    active memberships only. Each tenant includes its logo URL and an
    is_owner flag. Also returns pending invitations the user hasn't
    acted on yet.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OutputMyTenants]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
) -> OutputMyTenants | None:
    """My Tenants

     Retrieve the list of workspaces the current user belongs to, with
    active memberships only. Each tenant includes its logo URL and an
    is_owner flag. Also returns pending invitations the user hasn't
    acted on yet.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OutputMyTenants
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[OutputMyTenants]:
    """My Tenants

     Retrieve the list of workspaces the current user belongs to, with
    active memberships only. Each tenant includes its logo URL and an
    is_owner flag. Also returns pending invitations the user hasn't
    acted on yet.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OutputMyTenants]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
) -> OutputMyTenants | None:
    """My Tenants

     Retrieve the list of workspaces the current user belongs to, with
    active memberships only. Each tenant includes its logo URL and an
    is_owner flag. Also returns pending invitations the user hasn't
    acted on yet.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OutputMyTenants
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
