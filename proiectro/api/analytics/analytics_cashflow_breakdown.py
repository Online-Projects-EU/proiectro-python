from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.analytics_cashflow_breakdown import AnalyticsCashflowBreakdown
from ...models.analytics_cashflow_breakdown_period import (
    AnalyticsCashflowBreakdownPeriod,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    tenant_path: str,
    *,
    period: AnalyticsCashflowBreakdownPeriod
    | Unset = AnalyticsCashflowBreakdownPeriod.YTD,
    filter_type: None | str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_period: str | Unset = UNSET
    if not isinstance(period, Unset):
        json_period = period.value

    params["period"] = json_period

    json_filter_type: None | str | Unset
    if isinstance(filter_type, Unset):
        json_filter_type = UNSET
    else:
        json_filter_type = filter_type
    params["filter_type"] = json_filter_type

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/{tenant_path}/analytics/cashflow/breakdown".format(
            tenant_path=quote(str(tenant_path), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AnalyticsCashflowBreakdown | None:
    if response.status_code == 200:
        response_200 = AnalyticsCashflowBreakdown.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[AnalyticsCashflowBreakdown]:
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
    period: AnalyticsCashflowBreakdownPeriod
    | Unset = AnalyticsCashflowBreakdownPeriod.YTD,
    filter_type: None | str | Unset = UNSET,
) -> Response[AnalyticsCashflowBreakdown]:
    """Analytics Cashflow Breakdown

     Cash flow breakdown by source. Shows income and payments separated by domain:
    proposals, projects, support contracts, and other sources. Helps identify
    which business areas contribute most to cash flow health.

    Filters:
        filter_type: 'income' or 'payments' to show only one side

    Args:
        tenant_path (str):
        period (AnalyticsCashflowBreakdownPeriod | Unset):  Default:
            AnalyticsCashflowBreakdownPeriod.YTD.
        filter_type (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AnalyticsCashflowBreakdown]
    """

    kwargs = _get_kwargs(
        tenant_path=tenant_path,
        period=period,
        filter_type=filter_type,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    tenant_path: str,
    *,
    client: AuthenticatedClient,
    period: AnalyticsCashflowBreakdownPeriod
    | Unset = AnalyticsCashflowBreakdownPeriod.YTD,
    filter_type: None | str | Unset = UNSET,
) -> AnalyticsCashflowBreakdown | None:
    """Analytics Cashflow Breakdown

     Cash flow breakdown by source. Shows income and payments separated by domain:
    proposals, projects, support contracts, and other sources. Helps identify
    which business areas contribute most to cash flow health.

    Filters:
        filter_type: 'income' or 'payments' to show only one side

    Args:
        tenant_path (str):
        period (AnalyticsCashflowBreakdownPeriod | Unset):  Default:
            AnalyticsCashflowBreakdownPeriod.YTD.
        filter_type (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AnalyticsCashflowBreakdown
    """

    return sync_detailed(
        tenant_path=tenant_path,
        client=client,
        period=period,
        filter_type=filter_type,
    ).parsed


async def asyncio_detailed(
    tenant_path: str,
    *,
    client: AuthenticatedClient,
    period: AnalyticsCashflowBreakdownPeriod
    | Unset = AnalyticsCashflowBreakdownPeriod.YTD,
    filter_type: None | str | Unset = UNSET,
) -> Response[AnalyticsCashflowBreakdown]:
    """Analytics Cashflow Breakdown

     Cash flow breakdown by source. Shows income and payments separated by domain:
    proposals, projects, support contracts, and other sources. Helps identify
    which business areas contribute most to cash flow health.

    Filters:
        filter_type: 'income' or 'payments' to show only one side

    Args:
        tenant_path (str):
        period (AnalyticsCashflowBreakdownPeriod | Unset):  Default:
            AnalyticsCashflowBreakdownPeriod.YTD.
        filter_type (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AnalyticsCashflowBreakdown]
    """

    kwargs = _get_kwargs(
        tenant_path=tenant_path,
        period=period,
        filter_type=filter_type,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    tenant_path: str,
    *,
    client: AuthenticatedClient,
    period: AnalyticsCashflowBreakdownPeriod
    | Unset = AnalyticsCashflowBreakdownPeriod.YTD,
    filter_type: None | str | Unset = UNSET,
) -> AnalyticsCashflowBreakdown | None:
    """Analytics Cashflow Breakdown

     Cash flow breakdown by source. Shows income and payments separated by domain:
    proposals, projects, support contracts, and other sources. Helps identify
    which business areas contribute most to cash flow health.

    Filters:
        filter_type: 'income' or 'payments' to show only one side

    Args:
        tenant_path (str):
        period (AnalyticsCashflowBreakdownPeriod | Unset):  Default:
            AnalyticsCashflowBreakdownPeriod.YTD.
        filter_type (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AnalyticsCashflowBreakdown
    """

    return (
        await asyncio_detailed(
            tenant_path=tenant_path,
            client=client,
            period=period,
            filter_type=filter_type,
        )
    ).parsed
