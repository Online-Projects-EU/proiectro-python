from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.feed_event_reactions_response import FeedEventReactionsResponse
from ...types import Response


def _get_kwargs(
    tenant_path: str,
    event_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/{tenant_path}/reactions/{event_id}".format(
            tenant_path=quote(str(tenant_path), safe=""),
            event_id=quote(str(event_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> FeedEventReactionsResponse | None:
    if response.status_code == 200:
        response_200 = FeedEventReactionsResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[FeedEventReactionsResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    tenant_path: str,
    event_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[FeedEventReactionsResponse]:
    """Feed Event Reactions

     See who reacted to specific feed items to understand team engagement and sentiment.
    Returns all reactions grouped by type with reacting team members. Useful for
    gauging team morale, identifying highly engaged members, and understanding which
    activities resonate with your workspace culture.

    Args:
        tenant_path (str):
        event_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FeedEventReactionsResponse]
    """

    kwargs = _get_kwargs(
        tenant_path=tenant_path,
        event_id=event_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    tenant_path: str,
    event_id: str,
    *,
    client: AuthenticatedClient,
) -> FeedEventReactionsResponse | None:
    """Feed Event Reactions

     See who reacted to specific feed items to understand team engagement and sentiment.
    Returns all reactions grouped by type with reacting team members. Useful for
    gauging team morale, identifying highly engaged members, and understanding which
    activities resonate with your workspace culture.

    Args:
        tenant_path (str):
        event_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FeedEventReactionsResponse
    """

    return sync_detailed(
        tenant_path=tenant_path,
        event_id=event_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    tenant_path: str,
    event_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[FeedEventReactionsResponse]:
    """Feed Event Reactions

     See who reacted to specific feed items to understand team engagement and sentiment.
    Returns all reactions grouped by type with reacting team members. Useful for
    gauging team morale, identifying highly engaged members, and understanding which
    activities resonate with your workspace culture.

    Args:
        tenant_path (str):
        event_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FeedEventReactionsResponse]
    """

    kwargs = _get_kwargs(
        tenant_path=tenant_path,
        event_id=event_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    tenant_path: str,
    event_id: str,
    *,
    client: AuthenticatedClient,
) -> FeedEventReactionsResponse | None:
    """Feed Event Reactions

     See who reacted to specific feed items to understand team engagement and sentiment.
    Returns all reactions grouped by type with reacting team members. Useful for
    gauging team morale, identifying highly engaged members, and understanding which
    activities resonate with your workspace culture.

    Args:
        tenant_path (str):
        event_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FeedEventReactionsResponse
    """

    return (
        await asyncio_detailed(
            tenant_path=tenant_path,
            event_id=event_id,
            client=client,
        )
    ).parsed
