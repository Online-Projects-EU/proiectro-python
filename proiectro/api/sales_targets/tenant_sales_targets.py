from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.output_sales_targets import OutputSalesTargets
from ...types import UNSET, Response, Unset


def _get_kwargs(
    tenant_path: str,
    *,
    member_id: str | Unset = UNSET,
    period: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["member_id"] = member_id

    params["period"] = period

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/{tenant_path}/sales_targets".format(
            tenant_path=quote(str(tenant_path), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> OutputSalesTargets | None:
    if response.status_code == 200:
        response_200 = OutputSalesTargets.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[OutputSalesTargets]:
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
    member_id: str | Unset = UNSET,
    period: str | Unset = UNSET,
) -> Response[OutputSalesTargets]:
    """Tenant Sales Targets

     The targets your team is working to. Filter by team member, or by a date to see the targets
    that were live on that day, which is what you want when a quarterly number straddles the
    month you are looking at.

    Args:
        tenant_path (str):
        member_id (str | Unset):
        period (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OutputSalesTargets]
    """

    kwargs = _get_kwargs(
        tenant_path=tenant_path,
        member_id=member_id,
        period=period,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    tenant_path: str,
    *,
    client: AuthenticatedClient,
    member_id: str | Unset = UNSET,
    period: str | Unset = UNSET,
) -> OutputSalesTargets | None:
    """Tenant Sales Targets

     The targets your team is working to. Filter by team member, or by a date to see the targets
    that were live on that day, which is what you want when a quarterly number straddles the
    month you are looking at.

    Args:
        tenant_path (str):
        member_id (str | Unset):
        period (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OutputSalesTargets
    """

    return sync_detailed(
        tenant_path=tenant_path,
        client=client,
        member_id=member_id,
        period=period,
    ).parsed


async def asyncio_detailed(
    tenant_path: str,
    *,
    client: AuthenticatedClient,
    member_id: str | Unset = UNSET,
    period: str | Unset = UNSET,
) -> Response[OutputSalesTargets]:
    """Tenant Sales Targets

     The targets your team is working to. Filter by team member, or by a date to see the targets
    that were live on that day, which is what you want when a quarterly number straddles the
    month you are looking at.

    Args:
        tenant_path (str):
        member_id (str | Unset):
        period (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OutputSalesTargets]
    """

    kwargs = _get_kwargs(
        tenant_path=tenant_path,
        member_id=member_id,
        period=period,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    tenant_path: str,
    *,
    client: AuthenticatedClient,
    member_id: str | Unset = UNSET,
    period: str | Unset = UNSET,
) -> OutputSalesTargets | None:
    """Tenant Sales Targets

     The targets your team is working to. Filter by team member, or by a date to see the targets
    that were live on that day, which is what you want when a quarterly number straddles the
    month you are looking at.

    Args:
        tenant_path (str):
        member_id (str | Unset):
        period (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OutputSalesTargets
    """

    return (
        await asyncio_detailed(
            tenant_path=tenant_path,
            client=client,
            member_id=member_id,
            period=period,
        )
    ).parsed
