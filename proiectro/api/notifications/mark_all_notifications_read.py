from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_response import APIResponse
from ...types import Response


def _get_kwargs() -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/mark_all_notifications_read",
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
    *,
    client: AuthenticatedClient,
) -> Response[APIResponse]:
    """Mark All Notifications Read

     Clear all unread notifications in a single action for inbox zero management. Useful
    after returning from absence or when catching up on accumulated updates. Affects only
    the current user's notifications without impacting other team members. Consider reviewing
    important notifications individually before bulk marking to ensure nothing critical is
    missed.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[APIResponse]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
) -> APIResponse | None:
    """Mark All Notifications Read

     Clear all unread notifications in a single action for inbox zero management. Useful
    after returning from absence or when catching up on accumulated updates. Affects only
    the current user's notifications without impacting other team members. Consider reviewing
    important notifications individually before bulk marking to ensure nothing critical is
    missed.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        APIResponse
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[APIResponse]:
    """Mark All Notifications Read

     Clear all unread notifications in a single action for inbox zero management. Useful
    after returning from absence or when catching up on accumulated updates. Affects only
    the current user's notifications without impacting other team members. Consider reviewing
    important notifications individually before bulk marking to ensure nothing critical is
    missed.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[APIResponse]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
) -> APIResponse | None:
    """Mark All Notifications Read

     Clear all unread notifications in a single action for inbox zero management. Useful
    after returning from absence or when catching up on accumulated updates. Affects only
    the current user's notifications without impacting other team members. Consider reviewing
    important notifications individually before bulk marking to ensure nothing critical is
    missed.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        APIResponse
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
