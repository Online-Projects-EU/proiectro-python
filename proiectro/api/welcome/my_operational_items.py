from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.output_my_operational_items import OutputMyOperationalItems
from ...types import Response


def _get_kwargs() -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/my_operational_items",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> OutputMyOperationalItems | None:
    if response.status_code == 200:
        response_200 = OutputMyOperationalItems.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[OutputMyOperationalItems]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[OutputMyOperationalItems]:
    """My Operational Items

     Retrieve operational work items relevant to the current user across all
    workspaces. Items are grouped into approvals (awaiting user's review),
    pending approval (user's items at approval stages), and active tasks
    (user's items at non-approval stages). Only includes items from processes
    where the user has participation.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OutputMyOperationalItems]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
) -> OutputMyOperationalItems | None:
    """My Operational Items

     Retrieve operational work items relevant to the current user across all
    workspaces. Items are grouped into approvals (awaiting user's review),
    pending approval (user's items at approval stages), and active tasks
    (user's items at non-approval stages). Only includes items from processes
    where the user has participation.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OutputMyOperationalItems
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[OutputMyOperationalItems]:
    """My Operational Items

     Retrieve operational work items relevant to the current user across all
    workspaces. Items are grouped into approvals (awaiting user's review),
    pending approval (user's items at approval stages), and active tasks
    (user's items at non-approval stages). Only includes items from processes
    where the user has participation.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OutputMyOperationalItems]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
) -> OutputMyOperationalItems | None:
    """My Operational Items

     Retrieve operational work items relevant to the current user across all
    workspaces. Items are grouped into approvals (awaiting user's review),
    pending approval (user's items at approval stages), and active tasks
    (user's items at non-approval stages). Only includes items from processes
    where the user has participation.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OutputMyOperationalItems
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
