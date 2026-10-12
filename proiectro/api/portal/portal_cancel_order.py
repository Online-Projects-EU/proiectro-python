from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_response import APIResponse
from ...models.portal_cancel_order import PortalCancelOrder
from ...models.pydantic_detail import PydanticDetail
from ...types import Response


def _get_kwargs(
    customer_org_id: str,
    proposal_id: str,
    *,
    body: PortalCancelOrder,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/api/v1/portal/{customer_org_id}/orders/{proposal_id}/cancel".format(
            customer_org_id=quote(str(customer_org_id), safe=""),
            proposal_id=quote(str(proposal_id), safe=""),
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
    customer_org_id: str,
    proposal_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: PortalCancelOrder,
) -> Response[APIResponse | PydanticDetail]:
    """Portal Cancel Order

     Cancel an order the supplier has not accepted yet.

    Args:
        customer_org_id (str):
        proposal_id (str):
        body (PortalCancelOrder): Input schema for the customer cancelling a submitted order

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[APIResponse | PydanticDetail]
    """

    kwargs = _get_kwargs(
        customer_org_id=customer_org_id,
        proposal_id=proposal_id,
        body=body,
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
    body: PortalCancelOrder,
) -> APIResponse | PydanticDetail | None:
    """Portal Cancel Order

     Cancel an order the supplier has not accepted yet.

    Args:
        customer_org_id (str):
        proposal_id (str):
        body (PortalCancelOrder): Input schema for the customer cancelling a submitted order

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        APIResponse | PydanticDetail
    """

    return sync_detailed(
        customer_org_id=customer_org_id,
        proposal_id=proposal_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    customer_org_id: str,
    proposal_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: PortalCancelOrder,
) -> Response[APIResponse | PydanticDetail]:
    """Portal Cancel Order

     Cancel an order the supplier has not accepted yet.

    Args:
        customer_org_id (str):
        proposal_id (str):
        body (PortalCancelOrder): Input schema for the customer cancelling a submitted order

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[APIResponse | PydanticDetail]
    """

    kwargs = _get_kwargs(
        customer_org_id=customer_org_id,
        proposal_id=proposal_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    customer_org_id: str,
    proposal_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: PortalCancelOrder,
) -> APIResponse | PydanticDetail | None:
    """Portal Cancel Order

     Cancel an order the supplier has not accepted yet.

    Args:
        customer_org_id (str):
        proposal_id (str):
        body (PortalCancelOrder): Input schema for the customer cancelling a submitted order

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        APIResponse | PydanticDetail
    """

    return (
        await asyncio_detailed(
            customer_org_id=customer_org_id,
            proposal_id=proposal_id,
            client=client,
            body=body,
        )
    ).parsed
