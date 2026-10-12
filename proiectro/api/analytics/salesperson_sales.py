from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.analytics_salesperson_sales import AnalyticsSalespersonSales
from ...models.api_response import APIResponse
from ...models.salesperson_sales_compare import SalespersonSalesCompare
from ...models.salesperson_sales_period import SalespersonSalesPeriod
from ...types import UNSET, Response, Unset


def _get_kwargs(
    tenant_path: str,
    member_id: str,
    *,
    period: SalespersonSalesPeriod | Unset = SalespersonSalesPeriod.YTD,
    compare: SalespersonSalesCompare | Unset = SalespersonSalesCompare.NONE,
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
        "url": "/api/v1/{tenant_path}/salesperson_sales/{member_id}".format(
            tenant_path=quote(str(tenant_path), safe=""),
            member_id=quote(str(member_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> APIResponse | AnalyticsSalespersonSales | None:
    if response.status_code == 200:
        response_200 = AnalyticsSalespersonSales.from_dict(response.json())

        return response_200

    if response.status_code == 404:
        response_404 = APIResponse.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[APIResponse | AnalyticsSalespersonSales]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    tenant_path: str,
    member_id: str,
    *,
    client: AuthenticatedClient,
    period: SalespersonSalesPeriod | Unset = SalespersonSalesPeriod.YTD,
    compare: SalespersonSalesCompare | Unset = SalespersonSalesCompare.NONE,
) -> Response[APIResponse | AnalyticsSalespersonSales]:
    """Salesperson Sales

     One salesperson's won deals for the period, reached from the sales dashboard.

    Same numbers as the dashboard row for that person, listed deal by deal.

    Args:
        tenant_path (str):
        member_id (str):
        period (SalespersonSalesPeriod | Unset):  Default: SalespersonSalesPeriod.YTD.
        compare (SalespersonSalesCompare | Unset):  Default: SalespersonSalesCompare.NONE.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[APIResponse | AnalyticsSalespersonSales]
    """

    kwargs = _get_kwargs(
        tenant_path=tenant_path,
        member_id=member_id,
        period=period,
        compare=compare,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    tenant_path: str,
    member_id: str,
    *,
    client: AuthenticatedClient,
    period: SalespersonSalesPeriod | Unset = SalespersonSalesPeriod.YTD,
    compare: SalespersonSalesCompare | Unset = SalespersonSalesCompare.NONE,
) -> APIResponse | AnalyticsSalespersonSales | None:
    """Salesperson Sales

     One salesperson's won deals for the period, reached from the sales dashboard.

    Same numbers as the dashboard row for that person, listed deal by deal.

    Args:
        tenant_path (str):
        member_id (str):
        period (SalespersonSalesPeriod | Unset):  Default: SalespersonSalesPeriod.YTD.
        compare (SalespersonSalesCompare | Unset):  Default: SalespersonSalesCompare.NONE.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        APIResponse | AnalyticsSalespersonSales
    """

    return sync_detailed(
        tenant_path=tenant_path,
        member_id=member_id,
        client=client,
        period=period,
        compare=compare,
    ).parsed


async def asyncio_detailed(
    tenant_path: str,
    member_id: str,
    *,
    client: AuthenticatedClient,
    period: SalespersonSalesPeriod | Unset = SalespersonSalesPeriod.YTD,
    compare: SalespersonSalesCompare | Unset = SalespersonSalesCompare.NONE,
) -> Response[APIResponse | AnalyticsSalespersonSales]:
    """Salesperson Sales

     One salesperson's won deals for the period, reached from the sales dashboard.

    Same numbers as the dashboard row for that person, listed deal by deal.

    Args:
        tenant_path (str):
        member_id (str):
        period (SalespersonSalesPeriod | Unset):  Default: SalespersonSalesPeriod.YTD.
        compare (SalespersonSalesCompare | Unset):  Default: SalespersonSalesCompare.NONE.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[APIResponse | AnalyticsSalespersonSales]
    """

    kwargs = _get_kwargs(
        tenant_path=tenant_path,
        member_id=member_id,
        period=period,
        compare=compare,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    tenant_path: str,
    member_id: str,
    *,
    client: AuthenticatedClient,
    period: SalespersonSalesPeriod | Unset = SalespersonSalesPeriod.YTD,
    compare: SalespersonSalesCompare | Unset = SalespersonSalesCompare.NONE,
) -> APIResponse | AnalyticsSalespersonSales | None:
    """Salesperson Sales

     One salesperson's won deals for the period, reached from the sales dashboard.

    Same numbers as the dashboard row for that person, listed deal by deal.

    Args:
        tenant_path (str):
        member_id (str):
        period (SalespersonSalesPeriod | Unset):  Default: SalespersonSalesPeriod.YTD.
        compare (SalespersonSalesCompare | Unset):  Default: SalespersonSalesCompare.NONE.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        APIResponse | AnalyticsSalespersonSales
    """

    return (
        await asyncio_detailed(
            tenant_path=tenant_path,
            member_id=member_id,
            client=client,
            period=period,
            compare=compare,
        )
    ).parsed
