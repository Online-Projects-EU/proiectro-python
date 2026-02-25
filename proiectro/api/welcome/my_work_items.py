from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.output_my_work_items import OutputMyWorkItems
from ...types import Response


def _get_kwargs() -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/my_work_items",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> OutputMyWorkItems | None:
    if response.status_code == 200:
        response_200 = OutputMyWorkItems.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[OutputMyWorkItems]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[OutputMyWorkItems]:
    """My Work Items

     Retrieve all unfinished work items assigned to the current user across all
    workspaces. Items are grouped by urgency: overdue, due today, due this week,
    upcoming, and no date. Each item includes tenant and project context for
    cross-workspace navigation.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OutputMyWorkItems]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
) -> OutputMyWorkItems | None:
    """My Work Items

     Retrieve all unfinished work items assigned to the current user across all
    workspaces. Items are grouped by urgency: overdue, due today, due this week,
    upcoming, and no date. Each item includes tenant and project context for
    cross-workspace navigation.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OutputMyWorkItems
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[OutputMyWorkItems]:
    """My Work Items

     Retrieve all unfinished work items assigned to the current user across all
    workspaces. Items are grouped by urgency: overdue, due today, due this week,
    upcoming, and no date. Each item includes tenant and project context for
    cross-workspace navigation.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OutputMyWorkItems]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
) -> OutputMyWorkItems | None:
    """My Work Items

     Retrieve all unfinished work items assigned to the current user across all
    workspaces. Items are grouped by urgency: overdue, due today, due this week,
    upcoming, and no date. Each item includes tenant and project context for
    cross-workspace navigation.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OutputMyWorkItems
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
