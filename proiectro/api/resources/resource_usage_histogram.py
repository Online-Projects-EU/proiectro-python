from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.resource_usage_histogram_schema import ResourceUsageHistogramSchema
from ...types import Response


def _get_kwargs(
    tenant_path: str,
    resource_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/{tenant_path}/resource_usage_histogram/{resource_id}".format(
            tenant_path=quote(str(tenant_path), safe=""),
            resource_id=quote(str(resource_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ResourceUsageHistogramSchema | None:
    if response.status_code == 200:
        response_200 = ResourceUsageHistogramSchema.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ResourceUsageHistogramSchema]:
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
) -> Response[ResourceUsageHistogramSchema]:
    """Resource Usage Histogram

     Get weekly planned resource usage for the next 12 weeks. Aggregates ResourceBooking
    data by week to show planned utilization trends. Used for capacity planning and
    resource allocation visualization. Shows zero for weeks without bookings to maintain
    consistent chart display. Essential for identifying future resource bottlenecks.

    Args:
        tenant_path (str):
        resource_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ResourceUsageHistogramSchema]
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
) -> ResourceUsageHistogramSchema | None:
    """Resource Usage Histogram

     Get weekly planned resource usage for the next 12 weeks. Aggregates ResourceBooking
    data by week to show planned utilization trends. Used for capacity planning and
    resource allocation visualization. Shows zero for weeks without bookings to maintain
    consistent chart display. Essential for identifying future resource bottlenecks.

    Args:
        tenant_path (str):
        resource_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ResourceUsageHistogramSchema
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
) -> Response[ResourceUsageHistogramSchema]:
    """Resource Usage Histogram

     Get weekly planned resource usage for the next 12 weeks. Aggregates ResourceBooking
    data by week to show planned utilization trends. Used for capacity planning and
    resource allocation visualization. Shows zero for weeks without bookings to maintain
    consistent chart display. Essential for identifying future resource bottlenecks.

    Args:
        tenant_path (str):
        resource_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ResourceUsageHistogramSchema]
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
) -> ResourceUsageHistogramSchema | None:
    """Resource Usage Histogram

     Get weekly planned resource usage for the next 12 weeks. Aggregates ResourceBooking
    data by week to show planned utilization trends. Used for capacity planning and
    resource allocation visualization. Shows zero for weeks without bookings to maintain
    consistent chart display. Essential for identifying future resource bottlenecks.

    Args:
        tenant_path (str):
        resource_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ResourceUsageHistogramSchema
    """

    return (
        await asyncio_detailed(
            tenant_path=tenant_path,
            resource_id=resource_id,
            client=client,
        )
    ).parsed
