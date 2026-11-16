from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_response import APIResponse
from ...models.output_comments_feed import OutputCommentsFeed
from ...types import Response


def _get_kwargs(
    tenant_path: str,
    feed_post_id: str,
    page_number: int,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/{tenant_path}/feed_post_comments/{feed_post_id}/{page_number}".format(
            tenant_path=quote(str(tenant_path), safe=""),
            feed_post_id=quote(str(feed_post_id), safe=""),
            page_number=quote(str(page_number), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> APIResponse | OutputCommentsFeed | None:
    if response.status_code == 200:
        response_200 = OutputCommentsFeed.from_dict(response.json())

        return response_200

    if response.status_code == 404:
        response_404 = APIResponse.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[APIResponse | OutputCommentsFeed]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    tenant_path: str,
    feed_post_id: str,
    page_number: int,
    *,
    client: AuthenticatedClient,
) -> Response[APIResponse | OutputCommentsFeed]:
    """List Feed Post Comments

     View the conversation under a post in the workspace activity feed. Paginated
    results show comments with their replies. Only posts you can see in the feed
    have a visible thread.

    Args:
        tenant_path (str):
        feed_post_id (str):
        page_number (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[APIResponse | OutputCommentsFeed]
    """

    kwargs = _get_kwargs(
        tenant_path=tenant_path,
        feed_post_id=feed_post_id,
        page_number=page_number,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    tenant_path: str,
    feed_post_id: str,
    page_number: int,
    *,
    client: AuthenticatedClient,
) -> APIResponse | OutputCommentsFeed | None:
    """List Feed Post Comments

     View the conversation under a post in the workspace activity feed. Paginated
    results show comments with their replies. Only posts you can see in the feed
    have a visible thread.

    Args:
        tenant_path (str):
        feed_post_id (str):
        page_number (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        APIResponse | OutputCommentsFeed
    """

    return sync_detailed(
        tenant_path=tenant_path,
        feed_post_id=feed_post_id,
        page_number=page_number,
        client=client,
    ).parsed


async def asyncio_detailed(
    tenant_path: str,
    feed_post_id: str,
    page_number: int,
    *,
    client: AuthenticatedClient,
) -> Response[APIResponse | OutputCommentsFeed]:
    """List Feed Post Comments

     View the conversation under a post in the workspace activity feed. Paginated
    results show comments with their replies. Only posts you can see in the feed
    have a visible thread.

    Args:
        tenant_path (str):
        feed_post_id (str):
        page_number (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[APIResponse | OutputCommentsFeed]
    """

    kwargs = _get_kwargs(
        tenant_path=tenant_path,
        feed_post_id=feed_post_id,
        page_number=page_number,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    tenant_path: str,
    feed_post_id: str,
    page_number: int,
    *,
    client: AuthenticatedClient,
) -> APIResponse | OutputCommentsFeed | None:
    """List Feed Post Comments

     View the conversation under a post in the workspace activity feed. Paginated
    results show comments with their replies. Only posts you can see in the feed
    have a visible thread.

    Args:
        tenant_path (str):
        feed_post_id (str):
        page_number (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        APIResponse | OutputCommentsFeed
    """

    return (
        await asyncio_detailed(
            tenant_path=tenant_path,
            feed_post_id=feed_post_id,
            page_number=page_number,
            client=client,
        )
    ).parsed
