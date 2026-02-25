from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import Response


def _get_kwargs(
    tenant_path: str,
    proposal_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/{tenant_path}/proposal_general/{proposal_id}".format(
            tenant_path=quote(str(tenant_path), safe=""),
            proposal_id=quote(str(proposal_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | None:
    if response.status_code == 200:
        return None

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any]:
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
) -> Response[Any]:
    """Proposal General

     Access core proposal information including customer details, timeline, scope summary,
    and key stakeholders. Foundation view for understanding deal context and requirements.
    Shows proposal status, probability, and strategic importance. Essential for sales
    reviews and quick deal assessment.

    Args:
        tenant_path (str):
        proposal_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        tenant_path=tenant_path,
        proposal_id=proposal_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    tenant_path: str,
    proposal_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Any]:
    """Proposal General

     Access core proposal information including customer details, timeline, scope summary,
    and key stakeholders. Foundation view for understanding deal context and requirements.
    Shows proposal status, probability, and strategic importance. Essential for sales
    reviews and quick deal assessment.

    Args:
        tenant_path (str):
        proposal_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        tenant_path=tenant_path,
        proposal_id=proposal_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
