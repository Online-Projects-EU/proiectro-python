from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.funnel_lost_proposals import FunnelLostProposals
from ...types import Response


def _get_kwargs(
    tenant_path: str,
    funnel_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/{tenant_path}/funnel/{funnel_id}/lost_proposals".format(
            tenant_path=quote(str(tenant_path), safe=""),
            funnel_id=quote(str(funnel_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> FunnelLostProposals | None:
    if response.status_code == 200:
        response_200 = FunnelLostProposals.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[FunnelLostProposals]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    tenant_path: str,
    funnel_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[FunnelLostProposals]:
    """Funnel Lost Proposals

     Study lost opportunities to identify improvement areas and competitive weaknesses.
    Categorizes losses by reason, competitor, and stage for pattern recognition.
    Critical for refining value propositions and addressing objections. Regular review
    prevents repeat mistakes and improves win rates.

    Args:
        tenant_path (str):
        funnel_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FunnelLostProposals]
    """

    kwargs = _get_kwargs(
        tenant_path=tenant_path,
        funnel_id=funnel_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    tenant_path: str,
    funnel_id: str,
    *,
    client: AuthenticatedClient,
) -> FunnelLostProposals | None:
    """Funnel Lost Proposals

     Study lost opportunities to identify improvement areas and competitive weaknesses.
    Categorizes losses by reason, competitor, and stage for pattern recognition.
    Critical for refining value propositions and addressing objections. Regular review
    prevents repeat mistakes and improves win rates.

    Args:
        tenant_path (str):
        funnel_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FunnelLostProposals
    """

    return sync_detailed(
        tenant_path=tenant_path,
        funnel_id=funnel_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    tenant_path: str,
    funnel_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[FunnelLostProposals]:
    """Funnel Lost Proposals

     Study lost opportunities to identify improvement areas and competitive weaknesses.
    Categorizes losses by reason, competitor, and stage for pattern recognition.
    Critical for refining value propositions and addressing objections. Regular review
    prevents repeat mistakes and improves win rates.

    Args:
        tenant_path (str):
        funnel_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FunnelLostProposals]
    """

    kwargs = _get_kwargs(
        tenant_path=tenant_path,
        funnel_id=funnel_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    tenant_path: str,
    funnel_id: str,
    *,
    client: AuthenticatedClient,
) -> FunnelLostProposals | None:
    """Funnel Lost Proposals

     Study lost opportunities to identify improvement areas and competitive weaknesses.
    Categorizes losses by reason, competitor, and stage for pattern recognition.
    Critical for refining value propositions and addressing objections. Regular review
    prevents repeat mistakes and improves win rates.

    Args:
        tenant_path (str):
        funnel_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FunnelLostProposals
    """

    return (
        await asyncio_detailed(
            tenant_path=tenant_path,
            funnel_id=funnel_id,
            client=client,
        )
    ).parsed
