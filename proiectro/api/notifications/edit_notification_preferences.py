from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_response import APIResponse
from ...models.edit_notification_preferences import EditNotificationPreferences
from ...models.pydantic_detail import PydanticDetail
from ...types import Response


def _get_kwargs(
    tenant_path: str,
    *,
    body: EditNotificationPreferences,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/api/v1/{tenant_path}/notification_preferences".format(
            tenant_path=quote(str(tenant_path), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> APIResponse | PydanticDetail | None:
    if response.status_code == 200:
        response_200 = APIResponse.from_dict(response.json())

        return response_200

    if response.status_code == 404:
        response_404 = APIResponse.from_dict(response.json())

        return response_404

    if response.status_code == 422:
        response_422 = PydanticDetail.from_dict(response.json())

        return response_422

    if response.status_code == 500:
        response_500 = APIResponse.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[APIResponse | PydanticDetail]:
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
    body: EditNotificationPreferences,
) -> Response[APIResponse | PydanticDetail]:
    """Edit Notification Preferences

     Change which notifications reach you and on which channels. Send only what you are
    changing: anything you leave out keeps its current setting. Send a setting with no
    channels to stop overriding it and follow the product default again. Choices can be made
    for all your workspaces at once, or for this workspace alone.

    Args:
        tenant_path (str):
        body (EditNotificationPreferences): A **sparse** notification-preference edit.

            `preferences` maps a notification type or group key to the channels the user expressed an
            opinion about: `{"support": {"web": false}, "support_assigned": {"mobile": true}}`.

            Only the keys sent are written. An absent key keeps whatever was stored, and a stored key
            that is absent here is not cleared, matching how every other edit in this codebase
            behaves. To go back to following the product default, send the key with an empty object
            and it is removed.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[APIResponse | PydanticDetail]
    """

    kwargs = _get_kwargs(
        tenant_path=tenant_path,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    tenant_path: str,
    *,
    client: AuthenticatedClient,
    body: EditNotificationPreferences,
) -> APIResponse | PydanticDetail | None:
    """Edit Notification Preferences

     Change which notifications reach you and on which channels. Send only what you are
    changing: anything you leave out keeps its current setting. Send a setting with no
    channels to stop overriding it and follow the product default again. Choices can be made
    for all your workspaces at once, or for this workspace alone.

    Args:
        tenant_path (str):
        body (EditNotificationPreferences): A **sparse** notification-preference edit.

            `preferences` maps a notification type or group key to the channels the user expressed an
            opinion about: `{"support": {"web": false}, "support_assigned": {"mobile": true}}`.

            Only the keys sent are written. An absent key keeps whatever was stored, and a stored key
            that is absent here is not cleared, matching how every other edit in this codebase
            behaves. To go back to following the product default, send the key with an empty object
            and it is removed.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        APIResponse | PydanticDetail
    """

    return sync_detailed(
        tenant_path=tenant_path,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    tenant_path: str,
    *,
    client: AuthenticatedClient,
    body: EditNotificationPreferences,
) -> Response[APIResponse | PydanticDetail]:
    """Edit Notification Preferences

     Change which notifications reach you and on which channels. Send only what you are
    changing: anything you leave out keeps its current setting. Send a setting with no
    channels to stop overriding it and follow the product default again. Choices can be made
    for all your workspaces at once, or for this workspace alone.

    Args:
        tenant_path (str):
        body (EditNotificationPreferences): A **sparse** notification-preference edit.

            `preferences` maps a notification type or group key to the channels the user expressed an
            opinion about: `{"support": {"web": false}, "support_assigned": {"mobile": true}}`.

            Only the keys sent are written. An absent key keeps whatever was stored, and a stored key
            that is absent here is not cleared, matching how every other edit in this codebase
            behaves. To go back to following the product default, send the key with an empty object
            and it is removed.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[APIResponse | PydanticDetail]
    """

    kwargs = _get_kwargs(
        tenant_path=tenant_path,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    tenant_path: str,
    *,
    client: AuthenticatedClient,
    body: EditNotificationPreferences,
) -> APIResponse | PydanticDetail | None:
    """Edit Notification Preferences

     Change which notifications reach you and on which channels. Send only what you are
    changing: anything you leave out keeps its current setting. Send a setting with no
    channels to stop overriding it and follow the product default again. Choices can be made
    for all your workspaces at once, or for this workspace alone.

    Args:
        tenant_path (str):
        body (EditNotificationPreferences): A **sparse** notification-preference edit.

            `preferences` maps a notification type or group key to the channels the user expressed an
            opinion about: `{"support": {"web": false}, "support_assigned": {"mobile": true}}`.

            Only the keys sent are written. An absent key keeps whatever was stored, and a stored key
            that is absent here is not cleared, matching how every other edit in this codebase
            behaves. To go back to following the product default, send the key with an empty object
            and it is removed.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        APIResponse | PydanticDetail
    """

    return (
        await asyncio_detailed(
            tenant_path=tenant_path,
            client=client,
            body=body,
        )
    ).parsed
