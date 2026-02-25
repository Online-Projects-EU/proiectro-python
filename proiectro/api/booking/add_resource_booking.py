from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.add_resource_booking import AddResourceBooking
from ...models.add_resource_booking_response import AddResourceBookingResponse
from ...models.api_response import APIResponse
from ...types import Response


def _get_kwargs(
    tenant_path: str,
    *,
    body: AddResourceBooking,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/{tenant_path}/add_resource_booking".format(
            tenant_path=quote(str(tenant_path), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> APIResponse | AddResourceBookingResponse | None:
    if response.status_code == 200:
        response_200 = APIResponse.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = APIResponse.from_dict(response.json())

        return response_400

    if response.status_code == 422:
        response_422 = AddResourceBookingResponse.from_dict(response.json())

        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[APIResponse | AddResourceBookingResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    tenant_path: str,
    *,
    client: AuthenticatedClient,
    body: AddResourceBooking,
) -> Response[APIResponse | AddResourceBookingResponse]:
    """Add Resource Booking

     Reserve equipment, rooms, or other assets for project use. The system prevents
    double-booking and validates resource availability. Only leaf resources in the
    hierarchy can be booked - you must select specific items, not categories.
    Plan ahead for critical resources that are in high demand.

    Args:
        tenant_path (str):
        body (AddResourceBooking): Input schema for adding a resource booking

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[APIResponse | AddResourceBookingResponse]
    """

    kwargs = _get_kwargs(
        tenant_path=tenant_path,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    tenant_path: str,
    *,
    client: AuthenticatedClient,
    body: AddResourceBooking,
) -> APIResponse | AddResourceBookingResponse | None:
    """Add Resource Booking

     Reserve equipment, rooms, or other assets for project use. The system prevents
    double-booking and validates resource availability. Only leaf resources in the
    hierarchy can be booked - you must select specific items, not categories.
    Plan ahead for critical resources that are in high demand.

    Args:
        tenant_path (str):
        body (AddResourceBooking): Input schema for adding a resource booking

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        APIResponse | AddResourceBookingResponse
    """

    return sync_detailed(
        tenant_path=tenant_path,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    tenant_path: str,
    *,
    client: AuthenticatedClient,
    body: AddResourceBooking,
) -> Response[APIResponse | AddResourceBookingResponse]:
    """Add Resource Booking

     Reserve equipment, rooms, or other assets for project use. The system prevents
    double-booking and validates resource availability. Only leaf resources in the
    hierarchy can be booked - you must select specific items, not categories.
    Plan ahead for critical resources that are in high demand.

    Args:
        tenant_path (str):
        body (AddResourceBooking): Input schema for adding a resource booking

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[APIResponse | AddResourceBookingResponse]
    """

    kwargs = _get_kwargs(
        tenant_path=tenant_path,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    tenant_path: str,
    *,
    client: AuthenticatedClient,
    body: AddResourceBooking,
) -> APIResponse | AddResourceBookingResponse | None:
    """Add Resource Booking

     Reserve equipment, rooms, or other assets for project use. The system prevents
    double-booking and validates resource availability. Only leaf resources in the
    hierarchy can be booked - you must select specific items, not categories.
    Plan ahead for critical resources that are in high demand.

    Args:
        tenant_path (str):
        body (AddResourceBooking): Input schema for adding a resource booking

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        APIResponse | AddResourceBookingResponse
    """

    return (
        await asyncio_detailed(
            tenant_path=tenant_path,
            client=client,
            body=body,
        )
    ).parsed
