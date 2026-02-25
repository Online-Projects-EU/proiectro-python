from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.analytics_sales_kpis_period import AnalyticsSalesKpisPeriod
from ...models.sales_kp_is import SalesKPIs
from ...types import UNSET, Response, Unset


def _get_kwargs(
    tenant_path: str,
    *,
    period: AnalyticsSalesKpisPeriod | Unset = AnalyticsSalesKpisPeriod.YTD,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_period: str | Unset = UNSET
    if not isinstance(period, Unset):
        json_period = period.value

    params["period"] = json_period

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/{tenant_path}/analytics/sales/kpis".format(
            tenant_path=quote(str(tenant_path), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> SalesKPIs | None:
    if response.status_code == 200:
        response_200 = SalesKPIs.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[SalesKPIs]:
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
    period: AnalyticsSalesKpisPeriod | Unset = AnalyticsSalesKpisPeriod.YTD,
) -> Response[SalesKPIs]:
    """Analytics Sales Kpis

     Sales KPIs for the Sales dashboard. Provides pipeline health and deal flow status
    with stage breakdown, win rate vs benchmark, deal size distribution, and active
    deal health. Status indicators show whether metrics are healthy or need attention.

    Args:
        tenant_path (str):
        period (AnalyticsSalesKpisPeriod | Unset):  Default: AnalyticsSalesKpisPeriod.YTD.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SalesKPIs]
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
    period: AnalyticsSalesKpisPeriod | Unset = AnalyticsSalesKpisPeriod.YTD,
) -> SalesKPIs | None:
    """Analytics Sales Kpis

     Sales KPIs for the Sales dashboard. Provides pipeline health and deal flow status
    with stage breakdown, win rate vs benchmark, deal size distribution, and active
    deal health. Status indicators show whether metrics are healthy or need attention.

    Args:
        tenant_path (str):
        period (AnalyticsSalesKpisPeriod | Unset):  Default: AnalyticsSalesKpisPeriod.YTD.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SalesKPIs
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
    period: AnalyticsSalesKpisPeriod | Unset = AnalyticsSalesKpisPeriod.YTD,
) -> Response[SalesKPIs]:
    """Analytics Sales Kpis

     Sales KPIs for the Sales dashboard. Provides pipeline health and deal flow status
    with stage breakdown, win rate vs benchmark, deal size distribution, and active
    deal health. Status indicators show whether metrics are healthy or need attention.

    Args:
        tenant_path (str):
        period (AnalyticsSalesKpisPeriod | Unset):  Default: AnalyticsSalesKpisPeriod.YTD.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SalesKPIs]
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
    period: AnalyticsSalesKpisPeriod | Unset = AnalyticsSalesKpisPeriod.YTD,
) -> SalesKPIs | None:
    """Analytics Sales Kpis

     Sales KPIs for the Sales dashboard. Provides pipeline health and deal flow status
    with stage breakdown, win rate vs benchmark, deal size distribution, and active
    deal health. Status indicators show whether metrics are healthy or need attention.

    Args:
        tenant_path (str):
        period (AnalyticsSalesKpisPeriod | Unset):  Default: AnalyticsSalesKpisPeriod.YTD.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SalesKPIs
    """

    return (
        await asyncio_detailed(
            tenant_path=tenant_path,
            client=client,
            period=period,
        )
    ).parsed
