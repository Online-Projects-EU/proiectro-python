from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.team_load_schema import TeamLoadSchema
from ...types import Response


def _get_kwargs(
    tenant_path: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/{tenant_path}/analytics/team_load".format(
            tenant_path=quote(str(tenant_path), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> TeamLoadSchema | None:
    if response.status_code == 200:
        response_200 = TeamLoadSchema.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[TeamLoadSchema]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    tenant_path: str,
    *,
    client: AuthenticatedClient,
) -> Response[TeamLoadSchema]:
    """Team Load

     Get team load data for the team load page.
    Returns aggregated load data for all team members.
    This endpoint is specifically for the team load page display.

    Args:
        tenant_path (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TeamLoadSchema]
    """

    kwargs = _get_kwargs(
        tenant_path=tenant_path,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    tenant_path: str,
    *,
    client: AuthenticatedClient,
) -> TeamLoadSchema | None:
    """Team Load

     Get team load data for the team load page.
    Returns aggregated load data for all team members.
    This endpoint is specifically for the team load page display.

    Args:
        tenant_path (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        TeamLoadSchema
    """

    return sync_detailed(
        tenant_path=tenant_path,
        client=client,
    ).parsed


async def asyncio_detailed(
    tenant_path: str,
    *,
    client: AuthenticatedClient,
) -> Response[TeamLoadSchema]:
    """Team Load

     Get team load data for the team load page.
    Returns aggregated load data for all team members.
    This endpoint is specifically for the team load page display.

    Args:
        tenant_path (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TeamLoadSchema]
    """

    kwargs = _get_kwargs(
        tenant_path=tenant_path,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    tenant_path: str,
    *,
    client: AuthenticatedClient,
) -> TeamLoadSchema | None:
    """Team Load

     Get team load data for the team load page.
    Returns aggregated load data for all team members.
    This endpoint is specifically for the team load page display.

    Args:
        tenant_path (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        TeamLoadSchema
    """

    return (
        await asyncio_detailed(
            tenant_path=tenant_path,
            client=client,
        )
    ).parsed
