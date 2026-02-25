from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.output_process_stages_with_tasks import OutputProcessStagesWithTasks
from ...types import Response


def _get_kwargs(
    tenant_path: str,
    process_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/{tenant_path}/process_stage_tasks/{process_id}".format(
            tenant_path=quote(str(tenant_path), safe=""),
            process_id=quote(str(process_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> OutputProcessStagesWithTasks | None:
    if response.status_code == 200:
        response_200 = OutputProcessStagesWithTasks.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[OutputProcessStagesWithTasks]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    tenant_path: str,
    process_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[OutputProcessStagesWithTasks]:
    """Process Stage Tasks

    Args:
        tenant_path (str):
        process_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OutputProcessStagesWithTasks]
    """

    kwargs = _get_kwargs(
        tenant_path=tenant_path,
        process_id=process_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    tenant_path: str,
    process_id: str,
    *,
    client: AuthenticatedClient,
) -> OutputProcessStagesWithTasks | None:
    """Process Stage Tasks

    Args:
        tenant_path (str):
        process_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OutputProcessStagesWithTasks
    """

    return sync_detailed(
        tenant_path=tenant_path,
        process_id=process_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    tenant_path: str,
    process_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[OutputProcessStagesWithTasks]:
    """Process Stage Tasks

    Args:
        tenant_path (str):
        process_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OutputProcessStagesWithTasks]
    """

    kwargs = _get_kwargs(
        tenant_path=tenant_path,
        process_id=process_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    tenant_path: str,
    process_id: str,
    *,
    client: AuthenticatedClient,
) -> OutputProcessStagesWithTasks | None:
    """Process Stage Tasks

    Args:
        tenant_path (str):
        process_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OutputProcessStagesWithTasks
    """

    return (
        await asyncio_detailed(
            tenant_path=tenant_path,
            process_id=process_id,
            client=client,
        )
    ).parsed
