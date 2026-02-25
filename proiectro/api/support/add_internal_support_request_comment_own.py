from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.add_internal_support_request_comment import (
    AddInternalSupportRequestComment,
)
from ...models.api_response import APIResponse
from ...types import Response


def _get_kwargs(
    tenant_path: str,
    *,
    body: AddInternalSupportRequestComment,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/{tenant_path}/add_internal_support_request_comment_own".format(
            tenant_path=quote(str(tenant_path), safe=""),
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
    *,
    client: AuthenticatedClient,
    body: AddInternalSupportRequestComment,
) -> Response[APIResponse]:
    """Add Internal Support Request Comment Own

     Add clarifications or updates to your own support requests actively.
    Provide additional context discovered after submission. Respond to
    agent questions promptly to maintain momentum. Comments help build
    complete picture for effective resolution.

    Args:
        tenant_path (str):
        body (AddInternalSupportRequestComment): Input schema for adding a comment to an internal
            support request

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[APIResponse]
    """

    kwargs = _get_kwargs(
        tenant_path=tenant_path,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    tenant_path: str,
    *,
    client: AuthenticatedClient,
    body: AddInternalSupportRequestComment,
) -> APIResponse | None:
    """Add Internal Support Request Comment Own

     Add clarifications or updates to your own support requests actively.
    Provide additional context discovered after submission. Respond to
    agent questions promptly to maintain momentum. Comments help build
    complete picture for effective resolution.

    Args:
        tenant_path (str):
        body (AddInternalSupportRequestComment): Input schema for adding a comment to an internal
            support request

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        APIResponse
    """

    return sync_detailed(
        tenant_path=tenant_path,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    tenant_path: str,
    *,
    client: AuthenticatedClient,
    body: AddInternalSupportRequestComment,
) -> Response[APIResponse]:
    """Add Internal Support Request Comment Own

     Add clarifications or updates to your own support requests actively.
    Provide additional context discovered after submission. Respond to
    agent questions promptly to maintain momentum. Comments help build
    complete picture for effective resolution.

    Args:
        tenant_path (str):
        body (AddInternalSupportRequestComment): Input schema for adding a comment to an internal
            support request

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[APIResponse]
    """

    kwargs = _get_kwargs(
        tenant_path=tenant_path,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    tenant_path: str,
    *,
    client: AuthenticatedClient,
    body: AddInternalSupportRequestComment,
) -> APIResponse | None:
    """Add Internal Support Request Comment Own

     Add clarifications or updates to your own support requests actively.
    Provide additional context discovered after submission. Respond to
    agent questions promptly to maintain momentum. Comments help build
    complete picture for effective resolution.

    Args:
        tenant_path (str):
        body (AddInternalSupportRequestComment): Input schema for adding a comment to an internal
            support request

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        APIResponse
    """

    return (
        await asyncio_detailed(
            tenant_path=tenant_path,
            client=client,
            body=body,
        )
    ).parsed
