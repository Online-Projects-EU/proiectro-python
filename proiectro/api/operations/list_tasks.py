from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.output_operational_items import OutputOperationalItems
from ...types import UNSET, Response, Unset


def _get_kwargs(
    tenant_path: str,
    *,
    exclude_mode: bool | None | Unset = UNSET,
    search: None | str | Unset = UNSET,
    process: None | str | Unset = UNSET,
    current_stage: None | str | Unset = UNSET,
    owner: None | str | Unset = UNSET,
    customer: None | str | Unset = UNSET,
    priority: None | str | Unset = UNSET,
    due_from: None | str | Unset = UNSET,
    due_to: None | str | Unset = UNSET,
    is_finished: bool | None | Unset = UNSET,
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

    json_process: None | str | Unset
    if isinstance(process, Unset):
        json_process = UNSET
    else:
        json_process = process
    params["process"] = json_process

    json_current_stage: None | str | Unset
    if isinstance(current_stage, Unset):
        json_current_stage = UNSET
    else:
        json_current_stage = current_stage
    params["current_stage"] = json_current_stage

    json_owner: None | str | Unset
    if isinstance(owner, Unset):
        json_owner = UNSET
    else:
        json_owner = owner
    params["owner"] = json_owner

    json_customer: None | str | Unset
    if isinstance(customer, Unset):
        json_customer = UNSET
    else:
        json_customer = customer
    params["customer"] = json_customer

    json_priority: None | str | Unset
    if isinstance(priority, Unset):
        json_priority = UNSET
    else:
        json_priority = priority
    params["priority"] = json_priority

    json_due_from: None | str | Unset
    if isinstance(due_from, Unset):
        json_due_from = UNSET
    else:
        json_due_from = due_from
    params["due_from"] = json_due_from

    json_due_to: None | str | Unset
    if isinstance(due_to, Unset):
        json_due_to = UNSET
    else:
        json_due_to = due_to
    params["due_to"] = json_due_to

    json_is_finished: bool | None | Unset
    if isinstance(is_finished, Unset):
        json_is_finished = UNSET
    else:
        json_is_finished = is_finished
    params["is_finished"] = json_is_finished

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
        "url": "/api/v1/{tenant_path}/tasks".format(
            tenant_path=quote(str(tenant_path), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> OutputOperationalItems | None:
    if response.status_code == 200:
        response_200 = OutputOperationalItems.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[OutputOperationalItems]:
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
    process: None | str | Unset = UNSET,
    current_stage: None | str | Unset = UNSET,
    owner: None | str | Unset = UNSET,
    customer: None | str | Unset = UNSET,
    priority: None | str | Unset = UNSET,
    due_from: None | str | Unset = UNSET,
    due_to: None | str | Unset = UNSET,
    is_finished: bool | None | Unset = UNSET,
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
) -> Response[OutputOperationalItems]:
    """List Tasks

    Args:
        tenant_path (str):
        exclude_mode (bool | None | Unset): Invert filter logic to exclude matching results
        search (None | str | Unset): Search by name or description
        process (None | str | Unset): Filter by process
        current_stage (None | str | Unset): Filter by current stage
        owner (None | str | Unset): Filter by owner
        customer (None | str | Unset): Filter by customer organization
        priority (None | str | Unset): Filter by priority
        due_from (None | str | Unset): Due on or after this date, e.g. '02 Jan, 2025'
        due_to (None | str | Unset): Due on or before this date, e.g. '02 Jan, 2025'
        is_finished (bool | None | Unset): Only finished tasks
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
        Response[OutputOperationalItems]
    """

    kwargs = _get_kwargs(
        tenant_path=tenant_path,
        exclude_mode=exclude_mode,
        search=search,
        process=process,
        current_stage=current_stage,
        owner=owner,
        customer=customer,
        priority=priority,
        due_from=due_from,
        due_to=due_to,
        is_finished=is_finished,
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
    process: None | str | Unset = UNSET,
    current_stage: None | str | Unset = UNSET,
    owner: None | str | Unset = UNSET,
    customer: None | str | Unset = UNSET,
    priority: None | str | Unset = UNSET,
    due_from: None | str | Unset = UNSET,
    due_to: None | str | Unset = UNSET,
    is_finished: bool | None | Unset = UNSET,
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
) -> OutputOperationalItems | None:
    """List Tasks

    Args:
        tenant_path (str):
        exclude_mode (bool | None | Unset): Invert filter logic to exclude matching results
        search (None | str | Unset): Search by name or description
        process (None | str | Unset): Filter by process
        current_stage (None | str | Unset): Filter by current stage
        owner (None | str | Unset): Filter by owner
        customer (None | str | Unset): Filter by customer organization
        priority (None | str | Unset): Filter by priority
        due_from (None | str | Unset): Due on or after this date, e.g. '02 Jan, 2025'
        due_to (None | str | Unset): Due on or before this date, e.g. '02 Jan, 2025'
        is_finished (bool | None | Unset): Only finished tasks
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
        OutputOperationalItems
    """

    return sync_detailed(
        tenant_path=tenant_path,
        client=client,
        exclude_mode=exclude_mode,
        search=search,
        process=process,
        current_stage=current_stage,
        owner=owner,
        customer=customer,
        priority=priority,
        due_from=due_from,
        due_to=due_to,
        is_finished=is_finished,
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
    process: None | str | Unset = UNSET,
    current_stage: None | str | Unset = UNSET,
    owner: None | str | Unset = UNSET,
    customer: None | str | Unset = UNSET,
    priority: None | str | Unset = UNSET,
    due_from: None | str | Unset = UNSET,
    due_to: None | str | Unset = UNSET,
    is_finished: bool | None | Unset = UNSET,
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
) -> Response[OutputOperationalItems]:
    """List Tasks

    Args:
        tenant_path (str):
        exclude_mode (bool | None | Unset): Invert filter logic to exclude matching results
        search (None | str | Unset): Search by name or description
        process (None | str | Unset): Filter by process
        current_stage (None | str | Unset): Filter by current stage
        owner (None | str | Unset): Filter by owner
        customer (None | str | Unset): Filter by customer organization
        priority (None | str | Unset): Filter by priority
        due_from (None | str | Unset): Due on or after this date, e.g. '02 Jan, 2025'
        due_to (None | str | Unset): Due on or before this date, e.g. '02 Jan, 2025'
        is_finished (bool | None | Unset): Only finished tasks
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
        Response[OutputOperationalItems]
    """

    kwargs = _get_kwargs(
        tenant_path=tenant_path,
        exclude_mode=exclude_mode,
        search=search,
        process=process,
        current_stage=current_stage,
        owner=owner,
        customer=customer,
        priority=priority,
        due_from=due_from,
        due_to=due_to,
        is_finished=is_finished,
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
    process: None | str | Unset = UNSET,
    current_stage: None | str | Unset = UNSET,
    owner: None | str | Unset = UNSET,
    customer: None | str | Unset = UNSET,
    priority: None | str | Unset = UNSET,
    due_from: None | str | Unset = UNSET,
    due_to: None | str | Unset = UNSET,
    is_finished: bool | None | Unset = UNSET,
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
) -> OutputOperationalItems | None:
    """List Tasks

    Args:
        tenant_path (str):
        exclude_mode (bool | None | Unset): Invert filter logic to exclude matching results
        search (None | str | Unset): Search by name or description
        process (None | str | Unset): Filter by process
        current_stage (None | str | Unset): Filter by current stage
        owner (None | str | Unset): Filter by owner
        customer (None | str | Unset): Filter by customer organization
        priority (None | str | Unset): Filter by priority
        due_from (None | str | Unset): Due on or after this date, e.g. '02 Jan, 2025'
        due_to (None | str | Unset): Due on or before this date, e.g. '02 Jan, 2025'
        is_finished (bool | None | Unset): Only finished tasks
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
        OutputOperationalItems
    """

    return (
        await asyncio_detailed(
            tenant_path=tenant_path,
            client=client,
            exclude_mode=exclude_mode,
            search=search,
            process=process,
            current_stage=current_stage,
            owner=owner,
            customer=customer,
            priority=priority,
            due_from=due_from,
            due_to=due_to,
            is_finished=is_finished,
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
