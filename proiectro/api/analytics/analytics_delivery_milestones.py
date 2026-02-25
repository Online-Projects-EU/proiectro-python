from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.analytics_delivery_milestones import AnalyticsDeliveryMilestones
from ...models.analytics_delivery_milestones_period import (
    AnalyticsDeliveryMilestonesPeriod,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    tenant_path: str,
    *,
    period: AnalyticsDeliveryMilestonesPeriod
    | Unset = AnalyticsDeliveryMilestonesPeriod.YTD,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_period: str | Unset = UNSET
    if not isinstance(period, Unset):
        json_period = period.value

    params["period"] = json_period

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/{tenant_path}/analytics/delivery/milestones".format(
            tenant_path=quote(str(tenant_path), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AnalyticsDeliveryMilestones | None:
    if response.status_code == 200:
        response_200 = AnalyticsDeliveryMilestones.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[AnalyticsDeliveryMilestones]:
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
    period: AnalyticsDeliveryMilestonesPeriod
    | Unset = AnalyticsDeliveryMilestonesPeriod.YTD,
) -> Response[AnalyticsDeliveryMilestones]:
    """Analytics Delivery Milestones

     Milestone tracking and delivery metrics. Shows on-time delivery rates,
    upcoming milestones, and milestone slip trends. Critical for customer
    communication and project planning.

    Args:
        tenant_path (str):
        period (AnalyticsDeliveryMilestonesPeriod | Unset):  Default:
            AnalyticsDeliveryMilestonesPeriod.YTD.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AnalyticsDeliveryMilestones]
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
    period: AnalyticsDeliveryMilestonesPeriod
    | Unset = AnalyticsDeliveryMilestonesPeriod.YTD,
) -> AnalyticsDeliveryMilestones | None:
    """Analytics Delivery Milestones

     Milestone tracking and delivery metrics. Shows on-time delivery rates,
    upcoming milestones, and milestone slip trends. Critical for customer
    communication and project planning.

    Args:
        tenant_path (str):
        period (AnalyticsDeliveryMilestonesPeriod | Unset):  Default:
            AnalyticsDeliveryMilestonesPeriod.YTD.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AnalyticsDeliveryMilestones
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
    period: AnalyticsDeliveryMilestonesPeriod
    | Unset = AnalyticsDeliveryMilestonesPeriod.YTD,
) -> Response[AnalyticsDeliveryMilestones]:
    """Analytics Delivery Milestones

     Milestone tracking and delivery metrics. Shows on-time delivery rates,
    upcoming milestones, and milestone slip trends. Critical for customer
    communication and project planning.

    Args:
        tenant_path (str):
        period (AnalyticsDeliveryMilestonesPeriod | Unset):  Default:
            AnalyticsDeliveryMilestonesPeriod.YTD.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AnalyticsDeliveryMilestones]
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
    period: AnalyticsDeliveryMilestonesPeriod
    | Unset = AnalyticsDeliveryMilestonesPeriod.YTD,
) -> AnalyticsDeliveryMilestones | None:
    """Analytics Delivery Milestones

     Milestone tracking and delivery metrics. Shows on-time delivery rates,
    upcoming milestones, and milestone slip trends. Critical for customer
    communication and project planning.

    Args:
        tenant_path (str):
        period (AnalyticsDeliveryMilestonesPeriod | Unset):  Default:
            AnalyticsDeliveryMilestonesPeriod.YTD.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AnalyticsDeliveryMilestones
    """

    return (
        await asyncio_detailed(
            tenant_path=tenant_path,
            client=client,
            period=period,
        )
    ).parsed
