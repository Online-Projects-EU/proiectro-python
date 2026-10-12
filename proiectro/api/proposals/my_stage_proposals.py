from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_response import APIResponse
from ...models.stage_proposals import StageProposals
from ...types import Response


def _get_kwargs(
    tenant_path: str,
    stage_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/{tenant_path}/my_stage_proposals/{stage_id}".format(
            tenant_path=quote(str(tenant_path), safe=""),
            stage_id=quote(str(stage_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> APIResponse | StageProposals | None:
    if response.status_code == 200:
        response_200 = StageProposals.from_dict(response.json())

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
) -> Response[APIResponse | StageProposals]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    tenant_path: str,
    stage_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[APIResponse | StageProposals]:
    """My Stage Proposals

     List your own open proposals in one funnel stage, with customer, value, days in stage and the
    stages each can move to next.

    Args:
        tenant_path (str):
        stage_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[APIResponse | StageProposals]
    """

    kwargs = _get_kwargs(
        tenant_path=tenant_path,
        stage_id=stage_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    tenant_path: str,
    stage_id: str,
    *,
    client: AuthenticatedClient,
) -> APIResponse | StageProposals | None:
    """My Stage Proposals

     List your own open proposals in one funnel stage, with customer, value, days in stage and the
    stages each can move to next.

    Args:
        tenant_path (str):
        stage_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        APIResponse | StageProposals
    """

    return sync_detailed(
        tenant_path=tenant_path,
        stage_id=stage_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    tenant_path: str,
    stage_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[APIResponse | StageProposals]:
    """My Stage Proposals

     List your own open proposals in one funnel stage, with customer, value, days in stage and the
    stages each can move to next.

    Args:
        tenant_path (str):
        stage_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[APIResponse | StageProposals]
    """

    kwargs = _get_kwargs(
        tenant_path=tenant_path,
        stage_id=stage_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    tenant_path: str,
    stage_id: str,
    *,
    client: AuthenticatedClient,
) -> APIResponse | StageProposals | None:
    """My Stage Proposals

     List your own open proposals in one funnel stage, with customer, value, days in stage and the
    stages each can move to next.

    Args:
        tenant_path (str):
        stage_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        APIResponse | StageProposals
    """

    return (
        await asyncio_detailed(
            tenant_path=tenant_path,
            stage_id=stage_id,
            client=client,
        )
    ).parsed
