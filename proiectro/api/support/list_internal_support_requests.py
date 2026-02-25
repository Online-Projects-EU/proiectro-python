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
    *,
    customer_id: None | str | Unset = UNSET,
    project_id: None | str | Unset = UNSET,
    resource_id: None | str | Unset = UNSET,
    queue_id: None | str | Unset = UNSET,
    type_id: None | str | Unset = UNSET,
    severity_id: None | str | Unset = UNSET,
    status_id: None | str | Unset = UNSET,
    assignee_id: None | str | Unset = UNSET,
    requester_id: None | str | Unset = UNSET,
    my_requests: bool | Unset = False,
    assigned_to_me: bool | Unset = False,
    lifecycle_filter: None | str | Unset = UNSET,
    limit: int | Unset = 100,
    offset: int | Unset = 0,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_customer_id: None | str | Unset
    if isinstance(customer_id, Unset):
        json_customer_id = UNSET
    else:
        json_customer_id = customer_id
    params["customer_id"] = json_customer_id

    json_project_id: None | str | Unset
    if isinstance(project_id, Unset):
        json_project_id = UNSET
    else:
        json_project_id = project_id
    params["project_id"] = json_project_id

    json_resource_id: None | str | Unset
    if isinstance(resource_id, Unset):
        json_resource_id = UNSET
    else:
        json_resource_id = resource_id
    params["resource_id"] = json_resource_id

    json_queue_id: None | str | Unset
    if isinstance(queue_id, Unset):
        json_queue_id = UNSET
    else:
        json_queue_id = queue_id
    params["queue_id"] = json_queue_id

    json_type_id: None | str | Unset
    if isinstance(type_id, Unset):
        json_type_id = UNSET
    else:
        json_type_id = type_id
    params["type_id"] = json_type_id

    json_severity_id: None | str | Unset
    if isinstance(severity_id, Unset):
        json_severity_id = UNSET
    else:
        json_severity_id = severity_id
    params["severity_id"] = json_severity_id

    json_status_id: None | str | Unset
    if isinstance(status_id, Unset):
        json_status_id = UNSET
    else:
        json_status_id = status_id
    params["status_id"] = json_status_id

    json_assignee_id: None | str | Unset
    if isinstance(assignee_id, Unset):
        json_assignee_id = UNSET
    else:
        json_assignee_id = assignee_id
    params["assignee_id"] = json_assignee_id

    json_requester_id: None | str | Unset
    if isinstance(requester_id, Unset):
        json_requester_id = UNSET
    else:
        json_requester_id = requester_id
    params["requester_id"] = json_requester_id

    params["my_requests"] = my_requests

    params["assigned_to_me"] = assigned_to_me

    json_lifecycle_filter: None | str | Unset
    if isinstance(lifecycle_filter, Unset):
        json_lifecycle_filter = UNSET
    else:
        json_lifecycle_filter = lifecycle_filter
    params["lifecycle_filter"] = json_lifecycle_filter

    params["limit"] = limit

    params["offset"] = offset

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/{tenant_path}/internal_support_requests".format(
            tenant_path=quote(str(tenant_path), safe=""),
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
    *,
    client: AuthenticatedClient,
    customer_id: None | str | Unset = UNSET,
    project_id: None | str | Unset = UNSET,
    resource_id: None | str | Unset = UNSET,
    queue_id: None | str | Unset = UNSET,
    type_id: None | str | Unset = UNSET,
    severity_id: None | str | Unset = UNSET,
    status_id: None | str | Unset = UNSET,
    assignee_id: None | str | Unset = UNSET,
    requester_id: None | str | Unset = UNSET,
    my_requests: bool | Unset = False,
    assigned_to_me: bool | Unset = False,
    lifecycle_filter: None | str | Unset = UNSET,
    limit: int | Unset = 100,
    offset: int | Unset = 0,
) -> Response[OutputMySupportRequests]:
    """List Internal Support Requests

     Search and filter internal requests with multiple criteria combinations.
    Build custom views for different support roles and responsibilities.
    Powerful filtering enables workload analysis and trend identification.
    Use pagination for large result sets to maintain performance.

    Args:
        tenant_path (str):
        customer_id (None | str | Unset):
        project_id (None | str | Unset):
        resource_id (None | str | Unset):
        queue_id (None | str | Unset):
        type_id (None | str | Unset):
        severity_id (None | str | Unset):
        status_id (None | str | Unset):
        assignee_id (None | str | Unset):
        requester_id (None | str | Unset):
        my_requests (bool | Unset):  Default: False.
        assigned_to_me (bool | Unset):  Default: False.
        lifecycle_filter (None | str | Unset):
        limit (int | Unset):  Default: 100.
        offset (int | Unset):  Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OutputMySupportRequests]
    """

    kwargs = _get_kwargs(
        tenant_path=tenant_path,
        customer_id=customer_id,
        project_id=project_id,
        resource_id=resource_id,
        queue_id=queue_id,
        type_id=type_id,
        severity_id=severity_id,
        status_id=status_id,
        assignee_id=assignee_id,
        requester_id=requester_id,
        my_requests=my_requests,
        assigned_to_me=assigned_to_me,
        lifecycle_filter=lifecycle_filter,
        limit=limit,
        offset=offset,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    tenant_path: str,
    *,
    client: AuthenticatedClient,
    customer_id: None | str | Unset = UNSET,
    project_id: None | str | Unset = UNSET,
    resource_id: None | str | Unset = UNSET,
    queue_id: None | str | Unset = UNSET,
    type_id: None | str | Unset = UNSET,
    severity_id: None | str | Unset = UNSET,
    status_id: None | str | Unset = UNSET,
    assignee_id: None | str | Unset = UNSET,
    requester_id: None | str | Unset = UNSET,
    my_requests: bool | Unset = False,
    assigned_to_me: bool | Unset = False,
    lifecycle_filter: None | str | Unset = UNSET,
    limit: int | Unset = 100,
    offset: int | Unset = 0,
) -> OutputMySupportRequests | None:
    """List Internal Support Requests

     Search and filter internal requests with multiple criteria combinations.
    Build custom views for different support roles and responsibilities.
    Powerful filtering enables workload analysis and trend identification.
    Use pagination for large result sets to maintain performance.

    Args:
        tenant_path (str):
        customer_id (None | str | Unset):
        project_id (None | str | Unset):
        resource_id (None | str | Unset):
        queue_id (None | str | Unset):
        type_id (None | str | Unset):
        severity_id (None | str | Unset):
        status_id (None | str | Unset):
        assignee_id (None | str | Unset):
        requester_id (None | str | Unset):
        my_requests (bool | Unset):  Default: False.
        assigned_to_me (bool | Unset):  Default: False.
        lifecycle_filter (None | str | Unset):
        limit (int | Unset):  Default: 100.
        offset (int | Unset):  Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OutputMySupportRequests
    """

    return sync_detailed(
        tenant_path=tenant_path,
        client=client,
        customer_id=customer_id,
        project_id=project_id,
        resource_id=resource_id,
        queue_id=queue_id,
        type_id=type_id,
        severity_id=severity_id,
        status_id=status_id,
        assignee_id=assignee_id,
        requester_id=requester_id,
        my_requests=my_requests,
        assigned_to_me=assigned_to_me,
        lifecycle_filter=lifecycle_filter,
        limit=limit,
        offset=offset,
    ).parsed


