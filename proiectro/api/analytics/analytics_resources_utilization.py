from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.analytics_resources_utilization import AnalyticsResourcesUtilization
from ...models.analytics_resources_utilization_compare import (
    AnalyticsResourcesUtilizationCompare,
)
from ...models.analytics_resources_utilization_period import (
    AnalyticsResourcesUtilizationPeriod,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    tenant_path: str,
    *,
    period: AnalyticsResourcesUtilizationPeriod
    | Unset = AnalyticsResourcesUtilizationPeriod.YTD,
    compare: AnalyticsResourcesUtilizationCompare
    | Unset = AnalyticsResourcesUtilizationCompare.NONE,
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
        "url": "/api/v1/{tenant_path}/analytics/resources/utilization".format(
            tenant_path=quote(str(tenant_path), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AnalyticsResourcesUtilization | None:
    if response.status_code == 200:
        response_200 = AnalyticsResourcesUtilization.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[AnalyticsResourcesUtilization]:
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
    period: AnalyticsResourcesUtilizationPeriod
    | Unset = AnalyticsResourcesUtilizationPeriod.YTD,
    compare: AnalyticsResourcesUtilizationCompare
    | Unset = AnalyticsResourcesUtilizationCompare.NONE,
) -> Response[AnalyticsResourcesUtilization]:
    """Analytics Resources Utilization

     Equipment utilization over the selected period: booked hours against available hours, broken
    down per resource and per category, with an optional comparison against the previous period.

    Params:
        compare: Comparison mode (none, yoy, pop, mom)

    Args:
        tenant_path (str):
        period (AnalyticsResourcesUtilizationPeriod | Unset):  Default:
            AnalyticsResourcesUtilizationPeriod.YTD.
        compare (AnalyticsResourcesUtilizationCompare | Unset):  Default:
            AnalyticsResourcesUtilizationCompare.NONE.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AnalyticsResourcesUtilization]
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
    period: AnalyticsResourcesUtilizationPeriod
    | Unset = AnalyticsResourcesUtilizationPeriod.YTD,
    compare: AnalyticsResourcesUtilizationCompare
    | Unset = AnalyticsResourcesUtilizationCompare.NONE,
) -> AnalyticsResourcesUtilization | None:
    """Analytics Resources Utilization

     Equipment utilization over the selected period: booked hours against available hours, broken
    down per resource and per category, with an optional comparison against the previous period.

    Params:
        compare: Comparison mode (none, yoy, pop, mom)

    Args:
        tenant_path (str):
        period (AnalyticsResourcesUtilizationPeriod | Unset):  Default:
            AnalyticsResourcesUtilizationPeriod.YTD.
        compare (AnalyticsResourcesUtilizationCompare | Unset):  Default:
            AnalyticsResourcesUtilizationCompare.NONE.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AnalyticsResourcesUtilization
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
    period: AnalyticsResourcesUtilizationPeriod
    | Unset = AnalyticsResourcesUtilizationPeriod.YTD,
    compare: AnalyticsResourcesUtilizationCompare
    | Unset = AnalyticsResourcesUtilizationCompare.NONE,
) -> Response[AnalyticsResourcesUtilization]:
    """Analytics Resources Utilization

     Equipment utilization over the selected period: booked hours against available hours, broken
    down per resource and per category, with an optional comparison against the previous period.

    Params:
        compare: Comparison mode (none, yoy, pop, mom)

    Args:
        tenant_path (str):
        period (AnalyticsResourcesUtilizationPeriod | Unset):  Default:
            AnalyticsResourcesUtilizationPeriod.YTD.
        compare (AnalyticsResourcesUtilizationCompare | Unset):  Default:
            AnalyticsResourcesUtilizationCompare.NONE.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AnalyticsResourcesUtilization]
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
    period: AnalyticsResourcesUtilizationPeriod
    | Unset = AnalyticsResourcesUtilizationPeriod.YTD,
    compare: AnalyticsResourcesUtilizationCompare
    | Unset = AnalyticsResourcesUtilizationCompare.NONE,
) -> AnalyticsResourcesUtilization | None:
    """Analytics Resources Utilization

     Equipment utilization over the selected period: booked hours against available hours, broken
    down per resource and per category, with an optional comparison against the previous period.

    Params:
        compare: Comparison mode (none, yoy, pop, mom)

    Args:
        tenant_path (str):
        period (AnalyticsResourcesUtilizationPeriod | Unset):  Default:
            AnalyticsResourcesUtilizationPeriod.YTD.
        compare (AnalyticsResourcesUtilizationCompare | Unset):  Default:
            AnalyticsResourcesUtilizationCompare.NONE.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AnalyticsResourcesUtilization
    """

    return (
        await asyncio_detailed(
            tenant_path=tenant_path,
            client=client,
            period=period,
            compare=compare,
        )
    ).parsed
