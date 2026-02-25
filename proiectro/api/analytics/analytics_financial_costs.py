from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.analytics_financial_costs import AnalyticsFinancialCosts
from ...models.analytics_financial_costs_compare import AnalyticsFinancialCostsCompare
from ...models.analytics_financial_costs_period import AnalyticsFinancialCostsPeriod
from ...types import UNSET, Response, Unset


def _get_kwargs(
    tenant_path: str,
    *,
    period: AnalyticsFinancialCostsPeriod | Unset = AnalyticsFinancialCostsPeriod.YTD,
    compare: AnalyticsFinancialCostsCompare
    | Unset = AnalyticsFinancialCostsCompare.NONE,
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
        "url": "/api/v1/{tenant_path}/analytics/financial/costs".format(
            tenant_path=quote(str(tenant_path), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AnalyticsFinancialCosts | None:
    if response.status_code == 200:
        response_200 = AnalyticsFinancialCosts.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[AnalyticsFinancialCosts]:
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
    period: AnalyticsFinancialCostsPeriod | Unset = AnalyticsFinancialCostsPeriod.YTD,
    compare: AnalyticsFinancialCostsCompare
    | Unset = AnalyticsFinancialCostsCompare.NONE,
) -> Response[AnalyticsFinancialCosts]:
    """Analytics Financial Costs

     Cost analysis with category breakdowns. Shows direct costs, overhead
    allocation, and cost trends over time. Identifies cost optimization
    opportunities and margin improvement areas.

    Params:
        compare: Comparison mode (none, yoy, pop, mom)

    Args:
        tenant_path (str):
        period (AnalyticsFinancialCostsPeriod | Unset):  Default:
            AnalyticsFinancialCostsPeriod.YTD.
        compare (AnalyticsFinancialCostsCompare | Unset):  Default:
            AnalyticsFinancialCostsCompare.NONE.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AnalyticsFinancialCosts]
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
    period: AnalyticsFinancialCostsPeriod | Unset = AnalyticsFinancialCostsPeriod.YTD,
    compare: AnalyticsFinancialCostsCompare
    | Unset = AnalyticsFinancialCostsCompare.NONE,
) -> AnalyticsFinancialCosts | None:
    """Analytics Financial Costs

     Cost analysis with category breakdowns. Shows direct costs, overhead
    allocation, and cost trends over time. Identifies cost optimization
    opportunities and margin improvement areas.

    Params:
        compare: Comparison mode (none, yoy, pop, mom)

    Args:
        tenant_path (str):
        period (AnalyticsFinancialCostsPeriod | Unset):  Default:
            AnalyticsFinancialCostsPeriod.YTD.
        compare (AnalyticsFinancialCostsCompare | Unset):  Default:
            AnalyticsFinancialCostsCompare.NONE.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AnalyticsFinancialCosts
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
    period: AnalyticsFinancialCostsPeriod | Unset = AnalyticsFinancialCostsPeriod.YTD,
    compare: AnalyticsFinancialCostsCompare
    | Unset = AnalyticsFinancialCostsCompare.NONE,
) -> Response[AnalyticsFinancialCosts]:
    """Analytics Financial Costs

     Cost analysis with category breakdowns. Shows direct costs, overhead
    allocation, and cost trends over time. Identifies cost optimization
    opportunities and margin improvement areas.

    Params:
        compare: Comparison mode (none, yoy, pop, mom)

    Args:
        tenant_path (str):
        period (AnalyticsFinancialCostsPeriod | Unset):  Default:
            AnalyticsFinancialCostsPeriod.YTD.
        compare (AnalyticsFinancialCostsCompare | Unset):  Default:
            AnalyticsFinancialCostsCompare.NONE.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AnalyticsFinancialCosts]
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
    period: AnalyticsFinancialCostsPeriod | Unset = AnalyticsFinancialCostsPeriod.YTD,
    compare: AnalyticsFinancialCostsCompare
    | Unset = AnalyticsFinancialCostsCompare.NONE,
) -> AnalyticsFinancialCosts | None:
    """Analytics Financial Costs

     Cost analysis with category breakdowns. Shows direct costs, overhead
    allocation, and cost trends over time. Identifies cost optimization
    opportunities and margin improvement areas.

    Params:
        compare: Comparison mode (none, yoy, pop, mom)

    Args:
        tenant_path (str):
        period (AnalyticsFinancialCostsPeriod | Unset):  Default:
            AnalyticsFinancialCostsPeriod.YTD.
        compare (AnalyticsFinancialCostsCompare | Unset):  Default:
            AnalyticsFinancialCostsCompare.NONE.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AnalyticsFinancialCosts
    """

    return (
        await asyncio_detailed(
            tenant_path=tenant_path,
            client=client,
            period=period,
            compare=compare,
        )
    ).parsed
