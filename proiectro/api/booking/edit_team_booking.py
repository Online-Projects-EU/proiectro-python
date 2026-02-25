from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_response import APIResponse
from ...models.edit_team_booking import EditTeamBooking
from ...models.edit_team_booking_response import EditTeamBookingResponse
from ...types import Response


def _get_kwargs(
    tenant_path: str,
    booking_id: str,
    *,
    body: EditTeamBooking,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/api/v1/{tenant_path}/edit_team_booking/{booking_id}".format(
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
) -> APIResponse | EditTeamBookingResponse | None:
    if response.status_code == 200:
        response_200 = APIResponse.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = APIResponse.from_dict(response.json())

        return response_400

    if response.status_code == 422:
        response_422 = EditTeamBookingResponse.from_dict(response.json())

        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[APIResponse | EditTeamBookingResponse]:
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
    body: EditTeamBooking,
) -> Response[APIResponse | EditTeamBookingResponse]:
    """Edit Team Booking

     Adjust team member allocation when project timelines shift or requirements change.
    Extends or shortens booking periods, reassigns to different deliverables, or updates
    allocation percentages. Changes immediately affect availability calculations and capacity
    reports. Notify affected team members of significant schedule changes.

    Args:
        tenant_path (str):
        booking_id (str):
        body (EditTeamBooking): Input schema for editing a team booking

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[APIResponse | EditTeamBookingResponse]
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
    body: EditTeamBooking,
) -> APIResponse | EditTeamBookingResponse | None:
    """Edit Team Booking

     Adjust team member allocation when project timelines shift or requirements change.
    Extends or shortens booking periods, reassigns to different deliverables, or updates
    allocation percentages. Changes immediately affect availability calculations and capacity
    reports. Notify affected team members of significant schedule changes.

    Args:
        tenant_path (str):
        booking_id (str):
        body (EditTeamBooking): Input schema for editing a team booking

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        APIResponse | EditTeamBookingResponse
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
    body: EditTeamBooking,
) -> Response[APIResponse | EditTeamBookingResponse]:
    """Edit Team Booking

     Adjust team member allocation when project timelines shift or requirements change.
    Extends or shortens booking periods, reassigns to different deliverables, or updates
    allocation percentages. Changes immediately affect availability calculations and capacity
    reports. Notify affected team members of significant schedule changes.

    Args:
        tenant_path (str):
        booking_id (str):
        body (EditTeamBooking): Input schema for editing a team booking

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[APIResponse | EditTeamBookingResponse]
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
    body: EditTeamBooking,
) -> APIResponse | EditTeamBookingResponse | None:
    """Edit Team Booking

     Adjust team member allocation when project timelines shift or requirements change.
    Extends or shortens booking periods, reassigns to different deliverables, or updates
    allocation percentages. Changes immediately affect availability calculations and capacity
    reports. Notify affected team members of significant schedule changes.

    Args:
        tenant_path (str):
        booking_id (str):
        body (EditTeamBooking): Input schema for editing a team booking

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        APIResponse | EditTeamBookingResponse
    """

    return (
        await asyncio_detailed(
            tenant_path=tenant_path,
            booking_id=booking_id,
            client=client,
            body=body,
        )
    ).parsed
