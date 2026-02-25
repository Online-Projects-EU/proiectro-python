from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.product_work_items import ProductWorkItems
from ...types import Response


def _get_kwargs(
    tenant_path: str,
    project_id: str,
    product_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/{tenant_path}/project_product_work_items/{project_id}/{product_id}".format(
            tenant_path=quote(str(tenant_path), safe=""),
            project_id=quote(str(project_id), safe=""),
            product_id=quote(str(product_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ProductWorkItems | None:
    if response.status_code == 200:
        response_200 = ProductWorkItems.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ProductWorkItems]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    tenant_path: str,
    project_id: str,
    product_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[ProductWorkItems]:
    """Project Product Work Items

     List all work items linked to a specific product in a project.
    Shows flat list of work items with hierarchy IDs, types, and status.
    Useful for product scope analysis and understanding product composition.

    Args:
        tenant_path (str):
        project_id (str):
        product_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ProductWorkItems]
    """

    kwargs = _get_kwargs(
        tenant_path=tenant_path,
        project_id=project_id,
        product_id=product_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    tenant_path: str,
    project_id: str,
    product_id: str,
    *,
    client: AuthenticatedClient,
) -> ProductWorkItems | None:
    """Project Product Work Items

     List all work items linked to a specific product in a project.
    Shows flat list of work items with hierarchy IDs, types, and status.
    Useful for product scope analysis and understanding product composition.

    Args:
        tenant_path (str):
        project_id (str):
        product_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ProductWorkItems
    """

    return sync_detailed(
        tenant_path=tenant_path,
        project_id=project_id,
        product_id=product_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    tenant_path: str,
    project_id: str,
    product_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[ProductWorkItems]:
    """Project Product Work Items

     List all work items linked to a specific product in a project.
    Shows flat list of work items with hierarchy IDs, types, and status.
    Useful for product scope analysis and understanding product composition.

    Args:
        tenant_path (str):
        project_id (str):
        product_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ProductWorkItems]
    """

    kwargs = _get_kwargs(
        tenant_path=tenant_path,
        project_id=project_id,
        product_id=product_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    tenant_path: str,
    project_id: str,
    product_id: str,
    *,
    client: AuthenticatedClient,
) -> ProductWorkItems | None:
    """Project Product Work Items

     List all work items linked to a specific product in a project.
    Shows flat list of work items with hierarchy IDs, types, and status.
    Useful for product scope analysis and understanding product composition.

    Args:
        tenant_path (str):
        project_id (str):
        product_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ProductWorkItems
    """

    return (
        await asyncio_detailed(
            tenant_path=tenant_path,
            project_id=project_id,
            product_id=product_id,
            client=client,
        )
    ).parsed
