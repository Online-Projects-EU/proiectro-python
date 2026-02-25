from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_response import APIResponse
from ...models.edit_resource_booking import EditResourceBooking
from ...models.edit_resource_booking_response import EditResourceBookingResponse
from ...types import Response


def _get_kwargs(
    tenant_path: str,
    booking_id: str,
    *,
    body: EditResourceBooking,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/api/v1/{tenant_path}/edit_resource_booking/{booking_id}".format(
            tenant_path=quote(str(tenant_path), safe=""),
            booking_id=quote(str(booking_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> APIResponse | EditResourceBookingResponse | None:
    if response.status_code == 200:
        response_200 = APIResponse.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = APIResponse.from_dict(response.json())

        return response_400

    if response.status_code == 422:
        response_422 = EditResourceBookingResponse.from_dict(response.json())

        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[APIResponse | EditResourceBookingResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    tenant_path: str,
    booking_id: str,
    *,
    client: AuthenticatedClient,
    body: EditResourceBooking,
) -> Response[APIResponse | EditResourceBookingResponse]:
    """Edit Resource Booking

     Modify resource reservations when project needs evolve. Extend rental periods,
    change quantities, or adjust booking dates. Updates immediately affect resource
    availability for other projects. Check for conflicts before extending bookings
    during peak usage periods.

    Args:
        tenant_path (str):
        booking_id (str):
        body (EditResourceBooking): Input schema for editing a resource booking

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[APIResponse | EditResourceBookingResponse]
    """

    kwargs = _get_kwargs(
        tenant_path=tenant_path,
        booking_id=booking_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    tenant_path: str,
    booking_id: str,
    *,
    client: AuthenticatedClient,
    body: EditResourceBooking,
) -> APIResponse | EditResourceBookingResponse | None:
    """Edit Resource Booking

     Modify resource reservations when project needs evolve. Extend rental periods,
    change quantities, or adjust booking dates. Updates immediately affect resource
    availability for other projects. Check for conflicts before extending bookings
    during peak usage periods.

    Args:
        tenant_path (str):
        booking_id (str):
        body (EditResourceBooking): Input schema for editing a resource booking

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        APIResponse | EditResourceBookingResponse
    """

    return sync_detailed(
        tenant_path=tenant_path,
        booking_id=booking_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    tenant_path: str,
    booking_id: str,
    *,
    client: AuthenticatedClient,
    body: EditResourceBooking,
) -> Response[APIResponse | EditResourceBookingResponse]:
    """Edit Resource Booking

     Modify resource reservations when project needs evolve. Extend rental periods,
    change quantities, or adjust booking dates. Updates immediately affect resource
    availability for other projects. Check for conflicts before extending bookings
    during peak usage periods.

    Args:
        tenant_path (str):
        booking_id (str):
        body (EditResourceBooking): Input schema for editing a resource booking

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[APIResponse | EditResourceBookingResponse]
    """

    kwargs = _get_kwargs(
        tenant_path=tenant_path,
        booking_id=booking_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    tenant_path: str,
    booking_id: str,
    *,
    client: AuthenticatedClient,
    body: EditResourceBooking,
) -> APIResponse | EditResourceBookingResponse | None:
    """Edit Resource Booking

     Modify resource reservations when project needs evolve. Extend rental periods,
    change quantities, or adjust booking dates. Updates immediately affect resource
    availability for other projects. Check for conflicts before extending bookings
    during peak usage periods.

    Args:
        tenant_path (str):
        booking_id (str):
        body (EditResourceBooking): Input schema for editing a resource booking

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        APIResponse | EditResourceBookingResponse
    """

    return (
        await asyncio_detailed(
            tenant_path=tenant_path,
            booking_id=booking_id,
            client=client,
            body=body,
        )
    ).parsed
