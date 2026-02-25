from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.tenant_funnel_configuration_stages import TenantFunnelConfigurationStages
from ...types import Response


def _get_kwargs(
    tenant_path: str,
    funnel_configuration_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/{tenant_path}/funnel_configuration_stages/{funnel_configuration_id}".format(
            tenant_path=quote(str(tenant_path), safe=""),
            funnel_configuration_id=quote(str(funnel_configuration_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> TenantFunnelConfigurationStages | None:
    if response.status_code == 200:
        response_200 = TenantFunnelConfigurationStages.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[TenantFunnelConfigurationStages]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    tenant_path: str,
    funnel_configuration_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[TenantFunnelConfigurationStages]:
    """Tenant Funnel Configuration Stages

     Examine the stage progression for a specific sales funnel configuration. Shows
    qualification gates, conversion probabilities, and typical duration for each stage.
    Essential for training sales teams and setting expectations. Stage definitions
    drive reporting metrics and forecast accuracy.

    Args:
        tenant_path (str):
        funnel_configuration_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TenantFunnelConfigurationStages]
    """

    kwargs = _get_kwargs(
        tenant_path=tenant_path,
        funnel_configuration_id=funnel_configuration_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    tenant_path: str,
    funnel_configuration_id: str,
    *,
    client: AuthenticatedClient,
) -> TenantFunnelConfigurationStages | None:
    """Tenant Funnel Configuration Stages

     Examine the stage progression for a specific sales funnel configuration. Shows
    qualification gates, conversion probabilities, and typical duration for each stage.
    Essential for training sales teams and setting expectations. Stage definitions
    drive reporting metrics and forecast accuracy.

    Args:
        tenant_path (str):
        funnel_configuration_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        TenantFunnelConfigurationStages
    """

    return sync_detailed(
        tenant_path=tenant_path,
        funnel_configuration_id=funnel_configuration_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    tenant_path: str,
    funnel_configuration_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[TenantFunnelConfigurationStages]:
    """Tenant Funnel Configuration Stages

     Examine the stage progression for a specific sales funnel configuration. Shows
    qualification gates, conversion probabilities, and typical duration for each stage.
    Essential for training sales teams and setting expectations. Stage definitions
    drive reporting metrics and forecast accuracy.

    Args:
        tenant_path (str):
        funnel_configuration_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TenantFunnelConfigurationStages]
    """

    kwargs = _get_kwargs(
        tenant_path=tenant_path,
        funnel_configuration_id=funnel_configuration_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    tenant_path: str,
    funnel_configuration_id: str,
    *,
    client: AuthenticatedClient,
) -> TenantFunnelConfigurationStages | None:
    """Tenant Funnel Configuration Stages

     Examine the stage progression for a specific sales funnel configuration. Shows
    qualification gates, conversion probabilities, and typical duration for each stage.
    Essential for training sales teams and setting expectations. Stage definitions
    drive reporting metrics and forecast accuracy.

    Args:
        tenant_path (str):
        funnel_configuration_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        TenantFunnelConfigurationStages
    """

    return (
        await asyncio_detailed(
            tenant_path=tenant_path,
            funnel_configuration_id=funnel_configuration_id,
            client=client,
        )
    ).parsed
