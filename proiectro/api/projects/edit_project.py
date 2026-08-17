from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_response import APIResponse
from ...models.edit_project import EditProject
from ...models.edit_project_response import EditProjectResponse
from ...types import Response


def _get_kwargs(
    tenant_path: str,
    project_id: str,
    *,
    body: EditProject,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/api/v1/{tenant_path}/edit_project/{project_id}".format(
            tenant_path=quote(str(tenant_path), safe=""),
            project_id=quote(str(project_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> APIResponse | EditProjectResponse | None:
    if response.status_code == 200:
        response_200 = APIResponse.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = APIResponse.from_dict(response.json())

        return response_400

    if response.status_code == 404:
        response_404 = APIResponse.from_dict(response.json())

        return response_404

    if response.status_code == 409:
        response_409 = APIResponse.from_dict(response.json())

        return response_409

    if response.status_code == 422:
        response_422 = EditProjectResponse.from_dict(response.json())

        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[APIResponse | EditProjectResponse]:
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
    body: EditProject,
) -> Response[APIResponse | EditProjectResponse]:
    """Edit Project

     Update a live project's name, description, internal code, manager, dates, and
    capability toggles as delivery proceeds. Disabling a capability with attached
    data is refused with the reason. Commercial terms set when the proposal was won
    are not editable here.

    Args:
        tenant_path (str):
        project_id (str):
        body (EditProject):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[APIResponse | EditProjectResponse]
    """

    kwargs = _get_kwargs(
        tenant_path=tenant_path,
        project_id=project_id,
        body=body,
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
    body: EditProject,
) -> APIResponse | EditProjectResponse | None:
    """Edit Project

     Update a live project's name, description, internal code, manager, dates, and
    capability toggles as delivery proceeds. Disabling a capability with attached
    data is refused with the reason. Commercial terms set when the proposal was won
    are not editable here.

    Args:
        tenant_path (str):
        project_id (str):
        body (EditProject):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        APIResponse | EditProjectResponse
    """

    return sync_detailed(
        tenant_path=tenant_path,
        project_id=project_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    tenant_path: str,
    project_id: str,
    *,
    client: AuthenticatedClient,
    body: EditProject,
) -> Response[APIResponse | EditProjectResponse]:
    """Edit Project

     Update a live project's name, description, internal code, manager, dates, and
    capability toggles as delivery proceeds. Disabling a capability with attached
    data is refused with the reason. Commercial terms set when the proposal was won
    are not editable here.

    Args:
        tenant_path (str):
        project_id (str):
        body (EditProject):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[APIResponse | EditProjectResponse]
    """

    kwargs = _get_kwargs(
        tenant_path=tenant_path,
        project_id=project_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    tenant_path: str,
    project_id: str,
    *,
    client: AuthenticatedClient,
    body: EditProject,
) -> APIResponse | EditProjectResponse | None:
    """Edit Project

     Update a live project's name, description, internal code, manager, dates, and
    capability toggles as delivery proceeds. Disabling a capability with attached
    data is refused with the reason. Commercial terms set when the proposal was won
    are not editable here.

    Args:
        tenant_path (str):
        project_id (str):
        body (EditProject):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        APIResponse | EditProjectResponse
    """

    return (
        await asyncio_detailed(
            tenant_path=tenant_path,
            project_id=project_id,
            client=client,
            body=body,
        )
    ).parsed
