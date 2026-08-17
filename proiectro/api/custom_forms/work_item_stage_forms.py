from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.output_work_item_stage_forms import OutputWorkItemStageForms
from ...types import Response


def _get_kwargs(
    tenant_path: str,
    item_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/{tenant_path}/work_item_stage_forms/{item_id}".format(
            tenant_path=quote(str(tenant_path), safe=""),
            item_id=quote(str(item_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> OutputWorkItemStageForms | None:
    if response.status_code == 200:
        response_200 = OutputWorkItemStageForms.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[OutputWorkItemStageForms]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    tenant_path: str,
    item_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[OutputWorkItemStageForms]:
    """Work Item Stage Forms

     The current stage's forms for one work item, with this item's completion state.

    Args:
        tenant_path (str):
        item_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OutputWorkItemStageForms]
    """

    kwargs = _get_kwargs(
        tenant_path=tenant_path,
        item_id=item_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    tenant_path: str,
    item_id: str,
    *,
    client: AuthenticatedClient,
) -> OutputWorkItemStageForms | None:
    """Work Item Stage Forms

     The current stage's forms for one work item, with this item's completion state.

    Args:
        tenant_path (str):
        item_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OutputWorkItemStageForms
    """

    return sync_detailed(
        tenant_path=tenant_path,
        item_id=item_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    tenant_path: str,
    item_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[OutputWorkItemStageForms]:
    """Work Item Stage Forms

     The current stage's forms for one work item, with this item's completion state.

    Args:
        tenant_path (str):
        item_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OutputWorkItemStageForms]
    """

    kwargs = _get_kwargs(
        tenant_path=tenant_path,
        item_id=item_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    tenant_path: str,
    item_id: str,
    *,
    client: AuthenticatedClient,
) -> OutputWorkItemStageForms | None:
    """Work Item Stage Forms

     The current stage's forms for one work item, with this item's completion state.

    Args:
        tenant_path (str):
        item_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OutputWorkItemStageForms
    """

    return (
        await asyncio_detailed(
            tenant_path=tenant_path,
            item_id=item_id,
            client=client,
        )
    ).parsed
