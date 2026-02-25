from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_response import APIResponse
from ...types import Response


def _get_kwargs(
    notification_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/mark_notification_read/{notification_id}".format(
            notification_id=quote(str(notification_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> APIResponse | None:
    if response.status_code == 200:
        response_200 = APIResponse.from_dict(response.json())

        return response_200

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
    notification_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[APIResponse]:
    """Mark Notification Read

     Mark individual notifications as read to track user acknowledgment and clear unread
    indicators. Updates badge counts immediately across all user sessions. Useful for
    processing notifications one at a time while maintaining awareness of remaining items.
    Read status helps identify which team members have seen critical announcements.

    Args:
        notification_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[APIResponse]
    """

    kwargs = _get_kwargs(
        notification_id=notification_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    notification_id: str,
    *,
    client: AuthenticatedClient,
) -> APIResponse | None:
    """Mark Notification Read

     Mark individual notifications as read to track user acknowledgment and clear unread
    indicators. Updates badge counts immediately across all user sessions. Useful for
    processing notifications one at a time while maintaining awareness of remaining items.
    Read status helps identify which team members have seen critical announcements.

    Args:
        notification_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        APIResponse
    """

    return sync_detailed(
        notification_id=notification_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    notification_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[APIResponse]:
    """Mark Notification Read

     Mark individual notifications as read to track user acknowledgment and clear unread
    indicators. Updates badge counts immediately across all user sessions. Useful for
    processing notifications one at a time while maintaining awareness of remaining items.
    Read status helps identify which team members have seen critical announcements.

    Args:
        notification_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[APIResponse]
    """

    kwargs = _get_kwargs(
        notification_id=notification_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    notification_id: str,
    *,
    client: AuthenticatedClient,
) -> APIResponse | None:
    """Mark Notification Read

     Mark individual notifications as read to track user acknowledgment and clear unread
    indicators. Updates badge counts immediately across all user sessions. Useful for
    processing notifications one at a time while maintaining awareness of remaining items.
    Read status helps identify which team members have seen critical announcements.

    Args:
        notification_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        APIResponse
    """

    return (
        await asyncio_detailed(
            notification_id=notification_id,
            client=client,
        )
    ).parsed
