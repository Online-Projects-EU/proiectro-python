from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_response import APIResponse
from ...models.pydantic_detail import PydanticDetail
from ...models.send_proposal_by_email_and_move import SendProposalByEmailAndMove
from ...types import Response


def _get_kwargs(
    tenant_path: str,
    proposal_id: str,
    stage_id: str,
    *,
    body: SendProposalByEmailAndMove,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/{tenant_path}/send_proposal_by_email_and_move/{proposal_id}/{stage_id}".format(
            tenant_path=quote(str(tenant_path), safe=""),
            proposal_id=quote(str(proposal_id), safe=""),
            stage_id=quote(str(stage_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> APIResponse | PydanticDetail | None:
    if response.status_code == 200:
        response_200 = APIResponse.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = APIResponse.from_dict(response.json())

        return response_400

    if response.status_code == 403:
        response_403 = APIResponse.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = APIResponse.from_dict(response.json())

        return response_404

    if response.status_code == 409:
        response_409 = APIResponse.from_dict(response.json())

        return response_409

    if response.status_code == 422:
        response_422 = PydanticDetail.from_dict(response.json())

        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[APIResponse | PydanticDetail]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    tenant_path: str,
    proposal_id: str,
    stage_id: str,
    *,
    client: AuthenticatedClient,
    body: SendProposalByEmailAndMove,
) -> Response[APIResponse | PydanticDetail]:
    """Send Proposal By Email And Move

     Send a proposal's email as `send_proposal_by_email` does and, with `move_stage`, move the proposal
    to the
    Proposal Sent stage `stage_id` first. A refused move sends nothing, and a refused email leaves the
    stage
    where it was.

    Args:
        tenant_path (str):
        proposal_id (str):
        stage_id (str):
        body (SendProposalByEmailAndMove):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[APIResponse | PydanticDetail]
    """

    kwargs = _get_kwargs(
        tenant_path=tenant_path,
        proposal_id=proposal_id,
        stage_id=stage_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    tenant_path: str,
    proposal_id: str,
    stage_id: str,
    *,
    client: AuthenticatedClient,
    body: SendProposalByEmailAndMove,
) -> APIResponse | PydanticDetail | None:
    """Send Proposal By Email And Move

     Send a proposal's email as `send_proposal_by_email` does and, with `move_stage`, move the proposal
    to the
    Proposal Sent stage `stage_id` first. A refused move sends nothing, and a refused email leaves the
    stage
    where it was.

    Args:
        tenant_path (str):
        proposal_id (str):
        stage_id (str):
        body (SendProposalByEmailAndMove):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        APIResponse | PydanticDetail
    """

    return sync_detailed(
        tenant_path=tenant_path,
        proposal_id=proposal_id,
        stage_id=stage_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    tenant_path: str,
    proposal_id: str,
    stage_id: str,
    *,
    client: AuthenticatedClient,
    body: SendProposalByEmailAndMove,
) -> Response[APIResponse | PydanticDetail]:
    """Send Proposal By Email And Move

     Send a proposal's email as `send_proposal_by_email` does and, with `move_stage`, move the proposal
    to the
    Proposal Sent stage `stage_id` first. A refused move sends nothing, and a refused email leaves the
    stage
    where it was.

    Args:
        tenant_path (str):
        proposal_id (str):
        stage_id (str):
        body (SendProposalByEmailAndMove):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[APIResponse | PydanticDetail]
    """

    kwargs = _get_kwargs(
        tenant_path=tenant_path,
        proposal_id=proposal_id,
        stage_id=stage_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    tenant_path: str,
    proposal_id: str,
    stage_id: str,
    *,
    client: AuthenticatedClient,
    body: SendProposalByEmailAndMove,
) -> APIResponse | PydanticDetail | None:
    """Send Proposal By Email And Move

     Send a proposal's email as `send_proposal_by_email` does and, with `move_stage`, move the proposal
    to the
    Proposal Sent stage `stage_id` first. A refused move sends nothing, and a refused email leaves the
    stage
    where it was.

    Args:
        tenant_path (str):
        proposal_id (str):
        stage_id (str):
        body (SendProposalByEmailAndMove):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        APIResponse | PydanticDetail
    """

    return (
        await asyncio_detailed(
            tenant_path=tenant_path,
            proposal_id=proposal_id,
            stage_id=stage_id,
            client=client,
            body=body,
        )
    ).parsed
