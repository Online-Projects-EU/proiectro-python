from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.output_business_process import OutputBusinessProcess
from ...types import UNSET, Response, Unset


def _get_kwargs(
    tenant_path: str,
    process_name: str,
    *,
    highlight_task: int | None | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_highlight_task: int | None | Unset
    if isinstance(highlight_task, Unset):
        json_highlight_task = UNSET
    else:
        json_highlight_task = highlight_task
    params["highlight_task"] = json_highlight_task

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/{tenant_path}/business_process/{process_name}".format(
            tenant_path=quote(str(tenant_path), safe=""),
            process_name=quote(str(process_name), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> OutputBusinessProcess | None:
    if response.status_code == 200:
        response_200 = OutputBusinessProcess.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[OutputBusinessProcess]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    tenant_path: str,
    process_name: str,
    *,
    client: AuthenticatedClient,
    highlight_task: int | None | Unset = UNSET,
) -> Response[OutputBusinessProcess]:
    """Tenant Business Process

     Get detailed information about a business process.
    Shows all tasks in order with optional highlighting of the current task.

    Args:
        tenant_path (str):
        process_name (str):
        highlight_task (int | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OutputBusinessProcess]
    """

    kwargs = _get_kwargs(
        tenant_path=tenant_path,
        process_name=process_name,
        highlight_task=highlight_task,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    tenant_path: str,
    process_name: str,
    *,
    client: AuthenticatedClient,
    highlight_task: int | None | Unset = UNSET,
) -> OutputBusinessProcess | None:
    """Tenant Business Process

     Get detailed information about a business process.
    Shows all tasks in order with optional highlighting of the current task.

    Args:
        tenant_path (str):
        process_name (str):
        highlight_task (int | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OutputBusinessProcess
    """

    return sync_detailed(
        tenant_path=tenant_path,
        process_name=process_name,
        client=client,
        highlight_task=highlight_task,
    ).parsed


async def asyncio_detailed(
    tenant_path: str,
    process_name: str,
    *,
    client: AuthenticatedClient,
    highlight_task: int | None | Unset = UNSET,
) -> Response[OutputBusinessProcess]:
    """Tenant Business Process

     Get detailed information about a business process.
    Shows all tasks in order with optional highlighting of the current task.

    Args:
        tenant_path (str):
        process_name (str):
        highlight_task (int | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OutputBusinessProcess]
    """

    kwargs = _get_kwargs(
        tenant_path=tenant_path,
        process_name=process_name,
        highlight_task=highlight_task,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    tenant_path: str,
    process_name: str,
    *,
    client: AuthenticatedClient,
    highlight_task: int | None | Unset = UNSET,
) -> OutputBusinessProcess | None:
    """Tenant Business Process

     Get detailed information about a business process.
    Shows all tasks in order with optional highlighting of the current task.

    Args:
        tenant_path (str):
        process_name (str):
        highlight_task (int | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OutputBusinessProcess
    """

    return (
        await asyncio_detailed(
            tenant_path=tenant_path,
            process_name=process_name,
            client=client,
            highlight_task=highlight_task,
        )
    ).parsed
