from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.output_internal_support_request import OutputInternalSupportRequest
from ...types import Response


def _get_kwargs(
    tenant_path: str,
    support_request_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/{tenant_path}/my_support_request/{support_request_id}".format(
            tenant_path=quote(str(tenant_path), safe=""),
            support_request_id=quote(str(support_request_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> OutputInternalSupportRequest | None:
    if response.status_code == 200:
        response_200 = OutputInternalSupportRequest.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[OutputInternalSupportRequest]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    tenant_path: str,
    support_request_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[OutputInternalSupportRequest]:
    """My Support Request

     View detailed status of your submitted request with full context.
    Track progress, see agent notes, and understand next steps.
    Real-time updates show latest changes. Essential for following
    up on critical issues affecting your work.

    Args:
        tenant_path (str):
        support_request_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OutputInternalSupportRequest]
    """

    kwargs = _get_kwargs(
        tenant_path=tenant_path,
        support_request_id=support_request_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    tenant_path: str,
    support_request_id: str,
    *,
    client: AuthenticatedClient,
) -> OutputInternalSupportRequest | None:
    """My Support Request

     View detailed status of your submitted request with full context.
    Track progress, see agent notes, and understand next steps.
    Real-time updates show latest changes. Essential for following
    up on critical issues affecting your work.

    Args:
        tenant_path (str):
        support_request_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OutputInternalSupportRequest
    """

    return sync_detailed(
        tenant_path=tenant_path,
        support_request_id=support_request_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    tenant_path: str,
    support_request_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[OutputInternalSupportRequest]:
    """My Support Request

     View detailed status of your submitted request with full context.
    Track progress, see agent notes, and understand next steps.
    Real-time updates show latest changes. Essential for following
    up on critical issues affecting your work.

    Args:
        tenant_path (str):
        support_request_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OutputInternalSupportRequest]
    """

    kwargs = _get_kwargs(
        tenant_path=tenant_path,
        support_request_id=support_request_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    tenant_path: str,
    support_request_id: str,
    *,
    client: AuthenticatedClient,
) -> OutputInternalSupportRequest | None:
    """My Support Request

     View detailed status of your submitted request with full context.
    Track progress, see agent notes, and understand next steps.
    Real-time updates show latest changes. Essential for following
    up on critical issues affecting your work.

    Args:
        tenant_path (str):
        support_request_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OutputInternalSupportRequest
    """

    return (
        await asyncio_detailed(
            tenant_path=tenant_path,
            support_request_id=support_request_id,
            client=client,
        )
    ).parsed
