from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.output_saved_filters_list import OutputSavedFiltersList
from ...types import Response


def _get_kwargs(
    tenant_path: str,
    queue_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/{tenant_path}/list_saved_filters_queue_closed_external_support_requests/{queue_id}".format(
            tenant_path=quote(str(tenant_path), safe=""),
            queue_id=quote(str(queue_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> OutputSavedFiltersList | None:
    if response.status_code == 200:
        response_200 = OutputSavedFiltersList.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[OutputSavedFiltersList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    tenant_path: str,
    queue_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[OutputSavedFiltersList]:
    """List Saved Filters Queue Closed External Support Requests

     List all available saved filters for a specific external closed support request queue. Returns
    filters
    you created (personal) and filters shared by your team members. Filters are queue-specific, so
    you only see filters saved for this particular closed queue. Use these saved filters to quickly
    apply
    complex filter combinations for historical analysis without manually rebuilding criteria.

    Args:
        tenant_path (str):
        queue_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OutputSavedFiltersList]
    """

    kwargs = _get_kwargs(
        tenant_path=tenant_path,
        queue_id=queue_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    tenant_path: str,
    queue_id: str,
    *,
    client: AuthenticatedClient,
) -> OutputSavedFiltersList | None:
    """List Saved Filters Queue Closed External Support Requests

     List all available saved filters for a specific external closed support request queue. Returns
    filters
    you created (personal) and filters shared by your team members. Filters are queue-specific, so
    you only see filters saved for this particular closed queue. Use these saved filters to quickly
    apply
    complex filter combinations for historical analysis without manually rebuilding criteria.

    Args:
        tenant_path (str):
        queue_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OutputSavedFiltersList
    """

    return sync_detailed(
        tenant_path=tenant_path,
        queue_id=queue_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    tenant_path: str,
    queue_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[OutputSavedFiltersList]:
    """List Saved Filters Queue Closed External Support Requests

     List all available saved filters for a specific external closed support request queue. Returns
    filters
    you created (personal) and filters shared by your team members. Filters are queue-specific, so
    you only see filters saved for this particular closed queue. Use these saved filters to quickly
    apply
    complex filter combinations for historical analysis without manually rebuilding criteria.

    Args:
        tenant_path (str):
        queue_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OutputSavedFiltersList]
    """

    kwargs = _get_kwargs(
        tenant_path=tenant_path,
        queue_id=queue_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    tenant_path: str,
    queue_id: str,
    *,
    client: AuthenticatedClient,
) -> OutputSavedFiltersList | None:
    """List Saved Filters Queue Closed External Support Requests

     List all available saved filters for a specific external closed support request queue. Returns
    filters
    you created (personal) and filters shared by your team members. Filters are queue-specific, so
    you only see filters saved for this particular closed queue. Use these saved filters to quickly
    apply
    complex filter combinations for historical analysis without manually rebuilding criteria.

    Args:
        tenant_path (str):
        queue_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OutputSavedFiltersList
    """

    return (
        await asyncio_detailed(
            tenant_path=tenant_path,
            queue_id=queue_id,
            client=client,
        )
    ).parsed
