from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.files_storage_metrics import FilesStorageMetrics
from ...types import Response


def _get_kwargs(
    tenant_path: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/{tenant_path}/files_storage_metrics".format(
            tenant_path=quote(str(tenant_path), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> FilesStorageMetrics | None:
    if response.status_code == 200:
        response_200 = FilesStorageMetrics.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[FilesStorageMetrics]:
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
) -> Response[FilesStorageMetrics]:
    """Files Storage Metrics

     Monitor overall storage consumption and file activity across your workspace. Track
    total storage usage against quotas, daily upload patterns, and active user engagement.
    Essential for capacity planning and identifying unusual storage spikes that might
    indicate issues. Helps optimize storage costs by understanding usage patterns.

    Args:
        tenant_path (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FilesStorageMetrics]
    """

    kwargs = _get_kwargs(
        tenant_path=tenant_path,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    tenant_path: str,
    *,
    client: AuthenticatedClient,
) -> FilesStorageMetrics | None:
    """Files Storage Metrics

     Monitor overall storage consumption and file activity across your workspace. Track
    total storage usage against quotas, daily upload patterns, and active user engagement.
    Essential for capacity planning and identifying unusual storage spikes that might
    indicate issues. Helps optimize storage costs by understanding usage patterns.

    Args:
        tenant_path (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FilesStorageMetrics
    """

    return sync_detailed(
        tenant_path=tenant_path,
        client=client,
    ).parsed


async def asyncio_detailed(
    tenant_path: str,
    *,
    client: AuthenticatedClient,
) -> Response[FilesStorageMetrics]:
    """Files Storage Metrics

     Monitor overall storage consumption and file activity across your workspace. Track
    total storage usage against quotas, daily upload patterns, and active user engagement.
    Essential for capacity planning and identifying unusual storage spikes that might
    indicate issues. Helps optimize storage costs by understanding usage patterns.

    Args:
        tenant_path (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FilesStorageMetrics]
    """

    kwargs = _get_kwargs(
        tenant_path=tenant_path,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    tenant_path: str,
    *,
    client: AuthenticatedClient,
) -> FilesStorageMetrics | None:
    """Files Storage Metrics

     Monitor overall storage consumption and file activity across your workspace. Track
    total storage usage against quotas, daily upload patterns, and active user engagement.
    Essential for capacity planning and identifying unusual storage spikes that might
    indicate issues. Helps optimize storage costs by understanding usage patterns.

    Args:
        tenant_path (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FilesStorageMetrics
    """

    return (
        await asyncio_detailed(
            tenant_path=tenant_path,
            client=client,
        )
    ).parsed
