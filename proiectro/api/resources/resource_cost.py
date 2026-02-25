from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.resource_cost_output import ResourceCostOutput
from ...types import Response


def _get_kwargs(
    tenant_path: str,
    resource_id: str,
    cost_type_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/{tenant_path}/resource_cost/{resource_id}/{cost_type_id}".format(
            tenant_path=quote(str(tenant_path), safe=""),
            resource_id=quote(str(resource_id), safe=""),
            cost_type_id=quote(str(cost_type_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ResourceCostOutput | None:
    if response.status_code == 200:
        response_200 = ResourceCostOutput.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ResourceCostOutput]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    tenant_path: str,
    resource_id: str,
    cost_type_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[ResourceCostOutput]:
    """Resource Cost

     Examine detailed cost history for a specific resource and cost type combination.
    Shows rate evolution over time with correction audit trail. Critical for historical
    project cost analysis and rate validation. Includes all adjustments and corrections
    for accurate financial reconciliation.

    Args:
        tenant_path (str):
        resource_id (str):
        cost_type_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ResourceCostOutput]
    """

    kwargs = _get_kwargs(
        tenant_path=tenant_path,
        resource_id=resource_id,
        cost_type_id=cost_type_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    tenant_path: str,
    resource_id: str,
    cost_type_id: str,
    *,
    client: AuthenticatedClient,
) -> ResourceCostOutput | None:
    """Resource Cost

     Examine detailed cost history for a specific resource and cost type combination.
    Shows rate evolution over time with correction audit trail. Critical for historical
    project cost analysis and rate validation. Includes all adjustments and corrections
    for accurate financial reconciliation.

    Args:
        tenant_path (str):
        resource_id (str):
        cost_type_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ResourceCostOutput
    """

    return sync_detailed(
        tenant_path=tenant_path,
        resource_id=resource_id,
        cost_type_id=cost_type_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    tenant_path: str,
    resource_id: str,
    cost_type_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[ResourceCostOutput]:
    """Resource Cost

     Examine detailed cost history for a specific resource and cost type combination.
    Shows rate evolution over time with correction audit trail. Critical for historical
    project cost analysis and rate validation. Includes all adjustments and corrections
    for accurate financial reconciliation.

    Args:
        tenant_path (str):
        resource_id (str):
        cost_type_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ResourceCostOutput]
    """

    kwargs = _get_kwargs(
        tenant_path=tenant_path,
        resource_id=resource_id,
        cost_type_id=cost_type_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    tenant_path: str,
    resource_id: str,
    cost_type_id: str,
    *,
    client: AuthenticatedClient,
) -> ResourceCostOutput | None:
    """Resource Cost

     Examine detailed cost history for a specific resource and cost type combination.
    Shows rate evolution over time with correction audit trail. Critical for historical
    project cost analysis and rate validation. Includes all adjustments and corrections
    for accurate financial reconciliation.

    Args:
        tenant_path (str):
        resource_id (str):
        cost_type_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ResourceCostOutput
    """

    return (
        await asyncio_detailed(
            tenant_path=tenant_path,
            resource_id=resource_id,
            cost_type_id=cost_type_id,
            client=client,
        )
    ).parsed
