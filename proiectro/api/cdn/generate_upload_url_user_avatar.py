from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.request_upload_url_gcs import RequestUploadUrlGCS
from ...models.upload_url_gcs import UploadUrlGCS
from ...types import Response


def _get_kwargs(
    *,
    body: RequestUploadUrlGCS,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/generate_upload_url_user_avatar",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> UploadUrlGCS | None:
    if response.status_code == 200:
        response_200 = UploadUrlGCS.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[UploadUrlGCS]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: RequestUploadUrlGCS,
) -> Response[UploadUrlGCS]:
    """Generate Upload Url User Avatar

     Upload your global user avatar that appears across all workspaces you access.
    This avatar is your default identity throughout the platform. The secure URL
    expires in 15 minutes - upload immediately after generation. Previous global
    avatars are replaced. Workspace-specific avatars can override this in individual tenants.

    Args:
        body (RequestUploadUrlGCS):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UploadUrlGCS]
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
    body: RequestUploadUrlGCS,
) -> UploadUrlGCS | None:
    """Generate Upload Url User Avatar

     Upload your global user avatar that appears across all workspaces you access.
    This avatar is your default identity throughout the platform. The secure URL
    expires in 15 minutes - upload immediately after generation. Previous global
    avatars are replaced. Workspace-specific avatars can override this in individual tenants.

    Args:
        body (RequestUploadUrlGCS):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UploadUrlGCS
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: RequestUploadUrlGCS,
) -> Response[UploadUrlGCS]:
    """Generate Upload Url User Avatar

     Upload your global user avatar that appears across all workspaces you access.
    This avatar is your default identity throughout the platform. The secure URL
    expires in 15 minutes - upload immediately after generation. Previous global
    avatars are replaced. Workspace-specific avatars can override this in individual tenants.

    Args:
        body (RequestUploadUrlGCS):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UploadUrlGCS]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: RequestUploadUrlGCS,
) -> UploadUrlGCS | None:
    """Generate Upload Url User Avatar

     Upload your global user avatar that appears across all workspaces you access.
    This avatar is your default identity throughout the platform. The secure URL
    expires in 15 minutes - upload immediately after generation. Previous global
    avatars are replaced. Workspace-specific avatars can override this in individual tenants.

    Args:
        body (RequestUploadUrlGCS):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UploadUrlGCS
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
