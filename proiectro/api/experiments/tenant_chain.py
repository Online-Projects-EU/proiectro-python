from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_response import APIResponse
from ...models.output_chain import OutputChain
from ...types import UNSET, Response, Unset


def _get_kwargs(
    tenant_path: str,
    pipeline: str,
    *,
    scope: str | Unset = UNSET,
    period: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["scope"] = scope

    params["period"] = period

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/{tenant_path}/chain/{pipeline}".format(
            tenant_path=quote(str(tenant_path), safe=""),
            pipeline=quote(str(pipeline), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> APIResponse | OutputChain | None:
    if response.status_code == 200:
        response_200 = OutputChain.from_dict(response.json())

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
) -> Response[APIResponse | OutputChain]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    tenant_path: str,
    pipeline: str,
    *,
    client: AuthenticatedClient,
    scope: str | Unset = UNSET,
    period: str | Unset = UNSET,
) -> Response[APIResponse | OutputChain]:
    """Tenant Chain

     Where items in a pipeline go next and where they finish, from the moves the app recorded: leads,
    proposals, projects, deliverables, operations or support. Each share comes with its count and likely
    range, and each state with how long items usually stay in it.

    Args:
        tenant_path (str):
        pipeline (str):
        scope (str | Unset):
        period (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[APIResponse | OutputChain]
    """

    kwargs = _get_kwargs(
        tenant_path=tenant_path,
        pipeline=pipeline,
        scope=scope,
        period=period,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    tenant_path: str,
    pipeline: str,
    *,
    client: AuthenticatedClient,
    scope: str | Unset = UNSET,
    period: str | Unset = UNSET,
) -> APIResponse | OutputChain | None:
    """Tenant Chain

     Where items in a pipeline go next and where they finish, from the moves the app recorded: leads,
    proposals, projects, deliverables, operations or support. Each share comes with its count and likely
    range, and each state with how long items usually stay in it.

    Args:
        tenant_path (str):
        pipeline (str):
        scope (str | Unset):
        period (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        APIResponse | OutputChain
    """

    return sync_detailed(
        tenant_path=tenant_path,
        pipeline=pipeline,
        client=client,
        scope=scope,
        period=period,
    ).parsed


async def asyncio_detailed(
    tenant_path: str,
    pipeline: str,
    *,
    client: AuthenticatedClient,
    scope: str | Unset = UNSET,
    period: str | Unset = UNSET,
) -> Response[APIResponse | OutputChain]:
    """Tenant Chain

     Where items in a pipeline go next and where they finish, from the moves the app recorded: leads,
    proposals, projects, deliverables, operations or support. Each share comes with its count and likely
    range, and each state with how long items usually stay in it.

    Args:
        tenant_path (str):
        pipeline (str):
        scope (str | Unset):
        period (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[APIResponse | OutputChain]
    """

    kwargs = _get_kwargs(
        tenant_path=tenant_path,
        pipeline=pipeline,
        scope=scope,
        period=period,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    tenant_path: str,
    pipeline: str,
    *,
    client: AuthenticatedClient,
    scope: str | Unset = UNSET,
    period: str | Unset = UNSET,
) -> APIResponse | OutputChain | None:
    """Tenant Chain

     Where items in a pipeline go next and where they finish, from the moves the app recorded: leads,
    proposals, projects, deliverables, operations or support. Each share comes with its count and likely
    range, and each state with how long items usually stay in it.

    Args:
        tenant_path (str):
        pipeline (str):
        scope (str | Unset):
        period (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        APIResponse | OutputChain
    """

    return (
        await asyncio_detailed(
            tenant_path=tenant_path,
            pipeline=pipeline,
            client=client,
            scope=scope,
            period=period,
        )
    ).parsed
