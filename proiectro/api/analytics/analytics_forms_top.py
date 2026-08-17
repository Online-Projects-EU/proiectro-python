from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.analytics_forms_top import AnalyticsFormsTop
from ...models.analytics_forms_top_compare import AnalyticsFormsTopCompare
from ...models.analytics_forms_top_period import AnalyticsFormsTopPeriod
from ...types import UNSET, Response, Unset


def _get_kwargs(
    tenant_path: str,
    *,
    period: AnalyticsFormsTopPeriod | Unset = AnalyticsFormsTopPeriod.YTD,
    compare: AnalyticsFormsTopCompare | Unset = AnalyticsFormsTopCompare.NONE,
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
        "url": "/api/v1/{tenant_path}/analytics/forms/top".format(
            tenant_path=quote(str(tenant_path), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AnalyticsFormsTop | None:
    if response.status_code == 200:
        response_200 = AnalyticsFormsTop.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[AnalyticsFormsTop]:
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
    period: AnalyticsFormsTopPeriod | Unset = AnalyticsFormsTopPeriod.YTD,
    compare: AnalyticsFormsTopCompare | Unset = AnalyticsFormsTopCompare.NONE,
    form_id: None | str | Unset = UNSET,
) -> Response[AnalyticsFormsTop]:
    """Analytics Forms Top

     The busiest forms in the selected period, ranked by submissions received, with
    per-form change against a comparison window. Each entry links to the form's
    submission review page.

    Params:
        compare: Comparison mode (none, yoy, pop, mom)
        form_id: Optional form to scope the ranking to

    Args:
        tenant_path (str):
        period (AnalyticsFormsTopPeriod | Unset):  Default: AnalyticsFormsTopPeriod.YTD.
        compare (AnalyticsFormsTopCompare | Unset):  Default: AnalyticsFormsTopCompare.NONE.
        form_id (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AnalyticsFormsTop]
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
    period: AnalyticsFormsTopPeriod | Unset = AnalyticsFormsTopPeriod.YTD,
    compare: AnalyticsFormsTopCompare | Unset = AnalyticsFormsTopCompare.NONE,
    form_id: None | str | Unset = UNSET,
) -> AnalyticsFormsTop | None:
    """Analytics Forms Top

     The busiest forms in the selected period, ranked by submissions received, with
    per-form change against a comparison window. Each entry links to the form's
    submission review page.

    Params:
        compare: Comparison mode (none, yoy, pop, mom)
        form_id: Optional form to scope the ranking to

    Args:
        tenant_path (str):
        period (AnalyticsFormsTopPeriod | Unset):  Default: AnalyticsFormsTopPeriod.YTD.
        compare (AnalyticsFormsTopCompare | Unset):  Default: AnalyticsFormsTopCompare.NONE.
        form_id (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AnalyticsFormsTop
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
    period: AnalyticsFormsTopPeriod | Unset = AnalyticsFormsTopPeriod.YTD,
    compare: AnalyticsFormsTopCompare | Unset = AnalyticsFormsTopCompare.NONE,
    form_id: None | str | Unset = UNSET,
) -> Response[AnalyticsFormsTop]:
    """Analytics Forms Top

     The busiest forms in the selected period, ranked by submissions received, with
    per-form change against a comparison window. Each entry links to the form's
    submission review page.

    Params:
        compare: Comparison mode (none, yoy, pop, mom)
        form_id: Optional form to scope the ranking to

    Args:
        tenant_path (str):
        period (AnalyticsFormsTopPeriod | Unset):  Default: AnalyticsFormsTopPeriod.YTD.
        compare (AnalyticsFormsTopCompare | Unset):  Default: AnalyticsFormsTopCompare.NONE.
        form_id (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AnalyticsFormsTop]
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
    period: AnalyticsFormsTopPeriod | Unset = AnalyticsFormsTopPeriod.YTD,
    compare: AnalyticsFormsTopCompare | Unset = AnalyticsFormsTopCompare.NONE,
    form_id: None | str | Unset = UNSET,
) -> AnalyticsFormsTop | None:
    """Analytics Forms Top

     The busiest forms in the selected period, ranked by submissions received, with
    per-form change against a comparison window. Each entry links to the form's
    submission review page.

    Params:
        compare: Comparison mode (none, yoy, pop, mom)
        form_id: Optional form to scope the ranking to

    Args:
        tenant_path (str):
        period (AnalyticsFormsTopPeriod | Unset):  Default: AnalyticsFormsTopPeriod.YTD.
        compare (AnalyticsFormsTopCompare | Unset):  Default: AnalyticsFormsTopCompare.NONE.
        form_id (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AnalyticsFormsTop
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
