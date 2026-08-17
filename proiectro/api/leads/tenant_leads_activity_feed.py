from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.sales_activity_feed import SalesActivityFeed
from ...types import Response


def _get_kwargs(
    tenant_path: str,
    page_number: int,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/{tenant_path}/leads_activity_feed/{page_number}".format(
            tenant_path=quote(str(tenant_path), safe=""),
            page_number=quote(str(page_number), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> SalesActivityFeed | None:
    if response.status_code == 200:
        response_200 = SalesActivityFeed.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[SalesActivityFeed]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    tenant_path: str,
    page_number: int,
    *,
    client: AuthenticatedClient,
) -> Response[SalesActivityFeed]:
    """Tenant Leads Activity Feed

     View a unified stream of every recent sales touch across all your leads in one place.
    Calls, emails, meetings, and notes appear newest first with the rep who logged them
    and the lead they relate to. Essential for managers who want a pulse on team activity,
    catch stalled outreach, and surface coaching moments without opening each lead.

    Args:
        tenant_path (str):
        page_number (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SalesActivityFeed]
    """

    kwargs = _get_kwargs(
        tenant_path=tenant_path,
        page_number=page_number,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    tenant_path: str,
    page_number: int,
    *,
    client: AuthenticatedClient,
) -> SalesActivityFeed | None:
    """Tenant Leads Activity Feed

     View a unified stream of every recent sales touch across all your leads in one place.
    Calls, emails, meetings, and notes appear newest first with the rep who logged them
    and the lead they relate to. Essential for managers who want a pulse on team activity,
    catch stalled outreach, and surface coaching moments without opening each lead.

    Args:
        tenant_path (str):
        page_number (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SalesActivityFeed
    """

    return sync_detailed(
        tenant_path=tenant_path,
        page_number=page_number,
        client=client,
    ).parsed


async def asyncio_detailed(
    tenant_path: str,
    page_number: int,
    *,
    client: AuthenticatedClient,
) -> Response[SalesActivityFeed]:
    """Tenant Leads Activity Feed

     View a unified stream of every recent sales touch across all your leads in one place.
    Calls, emails, meetings, and notes appear newest first with the rep who logged them
    and the lead they relate to. Essential for managers who want a pulse on team activity,
    catch stalled outreach, and surface coaching moments without opening each lead.

    Args:
        tenant_path (str):
        page_number (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SalesActivityFeed]
    """

    kwargs = _get_kwargs(
        tenant_path=tenant_path,
        page_number=page_number,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    tenant_path: str,
    page_number: int,
    *,
    client: AuthenticatedClient,
) -> SalesActivityFeed | None:
    """Tenant Leads Activity Feed

     View a unified stream of every recent sales touch across all your leads in one place.
    Calls, emails, meetings, and notes appear newest first with the rep who logged them
    and the lead they relate to. Essential for managers who want a pulse on team activity,
    catch stalled outreach, and surface coaching moments without opening each lead.

    Args:
        tenant_path (str):
        page_number (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SalesActivityFeed
    """

    return (
        await asyncio_detailed(
            tenant_path=tenant_path,
            page_number=page_number,
            client=client,
        )
    ).parsed
