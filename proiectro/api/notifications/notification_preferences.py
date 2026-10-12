from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.output_notification_preferences import OutputNotificationPreferences
from ...types import UNSET, Response, Unset


def _get_kwargs(
    tenant_path: str,
    *,
    scope: str | Unset = "user",
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["scope"] = scope

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/{tenant_path}/notification_preferences".format(
            tenant_path=quote(str(tenant_path), safe=""),
        ),
        "params": params,
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
    tenant_path: str,
    *,
    client: AuthenticatedClient,
    scope: str | Unset = "user",
) -> Response[OutputNotificationPreferences]:
    """Notification Preferences

     List every notification you can be sent, grouped by area, with the channels each one
    currently uses and whether that came from your own choice or the product default. Pass
    scope=tenant to see and tune the settings for this workspace only; the default scope=user
    is your standing preference across every workspace you belong to. A few notifications
    about your access and credentials are always delivered and are marked as such.

    Args:
        tenant_path (str):
        scope (str | Unset):  Default: 'user'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OutputNotificationPreferences]
    """

    kwargs = _get_kwargs(
        tenant_path=tenant_path,
        scope=scope,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    tenant_path: str,
    *,
    client: AuthenticatedClient,
    scope: str | Unset = "user",
) -> OutputNotificationPreferences | None:
    """Notification Preferences

     List every notification you can be sent, grouped by area, with the channels each one
    currently uses and whether that came from your own choice or the product default. Pass
    scope=tenant to see and tune the settings for this workspace only; the default scope=user
    is your standing preference across every workspace you belong to. A few notifications
    about your access and credentials are always delivered and are marked as such.

    Args:
        tenant_path (str):
        scope (str | Unset):  Default: 'user'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OutputNotificationPreferences
    """

    return sync_detailed(
        tenant_path=tenant_path,
        client=client,
        scope=scope,
    ).parsed


async def asyncio_detailed(
    tenant_path: str,
    *,
    client: AuthenticatedClient,
    scope: str | Unset = "user",
) -> Response[OutputNotificationPreferences]:
    """Notification Preferences

     List every notification you can be sent, grouped by area, with the channels each one
    currently uses and whether that came from your own choice or the product default. Pass
    scope=tenant to see and tune the settings for this workspace only; the default scope=user
    is your standing preference across every workspace you belong to. A few notifications
    about your access and credentials are always delivered and are marked as such.

    Args:
        tenant_path (str):
        scope (str | Unset):  Default: 'user'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OutputNotificationPreferences]
    """

    kwargs = _get_kwargs(
        tenant_path=tenant_path,
        scope=scope,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    tenant_path: str,
    *,
    client: AuthenticatedClient,
    scope: str | Unset = "user",
) -> OutputNotificationPreferences | None:
    """Notification Preferences

     List every notification you can be sent, grouped by area, with the channels each one
    currently uses and whether that came from your own choice or the product default. Pass
    scope=tenant to see and tune the settings for this workspace only; the default scope=user
    is your standing preference across every workspace you belong to. A few notifications
    about your access and credentials are always delivered and are marked as such.

    Args:
        tenant_path (str):
        scope (str | Unset):  Default: 'user'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OutputNotificationPreferences
    """

    return (
        await asyncio_detailed(
            tenant_path=tenant_path,
            client=client,
            scope=scope,
        )
    ).parsed
