from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.analytics_delivery_kpis_period import AnalyticsDeliveryKpisPeriod
from ...models.delivery_kp_is import DeliveryKPIs
from ...types import UNSET, Response, Unset


def _get_kwargs(
    tenant_path: str,
    *,
    period: AnalyticsDeliveryKpisPeriod | Unset = AnalyticsDeliveryKpisPeriod.YTD,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_period: str | Unset = UNSET
    if not isinstance(period, Unset):
        json_period = period.value

    params["period"] = json_period

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/{tenant_path}/analytics/delivery/kpis".format(
            tenant_path=quote(str(tenant_path), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> DeliveryKPIs | None:
    if response.status_code == 200:
        response_200 = DeliveryKPIs.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[DeliveryKPIs]:
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
    period: AnalyticsDeliveryKpisPeriod | Unset = AnalyticsDeliveryKpisPeriod.YTD,
) -> Response[DeliveryKPIs]:
    """Analytics Delivery Kpis

     Delivery KPIs for the Delivery dashboard. Provides project portfolio health
    distribution, on-time delivery status, health score breakdown by dimension,
    and milestone urgency indicators. Status badges show portfolio health.

    Args:
        tenant_path (str):
        period (AnalyticsDeliveryKpisPeriod | Unset):  Default: AnalyticsDeliveryKpisPeriod.YTD.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeliveryKPIs]
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
    period: AnalyticsDeliveryKpisPeriod | Unset = AnalyticsDeliveryKpisPeriod.YTD,
) -> DeliveryKPIs | None:
    """Analytics Delivery Kpis

     Delivery KPIs for the Delivery dashboard. Provides project portfolio health
    distribution, on-time delivery status, health score breakdown by dimension,
    and milestone urgency indicators. Status badges show portfolio health.

    Args:
        tenant_path (str):
        period (AnalyticsDeliveryKpisPeriod | Unset):  Default: AnalyticsDeliveryKpisPeriod.YTD.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeliveryKPIs
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
    period: AnalyticsDeliveryKpisPeriod | Unset = AnalyticsDeliveryKpisPeriod.YTD,
) -> Response[DeliveryKPIs]:
    """Analytics Delivery Kpis

     Delivery KPIs for the Delivery dashboard. Provides project portfolio health
    distribution, on-time delivery status, health score breakdown by dimension,
    and milestone urgency indicators. Status badges show portfolio health.

    Args:
        tenant_path (str):
        period (AnalyticsDeliveryKpisPeriod | Unset):  Default: AnalyticsDeliveryKpisPeriod.YTD.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeliveryKPIs]
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
    period: AnalyticsDeliveryKpisPeriod | Unset = AnalyticsDeliveryKpisPeriod.YTD,
) -> DeliveryKPIs | None:
    """Analytics Delivery Kpis

     Delivery KPIs for the Delivery dashboard. Provides project portfolio health
    distribution, on-time delivery status, health score breakdown by dimension,
    and milestone urgency indicators. Status badges show portfolio health.

    Args:
        tenant_path (str):
        period (AnalyticsDeliveryKpisPeriod | Unset):  Default: AnalyticsDeliveryKpisPeriod.YTD.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeliveryKPIs
    """

    return (
        await asyncio_detailed(
            tenant_path=tenant_path,
            client=client,
            period=period,
        )
    ).parsed
