from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.output_support_request_type import OutputSupportRequestType
from ...types import Response


def _get_kwargs(
    tenant_path: str,
    type_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/{tenant_path}/support_request_type/{type_id}".format(
            tenant_path=quote(str(tenant_path), safe=""),
            type_id=quote(str(type_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> OutputSupportRequestType | None:
    if response.status_code == 200:
        response_200 = OutputSupportRequestType.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[OutputSupportRequestType]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    tenant_path: str,
    type_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[OutputSupportRequestType]:
    """Get Support Request Type

     Examine detailed configuration of a specific request type including routing rules.
    Shows associated queues, default assignments, and escalation paths.
    Critical for understanding how requests of this type will be handled.

    Args:
        tenant_path (str):
        type_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OutputSupportRequestType]
    """

    kwargs = _get_kwargs(
        tenant_path=tenant_path,
        type_id=type_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    tenant_path: str,
    type_id: str,
    *,
    client: AuthenticatedClient,
) -> OutputSupportRequestType | None:
    """Get Support Request Type

     Examine detailed configuration of a specific request type including routing rules.
    Shows associated queues, default assignments, and escalation paths.
    Critical for understanding how requests of this type will be handled.

    Args:
        tenant_path (str):
        type_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OutputSupportRequestType
    """

    return sync_detailed(
        tenant_path=tenant_path,
        type_id=type_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    tenant_path: str,
    type_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[OutputSupportRequestType]:
    """Get Support Request Type

     Examine detailed configuration of a specific request type including routing rules.
    Shows associated queues, default assignments, and escalation paths.
    Critical for understanding how requests of this type will be handled.

    Args:
        tenant_path (str):
        type_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OutputSupportRequestType]
    """

    kwargs = _get_kwargs(
        tenant_path=tenant_path,
        type_id=type_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    tenant_path: str,
    type_id: str,
    *,
    client: AuthenticatedClient,
) -> OutputSupportRequestType | None:
    """Get Support Request Type

     Examine detailed configuration of a specific request type including routing rules.
    Shows associated queues, default assignments, and escalation paths.
    Critical for understanding how requests of this type will be handled.

    Args:
        tenant_path (str):
        type_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OutputSupportRequestType
    """

    return (
        await asyncio_detailed(
            tenant_path=tenant_path,
            type_id=type_id,
            client=client,
        )
    ).parsed
