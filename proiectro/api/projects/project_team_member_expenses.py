from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.work_item_expenses_output import WorkItemExpensesOutput
from ...types import Response


def _get_kwargs(
    tenant_path: str,
    project_id: str,
    member_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/{tenant_path}/project_team_member_expenses/{project_id}/{member_id}".format(
            tenant_path=quote(str(tenant_path), safe=""),
            project_id=quote(str(project_id), safe=""),
            member_id=quote(str(member_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> WorkItemExpensesOutput | None:
    if response.status_code == 200:
        response_200 = WorkItemExpensesOutput.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[WorkItemExpensesOutput]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    tenant_path: str,
    project_id: str,
    member_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[WorkItemExpensesOutput]:
    """Project Team Member Expenses

     List all actual expenses created by a specific team member in a project.
    Shows real spending that the team member recorded for budget tracking.

    Args:
        tenant_path (str):
        project_id (str):
        member_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[WorkItemExpensesOutput]
    """

    kwargs = _get_kwargs(
        tenant_path=tenant_path,
        project_id=project_id,
        member_id=member_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    tenant_path: str,
    project_id: str,
    member_id: str,
    *,
    client: AuthenticatedClient,
) -> WorkItemExpensesOutput | None:
    """Project Team Member Expenses

     List all actual expenses created by a specific team member in a project.
    Shows real spending that the team member recorded for budget tracking.

    Args:
        tenant_path (str):
        project_id (str):
        member_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        WorkItemExpensesOutput
    """

    return sync_detailed(
        tenant_path=tenant_path,
        project_id=project_id,
        member_id=member_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    tenant_path: str,
    project_id: str,
    member_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[WorkItemExpensesOutput]:
    """Project Team Member Expenses

     List all actual expenses created by a specific team member in a project.
    Shows real spending that the team member recorded for budget tracking.

    Args:
        tenant_path (str):
        project_id (str):
        member_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[WorkItemExpensesOutput]
    """

    kwargs = _get_kwargs(
        tenant_path=tenant_path,
        project_id=project_id,
        member_id=member_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    tenant_path: str,
    project_id: str,
    member_id: str,
    *,
    client: AuthenticatedClient,
) -> WorkItemExpensesOutput | None:
    """Project Team Member Expenses

     List all actual expenses created by a specific team member in a project.
    Shows real spending that the team member recorded for budget tracking.

    Args:
        tenant_path (str):
        project_id (str):
        member_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        WorkItemExpensesOutput
    """

    return (
        await asyncio_detailed(
            tenant_path=tenant_path,
            project_id=project_id,
            member_id=member_id,
            client=client,
        )
    ).parsed
