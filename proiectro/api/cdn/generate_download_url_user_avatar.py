from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.download_url_gcs import DownloadUrlGCS
from ...models.request_download_url_gcs import RequestDownloadUrlGCS
from ...types import Response


def _get_kwargs(
    *,
    body: RequestDownloadUrlGCS,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/generate_download_url_user_avatar",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> DownloadUrlGCS | None:
    if response.status_code == 200:
        response_200 = DownloadUrlGCS.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[DownloadUrlGCS]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: RequestDownloadUrlGCS,
) -> Response[DownloadUrlGCS]:
    """Generate Download Url User Avatar

     Download your global user avatar. Access your profile picture with a time-limited
    secure URL that expires after 1 minute. Useful for viewing or backing up your
    avatar image before making changes.

    Args:
        body (RequestDownloadUrlGCS):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DownloadUrlGCS]
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
    body: RequestDownloadUrlGCS,
) -> DownloadUrlGCS | None:
    """Generate Download Url User Avatar

     Download your global user avatar. Access your profile picture with a time-limited
    secure URL that expires after 1 minute. Useful for viewing or backing up your
    avatar image before making changes.

    Args:
        body (RequestDownloadUrlGCS):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DownloadUrlGCS
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: RequestDownloadUrlGCS,
) -> Response[DownloadUrlGCS]:
    """Generate Download Url User Avatar

     Download your global user avatar. Access your profile picture with a time-limited
    secure URL that expires after 1 minute. Useful for viewing or backing up your
    avatar image before making changes.

    Args:
        body (RequestDownloadUrlGCS):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DownloadUrlGCS]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: RequestDownloadUrlGCS,
) -> DownloadUrlGCS | None:
    """Generate Download Url User Avatar

     Download your global user avatar. Access your profile picture with a time-limited
    secure URL that expires after 1 minute. Useful for viewing or backing up your
    avatar image before making changes.

    Args:
        body (RequestDownloadUrlGCS):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DownloadUrlGCS
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
