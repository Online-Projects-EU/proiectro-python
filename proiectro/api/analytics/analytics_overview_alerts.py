from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.analytics_alerts import AnalyticsAlerts
from ...models.analytics_overview_alerts_period import AnalyticsOverviewAlertsPeriod
from ...types import UNSET, Response, Unset


def _get_kwargs(
    tenant_path: str,
    *,
    period: AnalyticsOverviewAlertsPeriod | Unset = AnalyticsOverviewAlertsPeriod.YTD,
    filter_severity: None | str | Unset = UNSET,
    filter_category: None | str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_period: str | Unset = UNSET
    if not isinstance(period, Unset):
        json_period = period.value

    params["period"] = json_period

    json_filter_severity: None | str | Unset
    if isinstance(filter_severity, Unset):
        json_filter_severity = UNSET
    else:
        json_filter_severity = filter_severity
    params["filter_severity"] = json_filter_severity

    json_filter_category: None | str | Unset
    if isinstance(filter_category, Unset):
        json_filter_category = UNSET
    else:
        json_filter_category = filter_category
    params["filter_category"] = json_filter_category

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/{tenant_path}/analytics/overview/alerts".format(
            tenant_path=quote(str(tenant_path), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AnalyticsAlerts | None:
    if response.status_code == 200:
        response_200 = AnalyticsAlerts.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[AnalyticsAlerts]:
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
    period: AnalyticsOverviewAlertsPeriod | Unset = AnalyticsOverviewAlertsPeriod.YTD,
    filter_severity: None | str | Unset = UNSET,
    filter_category: None | str | Unset = UNSET,
) -> Response[AnalyticsAlerts]:
    """Analytics Overview Alerts

     Business health alerts requiring attention. Identifies critical issues across
    all domains: overdue payments, at-risk projects, SLA breaches, resource
    overallocation, and other actionable items for executive review.

    Filters:
        filter_severity: critical, warning, info (comma-separated for multiple)
        filter_category: financial, delivery, resources, sales, support

    Args:
        tenant_path (str):
        period (AnalyticsOverviewAlertsPeriod | Unset):  Default:
            AnalyticsOverviewAlertsPeriod.YTD.
        filter_severity (None | str | Unset):
        filter_category (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AnalyticsAlerts]
    """

    kwargs = _get_kwargs(
        tenant_path=tenant_path,
        period=period,
        filter_severity=filter_severity,
        filter_category=filter_category,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    tenant_path: str,
    *,
    client: AuthenticatedClient,
    period: AnalyticsOverviewAlertsPeriod | Unset = AnalyticsOverviewAlertsPeriod.YTD,
    filter_severity: None | str | Unset = UNSET,
    filter_category: None | str | Unset = UNSET,
) -> AnalyticsAlerts | None:
    """Analytics Overview Alerts

     Business health alerts requiring attention. Identifies critical issues across
    all domains: overdue payments, at-risk projects, SLA breaches, resource
    overallocation, and other actionable items for executive review.

    Filters:
        filter_severity: critical, warning, info (comma-separated for multiple)
        filter_category: financial, delivery, resources, sales, support

    Args:
        tenant_path (str):
        period (AnalyticsOverviewAlertsPeriod | Unset):  Default:
            AnalyticsOverviewAlertsPeriod.YTD.
        filter_severity (None | str | Unset):
        filter_category (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AnalyticsAlerts
    """

    return sync_detailed(
        tenant_path=tenant_path,
        client=client,
        period=period,
        filter_severity=filter_severity,
        filter_category=filter_category,
    ).parsed


async def asyncio_detailed(
    tenant_path: str,
    *,
    client: AuthenticatedClient,
    period: AnalyticsOverviewAlertsPeriod | Unset = AnalyticsOverviewAlertsPeriod.YTD,
    filter_severity: None | str | Unset = UNSET,
    filter_category: None | str | Unset = UNSET,
) -> Response[AnalyticsAlerts]:
    """Analytics Overview Alerts

     Business health alerts requiring attention. Identifies critical issues across
    all domains: overdue payments, at-risk projects, SLA breaches, resource
    overallocation, and other actionable items for executive review.

    Filters:
        filter_severity: critical, warning, info (comma-separated for multiple)
        filter_category: financial, delivery, resources, sales, support

    Args:
        tenant_path (str):
        period (AnalyticsOverviewAlertsPeriod | Unset):  Default:
            AnalyticsOverviewAlertsPeriod.YTD.
        filter_severity (None | str | Unset):
        filter_category (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AnalyticsAlerts]
    """

    kwargs = _get_kwargs(
        tenant_path=tenant_path,
        period=period,
        filter_severity=filter_severity,
        filter_category=filter_category,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    tenant_path: str,
    *,
    client: AuthenticatedClient,
    period: AnalyticsOverviewAlertsPeriod | Unset = AnalyticsOverviewAlertsPeriod.YTD,
    filter_severity: None | str | Unset = UNSET,
    filter_category: None | str | Unset = UNSET,
) -> AnalyticsAlerts | None:
    """Analytics Overview Alerts

     Business health alerts requiring attention. Identifies critical issues across
    all domains: overdue payments, at-risk projects, SLA breaches, resource
    overallocation, and other actionable items for executive review.

    Filters:
        filter_severity: critical, warning, info (comma-separated for multiple)
        filter_category: financial, delivery, resources, sales, support

    Args:
        tenant_path (str):
        period (AnalyticsOverviewAlertsPeriod | Unset):  Default:
            AnalyticsOverviewAlertsPeriod.YTD.
        filter_severity (None | str | Unset):
        filter_category (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AnalyticsAlerts
    """

    return (
        await asyncio_detailed(
            tenant_path=tenant_path,
            client=client,
            period=period,
            filter_severity=filter_severity,
            filter_category=filter_category,
        )
    ).parsed
