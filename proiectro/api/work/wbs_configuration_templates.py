from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.wbs_configuration_templates import WBSConfigurationTemplates
from ...types import Response


def _get_kwargs(
    tenant_path: str,
    wbs_configuration_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/{tenant_path}/wbs_configuration_templates/{wbs_configuration_id}".format(
            tenant_path=quote(str(tenant_path), safe=""),
            wbs_configuration_id=quote(str(wbs_configuration_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> WBSConfigurationTemplates | None:
    if response.status_code == 200:
        response_200 = WBSConfigurationTemplates.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[WBSConfigurationTemplates]:
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
) -> Response[WBSConfigurationTemplates]:
    """Wbs Configuration Templates

     Retrieve all root-level work item templates using this WBS Configuration. These templates
    follow the structural rules defined in this configuration and can serve as standardized
    starting points for new projects. Only top-level templates are shown - their child templates
    are managed within the template hierarchy. Both active and inactive templates are displayed.

    Args:
        tenant_path (str):
        wbs_configuration_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[WBSConfigurationTemplates]
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
) -> WBSConfigurationTemplates | None:
    """Wbs Configuration Templates

     Retrieve all root-level work item templates using this WBS Configuration. These templates
    follow the structural rules defined in this configuration and can serve as standardized
    starting points for new projects. Only top-level templates are shown - their child templates
    are managed within the template hierarchy. Both active and inactive templates are displayed.

    Args:
        tenant_path (str):
        wbs_configuration_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        WBSConfigurationTemplates
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
) -> Response[WBSConfigurationTemplates]:
    """Wbs Configuration Templates

     Retrieve all root-level work item templates using this WBS Configuration. These templates
    follow the structural rules defined in this configuration and can serve as standardized
    starting points for new projects. Only top-level templates are shown - their child templates
    are managed within the template hierarchy. Both active and inactive templates are displayed.

    Args:
        tenant_path (str):
        wbs_configuration_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[WBSConfigurationTemplates]
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
) -> WBSConfigurationTemplates | None:
    """Wbs Configuration Templates

     Retrieve all root-level work item templates using this WBS Configuration. These templates
    follow the structural rules defined in this configuration and can serve as standardized
    starting points for new projects. Only top-level templates are shown - their child templates
    are managed within the template hierarchy. Both active and inactive templates are displayed.

    Args:
        tenant_path (str):
        wbs_configuration_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        WBSConfigurationTemplates
    """

    return (
        await asyncio_detailed(
            tenant_path=tenant_path,
            wbs_configuration_id=wbs_configuration_id,
            client=client,
        )
    ).parsed
