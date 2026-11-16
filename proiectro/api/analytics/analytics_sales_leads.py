from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.analytics_sales_leads import AnalyticsSalesLeads
from ...models.analytics_sales_leads_period import AnalyticsSalesLeadsPeriod
from ...models.analytics_sales_leads_split_by import AnalyticsSalesLeadsSplitBy
from ...types import UNSET, Response, Unset


def _get_kwargs(
    tenant_path: str,
    *,
    period: AnalyticsSalesLeadsPeriod | Unset = AnalyticsSalesLeadsPeriod.YTD,
    split_by: AnalyticsSalesLeadsSplitBy | Unset = AnalyticsSalesLeadsSplitBy.LIST,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_period: str | Unset = UNSET
    if not isinstance(period, Unset):
        json_period = period.value

    params["period"] = json_period

    json_split_by: str | Unset = UNSET
    if not isinstance(split_by, Unset):
        json_split_by = split_by.value

    params["split_by"] = json_split_by

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/{tenant_path}/analytics/sales/leads".format(
            tenant_path=quote(str(tenant_path), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AnalyticsSalesLeads | None:
    if response.status_code == 200:
        response_200 = AnalyticsSalesLeads.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[AnalyticsSalesLeads]:
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
    period: AnalyticsSalesLeadsPeriod | Unset = AnalyticsSalesLeadsPeriod.YTD,
    split_by: AnalyticsSalesLeadsSplitBy | Unset = AnalyticsSalesLeadsSplitBy.LIST,
) -> Response[AnalyticsSalesLeads]:
    """Analytics Sales Leads

     What each lead list, or each lead source, produces. Of the leads first contacted
    in the period, shows how many replied, were qualified and became an opportunity.
    A lead counts for a milestone if it ever reached it or anything beyond it, so a
    lead that replied and was later disqualified still counts as replied.

    Each share is given from the first contacted lead, with its count and likely
    range, and is marked when it is very likely above or below that of all the other
    rows together. Covers the leads you can see; leads nobody has contacted yet are
    in no row and are counted separately.

    Params:
        split_by: Rows by lead list (list) or by lead source (source) - default list

    Args:
        tenant_path (str):
        period (AnalyticsSalesLeadsPeriod | Unset):  Default: AnalyticsSalesLeadsPeriod.YTD.
        split_by (AnalyticsSalesLeadsSplitBy | Unset):  Default: AnalyticsSalesLeadsSplitBy.LIST.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AnalyticsSalesLeads]
    """

    kwargs = _get_kwargs(
        tenant_path=tenant_path,
        period=period,
        split_by=split_by,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    tenant_path: str,
    *,
    client: AuthenticatedClient,
    period: AnalyticsSalesLeadsPeriod | Unset = AnalyticsSalesLeadsPeriod.YTD,
    split_by: AnalyticsSalesLeadsSplitBy | Unset = AnalyticsSalesLeadsSplitBy.LIST,
) -> AnalyticsSalesLeads | None:
    """Analytics Sales Leads

     What each lead list, or each lead source, produces. Of the leads first contacted
    in the period, shows how many replied, were qualified and became an opportunity.
    A lead counts for a milestone if it ever reached it or anything beyond it, so a
    lead that replied and was later disqualified still counts as replied.

    Each share is given from the first contacted lead, with its count and likely
    range, and is marked when it is very likely above or below that of all the other
    rows together. Covers the leads you can see; leads nobody has contacted yet are
    in no row and are counted separately.

    Params:
        split_by: Rows by lead list (list) or by lead source (source) - default list

    Args:
        tenant_path (str):
        period (AnalyticsSalesLeadsPeriod | Unset):  Default: AnalyticsSalesLeadsPeriod.YTD.
        split_by (AnalyticsSalesLeadsSplitBy | Unset):  Default: AnalyticsSalesLeadsSplitBy.LIST.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AnalyticsSalesLeads
    """

    return sync_detailed(
        tenant_path=tenant_path,
        client=client,
        period=period,
        split_by=split_by,
    ).parsed


async def asyncio_detailed(
    tenant_path: str,
    *,
    client: AuthenticatedClient,
    period: AnalyticsSalesLeadsPeriod | Unset = AnalyticsSalesLeadsPeriod.YTD,
    split_by: AnalyticsSalesLeadsSplitBy | Unset = AnalyticsSalesLeadsSplitBy.LIST,
) -> Response[AnalyticsSalesLeads]:
    """Analytics Sales Leads

     What each lead list, or each lead source, produces. Of the leads first contacted
    in the period, shows how many replied, were qualified and became an opportunity.
    A lead counts for a milestone if it ever reached it or anything beyond it, so a
    lead that replied and was later disqualified still counts as replied.

    Each share is given from the first contacted lead, with its count and likely
    range, and is marked when it is very likely above or below that of all the other
    rows together. Covers the leads you can see; leads nobody has contacted yet are
    in no row and are counted separately.

    Params:
        split_by: Rows by lead list (list) or by lead source (source) - default list

    Args:
        tenant_path (str):
        period (AnalyticsSalesLeadsPeriod | Unset):  Default: AnalyticsSalesLeadsPeriod.YTD.
        split_by (AnalyticsSalesLeadsSplitBy | Unset):  Default: AnalyticsSalesLeadsSplitBy.LIST.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AnalyticsSalesLeads]
    """

    kwargs = _get_kwargs(
        tenant_path=tenant_path,
        period=period,
        split_by=split_by,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    tenant_path: str,
    *,
    client: AuthenticatedClient,
    period: AnalyticsSalesLeadsPeriod | Unset = AnalyticsSalesLeadsPeriod.YTD,
    split_by: AnalyticsSalesLeadsSplitBy | Unset = AnalyticsSalesLeadsSplitBy.LIST,
) -> AnalyticsSalesLeads | None:
    """Analytics Sales Leads

     What each lead list, or each lead source, produces. Of the leads first contacted
    in the period, shows how many replied, were qualified and became an opportunity.
    A lead counts for a milestone if it ever reached it or anything beyond it, so a
    lead that replied and was later disqualified still counts as replied.

    Each share is given from the first contacted lead, with its count and likely
    range, and is marked when it is very likely above or below that of all the other
    rows together. Covers the leads you can see; leads nobody has contacted yet are
    in no row and are counted separately.

    Params:
        split_by: Rows by lead list (list) or by lead source (source) - default list

    Args:
        tenant_path (str):
        period (AnalyticsSalesLeadsPeriod | Unset):  Default: AnalyticsSalesLeadsPeriod.YTD.
        split_by (AnalyticsSalesLeadsSplitBy | Unset):  Default: AnalyticsSalesLeadsSplitBy.LIST.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AnalyticsSalesLeads
    """

    return (
        await asyncio_detailed(
            tenant_path=tenant_path,
            client=client,
            period=period,
            split_by=split_by,
        )
    ).parsed
