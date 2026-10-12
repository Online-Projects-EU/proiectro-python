from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_response import APIResponse
from ...models.pydantic_detail import PydanticDetail
from ...types import Response


def _get_kwargs(
    tenant_path: str,
    share_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/api/v1/{tenant_path}/remove_share_link/{share_id}".format(
            tenant_path=quote(str(tenant_path), safe=""),
            share_id=quote(str(share_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> APIResponse | PydanticDetail | None:
    if response.status_code == 200:
        response_200 = APIResponse.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = APIResponse.from_dict(response.json())

        return response_400

    if response.status_code == 404:
        response_404 = APIResponse.from_dict(response.json())

        return response_404

    if response.status_code == 409:
        response_409 = APIResponse.from_dict(response.json())

        return response_409

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
    tenant_path: str,
    share_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[APIResponse | PydanticDetail]:
    """Remove Share Link

     Remove the share's link: it shows a page saying it is not available. The share stays in the
    customer portal.

    Args:
        tenant_path (str):
        share_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[APIResponse | PydanticDetail]
    """

    kwargs = _get_kwargs(
        tenant_path=tenant_path,
        share_id=share_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    tenant_path: str,
    share_id: str,
    *,
    client: AuthenticatedClient,
) -> APIResponse | PydanticDetail | None:
    """Remove Share Link

     Remove the share's link: it shows a page saying it is not available. The share stays in the
    customer portal.

    Args:
        tenant_path (str):
        share_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        APIResponse | PydanticDetail
    """

    return sync_detailed(
        tenant_path=tenant_path,
        share_id=share_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    tenant_path: str,
    share_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[APIResponse | PydanticDetail]:
    """Remove Share Link

     Remove the share's link: it shows a page saying it is not available. The share stays in the
    customer portal.

    Args:
        tenant_path (str):
        share_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[APIResponse | PydanticDetail]
    """

    kwargs = _get_kwargs(
        tenant_path=tenant_path,
        share_id=share_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    tenant_path: str,
    share_id: str,
    *,
    client: AuthenticatedClient,
) -> APIResponse | PydanticDetail | None:
    """Remove Share Link

     Remove the share's link: it shows a page saying it is not available. The share stays in the
    customer portal.

    Args:
        tenant_path (str):
        share_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        APIResponse | PydanticDetail
    """

    return (
        await asyncio_detailed(
            tenant_path=tenant_path,
            share_id=share_id,
            client=client,
        )
    ).parsed
