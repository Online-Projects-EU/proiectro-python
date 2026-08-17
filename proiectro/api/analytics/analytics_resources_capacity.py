from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.analytics_resources_capacity import AnalyticsResourcesCapacity
from ...models.analytics_resources_capacity_horizon import (
    AnalyticsResourcesCapacityHorizon,
)
from ...models.analytics_resources_capacity_period import (
    AnalyticsResourcesCapacityPeriod,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    tenant_path: str,
    *,
    period: AnalyticsResourcesCapacityPeriod
    | Unset = AnalyticsResourcesCapacityPeriod.YTD,
    horizon: AnalyticsResourcesCapacityHorizon
    | Unset = AnalyticsResourcesCapacityHorizon.VALUE_1,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_period: str | Unset = UNSET
    if not isinstance(period, Unset):
        json_period = period.value

    params["period"] = json_period

    json_horizon: str | Unset = UNSET
    if not isinstance(horizon, Unset):
        json_horizon = horizon.value

    params["horizon"] = json_horizon

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/{tenant_path}/analytics/resources/capacity".format(
            tenant_path=quote(str(tenant_path), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AnalyticsResourcesCapacity | None:
    if response.status_code == 200:
        response_200 = AnalyticsResourcesCapacity.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[AnalyticsResourcesCapacity]:
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
    period: AnalyticsResourcesCapacityPeriod
    | Unset = AnalyticsResourcesCapacityPeriod.YTD,
    horizon: AnalyticsResourcesCapacityHorizon
    | Unset = AnalyticsResourcesCapacityHorizon.VALUE_1,
) -> Response[AnalyticsResourcesCapacity]:
    """Analytics Resources Capacity

     Capacity planning. The hours still free this month per resource, plus a month-by-month
    projection of booked demand against available capacity across the horizon.

    Params:
        horizon: Projection horizon (3m, 6m, 12m, 24m)

    Args:
        tenant_path (str):
        period (AnalyticsResourcesCapacityPeriod | Unset):  Default:
            AnalyticsResourcesCapacityPeriod.YTD.
        horizon (AnalyticsResourcesCapacityHorizon | Unset):  Default:
            AnalyticsResourcesCapacityHorizon.VALUE_1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AnalyticsResourcesCapacity]
    """

    kwargs = _get_kwargs(
        tenant_path=tenant_path,
        period=period,
        horizon=horizon,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    tenant_path: str,
    *,
    client: AuthenticatedClient,
    period: AnalyticsResourcesCapacityPeriod
    | Unset = AnalyticsResourcesCapacityPeriod.YTD,
    horizon: AnalyticsResourcesCapacityHorizon
    | Unset = AnalyticsResourcesCapacityHorizon.VALUE_1,
) -> AnalyticsResourcesCapacity | None:
    """Analytics Resources Capacity

     Capacity planning. The hours still free this month per resource, plus a month-by-month
    projection of booked demand against available capacity across the horizon.

    Params:
        horizon: Projection horizon (3m, 6m, 12m, 24m)

    Args:
        tenant_path (str):
        period (AnalyticsResourcesCapacityPeriod | Unset):  Default:
            AnalyticsResourcesCapacityPeriod.YTD.
        horizon (AnalyticsResourcesCapacityHorizon | Unset):  Default:
            AnalyticsResourcesCapacityHorizon.VALUE_1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AnalyticsResourcesCapacity
    """

    return sync_detailed(
        tenant_path=tenant_path,
        client=client,
        period=period,
        horizon=horizon,
    ).parsed


async def asyncio_detailed(
    tenant_path: str,
    *,
    client: AuthenticatedClient,
    period: AnalyticsResourcesCapacityPeriod
    | Unset = AnalyticsResourcesCapacityPeriod.YTD,
    horizon: AnalyticsResourcesCapacityHorizon
    | Unset = AnalyticsResourcesCapacityHorizon.VALUE_1,
) -> Response[AnalyticsResourcesCapacity]:
    """Analytics Resources Capacity

     Capacity planning. The hours still free this month per resource, plus a month-by-month
    projection of booked demand against available capacity across the horizon.

    Params:
        horizon: Projection horizon (3m, 6m, 12m, 24m)

    Args:
        tenant_path (str):
        period (AnalyticsResourcesCapacityPeriod | Unset):  Default:
            AnalyticsResourcesCapacityPeriod.YTD.
        horizon (AnalyticsResourcesCapacityHorizon | Unset):  Default:
            AnalyticsResourcesCapacityHorizon.VALUE_1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AnalyticsResourcesCapacity]
    """

    kwargs = _get_kwargs(
        tenant_path=tenant_path,
        period=period,
        horizon=horizon,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    tenant_path: str,
    *,
    client: AuthenticatedClient,
    period: AnalyticsResourcesCapacityPeriod
    | Unset = AnalyticsResourcesCapacityPeriod.YTD,
    horizon: AnalyticsResourcesCapacityHorizon
    | Unset = AnalyticsResourcesCapacityHorizon.VALUE_1,
) -> AnalyticsResourcesCapacity | None:
    """Analytics Resources Capacity

     Capacity planning. The hours still free this month per resource, plus a month-by-month
    projection of booked demand against available capacity across the horizon.

    Params:
        horizon: Projection horizon (3m, 6m, 12m, 24m)

    Args:
        tenant_path (str):
        period (AnalyticsResourcesCapacityPeriod | Unset):  Default:
            AnalyticsResourcesCapacityPeriod.YTD.
        horizon (AnalyticsResourcesCapacityHorizon | Unset):  Default:
            AnalyticsResourcesCapacityHorizon.VALUE_1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AnalyticsResourcesCapacity
    """

    return (
        await asyncio_detailed(
            tenant_path=tenant_path,
            client=client,
            period=period,
            horizon=horizon,
        )
    ).parsed
