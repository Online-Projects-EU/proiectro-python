from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.tenant_funnel_overview import TenantFunnelOverview
from ...types import Response


def _get_kwargs(
    tenant_path: str,
    funnel_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/{tenant_path}/funnel/{funnel_id}".format(
            tenant_path=quote(str(tenant_path), safe=""),
            funnel_id=quote(str(funnel_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> TenantFunnelOverview | None:
    if response.status_code == 200:
        response_200 = TenantFunnelOverview.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[TenantFunnelOverview]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    tenant_path: str,
    funnel_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[TenantFunnelOverview]:
    """Tenant Funnel

     Deep dive into specific funnel performance with stage-by-stage conversion analysis.
    Shows deal aging, value distribution, and progression patterns. Critical for
    identifying process improvements and forecast accuracy. Includes win/loss analytics
    for continuous methodology refinement.

    Args:
        tenant_path (str):
        funnel_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TenantFunnelOverview]
    """

    kwargs = _get_kwargs(
        tenant_path=tenant_path,
        funnel_id=funnel_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    tenant_path: str,
    funnel_id: str,
    *,
    client: AuthenticatedClient,
) -> TenantFunnelOverview | None:
    """Tenant Funnel

     Deep dive into specific funnel performance with stage-by-stage conversion analysis.
    Shows deal aging, value distribution, and progression patterns. Critical for
    identifying process improvements and forecast accuracy. Includes win/loss analytics
    for continuous methodology refinement.

    Args:
        tenant_path (str):
        funnel_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        TenantFunnelOverview
    """

    return sync_detailed(
        tenant_path=tenant_path,
        funnel_id=funnel_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    tenant_path: str,
    funnel_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[TenantFunnelOverview]:
    """Tenant Funnel

     Deep dive into specific funnel performance with stage-by-stage conversion analysis.
    Shows deal aging, value distribution, and progression patterns. Critical for
    identifying process improvements and forecast accuracy. Includes win/loss analytics
    for continuous methodology refinement.

    Args:
        tenant_path (str):
        funnel_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TenantFunnelOverview]
    """

    kwargs = _get_kwargs(
        tenant_path=tenant_path,
        funnel_id=funnel_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    tenant_path: str,
    funnel_id: str,
    *,
    client: AuthenticatedClient,
) -> TenantFunnelOverview | None:
    """Tenant Funnel

     Deep dive into specific funnel performance with stage-by-stage conversion analysis.
    Shows deal aging, value distribution, and progression patterns. Critical for
    identifying process improvements and forecast accuracy. Includes win/loss analytics
    for continuous methodology refinement.

    Args:
        tenant_path (str):
        funnel_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        TenantFunnelOverview
    """

    return (
        await asyncio_detailed(
            tenant_path=tenant_path,
            funnel_id=funnel_id,
            client=client,
        )
    ).parsed
