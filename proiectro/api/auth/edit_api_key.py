from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_response import APIResponse
from ...models.edit_api_key import EditApiKey
from ...types import Response


def _get_kwargs(
    tenant_path: str,
    api_key_id: str,
    *,
    body: EditApiKey,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/api/v1/{tenant_path}/edit_api_key/{api_key_id}".format(
            tenant_path=quote(str(tenant_path), safe=""),
            api_key_id=quote(str(api_key_id), safe=""),
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

    if response.status_code == 422:
        response_422 = APIResponse.from_dict(response.json())

        return response_422

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
    api_key_id: str,
    *,
    client: AuthenticatedClient,
    body: EditApiKey,
) -> Response[APIResponse]:
    """Edit Api Key

     Adjust API key permissions when integration requirements change. Reduce permissions
    to follow least-privilege principles or extend expiration for long-running projects.
    Changes take effect immediately for all systems using this key.

    Args:
        tenant_path (str):
        api_key_id (str):
        body (EditApiKey): Input schema for editing an API key

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[APIResponse]
    """

    kwargs = _get_kwargs(
        tenant_path=tenant_path,
        api_key_id=api_key_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    tenant_path: str,
    api_key_id: str,
    *,
    client: AuthenticatedClient,
    body: EditApiKey,
) -> APIResponse | None:
    """Edit Api Key

     Adjust API key permissions when integration requirements change. Reduce permissions
    to follow least-privilege principles or extend expiration for long-running projects.
    Changes take effect immediately for all systems using this key.

    Args:
        tenant_path (str):
        api_key_id (str):
        body (EditApiKey): Input schema for editing an API key

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        APIResponse
    """

    return sync_detailed(
        tenant_path=tenant_path,
        api_key_id=api_key_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    tenant_path: str,
    api_key_id: str,
    *,
    client: AuthenticatedClient,
    body: EditApiKey,
) -> Response[APIResponse]:
    """Edit Api Key

     Adjust API key permissions when integration requirements change. Reduce permissions
    to follow least-privilege principles or extend expiration for long-running projects.
    Changes take effect immediately for all systems using this key.

    Args:
        tenant_path (str):
        api_key_id (str):
        body (EditApiKey): Input schema for editing an API key

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[APIResponse]
    """

    kwargs = _get_kwargs(
        tenant_path=tenant_path,
        api_key_id=api_key_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    tenant_path: str,
    api_key_id: str,
    *,
    client: AuthenticatedClient,
    body: EditApiKey,
) -> APIResponse | None:
    """Edit Api Key

     Adjust API key permissions when integration requirements change. Reduce permissions
    to follow least-privilege principles or extend expiration for long-running projects.
    Changes take effect immediately for all systems using this key.

    Args:
        tenant_path (str):
        api_key_id (str):
        body (EditApiKey): Input schema for editing an API key

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        APIResponse
    """

    return (
        await asyncio_detailed(
            tenant_path=tenant_path,
            api_key_id=api_key_id,
            client=client,
            body=body,
        )
    ).parsed
