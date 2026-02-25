from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.analytics_financial_kpis_period import AnalyticsFinancialKpisPeriod
from ...models.financial_kp_is import FinancialKPIs
from ...types import UNSET, Response, Unset


def _get_kwargs(
    tenant_path: str,
    *,
    period: AnalyticsFinancialKpisPeriod | Unset = AnalyticsFinancialKpisPeriod.YTD,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_period: str | Unset = UNSET
    if not isinstance(period, Unset):
        json_period = period.value

    params["period"] = json_period

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/{tenant_path}/analytics/financial/kpis".format(
            tenant_path=quote(str(tenant_path), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> FinancialKPIs | None:
    if response.status_code == 200:
        response_200 = FinancialKPIs.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[FinancialKPIs]:
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
    period: AnalyticsFinancialKpisPeriod | Unset = AnalyticsFinancialKpisPeriod.YTD,
) -> Response[FinancialKPIs]:
    """Analytics Financial Kpis

     Financial KPIs for the Financial dashboard. Provides revenue vs target, margin
    health, AR aging summary, and DSO status. Each metric includes contextual
    status indicators to show financial health at a glance.

    Args:
        tenant_path (str):
        period (AnalyticsFinancialKpisPeriod | Unset):  Default: AnalyticsFinancialKpisPeriod.YTD.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FinancialKPIs]
    """

    kwargs = _get_kwargs(
        tenant_path=tenant_path,
        period=period,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    tenant_path: str,
    *,
    client: AuthenticatedClient,
    period: AnalyticsFinancialKpisPeriod | Unset = AnalyticsFinancialKpisPeriod.YTD,
) -> FinancialKPIs | None:
    """Analytics Financial Kpis

     Financial KPIs for the Financial dashboard. Provides revenue vs target, margin
    health, AR aging summary, and DSO status. Each metric includes contextual
    status indicators to show financial health at a glance.

    Args:
        tenant_path (str):
        period (AnalyticsFinancialKpisPeriod | Unset):  Default: AnalyticsFinancialKpisPeriod.YTD.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FinancialKPIs
    """

    return sync_detailed(
        tenant_path=tenant_path,
        client=client,
        period=period,
    ).parsed


async def asyncio_detailed(
    tenant_path: str,
    *,
    client: AuthenticatedClient,
    period: AnalyticsFinancialKpisPeriod | Unset = AnalyticsFinancialKpisPeriod.YTD,
) -> Response[FinancialKPIs]:
    """Analytics Financial Kpis

     Financial KPIs for the Financial dashboard. Provides revenue vs target, margin
    health, AR aging summary, and DSO status. Each metric includes contextual
    status indicators to show financial health at a glance.

    Args:
        tenant_path (str):
        period (AnalyticsFinancialKpisPeriod | Unset):  Default: AnalyticsFinancialKpisPeriod.YTD.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FinancialKPIs]
    """

    kwargs = _get_kwargs(
        tenant_path=tenant_path,
        period=period,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    tenant_path: str,
    *,
    client: AuthenticatedClient,
    period: AnalyticsFinancialKpisPeriod | Unset = AnalyticsFinancialKpisPeriod.YTD,
) -> FinancialKPIs | None:
    """Analytics Financial Kpis

     Financial KPIs for the Financial dashboard. Provides revenue vs target, margin
    health, AR aging summary, and DSO status. Each metric includes contextual
    status indicators to show financial health at a glance.

    Args:
        tenant_path (str):
        period (AnalyticsFinancialKpisPeriod | Unset):  Default: AnalyticsFinancialKpisPeriod.YTD.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FinancialKPIs
    """

    return (
        await asyncio_detailed(
            tenant_path=tenant_path,
            client=client,
            period=period,
        )
    ).parsed
