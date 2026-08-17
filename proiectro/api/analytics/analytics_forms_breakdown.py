from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.analytics_forms_breakdown import AnalyticsFormsBreakdown
from ...models.analytics_forms_breakdown_compare import AnalyticsFormsBreakdownCompare
from ...models.analytics_forms_breakdown_period import AnalyticsFormsBreakdownPeriod
from ...types import UNSET, Response, Unset


def _get_kwargs(
    tenant_path: str,
    *,
    period: AnalyticsFormsBreakdownPeriod | Unset = AnalyticsFormsBreakdownPeriod.YTD,
    compare: AnalyticsFormsBreakdownCompare
    | Unset = AnalyticsFormsBreakdownCompare.NONE,
    form_id: None | str | Unset = UNSET,
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

    json_form_id: None | str | Unset
    if isinstance(form_id, Unset):
        json_form_id = UNSET
    else:
        json_form_id = form_id
    params["form_id"] = json_form_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/{tenant_path}/analytics/forms/breakdown".format(
            tenant_path=quote(str(tenant_path), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AnalyticsFormsBreakdown | None:
    if response.status_code == 200:
        response_200 = AnalyticsFormsBreakdown.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[AnalyticsFormsBreakdown]:
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
    period: AnalyticsFormsBreakdownPeriod | Unset = AnalyticsFormsBreakdownPeriod.YTD,
    compare: AnalyticsFormsBreakdownCompare
    | Unset = AnalyticsFormsBreakdownCompare.NONE,
    form_id: None | str | Unset = UNSET,
) -> Response[AnalyticsFormsBreakdown]:
    """Analytics Forms Breakdown

     Submission distributions for the selected period. Splits responses by review
    status (new, reviewed, archived) and by source (direct, asset, process stage,
    customer portal, partner portal, sales funnel), with per-slice change against
    a comparison window.

    Params:
        compare: Comparison mode (none, yoy, pop, mom)
        form_id: Optional form to scope the distributions to

    Args:
        tenant_path (str):
        period (AnalyticsFormsBreakdownPeriod | Unset):  Default:
            AnalyticsFormsBreakdownPeriod.YTD.
        compare (AnalyticsFormsBreakdownCompare | Unset):  Default:
            AnalyticsFormsBreakdownCompare.NONE.
        form_id (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AnalyticsFormsBreakdown]
    """

    kwargs = _get_kwargs(
        tenant_path=tenant_path,
        period=period,
        compare=compare,
        form_id=form_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    tenant_path: str,
    *,
    client: AuthenticatedClient,
    period: AnalyticsFormsBreakdownPeriod | Unset = AnalyticsFormsBreakdownPeriod.YTD,
    compare: AnalyticsFormsBreakdownCompare
    | Unset = AnalyticsFormsBreakdownCompare.NONE,
    form_id: None | str | Unset = UNSET,
) -> AnalyticsFormsBreakdown | None:
    """Analytics Forms Breakdown

     Submission distributions for the selected period. Splits responses by review
    status (new, reviewed, archived) and by source (direct, asset, process stage,
    customer portal, partner portal, sales funnel), with per-slice change against
    a comparison window.

    Params:
        compare: Comparison mode (none, yoy, pop, mom)
        form_id: Optional form to scope the distributions to

    Args:
        tenant_path (str):
        period (AnalyticsFormsBreakdownPeriod | Unset):  Default:
            AnalyticsFormsBreakdownPeriod.YTD.
        compare (AnalyticsFormsBreakdownCompare | Unset):  Default:
            AnalyticsFormsBreakdownCompare.NONE.
        form_id (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AnalyticsFormsBreakdown
    """

    return sync_detailed(
        tenant_path=tenant_path,
        client=client,
        period=period,
        compare=compare,
        form_id=form_id,
    ).parsed


async def asyncio_detailed(
    tenant_path: str,
    *,
    client: AuthenticatedClient,
    period: AnalyticsFormsBreakdownPeriod | Unset = AnalyticsFormsBreakdownPeriod.YTD,
    compare: AnalyticsFormsBreakdownCompare
    | Unset = AnalyticsFormsBreakdownCompare.NONE,
    form_id: None | str | Unset = UNSET,
) -> Response[AnalyticsFormsBreakdown]:
    """Analytics Forms Breakdown

     Submission distributions for the selected period. Splits responses by review
    status (new, reviewed, archived) and by source (direct, asset, process stage,
    customer portal, partner portal, sales funnel), with per-slice change against
    a comparison window.

    Params:
        compare: Comparison mode (none, yoy, pop, mom)
        form_id: Optional form to scope the distributions to

    Args:
        tenant_path (str):
        period (AnalyticsFormsBreakdownPeriod | Unset):  Default:
            AnalyticsFormsBreakdownPeriod.YTD.
        compare (AnalyticsFormsBreakdownCompare | Unset):  Default:
            AnalyticsFormsBreakdownCompare.NONE.
        form_id (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AnalyticsFormsBreakdown]
    """

    kwargs = _get_kwargs(
        tenant_path=tenant_path,
        period=period,
        compare=compare,
        form_id=form_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    tenant_path: str,
    *,
    client: AuthenticatedClient,
    period: AnalyticsFormsBreakdownPeriod | Unset = AnalyticsFormsBreakdownPeriod.YTD,
    compare: AnalyticsFormsBreakdownCompare
    | Unset = AnalyticsFormsBreakdownCompare.NONE,
    form_id: None | str | Unset = UNSET,
) -> AnalyticsFormsBreakdown | None:
    """Analytics Forms Breakdown

     Submission distributions for the selected period. Splits responses by review
    status (new, reviewed, archived) and by source (direct, asset, process stage,
    customer portal, partner portal, sales funnel), with per-slice change against
    a comparison window.

    Params:
        compare: Comparison mode (none, yoy, pop, mom)
        form_id: Optional form to scope the distributions to

    Args:
        tenant_path (str):
        period (AnalyticsFormsBreakdownPeriod | Unset):  Default:
            AnalyticsFormsBreakdownPeriod.YTD.
        compare (AnalyticsFormsBreakdownCompare | Unset):  Default:
            AnalyticsFormsBreakdownCompare.NONE.
        form_id (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AnalyticsFormsBreakdown
    """

    return (
        await asyncio_detailed(
            tenant_path=tenant_path,
            client=client,
            period=period,
            compare=compare,
            form_id=form_id,
        )
    ).parsed
