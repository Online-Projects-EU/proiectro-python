from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.output_user_notifications import OutputUserNotifications
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    page: int | Unset = 1,
    page_size: int | Unset = 20,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["page"] = page

    params["page_size"] = page_size

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/user_notifications",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> OutputUserNotifications | None:
    if response.status_code == 200:
        response_200 = OutputUserNotifications.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[OutputUserNotifications]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    page: int | Unset = 1,
    page_size: int | Unset = 20,
) -> Response[OutputUserNotifications]:
    """User Notifications

     Retrieve personalized notification feed showing recent alerts, mentions, and updates.
    Paginated results include unread count for badge display. Notifications are ordered
    by recency with priority indicators for urgent items. Essential for keeping users
    informed without overwhelming them. Check frequently to stay current with workspace
    activities.

    Args:
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OutputUserNotifications]
    """

    kwargs = _get_kwargs(
        page=page,
        page_size=page_size,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    page: int | Unset = 1,
    page_size: int | Unset = 20,
) -> OutputUserNotifications | None:
    """User Notifications

     Retrieve personalized notification feed showing recent alerts, mentions, and updates.
    Paginated results include unread count for badge display. Notifications are ordered
    by recency with priority indicators for urgent items. Essential for keeping users
    informed without overwhelming them. Check frequently to stay current with workspace
    activities.

    Args:
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OutputUserNotifications
    """

    return sync_detailed(
        client=client,
        page=page,
        page_size=page_size,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    page: int | Unset = 1,
    page_size: int | Unset = 20,
) -> Response[OutputUserNotifications]:
    """User Notifications

     Retrieve personalized notification feed showing recent alerts, mentions, and updates.
    Paginated results include unread count for badge display. Notifications are ordered
    by recency with priority indicators for urgent items. Essential for keeping users
    informed without overwhelming them. Check frequently to stay current with workspace
    activities.

    Args:
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OutputUserNotifications]
    """

    kwargs = _get_kwargs(
        page=page,
        page_size=page_size,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    page: int | Unset = 1,
    page_size: int | Unset = 20,
) -> OutputUserNotifications | None:
    """User Notifications

     Retrieve personalized notification feed showing recent alerts, mentions, and updates.
    Paginated results include unread count for badge display. Notifications are ordered
    by recency with priority indicators for urgent items. Essential for keeping users
    informed without overwhelming them. Check frequently to stay current with workspace
    activities.

    Args:
        page (int | Unset):  Default: 1.
        page_size (int | Unset):  Default: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OutputUserNotifications
    """

    return (
        await asyncio_detailed(
            client=client,
            page=page,
            page_size=page_size,
        )
    ).parsed
