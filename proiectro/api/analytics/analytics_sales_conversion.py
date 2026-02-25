from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.analytics_sales_conversion import AnalyticsSalesConversion
from ...models.analytics_sales_conversion_compare import AnalyticsSalesConversionCompare
from ...models.analytics_sales_conversion_period import AnalyticsSalesConversionPeriod
from ...types import UNSET, Response, Unset


def _get_kwargs(
    tenant_path: str,
    *,
    period: AnalyticsSalesConversionPeriod | Unset = AnalyticsSalesConversionPeriod.YTD,
    compare: AnalyticsSalesConversionCompare
    | Unset = AnalyticsSalesConversionCompare.NONE,
    funnel_id: str | Unset = UNSET,
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

    params["funnel_id"] = funnel_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/{tenant_path}/analytics/sales/conversion".format(
            tenant_path=quote(str(tenant_path), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AnalyticsSalesConversion | None:
    if response.status_code == 200:
        response_200 = AnalyticsSalesConversion.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[AnalyticsSalesConversion]:
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
    period: AnalyticsSalesConversionPeriod | Unset = AnalyticsSalesConversionPeriod.YTD,
    compare: AnalyticsSalesConversionCompare
    | Unset = AnalyticsSalesConversionCompare.NONE,
    funnel_id: str | Unset = UNSET,
) -> Response[AnalyticsSalesConversion]:
    """Analytics Sales Conversion

     Sales conversion funnel analysis. Tracks conversion rates between stages,
    drop-off points, and win/loss reasons. Identifies process improvements
    to increase overall conversion effectiveness.

    Params:
        compare: Comparison mode (none, yoy, pop, mom)
        funnel_id: Optional funnel external_id. If None, uses first active funnel.

    Args:
        tenant_path (str):
        period (AnalyticsSalesConversionPeriod | Unset):  Default:
            AnalyticsSalesConversionPeriod.YTD.
        compare (AnalyticsSalesConversionCompare | Unset):  Default:
            AnalyticsSalesConversionCompare.NONE.
        funnel_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AnalyticsSalesConversion]
    """

    kwargs = _get_kwargs(
        tenant_path=tenant_path,
        period=period,
        compare=compare,
        funnel_id=funnel_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    tenant_path: str,
    *,
    client: AuthenticatedClient,
    period: AnalyticsSalesConversionPeriod | Unset = AnalyticsSalesConversionPeriod.YTD,
    compare: AnalyticsSalesConversionCompare
    | Unset = AnalyticsSalesConversionCompare.NONE,
    funnel_id: str | Unset = UNSET,
) -> AnalyticsSalesConversion | None:
    """Analytics Sales Conversion

     Sales conversion funnel analysis. Tracks conversion rates between stages,
    drop-off points, and win/loss reasons. Identifies process improvements
    to increase overall conversion effectiveness.

    Params:
        compare: Comparison mode (none, yoy, pop, mom)
        funnel_id: Optional funnel external_id. If None, uses first active funnel.

    Args:
        tenant_path (str):
        period (AnalyticsSalesConversionPeriod | Unset):  Default:
            AnalyticsSalesConversionPeriod.YTD.
        compare (AnalyticsSalesConversionCompare | Unset):  Default:
            AnalyticsSalesConversionCompare.NONE.
        funnel_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AnalyticsSalesConversion
    """

    return sync_detailed(
        tenant_path=tenant_path,
        client=client,
        period=period,
        compare=compare,
        funnel_id=funnel_id,
    ).parsed


async def asyncio_detailed(
    tenant_path: str,
    *,
    client: AuthenticatedClient,
    period: AnalyticsSalesConversionPeriod | Unset = AnalyticsSalesConversionPeriod.YTD,
    compare: AnalyticsSalesConversionCompare
    | Unset = AnalyticsSalesConversionCompare.NONE,
    funnel_id: str | Unset = UNSET,
) -> Response[AnalyticsSalesConversion]:
    """Analytics Sales Conversion

     Sales conversion funnel analysis. Tracks conversion rates between stages,
    drop-off points, and win/loss reasons. Identifies process improvements
    to increase overall conversion effectiveness.

    Params:
        compare: Comparison mode (none, yoy, pop, mom)
        funnel_id: Optional funnel external_id. If None, uses first active funnel.

    Args:
        tenant_path (str):
        period (AnalyticsSalesConversionPeriod | Unset):  Default:
            AnalyticsSalesConversionPeriod.YTD.
        compare (AnalyticsSalesConversionCompare | Unset):  Default:
            AnalyticsSalesConversionCompare.NONE.
        funnel_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AnalyticsSalesConversion]
    """

    kwargs = _get_kwargs(
        tenant_path=tenant_path,
        period=period,
        compare=compare,
        funnel_id=funnel_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    tenant_path: str,
    *,
    client: AuthenticatedClient,
    period: AnalyticsSalesConversionPeriod | Unset = AnalyticsSalesConversionPeriod.YTD,
    compare: AnalyticsSalesConversionCompare
    | Unset = AnalyticsSalesConversionCompare.NONE,
    funnel_id: str | Unset = UNSET,
) -> AnalyticsSalesConversion | None:
    """Analytics Sales Conversion

     Sales conversion funnel analysis. Tracks conversion rates between stages,
    drop-off points, and win/loss reasons. Identifies process improvements
    to increase overall conversion effectiveness.

    Params:
        compare: Comparison mode (none, yoy, pop, mom)
        funnel_id: Optional funnel external_id. If None, uses first active funnel.

    Args:
        tenant_path (str):
        period (AnalyticsSalesConversionPeriod | Unset):  Default:
            AnalyticsSalesConversionPeriod.YTD.
        compare (AnalyticsSalesConversionCompare | Unset):  Default:
            AnalyticsSalesConversionCompare.NONE.
        funnel_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AnalyticsSalesConversion
    """

    return (
        await asyncio_detailed(
            tenant_path=tenant_path,
            client=client,
            period=period,
            compare=compare,
            funnel_id=funnel_id,
        )
    ).parsed
