from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_response import APIResponse
from ...models.edit_resource import EditResource
from ...types import Response


def _get_kwargs(
    tenant_path: str,
    resource_id: str,
    *,
    body: EditResource,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/api/v1/{tenant_path}/edit_resource/{resource_id}".format(
            tenant_path=quote(str(tenant_path), safe=""),
            resource_id=quote(str(resource_id), safe=""),
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
    resource_id: str,
    *,
    client: AuthenticatedClient,
    body: EditResource,
) -> Response[APIResponse]:
    """Edit Resource

     Update resource details when capabilities, availability, or organizational structure
    changes. Modifications apply to future allocations while preserving historical data.
    Changes to parent relationships reorganize your resource hierarchy. Review dependent
    proposals and projects before making structural changes.

    Args:
        tenant_path (str):
        resource_id (str):
        body (EditResource):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[APIResponse]
    """

    kwargs = _get_kwargs(
        tenant_path=tenant_path,
        resource_id=resource_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    tenant_path: str,
    resource_id: str,
    *,
    client: AuthenticatedClient,
    body: EditResource,
) -> APIResponse | None:
    """Edit Resource

     Update resource details when capabilities, availability, or organizational structure
    changes. Modifications apply to future allocations while preserving historical data.
    Changes to parent relationships reorganize your resource hierarchy. Review dependent
    proposals and projects before making structural changes.

    Args:
        tenant_path (str):
        resource_id (str):
        body (EditResource):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        APIResponse
    """

    return sync_detailed(
        tenant_path=tenant_path,
        resource_id=resource_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    tenant_path: str,
    resource_id: str,
    *,
    client: AuthenticatedClient,
    body: EditResource,
) -> Response[APIResponse]:
    """Edit Resource

     Update resource details when capabilities, availability, or organizational structure
    changes. Modifications apply to future allocations while preserving historical data.
    Changes to parent relationships reorganize your resource hierarchy. Review dependent
    proposals and projects before making structural changes.

    Args:
        tenant_path (str):
        resource_id (str):
        body (EditResource):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[APIResponse]
    """

    kwargs = _get_kwargs(
        tenant_path=tenant_path,
        resource_id=resource_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    tenant_path: str,
    resource_id: str,
    *,
    client: AuthenticatedClient,
    body: EditResource,
) -> APIResponse | None:
    """Edit Resource

     Update resource details when capabilities, availability, or organizational structure
    changes. Modifications apply to future allocations while preserving historical data.
    Changes to parent relationships reorganize your resource hierarchy. Review dependent
    proposals and projects before making structural changes.

    Args:
        tenant_path (str):
        resource_id (str):
        body (EditResource):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        APIResponse
    """

    return (
        await asyncio_detailed(
            tenant_path=tenant_path,
            resource_id=resource_id,
            client=client,
            body=body,
        )
    ).parsed
