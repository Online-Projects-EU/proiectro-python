from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.work_item_work_logs_output import WorkItemWorkLogsOutput
from ...types import Response


def _get_kwargs(
    tenant_path: str,
    work_item_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/{tenant_path}/work_item_work_logs/{work_item_id}".format(
            tenant_path=quote(str(tenant_path), safe=""),
            work_item_id=quote(str(work_item_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> WorkItemWorkLogsOutput | None:
    if response.status_code == 200:
        response_200 = WorkItemWorkLogsOutput.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[WorkItemWorkLogsOutput]:
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
) -> Response[WorkItemWorkLogsOutput]:
    """Work Item Work Logs

     List all work logs for a work item.
    Shows time tracking entries by team members.

    Args:
        tenant_path (str):
        work_item_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[WorkItemWorkLogsOutput]
    """

    kwargs = _get_kwargs(
        tenant_path=tenant_path,
        work_item_id=work_item_id,
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
) -> WorkItemWorkLogsOutput | None:
    """Work Item Work Logs

     List all work logs for a work item.
    Shows time tracking entries by team members.

    Args:
        tenant_path (str):
        work_item_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        WorkItemWorkLogsOutput
    """

    return sync_detailed(
        tenant_path=tenant_path,
        work_item_id=work_item_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    tenant_path: str,
    work_item_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[WorkItemWorkLogsOutput]:
    """Work Item Work Logs

     List all work logs for a work item.
    Shows time tracking entries by team members.

    Args:
        tenant_path (str):
        work_item_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[WorkItemWorkLogsOutput]
    """

    kwargs = _get_kwargs(
        tenant_path=tenant_path,
        work_item_id=work_item_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    tenant_path: str,
    work_item_id: str,
    *,
    client: AuthenticatedClient,
) -> WorkItemWorkLogsOutput | None:
    """Work Item Work Logs

     List all work logs for a work item.
    Shows time tracking entries by team members.

    Args:
        tenant_path (str):
        work_item_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        WorkItemWorkLogsOutput
    """

    return (
        await asyncio_detailed(
            tenant_path=tenant_path,
            work_item_id=work_item_id,
            client=client,
        )
    ).parsed
