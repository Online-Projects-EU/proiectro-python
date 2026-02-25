from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.tenant_funnel_configurations import TenantFunnelConfigurations
from ...types import Response


def _get_kwargs(
    tenant_path: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/{tenant_path}/funnelconfigurations".format(
            tenant_path=quote(str(tenant_path), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> TenantFunnelConfigurations | None:
    if response.status_code == 200:
        response_200 = TenantFunnelConfigurations.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[TenantFunnelConfigurations]:
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
) -> Response[TenantFunnelConfigurations]:
    """Tenant Funnelconfigurations

     View all sales funnel configurations available in your workspace. Each funnel
    represents a different sales process for various product lines or customer segments.
    Essential for understanding your sales methodologies and choosing the right process
    for new opportunities. Shows stage counts and active proposal metrics.

    Args:
        tenant_path (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TenantFunnelConfigurations]
    """

    kwargs = _get_kwargs(
        tenant_path=tenant_path,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    tenant_path: str,
    *,
    client: AuthenticatedClient,
) -> TenantFunnelConfigurations | None:
    """Tenant Funnelconfigurations

     View all sales funnel configurations available in your workspace. Each funnel
    represents a different sales process for various product lines or customer segments.
    Essential for understanding your sales methodologies and choosing the right process
    for new opportunities. Shows stage counts and active proposal metrics.

    Args:
        tenant_path (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        TenantFunnelConfigurations
    """

    return sync_detailed(
        tenant_path=tenant_path,
        client=client,
    ).parsed


async def asyncio_detailed(
    tenant_path: str,
    *,
    client: AuthenticatedClient,
) -> Response[TenantFunnelConfigurations]:
    """Tenant Funnelconfigurations

     View all sales funnel configurations available in your workspace. Each funnel
    represents a different sales process for various product lines or customer segments.
    Essential for understanding your sales methodologies and choosing the right process
    for new opportunities. Shows stage counts and active proposal metrics.

    Args:
        tenant_path (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TenantFunnelConfigurations]
    """

    kwargs = _get_kwargs(
        tenant_path=tenant_path,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    tenant_path: str,
    *,
    client: AuthenticatedClient,
) -> TenantFunnelConfigurations | None:
    """Tenant Funnelconfigurations

     View all sales funnel configurations available in your workspace. Each funnel
    represents a different sales process for various product lines or customer segments.
    Essential for understanding your sales methodologies and choosing the right process
    for new opportunities. Shows stage counts and active proposal metrics.

    Args:
        tenant_path (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        TenantFunnelConfigurations
    """

    return (
        await asyncio_detailed(
            tenant_path=tenant_path,
            client=client,
        )
    ).parsed
