from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_response import APIResponse
from ...models.output_coordinates_conflict import OutputCoordinatesConflict
from ...models.pydantic_detail import PydanticDetail
from ...models.set_entity_coordinates import SetEntityCoordinates
from ...types import Response


def _get_kwargs(
    tenant_path: str,
    location_id: str,
    *,
    body: SetEntityCoordinates,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/{tenant_path}/set_location_coordinates/{location_id}".format(
            tenant_path=quote(str(tenant_path), safe=""),
            location_id=quote(str(location_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> APIResponse | OutputCoordinatesConflict | PydanticDetail | None:
    if response.status_code == 200:
        response_200 = APIResponse.from_dict(response.json())

        return response_200

    if response.status_code == 404:
        response_404 = APIResponse.from_dict(response.json())

        return response_404

    if response.status_code == 409:
        response_409 = OutputCoordinatesConflict.from_dict(response.json())

        return response_409

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
) -> Response[APIResponse | OutputCoordinatesConflict | PydanticDetail]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    tenant_path: str,
    location_id: str,
    *,
    client: AuthenticatedClient,
    body: SetEntityCoordinates,
) -> Response[APIResponse | OutputCoordinatesConflict | PydanticDetail]:
    """Set Location Coordinates

     Set a location's GPS coordinates from a device fix, typically captured in
    the field. Writes above the workspace accuracy floor are rejected, and an
    existing pin is only moved after an explicit confirmation.

    Args:
        tenant_path (str):
        location_id (str):
        body (SetEntityCoordinates): Field GPS capture for a location / customer location /
            customer asset.

            `accuracy_m` is the device-reported fix accuracy and is mandatory, writes
            above the workspace's `geo_capture_max_accuracy_m` floor are rejected, so a
            500 m fix never gets stored as truth. An existing point is never silently
            overwritten: without `confirm_overwrite` the endpoint answers 409 with the
            stored point so the client can show how far the pin would move.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[APIResponse | OutputCoordinatesConflict | PydanticDetail]
    """

    kwargs = _get_kwargs(
        tenant_path=tenant_path,
        location_id=location_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    tenant_path: str,
    location_id: str,
    *,
    client: AuthenticatedClient,
    body: SetEntityCoordinates,
) -> APIResponse | OutputCoordinatesConflict | PydanticDetail | None:
    """Set Location Coordinates

     Set a location's GPS coordinates from a device fix, typically captured in
    the field. Writes above the workspace accuracy floor are rejected, and an
    existing pin is only moved after an explicit confirmation.

    Args:
        tenant_path (str):
        location_id (str):
        body (SetEntityCoordinates): Field GPS capture for a location / customer location /
            customer asset.

            `accuracy_m` is the device-reported fix accuracy and is mandatory, writes
            above the workspace's `geo_capture_max_accuracy_m` floor are rejected, so a
            500 m fix never gets stored as truth. An existing point is never silently
            overwritten: without `confirm_overwrite` the endpoint answers 409 with the
            stored point so the client can show how far the pin would move.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        APIResponse | OutputCoordinatesConflict | PydanticDetail
    """

    return sync_detailed(
        tenant_path=tenant_path,
        location_id=location_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    tenant_path: str,
    location_id: str,
    *,
    client: AuthenticatedClient,
    body: SetEntityCoordinates,
) -> Response[APIResponse | OutputCoordinatesConflict | PydanticDetail]:
    """Set Location Coordinates

     Set a location's GPS coordinates from a device fix, typically captured in
    the field. Writes above the workspace accuracy floor are rejected, and an
    existing pin is only moved after an explicit confirmation.

    Args:
        tenant_path (str):
        location_id (str):
        body (SetEntityCoordinates): Field GPS capture for a location / customer location /
            customer asset.

            `accuracy_m` is the device-reported fix accuracy and is mandatory, writes
            above the workspace's `geo_capture_max_accuracy_m` floor are rejected, so a
            500 m fix never gets stored as truth. An existing point is never silently
            overwritten: without `confirm_overwrite` the endpoint answers 409 with the
            stored point so the client can show how far the pin would move.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[APIResponse | OutputCoordinatesConflict | PydanticDetail]
    """

    kwargs = _get_kwargs(
        tenant_path=tenant_path,
        location_id=location_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    tenant_path: str,
    location_id: str,
    *,
    client: AuthenticatedClient,
    body: SetEntityCoordinates,
) -> APIResponse | OutputCoordinatesConflict | PydanticDetail | None:
    """Set Location Coordinates

     Set a location's GPS coordinates from a device fix, typically captured in
    the field. Writes above the workspace accuracy floor are rejected, and an
    existing pin is only moved after an explicit confirmation.

    Args:
        tenant_path (str):
        location_id (str):
        body (SetEntityCoordinates): Field GPS capture for a location / customer location /
            customer asset.

            `accuracy_m` is the device-reported fix accuracy and is mandatory, writes
            above the workspace's `geo_capture_max_accuracy_m` floor are rejected, so a
            500 m fix never gets stored as truth. An existing point is never silently
            overwritten: without `confirm_overwrite` the endpoint answers 409 with the
            stored point so the client can show how far the pin would move.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        APIResponse | OutputCoordinatesConflict | PydanticDetail
    """

    return (
        await asyncio_detailed(
            tenant_path=tenant_path,
            location_id=location_id,
            client=client,
            body=body,
        )
    ).parsed
