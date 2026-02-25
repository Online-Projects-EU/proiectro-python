from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.analytics_support_trends import AnalyticsSupportTrends
from ...models.analytics_support_trends_compare import AnalyticsSupportTrendsCompare
from ...models.analytics_support_trends_period import AnalyticsSupportTrendsPeriod
from ...types import UNSET, Response, Unset


def _get_kwargs(
    tenant_path: str,
    *,
    period: AnalyticsSupportTrendsPeriod | Unset = AnalyticsSupportTrendsPeriod.YTD,
    compare: AnalyticsSupportTrendsCompare | Unset = AnalyticsSupportTrendsCompare.NONE,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_period: str | Unset = UNSET
    if not isinstance(period, Unset):
        json_period = period.value

    params["period"] = json_period

    json_compare: str | Unset = UNSET
    if not isinstance(compare, Unset):
        json_compare = compare.value

    params["compare"] = json_compare

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/{tenant_path}/analytics/support/trends".format(
            tenant_path=quote(str(tenant_path), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AnalyticsSupportTrends | None:
    if response.status_code == 200:
        response_200 = AnalyticsSupportTrends.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[AnalyticsSupportTrends]:
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
    period: AnalyticsSupportTrendsPeriod | Unset = AnalyticsSupportTrendsPeriod.YTD,
    compare: AnalyticsSupportTrendsCompare | Unset = AnalyticsSupportTrendsCompare.NONE,
) -> Response[AnalyticsSupportTrends]:
    """Analytics Support Trends

     Support trend analysis over time. Shows ticket volume trends, resolution
    time improvements, and seasonal patterns. Helps predict support demand
    and plan staffing accordingly.

    Params:
        compare: Comparison mode (none, yoy, pop, mom)

    Args:
        tenant_path (str):
        period (AnalyticsSupportTrendsPeriod | Unset):  Default: AnalyticsSupportTrendsPeriod.YTD.
        compare (AnalyticsSupportTrendsCompare | Unset):  Default:
            AnalyticsSupportTrendsCompare.NONE.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AnalyticsSupportTrends]
    """

    kwargs = _get_kwargs(
        tenant_path=tenant_path,
        period=period,
        compare=compare,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    tenant_path: str,
    *,
    client: AuthenticatedClient,
    period: AnalyticsSupportTrendsPeriod | Unset = AnalyticsSupportTrendsPeriod.YTD,
    compare: AnalyticsSupportTrendsCompare | Unset = AnalyticsSupportTrendsCompare.NONE,
) -> AnalyticsSupportTrends | None:
    """Analytics Support Trends

     Support trend analysis over time. Shows ticket volume trends, resolution
    time improvements, and seasonal patterns. Helps predict support demand
    and plan staffing accordingly.

    Params:
        compare: Comparison mode (none, yoy, pop, mom)

    Args:
        tenant_path (str):
        period (AnalyticsSupportTrendsPeriod | Unset):  Default: AnalyticsSupportTrendsPeriod.YTD.
        compare (AnalyticsSupportTrendsCompare | Unset):  Default:
            AnalyticsSupportTrendsCompare.NONE.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AnalyticsSupportTrends
    """

    return sync_detailed(
        tenant_path=tenant_path,
        client=client,
        period=period,
        compare=compare,
    ).parsed


async def asyncio_detailed(
    tenant_path: str,
    *,
    client: AuthenticatedClient,
    period: AnalyticsSupportTrendsPeriod | Unset = AnalyticsSupportTrendsPeriod.YTD,
    compare: AnalyticsSupportTrendsCompare | Unset = AnalyticsSupportTrendsCompare.NONE,
) -> Response[AnalyticsSupportTrends]:
    """Analytics Support Trends

     Support trend analysis over time. Shows ticket volume trends, resolution
    time improvements, and seasonal patterns. Helps predict support demand
    and plan staffing accordingly.

    Params:
        compare: Comparison mode (none, yoy, pop, mom)

    Args:
        tenant_path (str):
        period (AnalyticsSupportTrendsPeriod | Unset):  Default: AnalyticsSupportTrendsPeriod.YTD.
        compare (AnalyticsSupportTrendsCompare | Unset):  Default:
            AnalyticsSupportTrendsCompare.NONE.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AnalyticsSupportTrends]
    """

    kwargs = _get_kwargs(
        tenant_path=tenant_path,
        period=period,
        compare=compare,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    tenant_path: str,
    *,
    client: AuthenticatedClient,
    period: AnalyticsSupportTrendsPeriod | Unset = AnalyticsSupportTrendsPeriod.YTD,
    compare: AnalyticsSupportTrendsCompare | Unset = AnalyticsSupportTrendsCompare.NONE,
) -> AnalyticsSupportTrends | None:
    """Analytics Support Trends

     Support trend analysis over time. Shows ticket volume trends, resolution
    time improvements, and seasonal patterns. Helps predict support demand
    and plan staffing accordingly.

    Params:
        compare: Comparison mode (none, yoy, pop, mom)

    Args:
        tenant_path (str):
        period (AnalyticsSupportTrendsPeriod | Unset):  Default: AnalyticsSupportTrendsPeriod.YTD.
        compare (AnalyticsSupportTrendsCompare | Unset):  Default:
            AnalyticsSupportTrendsCompare.NONE.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AnalyticsSupportTrends
    """

    return (
        await asyncio_detailed(
            tenant_path=tenant_path,
            client=client,
            period=period,
            compare=compare,
        )
    ).parsed
