from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.output_portal_quote_requests import OutputPortalQuoteRequests
from ...types import Response


def _get_kwargs(
    customer_org_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/portal/{customer_org_id}/quote_requests".format(
            customer_org_id=quote(str(customer_org_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> OutputPortalQuoteRequests | None:
    if response.status_code == 200:
        response_200 = OutputPortalQuoteRequests.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[OutputPortalQuoteRequests]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    customer_org_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[OutputPortalQuoteRequests]:
    """Portal Quote Requests

     The organization's quote requests that are waiting for an offer.

    Args:
        customer_org_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OutputPortalQuoteRequests]
    """

    kwargs = _get_kwargs(
        customer_org_id=customer_org_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    customer_org_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> OutputPortalQuoteRequests | None:
    """Portal Quote Requests

     The organization's quote requests that are waiting for an offer.

    Args:
        customer_org_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OutputPortalQuoteRequests
    """

    return sync_detailed(
        customer_org_id=customer_org_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    customer_org_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[OutputPortalQuoteRequests]:
    """Portal Quote Requests

     The organization's quote requests that are waiting for an offer.

    Args:
        customer_org_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OutputPortalQuoteRequests]
    """

    kwargs = _get_kwargs(
        customer_org_id=customer_org_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    customer_org_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> OutputPortalQuoteRequests | None:
    """Portal Quote Requests

     The organization's quote requests that are waiting for an offer.

    Args:
        customer_org_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OutputPortalQuoteRequests
    """

    return (
        await asyncio_detailed(
            customer_org_id=customer_org_id,
            client=client,
        )
    ).parsed
