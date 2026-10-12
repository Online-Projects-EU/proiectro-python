from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.output_notification_preferences import OutputNotificationPreferences
from ...types import Response


def _get_kwargs() -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/notification_preferences",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> OutputNotificationPreferences | None:
    if response.status_code == 200:
        response_200 = OutputNotificationPreferences.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[OutputNotificationPreferences]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[OutputNotificationPreferences]:
    """My Notification Preferences

     List your notification settings across every workspace you belong to. These are your
    standing choices: they apply wherever you work unless a workspace has its own settings,
    which you can review on that workspace's preferences page. A few notifications about your
    access and credentials are always delivered and are marked as such.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OutputNotificationPreferences]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
) -> OutputNotificationPreferences | None:
    """My Notification Preferences

     List your notification settings across every workspace you belong to. These are your
    standing choices: they apply wherever you work unless a workspace has its own settings,
    which you can review on that workspace's preferences page. A few notifications about your
    access and credentials are always delivered and are marked as such.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OutputNotificationPreferences
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[OutputNotificationPreferences]:
    """My Notification Preferences

     List your notification settings across every workspace you belong to. These are your
    standing choices: they apply wherever you work unless a workspace has its own settings,
    which you can review on that workspace's preferences page. A few notifications about your
    access and credentials are always delivered and are marked as such.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OutputNotificationPreferences]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
) -> OutputNotificationPreferences | None:
    """My Notification Preferences

     List your notification settings across every workspace you belong to. These are your
    standing choices: they apply wherever you work unless a workspace has its own settings,
    which you can review on that workspace's preferences page. A few notifications about your
    access and credentials are always delivered and are marked as such.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OutputNotificationPreferences
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
