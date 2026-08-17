from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_response import APIResponse
from ...models.automation_pipeline_variables_response import (
    AutomationPipelineVariablesResponse,
)
from ...types import Response


def _get_kwargs(
    tenant_path: str,
    rule_id: str,
    action_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/{tenant_path}/automation_pipeline_variables/{rule_id}/{action_id}".format(
            tenant_path=quote(str(tenant_path), safe=""),
            rule_id=quote(str(rule_id), safe=""),
            action_id=quote(str(action_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> APIResponse | AutomationPipelineVariablesResponse | None:
    if response.status_code == 200:
        response_200 = AutomationPipelineVariablesResponse.from_dict(response.json())

        return response_200

    if response.status_code == 404:
        response_404 = APIResponse.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[APIResponse | AutomationPipelineVariablesResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    tenant_path: str,
    rule_id: str,
    action_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[APIResponse | AutomationPipelineVariablesResponse]:
    """Automation Pipeline Variables

     Get all variables available at a given action's position in the pipeline.
    Includes event variables, trigger state, and output fields from preceding actions.

    Args:
        tenant_path (str):
        rule_id (str):
        action_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[APIResponse | AutomationPipelineVariablesResponse]
    """

    kwargs = _get_kwargs(
        tenant_path=tenant_path,
        rule_id=rule_id,
        action_id=action_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    tenant_path: str,
    rule_id: str,
    action_id: str,
    *,
    client: AuthenticatedClient,
) -> APIResponse | AutomationPipelineVariablesResponse | None:
    """Automation Pipeline Variables

     Get all variables available at a given action's position in the pipeline.
    Includes event variables, trigger state, and output fields from preceding actions.

    Args:
        tenant_path (str):
        rule_id (str):
        action_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        APIResponse | AutomationPipelineVariablesResponse
    """

    return sync_detailed(
        tenant_path=tenant_path,
        rule_id=rule_id,
        action_id=action_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    tenant_path: str,
    rule_id: str,
    action_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[APIResponse | AutomationPipelineVariablesResponse]:
    """Automation Pipeline Variables

     Get all variables available at a given action's position in the pipeline.
    Includes event variables, trigger state, and output fields from preceding actions.

    Args:
        tenant_path (str):
        rule_id (str):
        action_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[APIResponse | AutomationPipelineVariablesResponse]
    """

    kwargs = _get_kwargs(
        tenant_path=tenant_path,
        rule_id=rule_id,
        action_id=action_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    tenant_path: str,
    rule_id: str,
    action_id: str,
    *,
    client: AuthenticatedClient,
) -> APIResponse | AutomationPipelineVariablesResponse | None:
    """Automation Pipeline Variables

     Get all variables available at a given action's position in the pipeline.
    Includes event variables, trigger state, and output fields from preceding actions.

    Args:
        tenant_path (str):
        rule_id (str):
        action_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        APIResponse | AutomationPipelineVariablesResponse
    """

    return (
        await asyncio_detailed(
            tenant_path=tenant_path,
            rule_id=rule_id,
            action_id=action_id,
            client=client,
        )
    ).parsed
