from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.automation_actions_response import AutomationActionsResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    tenant_path: str,
    *,
    event: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["event"] = event

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/{tenant_path}/automation_actions".format(
            tenant_path=quote(str(tenant_path), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AutomationActionsResponse | None:
    if response.status_code == 200:
        response_200 = AutomationActionsResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[AutomationActionsResponse]:
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
    event: str | Unset = UNSET,
) -> Response[AutomationActionsResponse]:
    """Automation Actions

     List available automation actions from the registry.
    Optionally pass ?event=triggerName to get template variables for that trigger.

    Args:
        tenant_path (str):
        event (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AutomationActionsResponse]
    """

    kwargs = _get_kwargs(
        tenant_path=tenant_path,
        event=event,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    tenant_path: str,
    *,
    client: AuthenticatedClient,
    event: str | Unset = UNSET,
) -> AutomationActionsResponse | None:
    """Automation Actions

     List available automation actions from the registry.
    Optionally pass ?event=triggerName to get template variables for that trigger.

    Args:
        tenant_path (str):
        event (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AutomationActionsResponse
    """

    return sync_detailed(
        tenant_path=tenant_path,
        client=client,
        event=event,
    ).parsed


async def asyncio_detailed(
    tenant_path: str,
    *,
    client: AuthenticatedClient,
    event: str | Unset = UNSET,
) -> Response[AutomationActionsResponse]:
    """Automation Actions

     List available automation actions from the registry.
    Optionally pass ?event=triggerName to get template variables for that trigger.

    Args:
        tenant_path (str):
        event (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AutomationActionsResponse]
    """

    kwargs = _get_kwargs(
        tenant_path=tenant_path,
        event=event,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    tenant_path: str,
    *,
    client: AuthenticatedClient,
    event: str | Unset = UNSET,
) -> AutomationActionsResponse | None:
    """Automation Actions

     List available automation actions from the registry.
    Optionally pass ?event=triggerName to get template variables for that trigger.

    Args:
        tenant_path (str):
        event (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AutomationActionsResponse
    """

    return (
        await asyncio_detailed(
            tenant_path=tenant_path,
            client=client,
            event=event,
        )
    ).parsed
