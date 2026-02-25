from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.add_team_booking import AddTeamBooking
from ...models.add_team_booking_response import AddTeamBookingResponse
from ...models.api_response import APIResponse
from ...types import Response


def _get_kwargs(
    tenant_path: str,
    *,
    body: AddTeamBooking,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/{tenant_path}/add_team_booking".format(
            tenant_path=quote(str(tenant_path), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> APIResponse | AddTeamBookingResponse | None:
    if response.status_code == 200:
        response_200 = APIResponse.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = APIResponse.from_dict(response.json())

        return response_400

    if response.status_code == 422:
        response_422 = AddTeamBookingResponse.from_dict(response.json())

        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[APIResponse | AddTeamBookingResponse]:
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
    body: AddTeamBooking,
) -> Response[APIResponse | AddTeamBookingResponse]:
    """Add Team Booking

     Allocate a team member to a project, blocking their calendar for the specified period.
    Link bookings to specific deliverables for granular work tracking. The system automatically
    creates availability exceptions to prevent double-booking. Consider team member workload
    and existing commitments before creating new bookings.

    Args:
        tenant_path (str):
        body (AddTeamBooking): Input schema for adding a team booking

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[APIResponse | AddTeamBookingResponse]
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
    body: AddTeamBooking,
) -> APIResponse | AddTeamBookingResponse | None:
    """Add Team Booking

     Allocate a team member to a project, blocking their calendar for the specified period.
    Link bookings to specific deliverables for granular work tracking. The system automatically
    creates availability exceptions to prevent double-booking. Consider team member workload
    and existing commitments before creating new bookings.

    Args:
        tenant_path (str):
        body (AddTeamBooking): Input schema for adding a team booking

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        APIResponse | AddTeamBookingResponse
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
    body: AddTeamBooking,
) -> Response[APIResponse | AddTeamBookingResponse]:
    """Add Team Booking

     Allocate a team member to a project, blocking their calendar for the specified period.
    Link bookings to specific deliverables for granular work tracking. The system automatically
    creates availability exceptions to prevent double-booking. Consider team member workload
    and existing commitments before creating new bookings.

    Args:
        tenant_path (str):
        body (AddTeamBooking): Input schema for adding a team booking

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[APIResponse | AddTeamBookingResponse]
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
    body: AddTeamBooking,
) -> APIResponse | AddTeamBookingResponse | None:
    """Add Team Booking

     Allocate a team member to a project, blocking their calendar for the specified period.
    Link bookings to specific deliverables for granular work tracking. The system automatically
    creates availability exceptions to prevent double-booking. Consider team member workload
    and existing commitments before creating new bookings.

    Args:
        tenant_path (str):
        body (AddTeamBooking): Input schema for adding a team booking

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        APIResponse | AddTeamBookingResponse
    """

    return (
        await asyncio_detailed(
            tenant_path=tenant_path,
            client=client,
            body=body,
        )
    ).parsed
