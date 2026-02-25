from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.output_wbs_configuration_rules import OutputWBSConfigurationRules
from ...types import Response


def _get_kwargs(
    tenant_path: str,
    wbs_configuration_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/{tenant_path}/wbs_configuration_rules/{wbs_configuration_id}".format(
            tenant_path=quote(str(tenant_path), safe=""),
            wbs_configuration_id=quote(str(wbs_configuration_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> OutputWBSConfigurationRules | None:
    if response.status_code == 200:
        response_200 = OutputWBSConfigurationRules.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[OutputWBSConfigurationRules]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    tenant_path: str,
    wbs_configuration_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[OutputWBSConfigurationRules]:
    """Tenant Wbs Configuration Rules

     Examine the structural rules defining valid work item relationships in a configuration.
    Shows which item types can contain other types, preventing illogical hierarchies
    like tasks containing deliverables. Essential for training project managers on proper
    decomposition and troubleshooting structure violations. Rules enforce consistency
    across all projects using the configuration.

    Args:
        tenant_path (str):
        wbs_configuration_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OutputWBSConfigurationRules]
    """

    kwargs = _get_kwargs(
        tenant_path=tenant_path,
        wbs_configuration_id=wbs_configuration_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    tenant_path: str,
    wbs_configuration_id: str,
    *,
    client: AuthenticatedClient,
) -> OutputWBSConfigurationRules | None:
    """Tenant Wbs Configuration Rules

     Examine the structural rules defining valid work item relationships in a configuration.
    Shows which item types can contain other types, preventing illogical hierarchies
    like tasks containing deliverables. Essential for training project managers on proper
    decomposition and troubleshooting structure violations. Rules enforce consistency
    across all projects using the configuration.

    Args:
        tenant_path (str):
        wbs_configuration_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OutputWBSConfigurationRules
    """

    return sync_detailed(
        tenant_path=tenant_path,
        wbs_configuration_id=wbs_configuration_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    tenant_path: str,
    wbs_configuration_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[OutputWBSConfigurationRules]:
    """Tenant Wbs Configuration Rules

     Examine the structural rules defining valid work item relationships in a configuration.
    Shows which item types can contain other types, preventing illogical hierarchies
    like tasks containing deliverables. Essential for training project managers on proper
    decomposition and troubleshooting structure violations. Rules enforce consistency
    across all projects using the configuration.

    Args:
        tenant_path (str):
        wbs_configuration_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OutputWBSConfigurationRules]
    """

    kwargs = _get_kwargs(
        tenant_path=tenant_path,
        wbs_configuration_id=wbs_configuration_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    tenant_path: str,
    wbs_configuration_id: str,
    *,
    client: AuthenticatedClient,
) -> OutputWBSConfigurationRules | None:
    """Tenant Wbs Configuration Rules

     Examine the structural rules defining valid work item relationships in a configuration.
    Shows which item types can contain other types, preventing illogical hierarchies
    like tasks containing deliverables. Essential for training project managers on proper
    decomposition and troubleshooting structure violations. Rules enforce consistency
    across all projects using the configuration.

    Args:
        tenant_path (str):
        wbs_configuration_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OutputWBSConfigurationRules
    """

    return (
        await asyncio_detailed(
            tenant_path=tenant_path,
            wbs_configuration_id=wbs_configuration_id,
            client=client,
        )
    ).parsed
