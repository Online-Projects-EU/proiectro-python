from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.member_load_detail_schema import MemberLoadDetailSchema
from ...types import Response


def _get_kwargs(
    tenant_path: str,
    member_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/{tenant_path}/member_load/{member_id}".format(
            tenant_path=quote(str(tenant_path), safe=""),
            member_id=quote(str(member_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> MemberLoadDetailSchema | None:
    if response.status_code == 200:
        response_200 = MemberLoadDetailSchema.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[MemberLoadDetailSchema]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    tenant_path: str,
    member_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[MemberLoadDetailSchema]:
    """Member Load

     View team member load and capacity utilization.
    Shows individual member load details with availability, holidays, and bookings.

    Args:
        tenant_path (str):
        member_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MemberLoadDetailSchema]
    """

    kwargs = _get_kwargs(
        tenant_path=tenant_path,
        member_id=member_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    tenant_path: str,
    member_id: str,
    *,
    client: AuthenticatedClient,
) -> MemberLoadDetailSchema | None:
    """Member Load

     View team member load and capacity utilization.
    Shows individual member load details with availability, holidays, and bookings.

    Args:
        tenant_path (str):
        member_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MemberLoadDetailSchema
    """

    return sync_detailed(
        tenant_path=tenant_path,
        member_id=member_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    tenant_path: str,
    member_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[MemberLoadDetailSchema]:
    """Member Load

     View team member load and capacity utilization.
    Shows individual member load details with availability, holidays, and bookings.

    Args:
        tenant_path (str):
        member_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MemberLoadDetailSchema]
    """

    kwargs = _get_kwargs(
        tenant_path=tenant_path,
        member_id=member_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    tenant_path: str,
    member_id: str,
    *,
    client: AuthenticatedClient,
) -> MemberLoadDetailSchema | None:
    """Member Load

     View team member load and capacity utilization.
    Shows individual member load details with availability, holidays, and bookings.

    Args:
        tenant_path (str):
        member_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MemberLoadDetailSchema
    """

    return (
        await asyncio_detailed(
            tenant_path=tenant_path,
            member_id=member_id,
            client=client,
        )
    ).parsed
