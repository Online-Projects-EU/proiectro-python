from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_response import APIResponse
from ...models.edit_support_request_queue import EditSupportRequestQueue
from ...models.edit_support_request_queue_response import (
    EditSupportRequestQueueResponse,
)
from ...types import Response


def _get_kwargs(
    tenant_path: str,
    queue_id: str,
    *,
    body: EditSupportRequestQueue,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/api/v1/{tenant_path}/edit_support_request_queue/{queue_id}".format(
            tenant_path=quote(str(tenant_path), safe=""),
            queue_id=quote(str(queue_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> APIResponse | EditSupportRequestQueueResponse | None:
    if response.status_code == 200:
        response_200 = APIResponse.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = APIResponse.from_dict(response.json())

        return response_400

    if response.status_code == 422:
        response_422 = EditSupportRequestQueueResponse.from_dict(response.json())

        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[APIResponse | EditSupportRequestQueueResponse]:
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
    body: EditSupportRequestQueue,
) -> Response[APIResponse | EditSupportRequestQueueResponse]:
    """Edit Support Request Queue

     Update queue configuration when team structures or responsibilities change.
    Modify assignments, descriptions, or routing priorities. Changes affect
    new request routing - existing requests remain in current queues.
    Review routing rules to ensure proper request distribution.

    Args:
        tenant_path (str):
        queue_id (str):
        body (EditSupportRequestQueue): Input schema for editing a support request queue

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[APIResponse | EditSupportRequestQueueResponse]
    """

    kwargs = _get_kwargs(
        tenant_path=tenant_path,
        queue_id=queue_id,
        body=body,
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
    body: EditSupportRequestQueue,
) -> APIResponse | EditSupportRequestQueueResponse | None:
    """Edit Support Request Queue

     Update queue configuration when team structures or responsibilities change.
    Modify assignments, descriptions, or routing priorities. Changes affect
    new request routing - existing requests remain in current queues.
    Review routing rules to ensure proper request distribution.

    Args:
        tenant_path (str):
        queue_id (str):
        body (EditSupportRequestQueue): Input schema for editing a support request queue

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        APIResponse | EditSupportRequestQueueResponse
    """

    return sync_detailed(
        tenant_path=tenant_path,
        queue_id=queue_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    tenant_path: str,
    queue_id: str,
    *,
    client: AuthenticatedClient,
    body: EditSupportRequestQueue,
) -> Response[APIResponse | EditSupportRequestQueueResponse]:
    """Edit Support Request Queue

     Update queue configuration when team structures or responsibilities change.
    Modify assignments, descriptions, or routing priorities. Changes affect
    new request routing - existing requests remain in current queues.
    Review routing rules to ensure proper request distribution.

    Args:
        tenant_path (str):
        queue_id (str):
        body (EditSupportRequestQueue): Input schema for editing a support request queue

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[APIResponse | EditSupportRequestQueueResponse]
    """

    kwargs = _get_kwargs(
        tenant_path=tenant_path,
        queue_id=queue_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    tenant_path: str,
    queue_id: str,
    *,
    client: AuthenticatedClient,
    body: EditSupportRequestQueue,
) -> APIResponse | EditSupportRequestQueueResponse | None:
    """Edit Support Request Queue

     Update queue configuration when team structures or responsibilities change.
    Modify assignments, descriptions, or routing priorities. Changes affect
    new request routing - existing requests remain in current queues.
    Review routing rules to ensure proper request distribution.

    Args:
        tenant_path (str):
        queue_id (str):
        body (EditSupportRequestQueue): Input schema for editing a support request queue

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        APIResponse | EditSupportRequestQueueResponse
    """

    return (
        await asyncio_detailed(
            tenant_path=tenant_path,
            queue_id=queue_id,
            client=client,
            body=body,
        )
    ).parsed
