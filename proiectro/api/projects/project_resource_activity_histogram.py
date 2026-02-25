from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.project_resource_activity_histogram_schema import (
    ProjectResourceActivityHistogramSchema,
)
from ...types import Response


def _get_kwargs(
    tenant_path: str,
    project_id: str,
    resource_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/{tenant_path}/project_resource_activity_histogram/{project_id}/{resource_id}".format(
            tenant_path=quote(str(tenant_path), safe=""),
            project_id=quote(str(project_id), safe=""),
            resource_id=quote(str(resource_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ProjectResourceActivityHistogramSchema | None:
    if response.status_code == 200:
        response_200 = ProjectResourceActivityHistogramSchema.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ProjectResourceActivityHistogramSchema]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    tenant_path: str,
    project_id: str,
    resource_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[ProjectResourceActivityHistogramSchema]:
    """Project Resource Activity Histogram

     Get histogram of resource usage by ISO year-week for a specific resource in a project.
    Aggregates WorkResourceUsage by week from earliest booking start to latest booking end.
    Shows usage patterns and identifies peak utilization periods across project timeline.
    Useful for capacity planning and understanding resource consumption trends.

    Args:
        tenant_path (str):
        project_id (str):
        resource_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ProjectResourceActivityHistogramSchema]
    """

    kwargs = _get_kwargs(
        tenant_path=tenant_path,
        project_id=project_id,
        resource_id=resource_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    tenant_path: str,
    project_id: str,
    resource_id: str,
    *,
    client: AuthenticatedClient,
) -> ProjectResourceActivityHistogramSchema | None:
    """Project Resource Activity Histogram

     Get histogram of resource usage by ISO year-week for a specific resource in a project.
    Aggregates WorkResourceUsage by week from earliest booking start to latest booking end.
    Shows usage patterns and identifies peak utilization periods across project timeline.
    Useful for capacity planning and understanding resource consumption trends.

    Args:
        tenant_path (str):
        project_id (str):
        resource_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ProjectResourceActivityHistogramSchema
    """

    return sync_detailed(
        tenant_path=tenant_path,
        project_id=project_id,
        resource_id=resource_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    tenant_path: str,
    project_id: str,
    resource_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[ProjectResourceActivityHistogramSchema]:
    """Project Resource Activity Histogram

     Get histogram of resource usage by ISO year-week for a specific resource in a project.
    Aggregates WorkResourceUsage by week from earliest booking start to latest booking end.
    Shows usage patterns and identifies peak utilization periods across project timeline.
    Useful for capacity planning and understanding resource consumption trends.

    Args:
        tenant_path (str):
        project_id (str):
        resource_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ProjectResourceActivityHistogramSchema]
    """

    kwargs = _get_kwargs(
        tenant_path=tenant_path,
        project_id=project_id,
        resource_id=resource_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    tenant_path: str,
    project_id: str,
    resource_id: str,
    *,
    client: AuthenticatedClient,
) -> ProjectResourceActivityHistogramSchema | None:
    """Project Resource Activity Histogram

     Get histogram of resource usage by ISO year-week for a specific resource in a project.
    Aggregates WorkResourceUsage by week from earliest booking start to latest booking end.
    Shows usage patterns and identifies peak utilization periods across project timeline.
    Useful for capacity planning and understanding resource consumption trends.

    Args:
        tenant_path (str):
        project_id (str):
        resource_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ProjectResourceActivityHistogramSchema
    """

    return (
        await asyncio_detailed(
            tenant_path=tenant_path,
            project_id=project_id,
            resource_id=resource_id,
            client=client,
        )
    ).parsed
