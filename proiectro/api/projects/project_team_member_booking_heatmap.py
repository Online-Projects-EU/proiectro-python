from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.output_team_member_booking_heatmap import OutputTeamMemberBookingHeatmap
from ...types import Response


def _get_kwargs(
    tenant_path: str,
    project_id: str,
    member_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/{tenant_path}/project_team_member_booking_heatmap/{project_id}/{member_id}".format(
            tenant_path=quote(str(tenant_path), safe=""),
            project_id=quote(str(project_id), safe=""),
            member_id=quote(str(member_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> OutputTeamMemberBookingHeatmap | None:
    if response.status_code == 200:
        response_200 = OutputTeamMemberBookingHeatmap.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[OutputTeamMemberBookingHeatmap]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    tenant_path: str,
    project_id: str,
    member_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[OutputTeamMemberBookingHeatmap]:
    """Project Team Member Booking Heatmap

     Generate adaptive booking/activity heatmap for a team member in a project.

    Dynamically adapts based on project settings:
    - Shows bookings if booking management is enabled
    - Shows work activity if effort management is enabled
    - Shows both when both features are enabled

    Foundation is always team member availability. Overlays adapt to enabled features.
    Time boundaries determined by available data sources (bookings and/or work logs).

    Args:
        tenant_path (str):
        project_id (str):
        member_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OutputTeamMemberBookingHeatmap]
    """

    kwargs = _get_kwargs(
        tenant_path=tenant_path,
        project_id=project_id,
        member_id=member_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    tenant_path: str,
    project_id: str,
    member_id: str,
    *,
    client: AuthenticatedClient,
) -> OutputTeamMemberBookingHeatmap | None:
    """Project Team Member Booking Heatmap

     Generate adaptive booking/activity heatmap for a team member in a project.

    Dynamically adapts based on project settings:
    - Shows bookings if booking management is enabled
    - Shows work activity if effort management is enabled
    - Shows both when both features are enabled

    Foundation is always team member availability. Overlays adapt to enabled features.
    Time boundaries determined by available data sources (bookings and/or work logs).

    Args:
        tenant_path (str):
        project_id (str):
        member_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OutputTeamMemberBookingHeatmap
    """

    return sync_detailed(
        tenant_path=tenant_path,
        project_id=project_id,
        member_id=member_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    tenant_path: str,
    project_id: str,
    member_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[OutputTeamMemberBookingHeatmap]:
    """Project Team Member Booking Heatmap

     Generate adaptive booking/activity heatmap for a team member in a project.

    Dynamically adapts based on project settings:
    - Shows bookings if booking management is enabled
    - Shows work activity if effort management is enabled
    - Shows both when both features are enabled

    Foundation is always team member availability. Overlays adapt to enabled features.
    Time boundaries determined by available data sources (bookings and/or work logs).

    Args:
        tenant_path (str):
        project_id (str):
        member_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OutputTeamMemberBookingHeatmap]
    """

    kwargs = _get_kwargs(
        tenant_path=tenant_path,
        project_id=project_id,
        member_id=member_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    tenant_path: str,
    project_id: str,
    member_id: str,
    *,
    client: AuthenticatedClient,
) -> OutputTeamMemberBookingHeatmap | None:
    """Project Team Member Booking Heatmap

     Generate adaptive booking/activity heatmap for a team member in a project.

    Dynamically adapts based on project settings:
    - Shows bookings if booking management is enabled
    - Shows work activity if effort management is enabled
    - Shows both when both features are enabled

    Foundation is always team member availability. Overlays adapt to enabled features.
    Time boundaries determined by available data sources (bookings and/or work logs).

    Args:
        tenant_path (str):
        project_id (str):
        member_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OutputTeamMemberBookingHeatmap
    """

    return (
        await asyncio_detailed(
            tenant_path=tenant_path,
            project_id=project_id,
            member_id=member_id,
            client=client,
        )
    ).parsed
