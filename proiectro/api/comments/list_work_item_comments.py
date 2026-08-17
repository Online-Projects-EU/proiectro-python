from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.output_comments_feed import OutputCommentsFeed
from ...types import Response


def _get_kwargs(
    tenant_path: str,
    work_item_id: str,
    page_number: int,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/{tenant_path}/work_item_comments/{work_item_id}/{page_number}".format(
            tenant_path=quote(str(tenant_path), safe=""),
            work_item_id=quote(str(work_item_id), safe=""),
            page_number=quote(str(page_number), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> OutputCommentsFeed | None:
    if response.status_code == 200:
        response_200 = OutputCommentsFeed.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[OutputCommentsFeed]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    tenant_path: str,
    work_item_id: str,
    page_number: int,
    *,
    client: AuthenticatedClient,
) -> Response[OutputCommentsFeed]:
    """List Work Item Comments

     View the discussion thread for a project work item. Paginated results show
    comments with nested replies, maintaining conversation context for decisions,
    progress notes, and implementation details.

    Args:
        tenant_path (str):
        work_item_id (str):
        page_number (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OutputCommentsFeed]
    """

    kwargs = _get_kwargs(
        tenant_path=tenant_path,
        work_item_id=work_item_id,
        page_number=page_number,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    tenant_path: str,
    work_item_id: str,
    page_number: int,
    *,
    client: AuthenticatedClient,
) -> OutputCommentsFeed | None:
    """List Work Item Comments

     View the discussion thread for a project work item. Paginated results show
    comments with nested replies, maintaining conversation context for decisions,
    progress notes, and implementation details.

    Args:
        tenant_path (str):
        work_item_id (str):
        page_number (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OutputCommentsFeed
    """

    return sync_detailed(
        tenant_path=tenant_path,
        work_item_id=work_item_id,
        page_number=page_number,
        client=client,
    ).parsed


async def asyncio_detailed(
    tenant_path: str,
    work_item_id: str,
    page_number: int,
    *,
    client: AuthenticatedClient,
) -> Response[OutputCommentsFeed]:
    """List Work Item Comments

     View the discussion thread for a project work item. Paginated results show
    comments with nested replies, maintaining conversation context for decisions,
    progress notes, and implementation details.

    Args:
        tenant_path (str):
        work_item_id (str):
        page_number (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OutputCommentsFeed]
    """

    kwargs = _get_kwargs(
        tenant_path=tenant_path,
        work_item_id=work_item_id,
        page_number=page_number,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    tenant_path: str,
    work_item_id: str,
    page_number: int,
    *,
    client: AuthenticatedClient,
) -> OutputCommentsFeed | None:
    """List Work Item Comments

     View the discussion thread for a project work item. Paginated results show
    comments with nested replies, maintaining conversation context for decisions,
    progress notes, and implementation details.

    Args:
        tenant_path (str):
        work_item_id (str):
        page_number (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OutputCommentsFeed
    """

    return (
        await asyncio_detailed(
            tenant_path=tenant_path,
            work_item_id=work_item_id,
            page_number=page_number,
            client=client,
        )
    ).parsed
