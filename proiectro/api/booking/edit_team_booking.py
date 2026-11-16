from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_response import APIResponse
from ...models.edit_team_booking import EditTeamBooking
from ...models.pydantic_detail import PydanticDetail
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
) -> APIResponse | PydanticDetail | None:
    if response.status_code == 200:
        response_200 = APIResponse.from_dict(response.json())

        return response_200

    if response.status_code == 404:
        response_404 = APIResponse.from_dict(response.json())

        return response_404

    if response.status_code == 422:
        response_422 = PydanticDetail.from_dict(response.json())

        return response_422

    if response.status_code == 500:
        response_500 = APIResponse.from_dict(response.json())

        return response_500

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
    tenant_path: str,
    booking_id: str,
    *,
    client: AuthenticatedClient,
    body: EditTeamBooking,
) -> Response[APIResponse | PydanticDetail]:
    """Edit Team Booking

     Change a team member's booking: the dates, the hours per day or the deliverable. The change is
    checked against their availability again. If you book someone else, both are notified.

    Args:
        tenant_path (str):
        booking_id (str):
        body (EditTeamBooking): Input schema for editing a team booking

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[APIResponse | PydanticDetail]
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
) -> APIResponse | PydanticDetail | None:
    """Edit Team Booking

     Change a team member's booking: the dates, the hours per day or the deliverable. The change is
    checked against their availability again. If you book someone else, both are notified.

    Args:
        tenant_path (str):
        booking_id (str):
        body (EditTeamBooking): Input schema for editing a team booking

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        APIResponse | PydanticDetail
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
) -> Response[APIResponse | PydanticDetail]:
    """Edit Team Booking

     Change a team member's booking: the dates, the hours per day or the deliverable. The change is
    checked against their availability again. If you book someone else, both are notified.

    Args:
        tenant_path (str):
        booking_id (str):
        body (EditTeamBooking): Input schema for editing a team booking

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[APIResponse | PydanticDetail]
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
) -> APIResponse | PydanticDetail | None:
    """Edit Team Booking

     Change a team member's booking: the dates, the hours per day or the deliverable. The change is
    checked against their availability again. If you book someone else, both are notified.

    Args:
        tenant_path (str):
        booking_id (str):
        body (EditTeamBooking): Input schema for editing a team booking

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        APIResponse | PydanticDetail
    """

    return (
        await asyncio_detailed(
            tenant_path=tenant_path,
            booking_id=booking_id,
            client=client,
            body=body,
        )
    ).parsed
