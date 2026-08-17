from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.output_project_work_items import OutputProjectWorkItems
from ...types import UNSET, Response, Unset


def _get_kwargs(
    tenant_path: str,
    project_id: str,
    *,
    exclude_mode: bool | None | Unset = UNSET,
    search: None | str | Unset = UNSET,
    internal_code: None | str | Unset = UNSET,
    work_item_type: None | str | Unset = UNSET,
    owner: None | str | Unset = UNSET,
    constraint_type: None | str | Unset = UNSET,
    planned_start_from: None | str | Unset = UNSET,
    planned_start_to: None | str | Unset = UNSET,
    planned_end_from: None | str | Unset = UNSET,
    planned_end_to: None | str | Unset = UNSET,
    is_finished: bool | None | Unset = UNSET,
    is_accepted: bool | None | Unset = UNSET,
    visible_to_customer: bool | None | Unset = UNSET,
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

    json_internal_code: None | str | Unset
    if isinstance(internal_code, Unset):
        json_internal_code = UNSET
    else:
        json_internal_code = internal_code
    params["internal_code"] = json_internal_code

    json_work_item_type: None | str | Unset
    if isinstance(work_item_type, Unset):
        json_work_item_type = UNSET
    else:
        json_work_item_type = work_item_type
    params["work_item_type"] = json_work_item_type

    json_owner: None | str | Unset
    if isinstance(owner, Unset):
        json_owner = UNSET
    else:
        json_owner = owner
    params["owner"] = json_owner

    json_constraint_type: None | str | Unset
    if isinstance(constraint_type, Unset):
        json_constraint_type = UNSET
    else:
        json_constraint_type = constraint_type
    params["constraint_type"] = json_constraint_type

    json_planned_start_from: None | str | Unset
    if isinstance(planned_start_from, Unset):
        json_planned_start_from = UNSET
    else:
        json_planned_start_from = planned_start_from
    params["planned_start_from"] = json_planned_start_from

    json_planned_start_to: None | str | Unset
    if isinstance(planned_start_to, Unset):
        json_planned_start_to = UNSET
    else:
        json_planned_start_to = planned_start_to
    params["planned_start_to"] = json_planned_start_to

    json_planned_end_from: None | str | Unset
    if isinstance(planned_end_from, Unset):
        json_planned_end_from = UNSET
    else:
        json_planned_end_from = planned_end_from
    params["planned_end_from"] = json_planned_end_from

    json_planned_end_to: None | str | Unset
    if isinstance(planned_end_to, Unset):
        json_planned_end_to = UNSET
    else:
        json_planned_end_to = planned_end_to
    params["planned_end_to"] = json_planned_end_to

    json_is_finished: bool | None | Unset
    if isinstance(is_finished, Unset):
        json_is_finished = UNSET
    else:
        json_is_finished = is_finished
    params["is_finished"] = json_is_finished

    json_is_accepted: bool | None | Unset
    if isinstance(is_accepted, Unset):
        json_is_accepted = UNSET
    else:
        json_is_accepted = is_accepted
    params["is_accepted"] = json_is_accepted

    json_visible_to_customer: bool | None | Unset
    if isinstance(visible_to_customer, Unset):
        json_visible_to_customer = UNSET
    else:
        json_visible_to_customer = visible_to_customer
    params["visible_to_customer"] = json_visible_to_customer

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
        "url": "/api/v1/{tenant_path}/project_work_items/{project_id}".format(
            tenant_path=quote(str(tenant_path), safe=""),
            project_id=quote(str(project_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> OutputProjectWorkItems | None:
    if response.status_code == 200:
        response_200 = OutputProjectWorkItems.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[OutputProjectWorkItems]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    tenant_path: str,
    project_id: str,
    *,
    client: AuthenticatedClient,
    exclude_mode: bool | None | Unset = UNSET,
    search: None | str | Unset = UNSET,
    internal_code: None | str | Unset = UNSET,
    work_item_type: None | str | Unset = UNSET,
    owner: None | str | Unset = UNSET,
    constraint_type: None | str | Unset = UNSET,
    planned_start_from: None | str | Unset = UNSET,
    planned_start_to: None | str | Unset = UNSET,
    planned_end_from: None | str | Unset = UNSET,
    planned_end_to: None | str | Unset = UNSET,
    is_finished: bool | None | Unset = UNSET,
    is_accepted: bool | None | Unset = UNSET,
    visible_to_customer: bool | None | Unset = UNSET,
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
) -> Response[OutputProjectWorkItems]:
    """Project Work Items

     Get work items hierarchy and available work item types for a project.
    Shows the complete work breakdown structure with all work items,
    and provides information about what types can be added at the top level
    based on the project's WBS configuration.

    Applying a filter returns the matching work items as a flat list instead of the tree,
    since a filtered hierarchy is not a hierarchy.

    Args:
        tenant_path (str):
        project_id (str):
        exclude_mode (bool | None | Unset): Invert filter logic to exclude matching results
        search (None | str | Unset): Search by name, description or internal code
        internal_code (None | str | Unset): Filter by exact internal code
        work_item_type (None | str | Unset): Filter by work item type
        owner (None | str | Unset): Filter by owner
        constraint_type (None | str | Unset): Filter by scheduling constraint
        planned_start_from (None | str | Unset): Planned start on or after this date, e.g. '02
            Jan, 2025'
        planned_start_to (None | str | Unset): Planned start on or before this date, e.g. '02 Jan,
            2025'
        planned_end_from (None | str | Unset): Planned end on or after this date, e.g. '02 Jan,
            2025'
        planned_end_to (None | str | Unset): Planned end on or before this date, e.g. '02 Jan,
            2025'
        is_finished (bool | None | Unset): Only finished work items
        is_accepted (bool | None | Unset): Only accepted work items
        visible_to_customer (bool | None | Unset): Only work items visible to the customer
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
        Response[OutputProjectWorkItems]
    """

    kwargs = _get_kwargs(
        tenant_path=tenant_path,
        project_id=project_id,
        exclude_mode=exclude_mode,
        search=search,
        internal_code=internal_code,
        work_item_type=work_item_type,
        owner=owner,
        constraint_type=constraint_type,
        planned_start_from=planned_start_from,
        planned_start_to=planned_start_to,
        planned_end_from=planned_end_from,
        planned_end_to=planned_end_to,
        is_finished=is_finished,
        is_accepted=is_accepted,
        visible_to_customer=visible_to_customer,
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
    project_id: str,
    *,
    client: AuthenticatedClient,
    exclude_mode: bool | None | Unset = UNSET,
    search: None | str | Unset = UNSET,
    internal_code: None | str | Unset = UNSET,
    work_item_type: None | str | Unset = UNSET,
    owner: None | str | Unset = UNSET,
    constraint_type: None | str | Unset = UNSET,
    planned_start_from: None | str | Unset = UNSET,
    planned_start_to: None | str | Unset = UNSET,
    planned_end_from: None | str | Unset = UNSET,
    planned_end_to: None | str | Unset = UNSET,
    is_finished: bool | None | Unset = UNSET,
    is_accepted: bool | None | Unset = UNSET,
    visible_to_customer: bool | None | Unset = UNSET,
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
) -> OutputProjectWorkItems | None:
    """Project Work Items

     Get work items hierarchy and available work item types for a project.
    Shows the complete work breakdown structure with all work items,
    and provides information about what types can be added at the top level
    based on the project's WBS configuration.

    Applying a filter returns the matching work items as a flat list instead of the tree,
    since a filtered hierarchy is not a hierarchy.

    Args:
        tenant_path (str):
        project_id (str):
        exclude_mode (bool | None | Unset): Invert filter logic to exclude matching results
        search (None | str | Unset): Search by name, description or internal code
        internal_code (None | str | Unset): Filter by exact internal code
        work_item_type (None | str | Unset): Filter by work item type
        owner (None | str | Unset): Filter by owner
        constraint_type (None | str | Unset): Filter by scheduling constraint
        planned_start_from (None | str | Unset): Planned start on or after this date, e.g. '02
            Jan, 2025'
        planned_start_to (None | str | Unset): Planned start on or before this date, e.g. '02 Jan,
            2025'
        planned_end_from (None | str | Unset): Planned end on or after this date, e.g. '02 Jan,
            2025'
        planned_end_to (None | str | Unset): Planned end on or before this date, e.g. '02 Jan,
            2025'
        is_finished (bool | None | Unset): Only finished work items
        is_accepted (bool | None | Unset): Only accepted work items
        visible_to_customer (bool | None | Unset): Only work items visible to the customer
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
        OutputProjectWorkItems
    """

    return sync_detailed(
        tenant_path=tenant_path,
        project_id=project_id,
        client=client,
        exclude_mode=exclude_mode,
        search=search,
        internal_code=internal_code,
        work_item_type=work_item_type,
        owner=owner,
        constraint_type=constraint_type,
        planned_start_from=planned_start_from,
        planned_start_to=planned_start_to,
        planned_end_from=planned_end_from,
        planned_end_to=planned_end_to,
        is_finished=is_finished,
        is_accepted=is_accepted,
        visible_to_customer=visible_to_customer,
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
    project_id: str,
    *,
    client: AuthenticatedClient,
    exclude_mode: bool | None | Unset = UNSET,
    search: None | str | Unset = UNSET,
    internal_code: None | str | Unset = UNSET,
    work_item_type: None | str | Unset = UNSET,
    owner: None | str | Unset = UNSET,
    constraint_type: None | str | Unset = UNSET,
    planned_start_from: None | str | Unset = UNSET,
    planned_start_to: None | str | Unset = UNSET,
    planned_end_from: None | str | Unset = UNSET,
    planned_end_to: None | str | Unset = UNSET,
    is_finished: bool | None | Unset = UNSET,
    is_accepted: bool | None | Unset = UNSET,
    visible_to_customer: bool | None | Unset = UNSET,
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
) -> Response[OutputProjectWorkItems]:
    """Project Work Items

     Get work items hierarchy and available work item types for a project.
    Shows the complete work breakdown structure with all work items,
    and provides information about what types can be added at the top level
    based on the project's WBS configuration.

    Applying a filter returns the matching work items as a flat list instead of the tree,
    since a filtered hierarchy is not a hierarchy.

    Args:
        tenant_path (str):
        project_id (str):
        exclude_mode (bool | None | Unset): Invert filter logic to exclude matching results
        search (None | str | Unset): Search by name, description or internal code
        internal_code (None | str | Unset): Filter by exact internal code
        work_item_type (None | str | Unset): Filter by work item type
        owner (None | str | Unset): Filter by owner
        constraint_type (None | str | Unset): Filter by scheduling constraint
        planned_start_from (None | str | Unset): Planned start on or after this date, e.g. '02
            Jan, 2025'
        planned_start_to (None | str | Unset): Planned start on or before this date, e.g. '02 Jan,
            2025'
        planned_end_from (None | str | Unset): Planned end on or after this date, e.g. '02 Jan,
            2025'
        planned_end_to (None | str | Unset): Planned end on or before this date, e.g. '02 Jan,
            2025'
        is_finished (bool | None | Unset): Only finished work items
        is_accepted (bool | None | Unset): Only accepted work items
        visible_to_customer (bool | None | Unset): Only work items visible to the customer
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
        Response[OutputProjectWorkItems]
    """

    kwargs = _get_kwargs(
        tenant_path=tenant_path,
        project_id=project_id,
        exclude_mode=exclude_mode,
        search=search,
        internal_code=internal_code,
        work_item_type=work_item_type,
        owner=owner,
        constraint_type=constraint_type,
        planned_start_from=planned_start_from,
        planned_start_to=planned_start_to,
        planned_end_from=planned_end_from,
        planned_end_to=planned_end_to,
        is_finished=is_finished,
        is_accepted=is_accepted,
        visible_to_customer=visible_to_customer,
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
    project_id: str,
    *,
    client: AuthenticatedClient,
    exclude_mode: bool | None | Unset = UNSET,
    search: None | str | Unset = UNSET,
    internal_code: None | str | Unset = UNSET,
    work_item_type: None | str | Unset = UNSET,
    owner: None | str | Unset = UNSET,
    constraint_type: None | str | Unset = UNSET,
    planned_start_from: None | str | Unset = UNSET,
    planned_start_to: None | str | Unset = UNSET,
    planned_end_from: None | str | Unset = UNSET,
    planned_end_to: None | str | Unset = UNSET,
    is_finished: bool | None | Unset = UNSET,
    is_accepted: bool | None | Unset = UNSET,
    visible_to_customer: bool | None | Unset = UNSET,
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
) -> OutputProjectWorkItems | None:
    """Project Work Items

     Get work items hierarchy and available work item types for a project.
    Shows the complete work breakdown structure with all work items,
    and provides information about what types can be added at the top level
    based on the project's WBS configuration.

    Applying a filter returns the matching work items as a flat list instead of the tree,
    since a filtered hierarchy is not a hierarchy.

    Args:
        tenant_path (str):
        project_id (str):
        exclude_mode (bool | None | Unset): Invert filter logic to exclude matching results
        search (None | str | Unset): Search by name, description or internal code
        internal_code (None | str | Unset): Filter by exact internal code
        work_item_type (None | str | Unset): Filter by work item type
        owner (None | str | Unset): Filter by owner
        constraint_type (None | str | Unset): Filter by scheduling constraint
        planned_start_from (None | str | Unset): Planned start on or after this date, e.g. '02
            Jan, 2025'
        planned_start_to (None | str | Unset): Planned start on or before this date, e.g. '02 Jan,
            2025'
        planned_end_from (None | str | Unset): Planned end on or after this date, e.g. '02 Jan,
            2025'
        planned_end_to (None | str | Unset): Planned end on or before this date, e.g. '02 Jan,
            2025'
        is_finished (bool | None | Unset): Only finished work items
        is_accepted (bool | None | Unset): Only accepted work items
        visible_to_customer (bool | None | Unset): Only work items visible to the customer
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
        OutputProjectWorkItems
    """

    return (
        await asyncio_detailed(
            tenant_path=tenant_path,
            project_id=project_id,
            client=client,
            exclude_mode=exclude_mode,
            search=search,
            internal_code=internal_code,
            work_item_type=work_item_type,
            owner=owner,
            constraint_type=constraint_type,
            planned_start_from=planned_start_from,
            planned_start_to=planned_start_to,
            planned_end_from=planned_end_from,
            planned_end_to=planned_end_to,
            is_finished=is_finished,
            is_accepted=is_accepted,
            visible_to_customer=visible_to_customer,
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
