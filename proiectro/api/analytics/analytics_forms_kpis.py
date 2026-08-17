from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.analytics_forms_kpis_period import AnalyticsFormsKpisPeriod
from ...models.forms_kp_is import FormsKPIs
from ...types import UNSET, Response, Unset


def _get_kwargs(
    tenant_path: str,
    *,
    period: AnalyticsFormsKpisPeriod | Unset = AnalyticsFormsKpisPeriod.YTD,
    form_id: None | str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_period: str | Unset = UNSET
    if not isinstance(period, Unset):
        json_period = period.value

    params["period"] = json_period

    json_form_id: None | str | Unset
    if isinstance(form_id, Unset):
        json_form_id = UNSET
    else:
        json_form_id = form_id
    params["form_id"] = json_form_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/{tenant_path}/analytics/forms/kpis".format(
            tenant_path=quote(str(tenant_path), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> FormsKPIs | None:
    if response.status_code == 200:
        response_200 = FormsKPIs.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[FormsKPIs]:
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
    period: AnalyticsFormsKpisPeriod | Unset = AnalyticsFormsKpisPeriod.YTD,
    form_id: None | str | Unset = UNSET,
) -> Response[FormsKPIs]:
    """Analytics Forms Kpis

     Form-collection KPIs for the Forms dashboard. Shows active forms, submissions
    received in the period with a source split, the review backlog, and the
    review rate with status badges for quick assessment.

    Params:
        form_id: Optional form to scope the submission metrics to

    Args:
        tenant_path (str):
        period (AnalyticsFormsKpisPeriod | Unset):  Default: AnalyticsFormsKpisPeriod.YTD.
        form_id (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FormsKPIs]
    """

    kwargs = _get_kwargs(
        tenant_path=tenant_path,
        period=period,
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
    period: AnalyticsFormsKpisPeriod | Unset = AnalyticsFormsKpisPeriod.YTD,
    form_id: None | str | Unset = UNSET,
) -> FormsKPIs | None:
    """Analytics Forms Kpis

     Form-collection KPIs for the Forms dashboard. Shows active forms, submissions
    received in the period with a source split, the review backlog, and the
    review rate with status badges for quick assessment.

    Params:
        form_id: Optional form to scope the submission metrics to

    Args:
        tenant_path (str):
        period (AnalyticsFormsKpisPeriod | Unset):  Default: AnalyticsFormsKpisPeriod.YTD.
        form_id (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FormsKPIs
    """

    return sync_detailed(
        tenant_path=tenant_path,
        client=client,
        period=period,
        form_id=form_id,
    ).parsed


async def asyncio_detailed(
    tenant_path: str,
    *,
    client: AuthenticatedClient,
    period: AnalyticsFormsKpisPeriod | Unset = AnalyticsFormsKpisPeriod.YTD,
    form_id: None | str | Unset = UNSET,
) -> Response[FormsKPIs]:
    """Analytics Forms Kpis

     Form-collection KPIs for the Forms dashboard. Shows active forms, submissions
    received in the period with a source split, the review backlog, and the
    review rate with status badges for quick assessment.

    Params:
        form_id: Optional form to scope the submission metrics to

    Args:
        tenant_path (str):
        period (AnalyticsFormsKpisPeriod | Unset):  Default: AnalyticsFormsKpisPeriod.YTD.
        form_id (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FormsKPIs]
    """

    kwargs = _get_kwargs(
        tenant_path=tenant_path,
        period=period,
        form_id=form_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    tenant_path: str,
    *,
    client: AuthenticatedClient,
    period: AnalyticsFormsKpisPeriod | Unset = AnalyticsFormsKpisPeriod.YTD,
    form_id: None | str | Unset = UNSET,
) -> FormsKPIs | None:
    """Analytics Forms Kpis

     Form-collection KPIs for the Forms dashboard. Shows active forms, submissions
    received in the period with a source split, the review backlog, and the
    review rate with status badges for quick assessment.

    Params:
        form_id: Optional form to scope the submission metrics to

    Args:
        tenant_path (str):
        period (AnalyticsFormsKpisPeriod | Unset):  Default: AnalyticsFormsKpisPeriod.YTD.
        form_id (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FormsKPIs
    """

    return (
        await asyncio_detailed(
            tenant_path=tenant_path,
            client=client,
            period=period,
            form_id=form_id,
        )
    ).parsed
