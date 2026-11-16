from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.output_proposal_lead_history import OutputProposalLeadHistory
from ...types import Response


def _get_kwargs(
    tenant_path: str,
    proposal_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/{tenant_path}/proposal_lead_history/{proposal_id}".format(
            tenant_path=quote(str(tenant_path), safe=""),
            proposal_id=quote(str(proposal_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> OutputProposalLeadHistory | None:
    if response.status_code == 200:
        response_200 = OutputProposalLeadHistory.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[OutputProposalLeadHistory]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    tenant_path: str,
    proposal_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[OutputProposalLeadHistory]:
    """Proposal Lead History

     View the history of the lead a proposal came from: the statuses the lead went through and the
    calls, emails and meetings logged on it before it became a customer. Covers every lead that was
    converted into the proposal's customer before the proposal was created, and only the leads you
    are allowed to see. Essential for reading a deal from the first contact to the signature.

    Args:
        tenant_path (str):
        proposal_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OutputProposalLeadHistory]
    """

    kwargs = _get_kwargs(
        tenant_path=tenant_path,
        proposal_id=proposal_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    tenant_path: str,
    proposal_id: str,
    *,
    client: AuthenticatedClient,
) -> OutputProposalLeadHistory | None:
    """Proposal Lead History

     View the history of the lead a proposal came from: the statuses the lead went through and the
    calls, emails and meetings logged on it before it became a customer. Covers every lead that was
    converted into the proposal's customer before the proposal was created, and only the leads you
    are allowed to see. Essential for reading a deal from the first contact to the signature.

    Args:
        tenant_path (str):
        proposal_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OutputProposalLeadHistory
    """

    return sync_detailed(
        tenant_path=tenant_path,
        proposal_id=proposal_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    tenant_path: str,
    proposal_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[OutputProposalLeadHistory]:
    """Proposal Lead History

     View the history of the lead a proposal came from: the statuses the lead went through and the
    calls, emails and meetings logged on it before it became a customer. Covers every lead that was
    converted into the proposal's customer before the proposal was created, and only the leads you
    are allowed to see. Essential for reading a deal from the first contact to the signature.

    Args:
        tenant_path (str):
        proposal_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OutputProposalLeadHistory]
    """

    kwargs = _get_kwargs(
        tenant_path=tenant_path,
        proposal_id=proposal_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    tenant_path: str,
    proposal_id: str,
    *,
    client: AuthenticatedClient,
) -> OutputProposalLeadHistory | None:
    """Proposal Lead History

     View the history of the lead a proposal came from: the statuses the lead went through and the
    calls, emails and meetings logged on it before it became a customer. Covers every lead that was
    converted into the proposal's customer before the proposal was created, and only the leads you
    are allowed to see. Essential for reading a deal from the first contact to the signature.

    Args:
        tenant_path (str):
        proposal_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OutputProposalLeadHistory
    """

    return (
        await asyncio_detailed(
            tenant_path=tenant_path,
            proposal_id=proposal_id,
            client=client,
        )
    ).parsed
