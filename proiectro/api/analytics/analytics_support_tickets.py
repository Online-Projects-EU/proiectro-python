from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.analytics_support_tickets import AnalyticsSupportTickets
from ...models.analytics_support_tickets_period import AnalyticsSupportTicketsPeriod
from ...types import UNSET, Response, Unset


def _get_kwargs(
    tenant_path: str,
    *,
    period: AnalyticsSupportTicketsPeriod | Unset = AnalyticsSupportTicketsPeriod.YTD,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_period: str | Unset = UNSET
    if not isinstance(period, Unset):
        json_period = period.value

    params["period"] = json_period

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/{tenant_path}/analytics/support/tickets".format(
            tenant_path=quote(str(tenant_path), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AnalyticsSupportTickets | None:
    if response.status_code == 200:
        response_200 = AnalyticsSupportTickets.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[AnalyticsSupportTickets]:
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
    period: AnalyticsSupportTicketsPeriod | Unset = AnalyticsSupportTicketsPeriod.YTD,
) -> Response[AnalyticsSupportTickets]:
    """Analytics Support Tickets

     Support ticket volume and distribution analysis. Shows ticket counts by
    type, severity, queue, and status. Identifies trends and staffing needs
    for support operations.

    Args:
        tenant_path (str):
        period (AnalyticsSupportTicketsPeriod | Unset):  Default:
            AnalyticsSupportTicketsPeriod.YTD.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AnalyticsSupportTickets]
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
    period: AnalyticsSupportTicketsPeriod | Unset = AnalyticsSupportTicketsPeriod.YTD,
) -> AnalyticsSupportTickets | None:
    """Analytics Support Tickets

     Support ticket volume and distribution analysis. Shows ticket counts by
    type, severity, queue, and status. Identifies trends and staffing needs
    for support operations.

    Args:
        tenant_path (str):
        period (AnalyticsSupportTicketsPeriod | Unset):  Default:
            AnalyticsSupportTicketsPeriod.YTD.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AnalyticsSupportTickets
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
    period: AnalyticsSupportTicketsPeriod | Unset = AnalyticsSupportTicketsPeriod.YTD,
) -> Response[AnalyticsSupportTickets]:
    """Analytics Support Tickets

     Support ticket volume and distribution analysis. Shows ticket counts by
    type, severity, queue, and status. Identifies trends and staffing needs
    for support operations.

    Args:
        tenant_path (str):
        period (AnalyticsSupportTicketsPeriod | Unset):  Default:
            AnalyticsSupportTicketsPeriod.YTD.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AnalyticsSupportTickets]
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
    period: AnalyticsSupportTicketsPeriod | Unset = AnalyticsSupportTicketsPeriod.YTD,
) -> AnalyticsSupportTickets | None:
    """Analytics Support Tickets

     Support ticket volume and distribution analysis. Shows ticket counts by
    type, severity, queue, and status. Identifies trends and staffing needs
    for support operations.

    Args:
        tenant_path (str):
        period (AnalyticsSupportTicketsPeriod | Unset):  Default:
            AnalyticsSupportTicketsPeriod.YTD.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AnalyticsSupportTickets
    """

    return (
        await asyncio_detailed(
            tenant_path=tenant_path,
            client=client,
            period=period,
        )
    ).parsed
