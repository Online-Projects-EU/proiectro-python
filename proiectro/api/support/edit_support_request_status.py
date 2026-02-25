from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_response import APIResponse
from ...models.edit_support_request_status import EditSupportRequestStatus
from ...models.edit_support_request_status_response import (
    EditSupportRequestStatusResponse,
)
from ...types import Response


def _get_kwargs(
    tenant_path: str,
    status_id: str,
    *,
    body: EditSupportRequestStatus,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/api/v1/{tenant_path}/edit_support_request_status/{status_id}".format(
            tenant_path=quote(str(tenant_path), safe=""),
            status_id=quote(str(status_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> APIResponse | EditSupportRequestStatusResponse | None:
    if response.status_code == 200:
        response_200 = APIResponse.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = APIResponse.from_dict(response.json())

        return response_400

    if response.status_code == 422:
        response_422 = EditSupportRequestStatusResponse.from_dict(response.json())

        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[APIResponse | EditSupportRequestStatusResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    tenant_path: str,
    status_id: str,
    *,
    client: AuthenticatedClient,
    body: EditSupportRequestStatus,
) -> Response[APIResponse | EditSupportRequestStatusResponse]:
    """Edit Support Request Status

     Refine status definitions when processes mature or requirements change.
    Update descriptions, lifecycle indicators, or notification rules.
    Cannot change core lifecycle position if requests use this status.
    Communicate workflow changes to support teams.

    Args:
        tenant_path (str):
        status_id (str):
        body (EditSupportRequestStatus): Input schema for editing a support request status

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[APIResponse | EditSupportRequestStatusResponse]
    """

    kwargs = _get_kwargs(
        tenant_path=tenant_path,
        status_id=status_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    tenant_path: str,
    status_id: str,
    *,
    client: AuthenticatedClient,
    body: EditSupportRequestStatus,
) -> APIResponse | EditSupportRequestStatusResponse | None:
    """Edit Support Request Status

     Refine status definitions when processes mature or requirements change.
    Update descriptions, lifecycle indicators, or notification rules.
    Cannot change core lifecycle position if requests use this status.
    Communicate workflow changes to support teams.

    Args:
        tenant_path (str):
        status_id (str):
        body (EditSupportRequestStatus): Input schema for editing a support request status

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        APIResponse | EditSupportRequestStatusResponse
    """

    return sync_detailed(
        tenant_path=tenant_path,
        status_id=status_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    tenant_path: str,
    status_id: str,
    *,
    client: AuthenticatedClient,
    body: EditSupportRequestStatus,
) -> Response[APIResponse | EditSupportRequestStatusResponse]:
    """Edit Support Request Status

     Refine status definitions when processes mature or requirements change.
    Update descriptions, lifecycle indicators, or notification rules.
    Cannot change core lifecycle position if requests use this status.
    Communicate workflow changes to support teams.

    Args:
        tenant_path (str):
        status_id (str):
        body (EditSupportRequestStatus): Input schema for editing a support request status

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[APIResponse | EditSupportRequestStatusResponse]
    """

    kwargs = _get_kwargs(
        tenant_path=tenant_path,
        status_id=status_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    tenant_path: str,
    status_id: str,
    *,
    client: AuthenticatedClient,
    body: EditSupportRequestStatus,
) -> APIResponse | EditSupportRequestStatusResponse | None:
    """Edit Support Request Status

     Refine status definitions when processes mature or requirements change.
    Update descriptions, lifecycle indicators, or notification rules.
    Cannot change core lifecycle position if requests use this status.
    Communicate workflow changes to support teams.

    Args:
        tenant_path (str):
        status_id (str):
        body (EditSupportRequestStatus): Input schema for editing a support request status

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        APIResponse | EditSupportRequestStatusResponse
    """

    return (
        await asyncio_detailed(
            tenant_path=tenant_path,
            status_id=status_id,
            client=client,
            body=body,
        )
    ).parsed
