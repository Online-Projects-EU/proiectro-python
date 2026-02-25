from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.analytics_sales_forecast import AnalyticsSalesForecast
from ...models.analytics_sales_forecast_horizon import AnalyticsSalesForecastHorizon
from ...models.analytics_sales_forecast_period import AnalyticsSalesForecastPeriod
from ...types import UNSET, Response, Unset


def _get_kwargs(
    tenant_path: str,
    *,
    period: AnalyticsSalesForecastPeriod | Unset = AnalyticsSalesForecastPeriod.YTD,
    horizon: AnalyticsSalesForecastHorizon
    | Unset = AnalyticsSalesForecastHorizon.VALUE_0,
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
        "url": "/api/v1/{tenant_path}/analytics/sales/forecast".format(
            tenant_path=quote(str(tenant_path), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AnalyticsSalesForecast | None:
    if response.status_code == 200:
        response_200 = AnalyticsSalesForecast.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[AnalyticsSalesForecast]:
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
    period: AnalyticsSalesForecastPeriod | Unset = AnalyticsSalesForecastPeriod.YTD,
    horizon: AnalyticsSalesForecastHorizon
    | Unset = AnalyticsSalesForecastHorizon.VALUE_0,
) -> Response[AnalyticsSalesForecast]:
    """Analytics Sales Forecast

     Sales forecasting based on current pipeline. Projects future revenue by
    weighting pipeline deals by stage probability and grouping by expected
    close date. Aggregates ALL deals across ALL funnels.

    Note: Comparisons (YoY, PoP) are not applicable to forecasts since
    forecasts are projections, not historical data.

    Params:
        period: Period selection (affects bucket granularity)
        horizon: Projection horizon (3m, 6m, 12m, 24m) - default 3m

    Args:
        tenant_path (str):
        period (AnalyticsSalesForecastPeriod | Unset):  Default: AnalyticsSalesForecastPeriod.YTD.
        horizon (AnalyticsSalesForecastHorizon | Unset):  Default:
            AnalyticsSalesForecastHorizon.VALUE_0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AnalyticsSalesForecast]
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
    period: AnalyticsSalesForecastPeriod | Unset = AnalyticsSalesForecastPeriod.YTD,
    horizon: AnalyticsSalesForecastHorizon
    | Unset = AnalyticsSalesForecastHorizon.VALUE_0,
) -> AnalyticsSalesForecast | None:
    """Analytics Sales Forecast

     Sales forecasting based on current pipeline. Projects future revenue by
    weighting pipeline deals by stage probability and grouping by expected
    close date. Aggregates ALL deals across ALL funnels.

    Note: Comparisons (YoY, PoP) are not applicable to forecasts since
    forecasts are projections, not historical data.

    Params:
        period: Period selection (affects bucket granularity)
        horizon: Projection horizon (3m, 6m, 12m, 24m) - default 3m

    Args:
        tenant_path (str):
        period (AnalyticsSalesForecastPeriod | Unset):  Default: AnalyticsSalesForecastPeriod.YTD.
        horizon (AnalyticsSalesForecastHorizon | Unset):  Default:
            AnalyticsSalesForecastHorizon.VALUE_0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AnalyticsSalesForecast
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
    period: AnalyticsSalesForecastPeriod | Unset = AnalyticsSalesForecastPeriod.YTD,
    horizon: AnalyticsSalesForecastHorizon
    | Unset = AnalyticsSalesForecastHorizon.VALUE_0,
) -> Response[AnalyticsSalesForecast]:
    """Analytics Sales Forecast

     Sales forecasting based on current pipeline. Projects future revenue by
    weighting pipeline deals by stage probability and grouping by expected
    close date. Aggregates ALL deals across ALL funnels.

    Note: Comparisons (YoY, PoP) are not applicable to forecasts since
    forecasts are projections, not historical data.

    Params:
        period: Period selection (affects bucket granularity)
        horizon: Projection horizon (3m, 6m, 12m, 24m) - default 3m

    Args:
        tenant_path (str):
        period (AnalyticsSalesForecastPeriod | Unset):  Default: AnalyticsSalesForecastPeriod.YTD.
        horizon (AnalyticsSalesForecastHorizon | Unset):  Default:
            AnalyticsSalesForecastHorizon.VALUE_0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AnalyticsSalesForecast]
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
    period: AnalyticsSalesForecastPeriod | Unset = AnalyticsSalesForecastPeriod.YTD,
    horizon: AnalyticsSalesForecastHorizon
    | Unset = AnalyticsSalesForecastHorizon.VALUE_0,
) -> AnalyticsSalesForecast | None:
    """Analytics Sales Forecast

     Sales forecasting based on current pipeline. Projects future revenue by
    weighting pipeline deals by stage probability and grouping by expected
    close date. Aggregates ALL deals across ALL funnels.

    Note: Comparisons (YoY, PoP) are not applicable to forecasts since
    forecasts are projections, not historical data.

    Params:
        period: Period selection (affects bucket granularity)
        horizon: Projection horizon (3m, 6m, 12m, 24m) - default 3m

    Args:
        tenant_path (str):
        period (AnalyticsSalesForecastPeriod | Unset):  Default: AnalyticsSalesForecastPeriod.YTD.
        horizon (AnalyticsSalesForecastHorizon | Unset):  Default:
            AnalyticsSalesForecastHorizon.VALUE_0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AnalyticsSalesForecast
    """

    return (
        await asyncio_detailed(
            tenant_path=tenant_path,
            client=client,
            period=period,
            horizon=horizon,
        )
    ).parsed
