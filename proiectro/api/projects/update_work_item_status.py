from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_response import APIResponse
from ...models.update_work_item_status import UpdateWorkItemStatus
from ...types import Response


def _get_kwargs(
    tenant_path: str,
    work_item_id: str,
    *,
    body: UpdateWorkItemStatus,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/api/v1/{tenant_path}/update_work_item_status/{work_item_id}".format(
            tenant_path=quote(str(tenant_path), safe=""),
            work_item_id=quote(str(work_item_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> APIResponse | None:
    if response.status_code == 200:
        response_200 = APIResponse.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = APIResponse.from_dict(response.json())

        return response_400

    if response.status_code == 422:
        response_422 = APIResponse.from_dict(response.json())

        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[APIResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    tenant_path: str,
    work_item_id: str,
    *,
    client: AuthenticatedClient,
    body: UpdateWorkItemStatus,
) -> Response[APIResponse]:
    """Update Work Item Status

     Update work item status (execution and event type work items).
    - EXECUTION: Updates percent_complete, is_finished, and finished_at fields
    - EVENT: Updates is_finished and finished_at fields only (no percent_complete)

    Args:
        tenant_path (str):
        work_item_id (str):
        body (UpdateWorkItemStatus): Schema for updating work item status (execution-type work
            items only).

            Dynamic behavior based on current state:
            - NOT finished: Send finished_at to mark as complete (auto-sets is_finished=True,
            percent=100)
            - IS finished: Send is_finished=False to unmark (clears finished_at, resets percent if was
            100)
            - Always: Send percent_complete to adjust progress independently

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[APIResponse]
    """

    kwargs = _get_kwargs(
        tenant_path=tenant_path,
        work_item_id=work_item_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    tenant_path: str,
    work_item_id: str,
    *,
    client: AuthenticatedClient,
    body: UpdateWorkItemStatus,
) -> APIResponse | None:
    """Update Work Item Status

     Update work item status (execution and event type work items).
    - EXECUTION: Updates percent_complete, is_finished, and finished_at fields
    - EVENT: Updates is_finished and finished_at fields only (no percent_complete)

    Args:
        tenant_path (str):
        work_item_id (str):
        body (UpdateWorkItemStatus): Schema for updating work item status (execution-type work
            items only).

            Dynamic behavior based on current state:
            - NOT finished: Send finished_at to mark as complete (auto-sets is_finished=True,
            percent=100)
            - IS finished: Send is_finished=False to unmark (clears finished_at, resets percent if was
            100)
            - Always: Send percent_complete to adjust progress independently

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        APIResponse
    """

    return sync_detailed(
        tenant_path=tenant_path,
        work_item_id=work_item_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    tenant_path: str,
    work_item_id: str,
    *,
    client: AuthenticatedClient,
    body: UpdateWorkItemStatus,
) -> Response[APIResponse]:
    """Update Work Item Status

     Update work item status (execution and event type work items).
    - EXECUTION: Updates percent_complete, is_finished, and finished_at fields
    - EVENT: Updates is_finished and finished_at fields only (no percent_complete)

    Args:
        tenant_path (str):
        work_item_id (str):
        body (UpdateWorkItemStatus): Schema for updating work item status (execution-type work
            items only).

            Dynamic behavior based on current state:
            - NOT finished: Send finished_at to mark as complete (auto-sets is_finished=True,
            percent=100)
            - IS finished: Send is_finished=False to unmark (clears finished_at, resets percent if was
            100)
            - Always: Send percent_complete to adjust progress independently

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[APIResponse]
    """

    kwargs = _get_kwargs(
        tenant_path=tenant_path,
        work_item_id=work_item_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    tenant_path: str,
    work_item_id: str,
    *,
    client: AuthenticatedClient,
    body: UpdateWorkItemStatus,
) -> APIResponse | None:
    """Update Work Item Status

     Update work item status (execution and event type work items).
    - EXECUTION: Updates percent_complete, is_finished, and finished_at fields
    - EVENT: Updates is_finished and finished_at fields only (no percent_complete)

    Args:
        tenant_path (str):
        work_item_id (str):
        body (UpdateWorkItemStatus): Schema for updating work item status (execution-type work
            items only).

            Dynamic behavior based on current state:
            - NOT finished: Send finished_at to mark as complete (auto-sets is_finished=True,
            percent=100)
            - IS finished: Send is_finished=False to unmark (clears finished_at, resets percent if was
            100)
            - Always: Send percent_complete to adjust progress independently

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        APIResponse
    """

    return (
        await asyncio_detailed(
            tenant_path=tenant_path,
            work_item_id=work_item_id,
            client=client,
            body=body,
        )
    ).parsed
