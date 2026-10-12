from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_response import APIResponse
from ...models.download_url_gcs import DownloadUrlGCS
from ...types import Response


def _get_kwargs(
    customer_org_id: str,
    share_id: str,
    item_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/portal/{customer_org_id}/shares/{share_id}/download_url/{item_id}".format(
            customer_org_id=quote(str(customer_org_id), safe=""),
            share_id=quote(str(share_id), safe=""),
            item_id=quote(str(item_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> APIResponse | DownloadUrlGCS | None:
    if response.status_code == 200:
        response_200 = DownloadUrlGCS.from_dict(response.json())

        return response_200

    if response.status_code == 404:
        response_404 = APIResponse.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[APIResponse | DownloadUrlGCS]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    customer_org_id: str,
    share_id: str,
    item_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[APIResponse | DownloadUrlGCS]:
    """Portal Share Generate Download Url

     Get a one-minute download link for a file in a share, as it was when it was shared.

    Args:
        customer_org_id (str):
        share_id (str):
        item_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[APIResponse | DownloadUrlGCS]
    """

    kwargs = _get_kwargs(
        customer_org_id=customer_org_id,
        share_id=share_id,
        item_id=item_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    customer_org_id: str,
    share_id: str,
    item_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> APIResponse | DownloadUrlGCS | None:
    """Portal Share Generate Download Url

     Get a one-minute download link for a file in a share, as it was when it was shared.

    Args:
        customer_org_id (str):
        share_id (str):
        item_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        APIResponse | DownloadUrlGCS
    """

    return sync_detailed(
        customer_org_id=customer_org_id,
        share_id=share_id,
        item_id=item_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    customer_org_id: str,
    share_id: str,
    item_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[APIResponse | DownloadUrlGCS]:
    """Portal Share Generate Download Url

     Get a one-minute download link for a file in a share, as it was when it was shared.

    Args:
        customer_org_id (str):
        share_id (str):
        item_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[APIResponse | DownloadUrlGCS]
    """

    kwargs = _get_kwargs(
        customer_org_id=customer_org_id,
        share_id=share_id,
        item_id=item_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    customer_org_id: str,
    share_id: str,
    item_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> APIResponse | DownloadUrlGCS | None:
    """Portal Share Generate Download Url

     Get a one-minute download link for a file in a share, as it was when it was shared.

    Args:
        customer_org_id (str):
        share_id (str):
        item_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        APIResponse | DownloadUrlGCS
    """

    return (
        await asyncio_detailed(
            customer_org_id=customer_org_id,
            share_id=share_id,
            item_id=item_id,
            client=client,
        )
    ).parsed
