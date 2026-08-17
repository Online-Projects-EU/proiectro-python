from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.automation_action_condition_input import AutomationActionConditionInput
from ...models.automation_condition_filters_response import (
    AutomationConditionFiltersResponse,
)
from ...types import Response


def _get_kwargs(
    tenant_path: str,
    *,
    body: AutomationActionConditionInput,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/{tenant_path}/automation_action_conditions".format(
            tenant_path=quote(str(tenant_path), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AutomationConditionFiltersResponse | None:
    if response.status_code == 200:
        response_200 = AutomationConditionFiltersResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[AutomationConditionFiltersResponse]:
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
    body: AutomationActionConditionInput,
) -> Response[AutomationConditionFiltersResponse]:
    """Automation Action Conditions

     Get available condition fields and operators for an action in the pipeline.
    Same structure as trigger filters so the template is a carbon copy.

    Args:
        tenant_path (str):
        body (AutomationActionConditionInput): Input: get condition fields for an action in the
            pipeline.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AutomationConditionFiltersResponse]
    """

    kwargs = _get_kwargs(
        tenant_path=tenant_path,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    tenant_path: str,
    *,
    client: AuthenticatedClient,
    body: AutomationActionConditionInput,
) -> AutomationConditionFiltersResponse | None:
    """Automation Action Conditions

     Get available condition fields and operators for an action in the pipeline.
    Same structure as trigger filters so the template is a carbon copy.

    Args:
        tenant_path (str):
        body (AutomationActionConditionInput): Input: get condition fields for an action in the
            pipeline.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AutomationConditionFiltersResponse
    """

    return sync_detailed(
        tenant_path=tenant_path,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    tenant_path: str,
    *,
    client: AuthenticatedClient,
    body: AutomationActionConditionInput,
) -> Response[AutomationConditionFiltersResponse]:
    """Automation Action Conditions

     Get available condition fields and operators for an action in the pipeline.
    Same structure as trigger filters so the template is a carbon copy.

    Args:
        tenant_path (str):
        body (AutomationActionConditionInput): Input: get condition fields for an action in the
            pipeline.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AutomationConditionFiltersResponse]
    """

    kwargs = _get_kwargs(
        tenant_path=tenant_path,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    tenant_path: str,
    *,
    client: AuthenticatedClient,
    body: AutomationActionConditionInput,
) -> AutomationConditionFiltersResponse | None:
    """Automation Action Conditions

     Get available condition fields and operators for an action in the pipeline.
    Same structure as trigger filters so the template is a carbon copy.

    Args:
        tenant_path (str):
        body (AutomationActionConditionInput): Input: get condition fields for an action in the
            pipeline.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AutomationConditionFiltersResponse
    """

    return (
        await asyncio_detailed(
            tenant_path=tenant_path,
            client=client,
            body=body,
        )
    ).parsed
