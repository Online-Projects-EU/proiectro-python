from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_response import APIResponse
from ...models.output_solicitation_detail import OutputSolicitationDetail
from ...types import Response


def _get_kwargs(
    tenant_path: str,
    publication_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/{tenant_path}/solicitation_detail/{publication_id}".format(
            tenant_path=quote(str(tenant_path), safe=""),
            publication_id=quote(str(publication_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> APIResponse | OutputSolicitationDetail | None:
    if response.status_code == 200:
        response_200 = OutputSolicitationDetail.from_dict(response.json())

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
) -> Response[APIResponse | OutputSolicitationDetail]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    tenant_path: str,
    publication_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[APIResponse | OutputSolicitationDetail]:
    """Solicitation Detail

     A solicitation is a request for proposal sent to you by one of your
    partners. Review the requirements, budget, and deadline to decide
    whether to submit a proposal or decline.

    Args:
        tenant_path (str):
        publication_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[APIResponse | OutputSolicitationDetail]
    """

    kwargs = _get_kwargs(
        tenant_path=tenant_path,
        publication_id=publication_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    tenant_path: str,
    publication_id: str,
    *,
    client: AuthenticatedClient,
) -> APIResponse | OutputSolicitationDetail | None:
    """Solicitation Detail

     A solicitation is a request for proposal sent to you by one of your
    partners. Review the requirements, budget, and deadline to decide
    whether to submit a proposal or decline.

    Args:
        tenant_path (str):
        publication_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        APIResponse | OutputSolicitationDetail
    """

    return sync_detailed(
        tenant_path=tenant_path,
        publication_id=publication_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    tenant_path: str,
    publication_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[APIResponse | OutputSolicitationDetail]:
    """Solicitation Detail

     A solicitation is a request for proposal sent to you by one of your
    partners. Review the requirements, budget, and deadline to decide
    whether to submit a proposal or decline.

    Args:
        tenant_path (str):
        publication_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[APIResponse | OutputSolicitationDetail]
    """

    kwargs = _get_kwargs(
        tenant_path=tenant_path,
        publication_id=publication_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    tenant_path: str,
    publication_id: str,
    *,
    client: AuthenticatedClient,
) -> APIResponse | OutputSolicitationDetail | None:
    """Solicitation Detail

     A solicitation is a request for proposal sent to you by one of your
    partners. Review the requirements, budget, and deadline to decide
    whether to submit a proposal or decline.

    Args:
        tenant_path (str):
        publication_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        APIResponse | OutputSolicitationDetail
    """

    return (
        await asyncio_detailed(
            tenant_path=tenant_path,
            publication_id=publication_id,
            client=client,
        )
    ).parsed
