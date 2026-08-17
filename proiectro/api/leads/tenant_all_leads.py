from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.output_all_leads import OutputAllLeads
from ...types import UNSET, Response, Unset


def _get_kwargs(
    tenant_path: str,
    *,
    exclude_mode: bool | None | Unset = UNSET,
    search: None | str | Unset = UNSET,
    status: None | str | Unset = UNSET,
    source: None | str | Unset = UNSET,
    owner: None | str | Unset = UNSET,
    lead_list: None | str | Unset = UNSET,
    has_email: bool | None | Unset = UNSET,
    has_phone: bool | None | Unset = UNSET,
    next_action_window: None | str | Unset = UNSET,
    country: None | str | Unset = UNSET,
    score_min: int | None | Unset = UNSET,
    score_max: int | None | Unset = UNSET,
    tags1: list[str] | None | Unset = UNSET,
    tags2: list[str] | None | Unset = UNSET,
    tags3: list[str] | None | Unset = UNSET,
    label_id1: None | str | Unset = UNSET,
    label_op1: None | str | Unset = UNSET,
    label_val1: None | str | Unset = UNSET,
    label_id2: None | str | Unset = UNSET,
    label_op2: None | str | Unset = UNSET,
    label_val2: None | str | Unset = UNSET,
    label_id3: None | str | Unset = UNSET,
    label_op3: None | str | Unset = UNSET,
    label_val3: None | str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_exclude_mode: bool | None | Unset
    if isinstance(exclude_mode, Unset):
        json_exclude_mode = UNSET
    else:
        json_exclude_mode = exclude_mode
    params["exclude_mode"] = json_exclude_mode

    json_search: None | str | Unset
    if isinstance(search, Unset):
        json_search = UNSET
    else:
        json_search = search
    params["search"] = json_search

    json_status: None | str | Unset
    if isinstance(status, Unset):
        json_status = UNSET
    else:
        json_status = status
    params["status"] = json_status

    json_source: None | str | Unset
    if isinstance(source, Unset):
        json_source = UNSET
    else:
        json_source = source
    params["source"] = json_source

    json_owner: None | str | Unset
    if isinstance(owner, Unset):
        json_owner = UNSET
    else:
        json_owner = owner
    params["owner"] = json_owner

    json_lead_list: None | str | Unset
    if isinstance(lead_list, Unset):
        json_lead_list = UNSET
    else:
        json_lead_list = lead_list
    params["lead_list"] = json_lead_list

    json_has_email: bool | None | Unset
    if isinstance(has_email, Unset):
        json_has_email = UNSET
    else:
        json_has_email = has_email
    params["has_email"] = json_has_email

    json_has_phone: bool | None | Unset
    if isinstance(has_phone, Unset):
        json_has_phone = UNSET
    else:
        json_has_phone = has_phone
    params["has_phone"] = json_has_phone

    json_next_action_window: None | str | Unset
    if isinstance(next_action_window, Unset):
        json_next_action_window = UNSET
    else:
        json_next_action_window = next_action_window
    params["next_action_window"] = json_next_action_window

    json_country: None | str | Unset
    if isinstance(country, Unset):
        json_country = UNSET
    else:
        json_country = country
    params["country"] = json_country

    json_score_min: int | None | Unset
    if isinstance(score_min, Unset):
        json_score_min = UNSET
    else:
        json_score_min = score_min
    params["score_min"] = json_score_min

    json_score_max: int | None | Unset
    if isinstance(score_max, Unset):
        json_score_max = UNSET
    else:
        json_score_max = score_max
    params["score_max"] = json_score_max

    json_tags1: list[str] | None | Unset
    if isinstance(tags1, Unset):
        json_tags1 = UNSET
    elif isinstance(tags1, list):
        json_tags1 = tags1

    else:
        json_tags1 = tags1
    params["tags1"] = json_tags1

    json_tags2: list[str] | None | Unset
    if isinstance(tags2, Unset):
        json_tags2 = UNSET
    elif isinstance(tags2, list):
        json_tags2 = tags2

    else:
        json_tags2 = tags2
    params["tags2"] = json_tags2

    json_tags3: list[str] | None | Unset
    if isinstance(tags3, Unset):
        json_tags3 = UNSET
    elif isinstance(tags3, list):
        json_tags3 = tags3

    else:
        json_tags3 = tags3
    params["tags3"] = json_tags3

    json_label_id1: None | str | Unset
    if isinstance(label_id1, Unset):
        json_label_id1 = UNSET
    else:
        json_label_id1 = label_id1
    params["label_id1"] = json_label_id1

    json_label_op1: None | str | Unset
    if isinstance(label_op1, Unset):
        json_label_op1 = UNSET
    else:
        json_label_op1 = label_op1
    params["label_op1"] = json_label_op1

    json_label_val1: None | str | Unset
    if isinstance(label_val1, Unset):
        json_label_val1 = UNSET
    else:
        json_label_val1 = label_val1
    params["label_val1"] = json_label_val1

    json_label_id2: None | str | Unset
    if isinstance(label_id2, Unset):
        json_label_id2 = UNSET
    else:
        json_label_id2 = label_id2
    params["label_id2"] = json_label_id2

    json_label_op2: None | str | Unset
    if isinstance(label_op2, Unset):
        json_label_op2 = UNSET
    else:
        json_label_op2 = label_op2
    params["label_op2"] = json_label_op2

    json_label_val2: None | str | Unset
    if isinstance(label_val2, Unset):
        json_label_val2 = UNSET
    else:
        json_label_val2 = label_val2
    params["label_val2"] = json_label_val2

    json_label_id3: None | str | Unset
    if isinstance(label_id3, Unset):
        json_label_id3 = UNSET
    else:
        json_label_id3 = label_id3
    params["label_id3"] = json_label_id3

    json_label_op3: None | str | Unset
    if isinstance(label_op3, Unset):
        json_label_op3 = UNSET
    else:
        json_label_op3 = label_op3
    params["label_op3"] = json_label_op3

    json_label_val3: None | str | Unset
    if isinstance(label_val3, Unset):
        json_label_val3 = UNSET
    else:
        json_label_val3 = label_val3
    params["label_val3"] = json_label_val3

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/{tenant_path}/all_leads".format(
            tenant_path=quote(str(tenant_path), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> OutputAllLeads | None:
    if response.status_code == 200:
        response_200 = OutputAllLeads.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[OutputAllLeads]:
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
    exclude_mode: bool | None | Unset = UNSET,
    search: None | str | Unset = UNSET,
    status: None | str | Unset = UNSET,
    source: None | str | Unset = UNSET,
    owner: None | str | Unset = UNSET,
    lead_list: None | str | Unset = UNSET,
    has_email: bool | None | Unset = UNSET,
    has_phone: bool | None | Unset = UNSET,
    next_action_window: None | str | Unset = UNSET,
    country: None | str | Unset = UNSET,
    score_min: int | None | Unset = UNSET,
    score_max: int | None | Unset = UNSET,
    tags1: list[str] | None | Unset = UNSET,
    tags2: list[str] | None | Unset = UNSET,
    tags3: list[str] | None | Unset = UNSET,
    label_id1: None | str | Unset = UNSET,
    label_op1: None | str | Unset = UNSET,
    label_val1: None | str | Unset = UNSET,
    label_id2: None | str | Unset = UNSET,
    label_op2: None | str | Unset = UNSET,
    label_val2: None | str | Unset = UNSET,
    label_id3: None | str | Unset = UNSET,
    label_op3: None | str | Unset = UNSET,
    label_val3: None | str | Unset = UNSET,
) -> Response[OutputAllLeads]:
    """Tenant All Leads

     Search and filter the leads that are still in play. Leads you have converted, disqualified
    or marked do not contact are kept in their own tabs and are left out here.

    Args:
        tenant_path (str):
        exclude_mode (bool | None | Unset): Invert filter logic to exclude matching results
        search (None | str | Unset): Search by lead name, company name, or email
        status (None | str | Unset): Filter by status
        source (None | str | Unset): Filter by source
        owner (None | str | Unset): Filter by owning team member
        lead_list (None | str | Unset): Filter by list assignment
        has_email (bool | None | Unset): Only leads with an email address
        has_phone (bool | None | Unset): Only leads with a phone number
        next_action_window (None | str | Unset): Worklist bucket: overdue / today / scheduled /
            none
        country (None | str | Unset): Filter by country (ISO alpha-2 code, or the country name)
        score_min (int | None | Unset): Minimum score
        score_max (int | None | Unset): Maximum score
        tags1 (list[str] | None | Unset): Filter by tags (first set)
        tags2 (list[str] | None | Unset): Filter by tags (second set)
        tags3 (list[str] | None | Unset): Filter by tags (third set)
        label_id1 (None | str | Unset): Filter by label (first set - select which label)
        label_op1 (None | str | Unset): Label comparison operator (first set)
        label_val1 (None | str | Unset): Label value to compare against (first set)
        label_id2 (None | str | Unset): Filter by label (second set - select which label)
        label_op2 (None | str | Unset): Label comparison operator (second set)
        label_val2 (None | str | Unset): Label value to compare against (second set)
        label_id3 (None | str | Unset): Filter by label (third set - select which label)
        label_op3 (None | str | Unset): Label comparison operator (third set)
        label_val3 (None | str | Unset): Label value to compare against (third set)

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OutputAllLeads]
    """

    kwargs = _get_kwargs(
        tenant_path=tenant_path,
        exclude_mode=exclude_mode,
        search=search,
        status=status,
        source=source,
        owner=owner,
        lead_list=lead_list,
        has_email=has_email,
        has_phone=has_phone,
        next_action_window=next_action_window,
        country=country,
        score_min=score_min,
        score_max=score_max,
        tags1=tags1,
        tags2=tags2,
        tags3=tags3,
        label_id1=label_id1,
        label_op1=label_op1,
        label_val1=label_val1,
        label_id2=label_id2,
        label_op2=label_op2,
        label_val2=label_val2,
        label_id3=label_id3,
        label_op3=label_op3,
        label_val3=label_val3,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    tenant_path: str,
    *,
    client: AuthenticatedClient,
    exclude_mode: bool | None | Unset = UNSET,
    search: None | str | Unset = UNSET,
    status: None | str | Unset = UNSET,
    source: None | str | Unset = UNSET,
    owner: None | str | Unset = UNSET,
    lead_list: None | str | Unset = UNSET,
    has_email: bool | None | Unset = UNSET,
    has_phone: bool | None | Unset = UNSET,
    next_action_window: None | str | Unset = UNSET,
    country: None | str | Unset = UNSET,
    score_min: int | None | Unset = UNSET,
    score_max: int | None | Unset = UNSET,
    tags1: list[str] | None | Unset = UNSET,
    tags2: list[str] | None | Unset = UNSET,
    tags3: list[str] | None | Unset = UNSET,
    label_id1: None | str | Unset = UNSET,
    label_op1: None | str | Unset = UNSET,
    label_val1: None | str | Unset = UNSET,
    label_id2: None | str | Unset = UNSET,
    label_op2: None | str | Unset = UNSET,
    label_val2: None | str | Unset = UNSET,
    label_id3: None | str | Unset = UNSET,
    label_op3: None | str | Unset = UNSET,
    label_val3: None | str | Unset = UNSET,
) -> OutputAllLeads | None:
    """Tenant All Leads

     Search and filter the leads that are still in play. Leads you have converted, disqualified
    or marked do not contact are kept in their own tabs and are left out here.

    Args:
        tenant_path (str):
        exclude_mode (bool | None | Unset): Invert filter logic to exclude matching results
        search (None | str | Unset): Search by lead name, company name, or email
        status (None | str | Unset): Filter by status
        source (None | str | Unset): Filter by source
        owner (None | str | Unset): Filter by owning team member
        lead_list (None | str | Unset): Filter by list assignment
        has_email (bool | None | Unset): Only leads with an email address
        has_phone (bool | None | Unset): Only leads with a phone number
        next_action_window (None | str | Unset): Worklist bucket: overdue / today / scheduled /
            none
        country (None | str | Unset): Filter by country (ISO alpha-2 code, or the country name)
        score_min (int | None | Unset): Minimum score
        score_max (int | None | Unset): Maximum score
        tags1 (list[str] | None | Unset): Filter by tags (first set)
        tags2 (list[str] | None | Unset): Filter by tags (second set)
        tags3 (list[str] | None | Unset): Filter by tags (third set)
        label_id1 (None | str | Unset): Filter by label (first set - select which label)
        label_op1 (None | str | Unset): Label comparison operator (first set)
        label_val1 (None | str | Unset): Label value to compare against (first set)
        label_id2 (None | str | Unset): Filter by label (second set - select which label)
        label_op2 (None | str | Unset): Label comparison operator (second set)
        label_val2 (None | str | Unset): Label value to compare against (second set)
        label_id3 (None | str | Unset): Filter by label (third set - select which label)
        label_op3 (None | str | Unset): Label comparison operator (third set)
        label_val3 (None | str | Unset): Label value to compare against (third set)

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OutputAllLeads
    """

    return sync_detailed(
        tenant_path=tenant_path,
        client=client,
        exclude_mode=exclude_mode,
        search=search,
        status=status,
        source=source,
        owner=owner,
        lead_list=lead_list,
        has_email=has_email,
        has_phone=has_phone,
        next_action_window=next_action_window,
        country=country,
        score_min=score_min,
        score_max=score_max,
        tags1=tags1,
        tags2=tags2,
        tags3=tags3,
        label_id1=label_id1,
        label_op1=label_op1,
        label_val1=label_val1,
        label_id2=label_id2,
        label_op2=label_op2,
        label_val2=label_val2,
        label_id3=label_id3,
        label_op3=label_op3,
        label_val3=label_val3,
    ).parsed


async def asyncio_detailed(
    tenant_path: str,
    *,
    client: AuthenticatedClient,
    exclude_mode: bool | None | Unset = UNSET,
    search: None | str | Unset = UNSET,
    status: None | str | Unset = UNSET,
    source: None | str | Unset = UNSET,
    owner: None | str | Unset = UNSET,
    lead_list: None | str | Unset = UNSET,
    has_email: bool | None | Unset = UNSET,
    has_phone: bool | None | Unset = UNSET,
    next_action_window: None | str | Unset = UNSET,
    country: None | str | Unset = UNSET,
    score_min: int | None | Unset = UNSET,
    score_max: int | None | Unset = UNSET,
    tags1: list[str] | None | Unset = UNSET,
    tags2: list[str] | None | Unset = UNSET,
    tags3: list[str] | None | Unset = UNSET,
    label_id1: None | str | Unset = UNSET,
    label_op1: None | str | Unset = UNSET,
    label_val1: None | str | Unset = UNSET,
    label_id2: None | str | Unset = UNSET,
    label_op2: None | str | Unset = UNSET,
    label_val2: None | str | Unset = UNSET,
    label_id3: None | str | Unset = UNSET,
    label_op3: None | str | Unset = UNSET,
    label_val3: None | str | Unset = UNSET,
) -> Response[OutputAllLeads]:
    """Tenant All Leads

     Search and filter the leads that are still in play. Leads you have converted, disqualified
    or marked do not contact are kept in their own tabs and are left out here.

    Args:
        tenant_path (str):
        exclude_mode (bool | None | Unset): Invert filter logic to exclude matching results
        search (None | str | Unset): Search by lead name, company name, or email
        status (None | str | Unset): Filter by status
        source (None | str | Unset): Filter by source
        owner (None | str | Unset): Filter by owning team member
        lead_list (None | str | Unset): Filter by list assignment
        has_email (bool | None | Unset): Only leads with an email address
        has_phone (bool | None | Unset): Only leads with a phone number
        next_action_window (None | str | Unset): Worklist bucket: overdue / today / scheduled /
            none
        country (None | str | Unset): Filter by country (ISO alpha-2 code, or the country name)
        score_min (int | None | Unset): Minimum score
        score_max (int | None | Unset): Maximum score
        tags1 (list[str] | None | Unset): Filter by tags (first set)
        tags2 (list[str] | None | Unset): Filter by tags (second set)
        tags3 (list[str] | None | Unset): Filter by tags (third set)
        label_id1 (None | str | Unset): Filter by label (first set - select which label)
        label_op1 (None | str | Unset): Label comparison operator (first set)
        label_val1 (None | str | Unset): Label value to compare against (first set)
        label_id2 (None | str | Unset): Filter by label (second set - select which label)
        label_op2 (None | str | Unset): Label comparison operator (second set)
        label_val2 (None | str | Unset): Label value to compare against (second set)
        label_id3 (None | str | Unset): Filter by label (third set - select which label)
        label_op3 (None | str | Unset): Label comparison operator (third set)
        label_val3 (None | str | Unset): Label value to compare against (third set)

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OutputAllLeads]
    """

    kwargs = _get_kwargs(
        tenant_path=tenant_path,
        exclude_mode=exclude_mode,
        search=search,
        status=status,
        source=source,
        owner=owner,
        lead_list=lead_list,
        has_email=has_email,
        has_phone=has_phone,
        next_action_window=next_action_window,
        country=country,
        score_min=score_min,
        score_max=score_max,
        tags1=tags1,
        tags2=tags2,
        tags3=tags3,
        label_id1=label_id1,
        label_op1=label_op1,
        label_val1=label_val1,
        label_id2=label_id2,
        label_op2=label_op2,
        label_val2=label_val2,
        label_id3=label_id3,
        label_op3=label_op3,
        label_val3=label_val3,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    tenant_path: str,
    *,
    client: AuthenticatedClient,
    exclude_mode: bool | None | Unset = UNSET,
    search: None | str | Unset = UNSET,
    status: None | str | Unset = UNSET,
    source: None | str | Unset = UNSET,
    owner: None | str | Unset = UNSET,
    lead_list: None | str | Unset = UNSET,
    has_email: bool | None | Unset = UNSET,
    has_phone: bool | None | Unset = UNSET,
    next_action_window: None | str | Unset = UNSET,
    country: None | str | Unset = UNSET,
    score_min: int | None | Unset = UNSET,
    score_max: int | None | Unset = UNSET,
    tags1: list[str] | None | Unset = UNSET,
    tags2: list[str] | None | Unset = UNSET,
    tags3: list[str] | None | Unset = UNSET,
    label_id1: None | str | Unset = UNSET,
    label_op1: None | str | Unset = UNSET,
    label_val1: None | str | Unset = UNSET,
    label_id2: None | str | Unset = UNSET,
    label_op2: None | str | Unset = UNSET,
    label_val2: None | str | Unset = UNSET,
    label_id3: None | str | Unset = UNSET,
    label_op3: None | str | Unset = UNSET,
    label_val3: None | str | Unset = UNSET,
) -> OutputAllLeads | None:
    """Tenant All Leads

     Search and filter the leads that are still in play. Leads you have converted, disqualified
    or marked do not contact are kept in their own tabs and are left out here.

    Args:
        tenant_path (str):
        exclude_mode (bool | None | Unset): Invert filter logic to exclude matching results
        search (None | str | Unset): Search by lead name, company name, or email
        status (None | str | Unset): Filter by status
        source (None | str | Unset): Filter by source
        owner (None | str | Unset): Filter by owning team member
        lead_list (None | str | Unset): Filter by list assignment
        has_email (bool | None | Unset): Only leads with an email address
        has_phone (bool | None | Unset): Only leads with a phone number
        next_action_window (None | str | Unset): Worklist bucket: overdue / today / scheduled /
            none
        country (None | str | Unset): Filter by country (ISO alpha-2 code, or the country name)
        score_min (int | None | Unset): Minimum score
        score_max (int | None | Unset): Maximum score
        tags1 (list[str] | None | Unset): Filter by tags (first set)
        tags2 (list[str] | None | Unset): Filter by tags (second set)
        tags3 (list[str] | None | Unset): Filter by tags (third set)
        label_id1 (None | str | Unset): Filter by label (first set - select which label)
        label_op1 (None | str | Unset): Label comparison operator (first set)
        label_val1 (None | str | Unset): Label value to compare against (first set)
        label_id2 (None | str | Unset): Filter by label (second set - select which label)
        label_op2 (None | str | Unset): Label comparison operator (second set)
        label_val2 (None | str | Unset): Label value to compare against (second set)
        label_id3 (None | str | Unset): Filter by label (third set - select which label)
        label_op3 (None | str | Unset): Label comparison operator (third set)
        label_val3 (None | str | Unset): Label value to compare against (third set)

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OutputAllLeads
    """

    return (
        await asyncio_detailed(
            tenant_path=tenant_path,
            client=client,
            exclude_mode=exclude_mode,
            search=search,
            status=status,
            source=source,
            owner=owner,
            lead_list=lead_list,
            has_email=has_email,
            has_phone=has_phone,
            next_action_window=next_action_window,
            country=country,
            score_min=score_min,
            score_max=score_max,
            tags1=tags1,
            tags2=tags2,
            tags3=tags3,
            label_id1=label_id1,
            label_op1=label_op1,
            label_val1=label_val1,
            label_id2=label_id2,
            label_op2=label_op2,
            label_val2=label_val2,
            label_id3=label_id3,
            label_op3=label_op3,
            label_val3=label_val3,
        )
    ).parsed
