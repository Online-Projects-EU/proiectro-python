from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.output_kpi_work_items_due import OutputKPIWorkItemsDue
from ...types import UNSET, Response, Unset


def _get_kwargs(
    tenant_path: str,
    *,
    due_within_days: int | None | Unset = UNSET,
    project_id: None | str | Unset = UNSET,
    include_items: bool | Unset = False,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_due_within_days: int | None | Unset
    if isinstance(due_within_days, Unset):
        json_due_within_days = UNSET
    else:
        json_due_within_days = due_within_days
    params["due_within_days"] = json_due_within_days

    json_project_id: None | str | Unset
    if isinstance(project_id, Unset):
        json_project_id = UNSET
    else:
        json_project_id = project_id
    params["project_id"] = json_project_id

    params["include_items"] = include_items

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/{tenant_path}/kpi/work_items_due".format(
            tenant_path=quote(str(tenant_path), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> OutputKPIWorkItemsDue | None:
    if response.status_code == 200:
        response_200 = OutputKPIWorkItemsDue.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[OutputKPIWorkItemsDue]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    tenant_path: str,
    *,
    client: AuthenticatedClient,
    due_within_days: int | None | Unset = UNSET,
    project_id: None | str | Unset = UNSET,
    include_items: bool | Unset = False,
) -> Response[OutputKPIWorkItemsDue]:
    """Kpi Work Items Due

    Args:
        tenant_path (str):
        due_within_days (int | None | Unset):
        project_id (None | str | Unset):
        include_items (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OutputKPIWorkItemsDue]
    """

    kwargs = _get_kwargs(
        tenant_path=tenant_path,
        due_within_days=due_within_days,
        project_id=project_id,
        include_items=include_items,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    tenant_path: str,
    *,
    client: AuthenticatedClient,
    due_within_days: int | None | Unset = UNSET,
    project_id: None | str | Unset = UNSET,
    include_items: bool | Unset = False,
) -> OutputKPIWorkItemsDue | None:
    """Kpi Work Items Due

    Args:
        tenant_path (str):
        due_within_days (int | None | Unset):
        project_id (None | str | Unset):
        include_items (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OutputKPIWorkItemsDue
    """

    return sync_detailed(
        tenant_path=tenant_path,
        client=client,
        due_within_days=due_within_days,
        project_id=project_id,
        include_items=include_items,
    ).parsed


async def asyncio_detailed(
    tenant_path: str,
    *,
    client: AuthenticatedClient,
    due_within_days: int | None | Unset = UNSET,
    project_id: None | str | Unset = UNSET,
    include_items: bool | Unset = False,
) -> Response[OutputKPIWorkItemsDue]:
    """Kpi Work Items Due

    Args:
        tenant_path (str):
        due_within_days (int | None | Unset):
        project_id (None | str | Unset):
        include_items (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OutputKPIWorkItemsDue]
    """

    kwargs = _get_kwargs(
        tenant_path=tenant_path,
        due_within_days=due_within_days,
        project_id=project_id,
        include_items=include_items,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    tenant_path: str,
    *,
    client: AuthenticatedClient,
    due_within_days: int | None | Unset = UNSET,
    project_id: None | str | Unset = UNSET,
    include_items: bool | Unset = False,
) -> OutputKPIWorkItemsDue | None:
    """Kpi Work Items Due

    Args:
        tenant_path (str):
        due_within_days (int | None | Unset):
        project_id (None | str | Unset):
        include_items (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OutputKPIWorkItemsDue
    """

    return (
        await asyncio_detailed(
            tenant_path=tenant_path,
            client=client,
            due_within_days=due_within_days,
            project_id=project_id,
            include_items=include_items,
        )
    ).parsed
