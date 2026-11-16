from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_response import APIResponse
from ...models.output_belief_detail import OutputBeliefDetail
from ...types import UNSET, Response, Unset


def _get_kwargs(
    tenant_path: str,
    belief_id: str,
    *,
    include_items: bool | Unset = False,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["include_items"] = include_items

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/{tenant_path}/belief/{belief_id}".format(
            tenant_path=quote(str(tenant_path), safe=""),
            belief_id=quote(str(belief_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> APIResponse | OutputBeliefDetail | None:
    if response.status_code == 200:
        response_200 = OutputBeliefDetail.from_dict(response.json())

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
) -> Response[APIResponse | OutputBeliefDetail]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    tenant_path: str,
    belief_id: str,
    *,
    client: AuthenticatedClient,
    include_items: bool | Unset = False,
) -> Response[APIResponse | OutputBeliefDetail]:
    """Tenant Belief

     One belief with its figure, its likely range and where it stands against your decision bar, split by
    list, source, owner or funnel when the belief has a split. Set include_items to list the cases
    counted.

    Args:
        tenant_path (str):
        belief_id (str):
        include_items (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[APIResponse | OutputBeliefDetail]
    """

    kwargs = _get_kwargs(
        tenant_path=tenant_path,
        belief_id=belief_id,
        include_items=include_items,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    tenant_path: str,
    belief_id: str,
    *,
    client: AuthenticatedClient,
    include_items: bool | Unset = False,
) -> APIResponse | OutputBeliefDetail | None:
    """Tenant Belief

     One belief with its figure, its likely range and where it stands against your decision bar, split by
    list, source, owner or funnel when the belief has a split. Set include_items to list the cases
    counted.

    Args:
        tenant_path (str):
        belief_id (str):
        include_items (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        APIResponse | OutputBeliefDetail
    """

    return sync_detailed(
        tenant_path=tenant_path,
        belief_id=belief_id,
        client=client,
        include_items=include_items,
    ).parsed


async def asyncio_detailed(
    tenant_path: str,
    belief_id: str,
    *,
    client: AuthenticatedClient,
    include_items: bool | Unset = False,
) -> Response[APIResponse | OutputBeliefDetail]:
    """Tenant Belief

     One belief with its figure, its likely range and where it stands against your decision bar, split by
    list, source, owner or funnel when the belief has a split. Set include_items to list the cases
    counted.

    Args:
        tenant_path (str):
        belief_id (str):
        include_items (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[APIResponse | OutputBeliefDetail]
    """

    kwargs = _get_kwargs(
        tenant_path=tenant_path,
        belief_id=belief_id,
        include_items=include_items,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    tenant_path: str,
    belief_id: str,
    *,
    client: AuthenticatedClient,
    include_items: bool | Unset = False,
) -> APIResponse | OutputBeliefDetail | None:
    """Tenant Belief

     One belief with its figure, its likely range and where it stands against your decision bar, split by
    list, source, owner or funnel when the belief has a split. Set include_items to list the cases
    counted.

    Args:
        tenant_path (str):
        belief_id (str):
        include_items (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        APIResponse | OutputBeliefDetail
    """

    return (
        await asyncio_detailed(
            tenant_path=tenant_path,
            belief_id=belief_id,
            client=client,
            include_items=include_items,
        )
    ).parsed
