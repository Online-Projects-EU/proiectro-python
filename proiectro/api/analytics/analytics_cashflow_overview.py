from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.analytics_cashflow_overview import AnalyticsCashflowOverview
from ...models.analytics_cashflow_overview_period import AnalyticsCashflowOverviewPeriod
from ...types import UNSET, Response, Unset


def _get_kwargs(
    tenant_path: str,
    *,
    period: AnalyticsCashflowOverviewPeriod
    | Unset = AnalyticsCashflowOverviewPeriod.YTD,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_period: str | Unset = UNSET
    if not isinstance(period, Unset):
        json_period = period.value

    params["period"] = json_period

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/{tenant_path}/analytics/cashflow/overview".format(
            tenant_path=quote(str(tenant_path), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AnalyticsCashflowOverview | None:
    if response.status_code == 200:
        response_200 = AnalyticsCashflowOverview.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[AnalyticsCashflowOverview]:
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
    period: AnalyticsCashflowOverviewPeriod
    | Unset = AnalyticsCashflowOverviewPeriod.YTD,
) -> Response[AnalyticsCashflowOverview]:
    """Analytics Cashflow Overview

     General Cash Flow overview combining ALL income vs ALL payments across the
    entire business. Shows scheduled vs realized amounts, net position, and
    cash health indicators. The unified view of financial flow unique to this platform.

    Args:
        tenant_path (str):
        period (AnalyticsCashflowOverviewPeriod | Unset):  Default:
            AnalyticsCashflowOverviewPeriod.YTD.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AnalyticsCashflowOverview]
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
    period: AnalyticsCashflowOverviewPeriod
    | Unset = AnalyticsCashflowOverviewPeriod.YTD,
) -> AnalyticsCashflowOverview | None:
    """Analytics Cashflow Overview

     General Cash Flow overview combining ALL income vs ALL payments across the
    entire business. Shows scheduled vs realized amounts, net position, and
    cash health indicators. The unified view of financial flow unique to this platform.

    Args:
        tenant_path (str):
        period (AnalyticsCashflowOverviewPeriod | Unset):  Default:
            AnalyticsCashflowOverviewPeriod.YTD.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AnalyticsCashflowOverview
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
    period: AnalyticsCashflowOverviewPeriod
    | Unset = AnalyticsCashflowOverviewPeriod.YTD,
) -> Response[AnalyticsCashflowOverview]:
    """Analytics Cashflow Overview

     General Cash Flow overview combining ALL income vs ALL payments across the
    entire business. Shows scheduled vs realized amounts, net position, and
    cash health indicators. The unified view of financial flow unique to this platform.

    Args:
        tenant_path (str):
        period (AnalyticsCashflowOverviewPeriod | Unset):  Default:
            AnalyticsCashflowOverviewPeriod.YTD.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AnalyticsCashflowOverview]
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
    period: AnalyticsCashflowOverviewPeriod
    | Unset = AnalyticsCashflowOverviewPeriod.YTD,
) -> AnalyticsCashflowOverview | None:
    """Analytics Cashflow Overview

     General Cash Flow overview combining ALL income vs ALL payments across the
    entire business. Shows scheduled vs realized amounts, net position, and
    cash health indicators. The unified view of financial flow unique to this platform.

    Args:
        tenant_path (str):
        period (AnalyticsCashflowOverviewPeriod | Unset):  Default:
            AnalyticsCashflowOverviewPeriod.YTD.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AnalyticsCashflowOverview
    """

    return (
        await asyncio_detailed(
            tenant_path=tenant_path,
            client=client,
            period=period,
        )
    ).parsed
