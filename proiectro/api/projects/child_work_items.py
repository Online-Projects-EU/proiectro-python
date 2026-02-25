from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.output_project_work_items import OutputProjectWorkItems
from ...types import Response


def _get_kwargs(
    tenant_path: str,
    project_id: str,
    parent_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/{tenant_path}/child_work_items/{project_id}/{parent_id}".format(
            tenant_path=quote(str(tenant_path), safe=""),
            project_id=quote(str(project_id), safe=""),
            parent_id=quote(str(parent_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> OutputProjectWorkItems | None:
    if response.status_code == 200:
        response_200 = OutputProjectWorkItems.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[OutputProjectWorkItems]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    tenant_path: str,
    project_id: str,
    parent_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[OutputProjectWorkItems]:
    """Child Work Items

     Get child work items hierarchy for a specific parent work item.
    Shows only the descendants of the specified parent work item,
    useful for drilling down into specific sections of the WBS.

    Args:
        tenant_path (str):
        project_id (str):
        parent_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OutputProjectWorkItems]
    """

    kwargs = _get_kwargs(
        tenant_path=tenant_path,
        project_id=project_id,
        parent_id=parent_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    tenant_path: str,
    project_id: str,
    parent_id: str,
    *,
    client: AuthenticatedClient,
) -> OutputProjectWorkItems | None:
    """Child Work Items

     Get child work items hierarchy for a specific parent work item.
    Shows only the descendants of the specified parent work item,
    useful for drilling down into specific sections of the WBS.

    Args:
        tenant_path (str):
        project_id (str):
        parent_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OutputProjectWorkItems
    """

    return sync_detailed(
        tenant_path=tenant_path,
        project_id=project_id,
        parent_id=parent_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    tenant_path: str,
    project_id: str,
    parent_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[OutputProjectWorkItems]:
    """Child Work Items

     Get child work items hierarchy for a specific parent work item.
    Shows only the descendants of the specified parent work item,
    useful for drilling down into specific sections of the WBS.

    Args:
        tenant_path (str):
        project_id (str):
        parent_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OutputProjectWorkItems]
    """

    kwargs = _get_kwargs(
        tenant_path=tenant_path,
        project_id=project_id,
        parent_id=parent_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    tenant_path: str,
    project_id: str,
    parent_id: str,
    *,
    client: AuthenticatedClient,
) -> OutputProjectWorkItems | None:
    """Child Work Items

     Get child work items hierarchy for a specific parent work item.
    Shows only the descendants of the specified parent work item,
    useful for drilling down into specific sections of the WBS.

    Args:
        tenant_path (str):
        project_id (str):
        parent_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OutputProjectWorkItems
    """

    return (
        await asyncio_detailed(
            tenant_path=tenant_path,
            project_id=project_id,
            parent_id=parent_id,
            client=client,
        )
    ).parsed
