from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_response import APIResponse
from ...models.update_project_wbs import UpdateProjectWBS
from ...types import Response


def _get_kwargs(
    tenant_path: str,
    project_id: str,
    *,
    body: UpdateProjectWBS,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/api/v1/{tenant_path}/update_project_wbs/{project_id}".format(
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
) -> APIResponse | None:
    if response.status_code == 200:
        response_200 = APIResponse.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = APIResponse.from_dict(response.json())

        return response_400

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[APIResponse]:
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
    body: UpdateProjectWBS,
) -> Response[APIResponse]:
    """Update Project Wbs

     Update the WBS configuration for a project.
    Sets or changes the Work Breakdown Structure template used for the project.

    Args:
        tenant_path (str):
        project_id (str):
        body (UpdateProjectWBS): Input schema for updating a project's WBS configuration

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[APIResponse]
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
    body: UpdateProjectWBS,
) -> APIResponse | None:
    """Update Project Wbs

     Update the WBS configuration for a project.
    Sets or changes the Work Breakdown Structure template used for the project.

    Args:
        tenant_path (str):
        project_id (str):
        body (UpdateProjectWBS): Input schema for updating a project's WBS configuration

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        APIResponse
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
    body: UpdateProjectWBS,
) -> Response[APIResponse]:
    """Update Project Wbs

     Update the WBS configuration for a project.
    Sets or changes the Work Breakdown Structure template used for the project.

    Args:
        tenant_path (str):
        project_id (str):
        body (UpdateProjectWBS): Input schema for updating a project's WBS configuration

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[APIResponse]
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
    body: UpdateProjectWBS,
) -> APIResponse | None:
    """Update Project Wbs

     Update the WBS configuration for a project.
    Sets or changes the Work Breakdown Structure template used for the project.

    Args:
        tenant_path (str):
        project_id (str):
        body (UpdateProjectWBS): Input schema for updating a project's WBS configuration

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        APIResponse
    """

    return (
        await asyncio_detailed(
            tenant_path=tenant_path,
            project_id=project_id,
            client=client,
            body=body,
        )
    ).parsed
