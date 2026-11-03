import datetime
from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_response import APIResponse
from ...models.output_sent_messages import OutputSentMessages
from ...types import UNSET, Response, Unset


def _get_kwargs(
    tenant_path: str,
    kind: str,
    *,
    recipient: None | str | Unset = UNSET,
    record: None | str | Unset = UNSET,
    since: datetime.date | None | Unset = UNSET,
    until: datetime.date | None | Unset = UNSET,
    page: int | Unset = 1,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_recipient: None | str | Unset
    if isinstance(recipient, Unset):
        json_recipient = UNSET
    else:
        json_recipient = recipient
    params["recipient"] = json_recipient

    json_record: None | str | Unset
    if isinstance(record, Unset):
        json_record = UNSET
    else:
        json_record = record
    params["record"] = json_record

    json_since: None | str | Unset
    if isinstance(since, Unset):
        json_since = UNSET
    elif isinstance(since, datetime.date):
        json_since = since.isoformat()
    else:
        json_since = since
    params["since"] = json_since

    json_until: None | str | Unset
    if isinstance(until, Unset):
        json_until = UNSET
    elif isinstance(until, datetime.date):
        json_until = until.isoformat()
    else:
        json_until = until
    params["until"] = json_until

    params["page"] = page

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/{tenant_path}/messages_list/{kind}".format(
            tenant_path=quote(str(tenant_path), safe=""),
            kind=quote(str(kind), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> APIResponse | OutputSentMessages | None:
    if response.status_code == 200:
        response_200 = OutputSentMessages.from_dict(response.json())

        return response_200

    if response.status_code == 404:
        response_404 = APIResponse.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[APIResponse | OutputSentMessages]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    tenant_path: str,
    kind: str,
    *,
    client: AuthenticatedClient,
    recipient: None | str | Unset = UNSET,
    record: None | str | Unset = UNSET,
    since: datetime.date | None | Unset = UNSET,
    until: datetime.date | None | Unset = UNSET,
    page: int | Unset = 1,
) -> Response[APIResponse | OutputSentMessages]:
    """Tenant Messages List

     List the emails (`email`) or chat messages (`chat_message`) the workspace sent, newest first,
    narrowed by recipient, record and date.

    Args:
        tenant_path (str):
        kind (str):
        recipient (None | str | Unset):
        record (None | str | Unset):
        since (datetime.date | None | Unset):
        until (datetime.date | None | Unset):
        page (int | Unset):  Default: 1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[APIResponse | OutputSentMessages]
    """

    kwargs = _get_kwargs(
        tenant_path=tenant_path,
        kind=kind,
        recipient=recipient,
        record=record,
        since=since,
        until=until,
        page=page,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    tenant_path: str,
    kind: str,
    *,
    client: AuthenticatedClient,
    recipient: None | str | Unset = UNSET,
    record: None | str | Unset = UNSET,
    since: datetime.date | None | Unset = UNSET,
    until: datetime.date | None | Unset = UNSET,
    page: int | Unset = 1,
) -> APIResponse | OutputSentMessages | None:
    """Tenant Messages List

     List the emails (`email`) or chat messages (`chat_message`) the workspace sent, newest first,
    narrowed by recipient, record and date.

    Args:
        tenant_path (str):
        kind (str):
        recipient (None | str | Unset):
        record (None | str | Unset):
        since (datetime.date | None | Unset):
        until (datetime.date | None | Unset):
        page (int | Unset):  Default: 1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        APIResponse | OutputSentMessages
    """

    return sync_detailed(
        tenant_path=tenant_path,
        kind=kind,
        client=client,
        recipient=recipient,
        record=record,
        since=since,
        until=until,
        page=page,
    ).parsed


async def asyncio_detailed(
    tenant_path: str,
    kind: str,
    *,
    client: AuthenticatedClient,
    recipient: None | str | Unset = UNSET,
    record: None | str | Unset = UNSET,
    since: datetime.date | None | Unset = UNSET,
    until: datetime.date | None | Unset = UNSET,
    page: int | Unset = 1,
) -> Response[APIResponse | OutputSentMessages]:
    """Tenant Messages List

     List the emails (`email`) or chat messages (`chat_message`) the workspace sent, newest first,
    narrowed by recipient, record and date.

    Args:
        tenant_path (str):
        kind (str):
        recipient (None | str | Unset):
        record (None | str | Unset):
        since (datetime.date | None | Unset):
        until (datetime.date | None | Unset):
        page (int | Unset):  Default: 1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[APIResponse | OutputSentMessages]
    """

    kwargs = _get_kwargs(
        tenant_path=tenant_path,
        kind=kind,
        recipient=recipient,
        record=record,
        since=since,
        until=until,
        page=page,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    tenant_path: str,
    kind: str,
    *,
    client: AuthenticatedClient,
    recipient: None | str | Unset = UNSET,
    record: None | str | Unset = UNSET,
    since: datetime.date | None | Unset = UNSET,
    until: datetime.date | None | Unset = UNSET,
    page: int | Unset = 1,
) -> APIResponse | OutputSentMessages | None:
    """Tenant Messages List

     List the emails (`email`) or chat messages (`chat_message`) the workspace sent, newest first,
    narrowed by recipient, record and date.

    Args:
        tenant_path (str):
        kind (str):
        recipient (None | str | Unset):
        record (None | str | Unset):
        since (datetime.date | None | Unset):
        until (datetime.date | None | Unset):
        page (int | Unset):  Default: 1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        APIResponse | OutputSentMessages
    """

    return (
        await asyncio_detailed(
            tenant_path=tenant_path,
            kind=kind,
            client=client,
            recipient=recipient,
            record=record,
            since=since,
            until=until,
            page=page,
        )
    ).parsed
