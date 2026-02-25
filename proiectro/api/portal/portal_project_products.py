from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.output_customer_portal_project_products import (
    OutputCustomerPortalProjectProducts,
)
from ...types import Response


def _get_kwargs(
    customer_org_id: str,
    project_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/portal/{customer_org_id}/projects/{project_id}/products".format(
            customer_org_id=quote(str(customer_org_id), safe=""),
            project_id=quote(str(project_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> OutputCustomerPortalProjectProducts | None:
    if response.status_code == 200:
        response_200 = OutputCustomerPortalProjectProducts.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[OutputCustomerPortalProjectProducts]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    customer_org_id: str,
    project_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[OutputCustomerPortalProjectProducts]:
    """Portal Project Products

     Get products for a specific project in customer portal.
    Returns product list with status badges (In Progress, Finished, Accepted).

    Args:
        customer_org_id (str):
        project_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OutputCustomerPortalProjectProducts]
    """

    kwargs = _get_kwargs(
        customer_org_id=customer_org_id,
        project_id=project_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    customer_org_id: str,
    project_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> OutputCustomerPortalProjectProducts | None:
    """Portal Project Products

     Get products for a specific project in customer portal.
    Returns product list with status badges (In Progress, Finished, Accepted).

    Args:
        customer_org_id (str):
        project_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OutputCustomerPortalProjectProducts
    """

    return sync_detailed(
        customer_org_id=customer_org_id,
        project_id=project_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    customer_org_id: str,
    project_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[OutputCustomerPortalProjectProducts]:
    """Portal Project Products

     Get products for a specific project in customer portal.
    Returns product list with status badges (In Progress, Finished, Accepted).

    Args:
        customer_org_id (str):
        project_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OutputCustomerPortalProjectProducts]
    """

    kwargs = _get_kwargs(
        customer_org_id=customer_org_id,
        project_id=project_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    customer_org_id: str,
    project_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> OutputCustomerPortalProjectProducts | None:
    """Portal Project Products

     Get products for a specific project in customer portal.
    Returns product list with status badges (In Progress, Finished, Accepted).

    Args:
        customer_org_id (str):
        project_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OutputCustomerPortalProjectProducts
    """

    return (
        await asyncio_detailed(
            customer_org_id=customer_org_id,
            project_id=project_id,
            client=client,
        )
    ).parsed
