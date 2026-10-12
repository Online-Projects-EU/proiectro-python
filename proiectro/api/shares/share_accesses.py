from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.output_share_accesses import OutputShareAccesses
from ...types import Response


def _get_kwargs(
    tenant_path: str,
    share_id: str,
    page_number: int,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/{tenant_path}/share_accesses/{share_id}/{page_number}".format(
            tenant_path=quote(str(tenant_path), safe=""),
            share_id=quote(str(share_id), safe=""),
            page_number=quote(str(page_number), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> OutputShareAccesses | None:
    if response.status_code == 200:
        response_200 = OutputShareAccesses.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[OutputShareAccesses]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    tenant_path: str,
    share_id: str,
    page_number: int,
    *,
    client: AuthenticatedClient,
) -> Response[OutputShareAccesses]:
    """Share Accesses

     List a share's activity, newest first, one page at a time: who opened it, which items they
    viewed or downloaded, and through which channel. `next_page` is 0 on the last page.

    Args:
        tenant_path (str):
        share_id (str):
        page_number (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OutputShareAccesses]
    """

    kwargs = _get_kwargs(
        tenant_path=tenant_path,
        share_id=share_id,
        page_number=page_number,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    tenant_path: str,
    share_id: str,
    page_number: int,
    *,
    client: AuthenticatedClient,
) -> OutputShareAccesses | None:
    """Share Accesses

     List a share's activity, newest first, one page at a time: who opened it, which items they
    viewed or downloaded, and through which channel. `next_page` is 0 on the last page.

    Args:
        tenant_path (str):
        share_id (str):
        page_number (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OutputShareAccesses
    """

    return sync_detailed(
        tenant_path=tenant_path,
        share_id=share_id,
        page_number=page_number,
        client=client,
    ).parsed


async def asyncio_detailed(
    tenant_path: str,
    share_id: str,
    page_number: int,
    *,
    client: AuthenticatedClient,
) -> Response[OutputShareAccesses]:
    """Share Accesses

     List a share's activity, newest first, one page at a time: who opened it, which items they
    viewed or downloaded, and through which channel. `next_page` is 0 on the last page.

    Args:
        tenant_path (str):
        share_id (str):
        page_number (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OutputShareAccesses]
    """

    kwargs = _get_kwargs(
        tenant_path=tenant_path,
        share_id=share_id,
        page_number=page_number,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    tenant_path: str,
    share_id: str,
    page_number: int,
    *,
    client: AuthenticatedClient,
) -> OutputShareAccesses | None:
    """Share Accesses

     List a share's activity, newest first, one page at a time: who opened it, which items they
    viewed or downloaded, and through which channel. `next_page` is 0 on the last page.

    Args:
        tenant_path (str):
        share_id (str):
        page_number (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OutputShareAccesses
    """

    return (
        await asyncio_detailed(
            tenant_path=tenant_path,
            share_id=share_id,
            page_number=page_number,
            client=client,
        )
    ).parsed
