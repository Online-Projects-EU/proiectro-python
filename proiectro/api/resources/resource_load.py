from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.resource_load_detail_schema import ResourceLoadDetailSchema
from ...types import Response


def _get_kwargs(
    tenant_path: str,
    resource_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/{tenant_path}/resource_load/{resource_id}".format(
            tenant_path=quote(str(tenant_path), safe=""),
            resource_id=quote(str(resource_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ResourceLoadDetailSchema | None:
    if response.status_code == 200:
        response_200 = ResourceLoadDetailSchema.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ResourceLoadDetailSchema]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    tenant_path: str,
    resource_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[ResourceLoadDetailSchema]:
    """Resource Load

     View resource utilization and load analysis. Shows current and projected workload
    for the resource across all active projects and proposals. Helps identify
    over-allocation and available capacity. Essential for resource planning and
    optimization decisions.

    Args:
        tenant_path (str):
        resource_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ResourceLoadDetailSchema]
    """

    kwargs = _get_kwargs(
        tenant_path=tenant_path,
        resource_id=resource_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    tenant_path: str,
    resource_id: str,
    *,
    client: AuthenticatedClient,
) -> ResourceLoadDetailSchema | None:
    """Resource Load

     View resource utilization and load analysis. Shows current and projected workload
    for the resource across all active projects and proposals. Helps identify
    over-allocation and available capacity. Essential for resource planning and
    optimization decisions.

    Args:
        tenant_path (str):
        resource_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ResourceLoadDetailSchema
    """

    return sync_detailed(
        tenant_path=tenant_path,
        resource_id=resource_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    tenant_path: str,
    resource_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[ResourceLoadDetailSchema]:
    """Resource Load

     View resource utilization and load analysis. Shows current and projected workload
    for the resource across all active projects and proposals. Helps identify
    over-allocation and available capacity. Essential for resource planning and
    optimization decisions.

    Args:
        tenant_path (str):
        resource_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ResourceLoadDetailSchema]
    """

    kwargs = _get_kwargs(
        tenant_path=tenant_path,
        resource_id=resource_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    tenant_path: str,
    resource_id: str,
    *,
    client: AuthenticatedClient,
) -> ResourceLoadDetailSchema | None:
    """Resource Load

     View resource utilization and load analysis. Shows current and projected workload
    for the resource across all active projects and proposals. Helps identify
    over-allocation and available capacity. Essential for resource planning and
    optimization decisions.

    Args:
        tenant_path (str):
        resource_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ResourceLoadDetailSchema
    """

    return (
        await asyncio_detailed(
            tenant_path=tenant_path,
            resource_id=resource_id,
            client=client,
        )
    ).parsed
