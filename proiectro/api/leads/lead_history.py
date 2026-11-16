from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.output_lead_history import OutputLeadHistory
from ...types import Response


def _get_kwargs(
    tenant_path: str,
    lead_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/{tenant_path}/lead_history/{lead_id}".format(
            tenant_path=quote(str(tenant_path), safe=""),
            lead_id=quote(str(lead_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> OutputLeadHistory | None:
    if response.status_code == 200:
        response_200 = OutputLeadHistory.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[OutputLeadHistory]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    tenant_path: str,
    lead_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[OutputLeadHistory]:
    """Lead History

     View the history of a lead as one timeline, newest first: every status it has been in, with
    when it entered and left, how long it stayed and who moved it, and every call, email, meeting
    and note logged on it in between. Shows the reason recorded when the lead was closed, and marks
    changes made through an API key or a connected app. Essential for seeing where leads wait and
    which contact moved them forward.

    Args:
        tenant_path (str):
        lead_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OutputLeadHistory]
    """

    kwargs = _get_kwargs(
        tenant_path=tenant_path,
        lead_id=lead_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    tenant_path: str,
    lead_id: str,
    *,
    client: AuthenticatedClient,
) -> OutputLeadHistory | None:
    """Lead History

     View the history of a lead as one timeline, newest first: every status it has been in, with
    when it entered and left, how long it stayed and who moved it, and every call, email, meeting
    and note logged on it in between. Shows the reason recorded when the lead was closed, and marks
    changes made through an API key or a connected app. Essential for seeing where leads wait and
    which contact moved them forward.

    Args:
        tenant_path (str):
        lead_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OutputLeadHistory
    """

    return sync_detailed(
        tenant_path=tenant_path,
        lead_id=lead_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    tenant_path: str,
    lead_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[OutputLeadHistory]:
    """Lead History

     View the history of a lead as one timeline, newest first: every status it has been in, with
    when it entered and left, how long it stayed and who moved it, and every call, email, meeting
    and note logged on it in between. Shows the reason recorded when the lead was closed, and marks
    changes made through an API key or a connected app. Essential for seeing where leads wait and
    which contact moved them forward.

    Args:
        tenant_path (str):
        lead_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OutputLeadHistory]
    """

    kwargs = _get_kwargs(
        tenant_path=tenant_path,
        lead_id=lead_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    tenant_path: str,
    lead_id: str,
    *,
    client: AuthenticatedClient,
) -> OutputLeadHistory | None:
    """Lead History

     View the history of a lead as one timeline, newest first: every status it has been in, with
    when it entered and left, how long it stayed and who moved it, and every call, email, meeting
    and note logged on it in between. Shows the reason recorded when the lead was closed, and marks
    changes made through an API key or a connected app. Essential for seeing where leads wait and
    which contact moved them forward.

    Args:
        tenant_path (str):
        lead_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OutputLeadHistory
    """

    return (
        await asyncio_detailed(
            tenant_path=tenant_path,
            lead_id=lead_id,
            client=client,
        )
    ).parsed
