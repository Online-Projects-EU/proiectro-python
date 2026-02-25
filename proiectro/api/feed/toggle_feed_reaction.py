from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_response import APIResponse
from ...types import Response


def _get_kwargs(
    tenant_path: str,
    event_id: str,
    reaction_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/api/v1/{tenant_path}/toggle_feed_reaction/{event_id}/{reaction_id}".format(
            tenant_path=quote(str(tenant_path), safe=""),
            event_id=quote(str(event_id), safe=""),
            reaction_id=quote(str(reaction_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> APIResponse | None:
    if response.status_code == 200:
        response_200 = APIResponse.from_dict(response.json())

        return response_200

    if response.status_code == 201:
        response_201 = APIResponse.from_dict(response.json())

        return response_201

    if response.status_code == 400:
        response_400 = APIResponse.from_dict(response.json())

        return response_400

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[APIResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    tenant_path: str,
    event_id: str,
    reaction_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[APIResponse]:
    """Toggle Feed Reaction

     Express support, celebrate wins, or acknowledge updates with emoji reactions.
    Toggle reactions on and off - adding if not present, removing if already reacted.
    Reactions appear instantly to foster real-time team engagement. Multiple reaction
    types available to match the sentiment - celebrate, support, acknowledge, or appreciate.

    Args:
        tenant_path (str):
        event_id (str):
        reaction_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[APIResponse]
    """

    kwargs = _get_kwargs(
        tenant_path=tenant_path,
        event_id=event_id,
        reaction_id=reaction_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    tenant_path: str,
    event_id: str,
    reaction_id: str,
    *,
    client: AuthenticatedClient,
) -> APIResponse | None:
    """Toggle Feed Reaction

     Express support, celebrate wins, or acknowledge updates with emoji reactions.
    Toggle reactions on and off - adding if not present, removing if already reacted.
    Reactions appear instantly to foster real-time team engagement. Multiple reaction
    types available to match the sentiment - celebrate, support, acknowledge, or appreciate.

    Args:
        tenant_path (str):
        event_id (str):
        reaction_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        APIResponse
    """

    return sync_detailed(
        tenant_path=tenant_path,
        event_id=event_id,
        reaction_id=reaction_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    tenant_path: str,
    event_id: str,
    reaction_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[APIResponse]:
    """Toggle Feed Reaction

     Express support, celebrate wins, or acknowledge updates with emoji reactions.
    Toggle reactions on and off - adding if not present, removing if already reacted.
    Reactions appear instantly to foster real-time team engagement. Multiple reaction
    types available to match the sentiment - celebrate, support, acknowledge, or appreciate.

    Args:
        tenant_path (str):
        event_id (str):
        reaction_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[APIResponse]
    """

    kwargs = _get_kwargs(
        tenant_path=tenant_path,
        event_id=event_id,
        reaction_id=reaction_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    tenant_path: str,
    event_id: str,
    reaction_id: str,
    *,
    client: AuthenticatedClient,
) -> APIResponse | None:
    """Toggle Feed Reaction

     Express support, celebrate wins, or acknowledge updates with emoji reactions.
    Toggle reactions on and off - adding if not present, removing if already reacted.
    Reactions appear instantly to foster real-time team engagement. Multiple reaction
    types available to match the sentiment - celebrate, support, acknowledge, or appreciate.

    Args:
        tenant_path (str):
        event_id (str):
        reaction_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        APIResponse
    """

    return (
        await asyncio_detailed(
            tenant_path=tenant_path,
            event_id=event_id,
            reaction_id=reaction_id,
            client=client,
        )
    ).parsed
