import datetime
from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.output_my_support_requests import OutputMySupportRequests
from ...types import UNSET, Response, Unset


def _get_kwargs(
    tenant_path: str,
    queue_id: str,
    *,
    exclude_mode: bool | None | Unset = UNSET,
    search: None | str | Unset = UNSET,
    type_: None | str | Unset = UNSET,
    severity: None | str | Unset = UNSET,
    status: None | str | Unset = UNSET,
    queue: None | str | Unset = UNSET,
    customer: None | str | Unset = UNSET,
    project: None | str | Unset = UNSET,
    resource: None | str | Unset = UNSET,
    assignee: None | str | Unset = UNSET,
    requester: None | str | Unset = UNSET,
    has_assignee: bool | None | Unset = UNSET,
    created_from: datetime.date | None | Unset = UNSET,
    created_to: datetime.date | None | Unset = UNSET,
    updated_from: datetime.date | None | Unset = UNSET,
    updated_to: datetime.date | None | Unset = UNSET,
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

    json_type_: None | str | Unset
    if isinstance(type_, Unset):
        json_type_ = UNSET
    else:
        json_type_ = type_
    params["type"] = json_type_

    json_severity: None | str | Unset
    if isinstance(severity, Unset):
        json_severity = UNSET
    else:
        json_severity = severity
    params["severity"] = json_severity

    json_status: None | str | Unset
    if isinstance(status, Unset):
        json_status = UNSET
    else:
        json_status = status
    params["status"] = json_status

    json_queue: None | str | Unset
    if isinstance(queue, Unset):
        json_queue = UNSET
    else:
        json_queue = queue
    params["queue"] = json_queue

    json_customer: None | str | Unset
    if isinstance(customer, Unset):
        json_customer = UNSET
    else:
        json_customer = customer
    params["customer"] = json_customer

    json_project: None | str | Unset
    if isinstance(project, Unset):
        json_project = UNSET
    else:
        json_project = project
    params["project"] = json_project

    json_resource: None | str | Unset
    if isinstance(resource, Unset):
        json_resource = UNSET
    else:
        json_resource = resource
    params["resource"] = json_resource

    json_assignee: None | str | Unset
    if isinstance(assignee, Unset):
        json_assignee = UNSET
    else:
        json_assignee = assignee
    params["assignee"] = json_assignee

    json_requester: None | str | Unset
    if isinstance(requester, Unset):
        json_requester = UNSET
    else:
        json_requester = requester
    params["requester"] = json_requester

    json_has_assignee: bool | None | Unset
    if isinstance(has_assignee, Unset):
        json_has_assignee = UNSET
    else:
        json_has_assignee = has_assignee
    params["has_assignee"] = json_has_assignee

    json_created_from: None | str | Unset
    if isinstance(created_from, Unset):
        json_created_from = UNSET
    elif isinstance(created_from, datetime.date):
        json_created_from = created_from.isoformat()
    else:
        json_created_from = created_from
    params["created_from"] = json_created_from

    json_created_to: None | str | Unset
    if isinstance(created_to, Unset):
        json_created_to = UNSET
    elif isinstance(created_to, datetime.date):
        json_created_to = created_to.isoformat()
    else:
        json_created_to = created_to
    params["created_to"] = json_created_to

    json_updated_from: None | str | Unset
    if isinstance(updated_from, Unset):
        json_updated_from = UNSET
    elif isinstance(updated_from, datetime.date):
        json_updated_from = updated_from.isoformat()
    else:
        json_updated_from = updated_from
    params["updated_from"] = json_updated_from

    json_updated_to: None | str | Unset
    if isinstance(updated_to, Unset):
        json_updated_to = UNSET
    elif isinstance(updated_to, datetime.date):
        json_updated_to = updated_to.isoformat()
    else:
        json_updated_to = updated_to
    params["updated_to"] = json_updated_to

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/{tenant_path}/queue_internal_support_requests/{queue_id}".format(
            tenant_path=quote(str(tenant_path), safe=""),
            queue_id=quote(str(queue_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> OutputMySupportRequests | None:
    if response.status_code == 200:
        response_200 = OutputMySupportRequests.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[OutputMySupportRequests]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    tenant_path: str,
    queue_id: str,
    *,
    client: AuthenticatedClient,
    exclude_mode: bool | None | Unset = UNSET,
    search: None | str | Unset = UNSET,
    type_: None | str | Unset = UNSET,
    severity: None | str | Unset = UNSET,
    status: None | str | Unset = UNSET,
    queue: None | str | Unset = UNSET,
    customer: None | str | Unset = UNSET,
    project: None | str | Unset = UNSET,
    resource: None | str | Unset = UNSET,
    assignee: None | str | Unset = UNSET,
    requester: None | str | Unset = UNSET,
    has_assignee: bool | None | Unset = UNSET,
    created_from: datetime.date | None | Unset = UNSET,
    created_to: datetime.date | None | Unset = UNSET,
    updated_from: datetime.date | None | Unset = UNSET,
    updated_to: datetime.date | None | Unset = UNSET,
) -> Response[OutputMySupportRequests]:
    """Queue Internal Support Requests

     View active internal requests requiring attention in specific queue.
    Focus on open items needing resolution. Essential for queue teams
    to manage daily workload. Helps identify aging requests requiring
    escalation or additional resources.

    Args:
        tenant_path (str):
        queue_id (str):
        exclude_mode (bool | None | Unset): Invert filter logic to exclude matching results
        search (None | str | Unset): Search by title, description, or reference ID
        type_ (None | str | Unset): Filter by request type
        severity (None | str | Unset): Filter by severity
        status (None | str | Unset): Filter by status
        queue (None | str | Unset): Filter by queue
        customer (None | str | Unset): Filter by customer organization
        project (None | str | Unset): Filter by project
        resource (None | str | Unset): Filter by resource
        assignee (None | str | Unset): Filter by assigned team member
        requester (None | str | Unset): Filter by requester
        has_assignee (bool | None | Unset): Filter by assignment status
        created_from (datetime.date | None | Unset): Filter by creation date (from)
        created_to (datetime.date | None | Unset): Filter by creation date (to)
        updated_from (datetime.date | None | Unset): Filter by last update date (from)
        updated_to (datetime.date | None | Unset): Filter by last update date (to)

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OutputMySupportRequests]
    """

    kwargs = _get_kwargs(
        tenant_path=tenant_path,
        queue_id=queue_id,
        exclude_mode=exclude_mode,
        search=search,
        type_=type_,
        severity=severity,
        status=status,
        queue=queue,
        customer=customer,
        project=project,
        resource=resource,
        assignee=assignee,
        requester=requester,
        has_assignee=has_assignee,
        created_from=created_from,
        created_to=created_to,
        updated_from=updated_from,
        updated_to=updated_to,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    tenant_path: str,
    queue_id: str,
    *,
    client: AuthenticatedClient,
    exclude_mode: bool | None | Unset = UNSET,
    search: None | str | Unset = UNSET,
    type_: None | str | Unset = UNSET,
    severity: None | str | Unset = UNSET,
    status: None | str | Unset = UNSET,
    queue: None | str | Unset = UNSET,
    customer: None | str | Unset = UNSET,
    project: None | str | Unset = UNSET,
    resource: None | str | Unset = UNSET,
    assignee: None | str | Unset = UNSET,
    requester: None | str | Unset = UNSET,
    has_assignee: bool | None | Unset = UNSET,
    created_from: datetime.date | None | Unset = UNSET,
    created_to: datetime.date | None | Unset = UNSET,
    updated_from: datetime.date | None | Unset = UNSET,
    updated_to: datetime.date | None | Unset = UNSET,
) -> OutputMySupportRequests | None:
    """Queue Internal Support Requests

     View active internal requests requiring attention in specific queue.
    Focus on open items needing resolution. Essential for queue teams
    to manage daily workload. Helps identify aging requests requiring
    escalation or additional resources.

    Args:
        tenant_path (str):
        queue_id (str):
        exclude_mode (bool | None | Unset): Invert filter logic to exclude matching results
        search (None | str | Unset): Search by title, description, or reference ID
        type_ (None | str | Unset): Filter by request type
        severity (None | str | Unset): Filter by severity
        status (None | str | Unset): Filter by status
        queue (None | str | Unset): Filter by queue
        customer (None | str | Unset): Filter by customer organization
        project (None | str | Unset): Filter by project
        resource (None | str | Unset): Filter by resource
        assignee (None | str | Unset): Filter by assigned team member
        requester (None | str | Unset): Filter by requester
        has_assignee (bool | None | Unset): Filter by assignment status
        created_from (datetime.date | None | Unset): Filter by creation date (from)
        created_to (datetime.date | None | Unset): Filter by creation date (to)
        updated_from (datetime.date | None | Unset): Filter by last update date (from)
        updated_to (datetime.date | None | Unset): Filter by last update date (to)

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OutputMySupportRequests
    """

    return sync_detailed(
        tenant_path=tenant_path,
        queue_id=queue_id,
        client=client,
        exclude_mode=exclude_mode,
        search=search,
        type_=type_,
        severity=severity,
        status=status,
        queue=queue,
        customer=customer,
        project=project,
        resource=resource,
        assignee=assignee,
        requester=requester,
        has_assignee=has_assignee,
        created_from=created_from,
        created_to=created_to,
        updated_from=updated_from,
        updated_to=updated_to,
    ).parsed


async def asyncio_detailed(
    tenant_path: str,
    queue_id: str,
    *,
    client: AuthenticatedClient,
    exclude_mode: bool | None | Unset = UNSET,
    search: None | str | Unset = UNSET,
    type_: None | str | Unset = UNSET,
    severity: None | str | Unset = UNSET,
    status: None | str | Unset = UNSET,
    queue: None | str | Unset = UNSET,
    customer: None | str | Unset = UNSET,
    project: None | str | Unset = UNSET,
    resource: None | str | Unset = UNSET,
    assignee: None | str | Unset = UNSET,
    requester: None | str | Unset = UNSET,
    has_assignee: bool | None | Unset = UNSET,
    created_from: datetime.date | None | Unset = UNSET,
    created_to: datetime.date | None | Unset = UNSET,
    updated_from: datetime.date | None | Unset = UNSET,
    updated_to: datetime.date | None | Unset = UNSET,
) -> Response[OutputMySupportRequests]:
    """Queue Internal Support Requests

     View active internal requests requiring attention in specific queue.
    Focus on open items needing resolution. Essential for queue teams
    to manage daily workload. Helps identify aging requests requiring
    escalation or additional resources.

    Args:
        tenant_path (str):
        queue_id (str):
        exclude_mode (bool | None | Unset): Invert filter logic to exclude matching results
        search (None | str | Unset): Search by title, description, or reference ID
        type_ (None | str | Unset): Filter by request type
        severity (None | str | Unset): Filter by severity
        status (None | str | Unset): Filter by status
        queue (None | str | Unset): Filter by queue
        customer (None | str | Unset): Filter by customer organization
        project (None | str | Unset): Filter by project
        resource (None | str | Unset): Filter by resource
        assignee (None | str | Unset): Filter by assigned team member
        requester (None | str | Unset): Filter by requester
        has_assignee (bool | None | Unset): Filter by assignment status
        created_from (datetime.date | None | Unset): Filter by creation date (from)
        created_to (datetime.date | None | Unset): Filter by creation date (to)
        updated_from (datetime.date | None | Unset): Filter by last update date (from)
        updated_to (datetime.date | None | Unset): Filter by last update date (to)

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OutputMySupportRequests]
    """

    kwargs = _get_kwargs(
        tenant_path=tenant_path,
        queue_id=queue_id,
        exclude_mode=exclude_mode,
        search=search,
        type_=type_,
        severity=severity,
        status=status,
        queue=queue,
        customer=customer,
        project=project,
        resource=resource,
        assignee=assignee,
        requester=requester,
        has_assignee=has_assignee,
        created_from=created_from,
        created_to=created_to,
        updated_from=updated_from,
        updated_to=updated_to,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    tenant_path: str,
    queue_id: str,
    *,
    client: AuthenticatedClient,
    exclude_mode: bool | None | Unset = UNSET,
    search: None | str | Unset = UNSET,
    type_: None | str | Unset = UNSET,
    severity: None | str | Unset = UNSET,
    status: None | str | Unset = UNSET,
    queue: None | str | Unset = UNSET,
    customer: None | str | Unset = UNSET,
    project: None | str | Unset = UNSET,
    resource: None | str | Unset = UNSET,
    assignee: None | str | Unset = UNSET,
    requester: None | str | Unset = UNSET,
    has_assignee: bool | None | Unset = UNSET,
    created_from: datetime.date | None | Unset = UNSET,
    created_to: datetime.date | None | Unset = UNSET,
    updated_from: datetime.date | None | Unset = UNSET,
    updated_to: datetime.date | None | Unset = UNSET,
) -> OutputMySupportRequests | None:
    """Queue Internal Support Requests

     View active internal requests requiring attention in specific queue.
    Focus on open items needing resolution. Essential for queue teams
    to manage daily workload. Helps identify aging requests requiring
    escalation or additional resources.

    Args:
        tenant_path (str):
        queue_id (str):
        exclude_mode (bool | None | Unset): Invert filter logic to exclude matching results
        search (None | str | Unset): Search by title, description, or reference ID
        type_ (None | str | Unset): Filter by request type
        severity (None | str | Unset): Filter by severity
        status (None | str | Unset): Filter by status
        queue (None | str | Unset): Filter by queue
        customer (None | str | Unset): Filter by customer organization
        project (None | str | Unset): Filter by project
        resource (None | str | Unset): Filter by resource
        assignee (None | str | Unset): Filter by assigned team member
        requester (None | str | Unset): Filter by requester
        has_assignee (bool | None | Unset): Filter by assignment status
        created_from (datetime.date | None | Unset): Filter by creation date (from)
        created_to (datetime.date | None | Unset): Filter by creation date (to)
        updated_from (datetime.date | None | Unset): Filter by last update date (from)
        updated_to (datetime.date | None | Unset): Filter by last update date (to)

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OutputMySupportRequests
    """

    return (
        await asyncio_detailed(
            tenant_path=tenant_path,
            queue_id=queue_id,
            client=client,
            exclude_mode=exclude_mode,
            search=search,
            type_=type_,
            severity=severity,
            status=status,
            queue=queue,
            customer=customer,
            project=project,
            resource=resource,
            assignee=assignee,
            requester=requester,
            has_assignee=has_assignee,
            created_from=created_from,
            created_to=created_to,
            updated_from=updated_from,
            updated_to=updated_to,
        )
    ).parsed
