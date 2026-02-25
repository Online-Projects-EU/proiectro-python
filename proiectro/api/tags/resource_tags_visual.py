from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.output_resource_tags import OutputResourceTags
from ...types import Response


def _get_kwargs(
    tenant_path: str,
    resource_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/{tenant_path}/resource_tags_visual/{resource_id}".format(
            tenant_path=quote(str(tenant_path), safe=""),
            resource_id=quote(str(resource_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> OutputResourceTags | None:
    if response.status_code == 200:
        response_200 = OutputResourceTags.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[OutputResourceTags]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    tenant_path: str,
    resource_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[OutputResourceTags]:
    """Resource Tags Visual

     Display resource tags with visual enhancements for improved UI presentation.
    Includes styling and color information for resource cards and lists.
    Optimized for resource planning interfaces and allocation screens.

    Args:
        tenant_path (str):
        resource_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OutputResourceTags]
    """

    kwargs = _get_kwargs(
        tenant_path=tenant_path,
        resource_id=resource_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    tenant_path: str,
    resource_id: str,
    *,
    client: AuthenticatedClient,
) -> OutputResourceTags | None:
    """Resource Tags Visual

     Display resource tags with visual enhancements for improved UI presentation.
    Includes styling and color information for resource cards and lists.
    Optimized for resource planning interfaces and allocation screens.

    Args:
        tenant_path (str):
        resource_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OutputResourceTags
    """

    return sync_detailed(
        tenant_path=tenant_path,
        resource_id=resource_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    tenant_path: str,
    resource_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[OutputResourceTags]:
    """Resource Tags Visual

     Display resource tags with visual enhancements for improved UI presentation.
    Includes styling and color information for resource cards and lists.
    Optimized for resource planning interfaces and allocation screens.

    Args:
        tenant_path (str):
        resource_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OutputResourceTags]
    """

    kwargs = _get_kwargs(
        tenant_path=tenant_path,
        resource_id=resource_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    tenant_path: str,
    resource_id: str,
    *,
    client: AuthenticatedClient,
) -> OutputResourceTags | None:
    """Resource Tags Visual

     Display resource tags with visual enhancements for improved UI presentation.
    Includes styling and color information for resource cards and lists.
    Optimized for resource planning interfaces and allocation screens.

    Args:
        tenant_path (str):
        resource_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OutputResourceTags
    """

    return (
        await asyncio_detailed(
            tenant_path=tenant_path,
            resource_id=resource_id,
            client=client,
        )
    ).parsed
