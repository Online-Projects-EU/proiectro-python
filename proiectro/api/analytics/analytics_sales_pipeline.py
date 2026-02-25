from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.analytics_sales_pipeline import AnalyticsSalesPipeline
from ...models.analytics_sales_pipeline_period import AnalyticsSalesPipelinePeriod
from ...types import UNSET, Response, Unset


def _get_kwargs(
    tenant_path: str,
    *,
    period: AnalyticsSalesPipelinePeriod | Unset = AnalyticsSalesPipelinePeriod.YTD,
    funnel_id: None | str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_period: str | Unset = UNSET
    if not isinstance(period, Unset):
        json_period = period.value

    params["period"] = json_period

    json_funnel_id: None | str | Unset
    if isinstance(funnel_id, Unset):
        json_funnel_id = UNSET
    else:
        json_funnel_id = funnel_id
    params["funnel_id"] = json_funnel_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/{tenant_path}/analytics/sales/pipeline".format(
            tenant_path=quote(str(tenant_path), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AnalyticsSalesPipeline | None:
    if response.status_code == 200:
        response_200 = AnalyticsSalesPipeline.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[AnalyticsSalesPipeline]:
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
    period: AnalyticsSalesPipelinePeriod | Unset = AnalyticsSalesPipelinePeriod.YTD,
    funnel_id: None | str | Unset = UNSET,
) -> Response[AnalyticsSalesPipeline]:
    """Analytics Sales Pipeline

     Sales pipeline analysis with value distribution across stages. Shows deal
    counts, weighted pipeline value, and stage velocity metrics. Identifies
    bottlenecks and opportunities for pipeline optimization.

    This is a SNAPSHOT view showing current pipeline state regardless of period.
    The period parameter is included for UI consistency but doesn't filter data.

    Params:
        funnel_id: Optional funnel external_id. If not provided, returns data
                   for the first active funnel.

    Args:
        tenant_path (str):
        period (AnalyticsSalesPipelinePeriod | Unset):  Default: AnalyticsSalesPipelinePeriod.YTD.
        funnel_id (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AnalyticsSalesPipeline]
    """

    kwargs = _get_kwargs(
        tenant_path=tenant_path,
        period=period,
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
    period: AnalyticsSalesPipelinePeriod | Unset = AnalyticsSalesPipelinePeriod.YTD,
    funnel_id: None | str | Unset = UNSET,
) -> AnalyticsSalesPipeline | None:
    """Analytics Sales Pipeline

     Sales pipeline analysis with value distribution across stages. Shows deal
    counts, weighted pipeline value, and stage velocity metrics. Identifies
    bottlenecks and opportunities for pipeline optimization.

    This is a SNAPSHOT view showing current pipeline state regardless of period.
    The period parameter is included for UI consistency but doesn't filter data.

    Params:
        funnel_id: Optional funnel external_id. If not provided, returns data
                   for the first active funnel.

    Args:
        tenant_path (str):
        period (AnalyticsSalesPipelinePeriod | Unset):  Default: AnalyticsSalesPipelinePeriod.YTD.
        funnel_id (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AnalyticsSalesPipeline
    """

    return sync_detailed(
        tenant_path=tenant_path,
        client=client,
        period=period,
        funnel_id=funnel_id,
    ).parsed


async def asyncio_detailed(
    tenant_path: str,
    *,
    client: AuthenticatedClient,
    period: AnalyticsSalesPipelinePeriod | Unset = AnalyticsSalesPipelinePeriod.YTD,
    funnel_id: None | str | Unset = UNSET,
) -> Response[AnalyticsSalesPipeline]:
    """Analytics Sales Pipeline

     Sales pipeline analysis with value distribution across stages. Shows deal
    counts, weighted pipeline value, and stage velocity metrics. Identifies
    bottlenecks and opportunities for pipeline optimization.

    This is a SNAPSHOT view showing current pipeline state regardless of period.
    The period parameter is included for UI consistency but doesn't filter data.

    Params:
        funnel_id: Optional funnel external_id. If not provided, returns data
                   for the first active funnel.

    Args:
        tenant_path (str):
        period (AnalyticsSalesPipelinePeriod | Unset):  Default: AnalyticsSalesPipelinePeriod.YTD.
        funnel_id (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AnalyticsSalesPipeline]
    """

    kwargs = _get_kwargs(
        tenant_path=tenant_path,
        period=period,
        funnel_id=funnel_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    tenant_path: str,
    *,
    client: AuthenticatedClient,
    period: AnalyticsSalesPipelinePeriod | Unset = AnalyticsSalesPipelinePeriod.YTD,
    funnel_id: None | str | Unset = UNSET,
) -> AnalyticsSalesPipeline | None:
    """Analytics Sales Pipeline

     Sales pipeline analysis with value distribution across stages. Shows deal
    counts, weighted pipeline value, and stage velocity metrics. Identifies
    bottlenecks and opportunities for pipeline optimization.

    This is a SNAPSHOT view showing current pipeline state regardless of period.
    The period parameter is included for UI consistency but doesn't filter data.

    Params:
        funnel_id: Optional funnel external_id. If not provided, returns data
                   for the first active funnel.

    Args:
        tenant_path (str):
        period (AnalyticsSalesPipelinePeriod | Unset):  Default: AnalyticsSalesPipelinePeriod.YTD.
        funnel_id (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AnalyticsSalesPipeline
    """

    return (
        await asyncio_detailed(
            tenant_path=tenant_path,
            client=client,
            period=period,
            funnel_id=funnel_id,
        )
    ).parsed
