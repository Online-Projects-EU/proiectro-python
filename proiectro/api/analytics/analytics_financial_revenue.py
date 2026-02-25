from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.analytics_financial_revenue import AnalyticsFinancialRevenue
from ...models.analytics_financial_revenue_compare import (
    AnalyticsFinancialRevenueCompare,
)
from ...models.analytics_financial_revenue_period import AnalyticsFinancialRevenuePeriod
from ...types import UNSET, Response, Unset


def _get_kwargs(
    tenant_path: str,
    *,
    period: AnalyticsFinancialRevenuePeriod
    | Unset = AnalyticsFinancialRevenuePeriod.YTD,
    compare: AnalyticsFinancialRevenueCompare
    | Unset = AnalyticsFinancialRevenueCompare.NONE,
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
        "url": "/api/v1/{tenant_path}/analytics/financial/revenue".format(
            tenant_path=quote(str(tenant_path), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AnalyticsFinancialRevenue | None:
    if response.status_code == 200:
        response_200 = AnalyticsFinancialRevenue.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[AnalyticsFinancialRevenue]:
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
    period: AnalyticsFinancialRevenuePeriod
    | Unset = AnalyticsFinancialRevenuePeriod.YTD,
    compare: AnalyticsFinancialRevenueCompare
    | Unset = AnalyticsFinancialRevenueCompare.NONE,
) -> Response[AnalyticsFinancialRevenue]:
    """Analytics Financial Revenue

     Revenue analysis with recognition timing and trends. Shows recurring vs
    one-time revenue, revenue by product/service line, and growth metrics.
    Supports fiscal period breakdowns for accurate reporting.

    Params:
        compare: Comparison mode (none, yoy, pop, mom)

    Args:
        tenant_path (str):
        period (AnalyticsFinancialRevenuePeriod | Unset):  Default:
            AnalyticsFinancialRevenuePeriod.YTD.
        compare (AnalyticsFinancialRevenueCompare | Unset):  Default:
            AnalyticsFinancialRevenueCompare.NONE.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AnalyticsFinancialRevenue]
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
    period: AnalyticsFinancialRevenuePeriod
    | Unset = AnalyticsFinancialRevenuePeriod.YTD,
    compare: AnalyticsFinancialRevenueCompare
    | Unset = AnalyticsFinancialRevenueCompare.NONE,
) -> AnalyticsFinancialRevenue | None:
    """Analytics Financial Revenue

     Revenue analysis with recognition timing and trends. Shows recurring vs
    one-time revenue, revenue by product/service line, and growth metrics.
    Supports fiscal period breakdowns for accurate reporting.

    Params:
        compare: Comparison mode (none, yoy, pop, mom)

    Args:
        tenant_path (str):
        period (AnalyticsFinancialRevenuePeriod | Unset):  Default:
            AnalyticsFinancialRevenuePeriod.YTD.
        compare (AnalyticsFinancialRevenueCompare | Unset):  Default:
            AnalyticsFinancialRevenueCompare.NONE.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AnalyticsFinancialRevenue
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
    period: AnalyticsFinancialRevenuePeriod
    | Unset = AnalyticsFinancialRevenuePeriod.YTD,
    compare: AnalyticsFinancialRevenueCompare
    | Unset = AnalyticsFinancialRevenueCompare.NONE,
) -> Response[AnalyticsFinancialRevenue]:
    """Analytics Financial Revenue

     Revenue analysis with recognition timing and trends. Shows recurring vs
    one-time revenue, revenue by product/service line, and growth metrics.
    Supports fiscal period breakdowns for accurate reporting.

    Params:
        compare: Comparison mode (none, yoy, pop, mom)

    Args:
        tenant_path (str):
        period (AnalyticsFinancialRevenuePeriod | Unset):  Default:
            AnalyticsFinancialRevenuePeriod.YTD.
        compare (AnalyticsFinancialRevenueCompare | Unset):  Default:
            AnalyticsFinancialRevenueCompare.NONE.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AnalyticsFinancialRevenue]
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
    period: AnalyticsFinancialRevenuePeriod
    | Unset = AnalyticsFinancialRevenuePeriod.YTD,
    compare: AnalyticsFinancialRevenueCompare
    | Unset = AnalyticsFinancialRevenueCompare.NONE,
) -> AnalyticsFinancialRevenue | None:
    """Analytics Financial Revenue

     Revenue analysis with recognition timing and trends. Shows recurring vs
    one-time revenue, revenue by product/service line, and growth metrics.
    Supports fiscal period breakdowns for accurate reporting.

    Params:
        compare: Comparison mode (none, yoy, pop, mom)

    Args:
        tenant_path (str):
        period (AnalyticsFinancialRevenuePeriod | Unset):  Default:
            AnalyticsFinancialRevenuePeriod.YTD.
        compare (AnalyticsFinancialRevenueCompare | Unset):  Default:
            AnalyticsFinancialRevenueCompare.NONE.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AnalyticsFinancialRevenue
    """

    return (
        await asyncio_detailed(
            tenant_path=tenant_path,
            client=client,
            period=period,
            compare=compare,
        )
    ).parsed
