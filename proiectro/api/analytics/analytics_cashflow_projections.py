from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.analytics_cashflow_projections import AnalyticsCashflowProjections
from ...models.analytics_cashflow_projections_horizon import (
    AnalyticsCashflowProjectionsHorizon,
)
from ...models.analytics_cashflow_projections_period import (
    AnalyticsCashflowProjectionsPeriod,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    tenant_path: str,
    *,
    period: AnalyticsCashflowProjectionsPeriod
    | Unset = AnalyticsCashflowProjectionsPeriod.YTD,
    horizon: AnalyticsCashflowProjectionsHorizon
    | Unset = AnalyticsCashflowProjectionsHorizon.VALUE_2,
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
        "url": "/api/v1/{tenant_path}/analytics/cashflow/projections".format(
            tenant_path=quote(str(tenant_path), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AnalyticsCashflowProjections | None:
    if response.status_code == 200:
        response_200 = AnalyticsCashflowProjections.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[AnalyticsCashflowProjections]:
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
    period: AnalyticsCashflowProjectionsPeriod
    | Unset = AnalyticsCashflowProjectionsPeriod.YTD,
    horizon: AnalyticsCashflowProjectionsHorizon
    | Unset = AnalyticsCashflowProjectionsHorizon.VALUE_2,
) -> Response[AnalyticsCashflowProjections]:
    """Analytics Cashflow Projections

     Cash flow projections by fiscal period. Forecasts future cash position based
    on scheduled payments, probability-weighted pipeline, and historical collection
    patterns. Organized by Q1-Q4 fiscal quarters with monthly granularity.

    Params:
        horizon: Projection horizon (3m, 6m, 12m, 24m)

    Args:
        tenant_path (str):
        period (AnalyticsCashflowProjectionsPeriod | Unset):  Default:
            AnalyticsCashflowProjectionsPeriod.YTD.
        horizon (AnalyticsCashflowProjectionsHorizon | Unset):  Default:
            AnalyticsCashflowProjectionsHorizon.VALUE_2.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AnalyticsCashflowProjections]
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
    period: AnalyticsCashflowProjectionsPeriod
    | Unset = AnalyticsCashflowProjectionsPeriod.YTD,
    horizon: AnalyticsCashflowProjectionsHorizon
    | Unset = AnalyticsCashflowProjectionsHorizon.VALUE_2,
) -> AnalyticsCashflowProjections | None:
    """Analytics Cashflow Projections

     Cash flow projections by fiscal period. Forecasts future cash position based
    on scheduled payments, probability-weighted pipeline, and historical collection
    patterns. Organized by Q1-Q4 fiscal quarters with monthly granularity.

    Params:
        horizon: Projection horizon (3m, 6m, 12m, 24m)

    Args:
        tenant_path (str):
        period (AnalyticsCashflowProjectionsPeriod | Unset):  Default:
            AnalyticsCashflowProjectionsPeriod.YTD.
        horizon (AnalyticsCashflowProjectionsHorizon | Unset):  Default:
            AnalyticsCashflowProjectionsHorizon.VALUE_2.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AnalyticsCashflowProjections
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
    period: AnalyticsCashflowProjectionsPeriod
    | Unset = AnalyticsCashflowProjectionsPeriod.YTD,
    horizon: AnalyticsCashflowProjectionsHorizon
    | Unset = AnalyticsCashflowProjectionsHorizon.VALUE_2,
) -> Response[AnalyticsCashflowProjections]:
    """Analytics Cashflow Projections

     Cash flow projections by fiscal period. Forecasts future cash position based
    on scheduled payments, probability-weighted pipeline, and historical collection
    patterns. Organized by Q1-Q4 fiscal quarters with monthly granularity.

    Params:
        horizon: Projection horizon (3m, 6m, 12m, 24m)

    Args:
        tenant_path (str):
        period (AnalyticsCashflowProjectionsPeriod | Unset):  Default:
            AnalyticsCashflowProjectionsPeriod.YTD.
        horizon (AnalyticsCashflowProjectionsHorizon | Unset):  Default:
            AnalyticsCashflowProjectionsHorizon.VALUE_2.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AnalyticsCashflowProjections]
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
    period: AnalyticsCashflowProjectionsPeriod
    | Unset = AnalyticsCashflowProjectionsPeriod.YTD,
    horizon: AnalyticsCashflowProjectionsHorizon
    | Unset = AnalyticsCashflowProjectionsHorizon.VALUE_2,
) -> AnalyticsCashflowProjections | None:
    """Analytics Cashflow Projections

     Cash flow projections by fiscal period. Forecasts future cash position based
    on scheduled payments, probability-weighted pipeline, and historical collection
    patterns. Organized by Q1-Q4 fiscal quarters with monthly granularity.

    Params:
        horizon: Projection horizon (3m, 6m, 12m, 24m)

    Args:
        tenant_path (str):
        period (AnalyticsCashflowProjectionsPeriod | Unset):  Default:
            AnalyticsCashflowProjectionsPeriod.YTD.
        horizon (AnalyticsCashflowProjectionsHorizon | Unset):  Default:
            AnalyticsCashflowProjectionsHorizon.VALUE_2.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AnalyticsCashflowProjections
    """

    return (
        await asyncio_detailed(
            tenant_path=tenant_path,
            client=client,
            period=period,
            horizon=horizon,
        )
    ).parsed
