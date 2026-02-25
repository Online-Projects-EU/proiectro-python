from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.output_proposal_preview import OutputProposalPreview
from ...types import Response


def _get_kwargs(
    customer_org_id: str,
    proposal_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/portal/{customer_org_id}/proposals/{proposal_id}".format(
            customer_org_id=quote(str(customer_org_id), safe=""),
            proposal_id=quote(str(proposal_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> OutputProposalPreview | None:
    if response.status_code == 200:
        response_200 = OutputProposalPreview.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[OutputProposalPreview]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    customer_org_id: str,
    proposal_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[OutputProposalPreview]:
    """Portal Proposal Preview

     Get full proposal preview for a specific proposal.
    Returns complete proposal details including products, payment schedule, and acceptance information.

    Args:
        customer_org_id (str):
        proposal_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OutputProposalPreview]
    """

    kwargs = _get_kwargs(
        customer_org_id=customer_org_id,
        proposal_id=proposal_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    customer_org_id: str,
    proposal_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> OutputProposalPreview | None:
    """Portal Proposal Preview

     Get full proposal preview for a specific proposal.
    Returns complete proposal details including products, payment schedule, and acceptance information.

    Args:
        customer_org_id (str):
        proposal_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OutputProposalPreview
    """

    return sync_detailed(
        customer_org_id=customer_org_id,
        proposal_id=proposal_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    customer_org_id: str,
    proposal_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[OutputProposalPreview]:
    """Portal Proposal Preview

     Get full proposal preview for a specific proposal.
    Returns complete proposal details including products, payment schedule, and acceptance information.

    Args:
        customer_org_id (str):
        proposal_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OutputProposalPreview]
    """

    kwargs = _get_kwargs(
        customer_org_id=customer_org_id,
        proposal_id=proposal_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    customer_org_id: str,
    proposal_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> OutputProposalPreview | None:
    """Portal Proposal Preview

     Get full proposal preview for a specific proposal.
    Returns complete proposal details including products, payment schedule, and acceptance information.

    Args:
        customer_org_id (str):
        proposal_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OutputProposalPreview
    """

    return (
        await asyncio_detailed(
            customer_org_id=customer_org_id,
            proposal_id=proposal_id,
            client=client,
        )
    ).parsed
