from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_response import APIResponse
from ...models.edit_my_profile import EditMyProfile
from ...models.pydantic_detail import PydanticDetail
from ...types import Response


def _get_kwargs(
    *,
    body: EditMyProfile,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/api/v1/my_profile",
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

    if response.status_code == 422:
        response_422 = PydanticDetail.from_dict(response.json())

        return response_422

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
    *,
    client: AuthenticatedClient,
    body: EditMyProfile,
) -> Response[APIResponse | PydanticDetail]:
    """Edit My Profile

     Update your account profile. Changing the language takes effect across
    the web and the mobile app; anything you leave out keeps its current
    value.

    Args:
        body (EditMyProfile): Partial: an omitted key keeps the stored value. Valid languages are
            settings.LANGUAGES, validated in the function so new languages need no
            schema change.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[APIResponse | PydanticDetail]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: EditMyProfile,
) -> APIResponse | PydanticDetail | None:
    """Edit My Profile

     Update your account profile. Changing the language takes effect across
    the web and the mobile app; anything you leave out keeps its current
    value.

    Args:
        body (EditMyProfile): Partial: an omitted key keeps the stored value. Valid languages are
            settings.LANGUAGES, validated in the function so new languages need no
            schema change.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        APIResponse | PydanticDetail
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: EditMyProfile,
) -> Response[APIResponse | PydanticDetail]:
    """Edit My Profile

     Update your account profile. Changing the language takes effect across
    the web and the mobile app; anything you leave out keeps its current
    value.

    Args:
        body (EditMyProfile): Partial: an omitted key keeps the stored value. Valid languages are
            settings.LANGUAGES, validated in the function so new languages need no
            schema change.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[APIResponse | PydanticDetail]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: EditMyProfile,
) -> APIResponse | PydanticDetail | None:
    """Edit My Profile

     Update your account profile. Changing the language takes effect across
    the web and the mobile app; anything you leave out keeps its current
    value.

    Args:
        body (EditMyProfile): Partial: an omitted key keeps the stored value. Valid languages are
            settings.LANGUAGES, validated in the function so new languages need no
            schema change.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        APIResponse | PydanticDetail
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
