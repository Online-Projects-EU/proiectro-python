from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.analytics_support_kpis_period import AnalyticsSupportKpisPeriod
from ...models.support_kp_is import SupportKPIs
from ...types import UNSET, Response, Unset


def _get_kwargs(
    tenant_path: str,
    *,
    period: AnalyticsSupportKpisPeriod | Unset = AnalyticsSupportKpisPeriod.YTD,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_period: str | Unset = UNSET
    if not isinstance(period, Unset):
        json_period = period.value

    params["period"] = json_period

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/{tenant_path}/analytics/support/kpis".format(
            tenant_path=quote(str(tenant_path), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> SupportKPIs | None:
    if response.status_code == 200:
        response_200 = SupportKPIs.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[SupportKPIs]:
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
    period: AnalyticsSupportKpisPeriod | Unset = AnalyticsSupportKpisPeriod.YTD,
) -> Response[SupportKPIs]:
    """Analytics Support Kpis

     Support KPIs for the Support dashboard. Provides ticket volume with severity
    breakdown, SLA compliance vs target, resolution efficiency status, and customer
    satisfaction scores. Each metric includes status badges for quick assessment.

    Args:
        tenant_path (str):
        period (AnalyticsSupportKpisPeriod | Unset):  Default: AnalyticsSupportKpisPeriod.YTD.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SupportKPIs]
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
    period: AnalyticsSupportKpisPeriod | Unset = AnalyticsSupportKpisPeriod.YTD,
) -> SupportKPIs | None:
    """Analytics Support Kpis

     Support KPIs for the Support dashboard. Provides ticket volume with severity
    breakdown, SLA compliance vs target, resolution efficiency status, and customer
    satisfaction scores. Each metric includes status badges for quick assessment.

    Args:
        tenant_path (str):
        period (AnalyticsSupportKpisPeriod | Unset):  Default: AnalyticsSupportKpisPeriod.YTD.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SupportKPIs
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
    period: AnalyticsSupportKpisPeriod | Unset = AnalyticsSupportKpisPeriod.YTD,
) -> Response[SupportKPIs]:
    """Analytics Support Kpis

     Support KPIs for the Support dashboard. Provides ticket volume with severity
    breakdown, SLA compliance vs target, resolution efficiency status, and customer
    satisfaction scores. Each metric includes status badges for quick assessment.

    Args:
        tenant_path (str):
        period (AnalyticsSupportKpisPeriod | Unset):  Default: AnalyticsSupportKpisPeriod.YTD.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SupportKPIs]
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
    period: AnalyticsSupportKpisPeriod | Unset = AnalyticsSupportKpisPeriod.YTD,
) -> SupportKPIs | None:
    """Analytics Support Kpis

     Support KPIs for the Support dashboard. Provides ticket volume with severity
    breakdown, SLA compliance vs target, resolution efficiency status, and customer
    satisfaction scores. Each metric includes status badges for quick assessment.

    Args:
        tenant_path (str):
        period (AnalyticsSupportKpisPeriod | Unset):  Default: AnalyticsSupportKpisPeriod.YTD.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SupportKPIs
    """

    return (
        await asyncio_detailed(
            tenant_path=tenant_path,
            client=client,
            period=period,
        )
    ).parsed