async def asyncio_detailed(
    tenant_path: str,
    *,
    client: AuthenticatedClient,
    customer_id: None | str | Unset = UNSET,
    project_id: None | str | Unset = UNSET,
    resource_id: None | str | Unset = UNSET,
    queue_id: None | str | Unset = UNSET,
    type_id: None | str | Unset = UNSET,
    severity_id: None | str | Unset = UNSET,
    status_id: None | str | Unset = UNSET,
    assignee_id: None | str | Unset = UNSET,
    requester_id: None | str | Unset = UNSET,
    my_requests: bool | Unset = False,
    assigned_to_me: bool | Unset = False,
    lifecycle_filter: None | str | Unset = UNSET,
    limit: int | Unset = 100,
    offset: int | Unset = 0,
) -> Response[OutputMySupportRequests]:
    """List Internal Support Requests

     Search and filter internal requests with multiple criteria combinations.
    Build custom views for different support roles and responsibilities.
    Powerful filtering enables workload analysis and trend identification.
    Use pagination for large result sets to maintain performance.

    Args:
        tenant_path (str):
        customer_id (None | str | Unset):
        project_id (None | str | Unset):
        resource_id (None | str | Unset):
        queue_id (None | str | Unset):
        type_id (None | str | Unset):
        severity_id (None | str | Unset):
        status_id (None | str | Unset):
        assignee_id (None | str | Unset):
        requester_id (None | str | Unset):
        my_requests (bool | Unset):  Default: False.
        assigned_to_me (bool | Unset):  Default: False.
        lifecycle_filter (None | str | Unset):
        limit (int | Unset):  Default: 100.
        offset (int | Unset):  Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OutputMySupportRequests]
    """

    kwargs = _get_kwargs(
        tenant_path=tenant_path,
        customer_id=customer_id,
        project_id=project_id,
        resource_id=resource_id,
        queue_id=queue_id,
        type_id=type_id,
        severity_id=severity_id,
        status_id=status_id,
        assignee_id=assignee_id,
        requester_id=requester_id,
        my_requests=my_requests,
        assigned_to_me=assigned_to_me,
        lifecycle_filter=lifecycle_filter,
        limit=limit,
        offset=offset,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    tenant_path: str,
    *,
    client: AuthenticatedClient,
    customer_id: None | str | Unset = UNSET,
    project_id: None | str | Unset = UNSET,
    resource_id: None | str | Unset = UNSET,
    queue_id: None | str | Unset = UNSET,
    type_id: None | str | Unset = UNSET,
    severity_id: None | str | Unset = UNSET,
    status_id: None | str | Unset = UNSET,
    assignee_id: None | str | Unset = UNSET,
    requester_id: None | str | Unset = UNSET,
    my_requests: bool | Unset = False,
    assigned_to_me: bool | Unset = False,
    lifecycle_filter: None | str | Unset = UNSET,
    limit: int | Unset = 100,
    offset: int | Unset = 0,
) -> OutputMySupportRequests | None:
    """List Internal Support Requests

     Search and filter internal requests with multiple criteria combinations.
    Build custom views for different support roles and responsibilities.
    Powerful filtering enables workload analysis and trend identification.
    Use pagination for large result sets to maintain performance.

    Args:
        tenant_path (str):
        customer_id (None | str | Unset):
        project_id (None | str | Unset):
        resource_id (None | str | Unset):
        queue_id (None | str | Unset):
        type_id (None | str | Unset):
        severity_id (None | str | Unset):
        status_id (None | str | Unset):
        assignee_id (None | str | Unset):
        requester_id (None | str | Unset):
        my_requests (bool | Unset):  Default: False.
        assigned_to_me (bool | Unset):  Default: False.
        lifecycle_filter (None | str | Unset):
        limit (int | Unset):  Default: 100.
        offset (int | Unset):  Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OutputMySupportRequests
    """

    return (
        await asyncio_detailed(
            tenant_path=tenant_path,
            client=client,
            customer_id=customer_id,
            project_id=project_id,
            resource_id=resource_id,
            queue_id=queue_id,
            type_id=type_id,
            severity_id=severity_id,
            status_id=status_id,
            assignee_id=assignee_id,
            requester_id=requester_id,
            my_requests=my_requests,
            assigned_to_me=assigned_to_me,
            lifecycle_filter=lifecycle_filter,
            limit=limit,
            offset=offset,
        )
    ).parsed
