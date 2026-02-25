from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.catalog_template_data_response import CatalogTemplateDataResponse
from ...types import Response


def _get_kwargs(
    tenant_path: str,
    catalog_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/{tenant_path}/catalog_template_data/{catalog_id}".format(
            tenant_path=quote(str(tenant_path), safe=""),
            catalog_id=quote(str(catalog_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> CatalogTemplateDataResponse | None:
    if response.status_code == 200:
        response_200 = CatalogTemplateDataResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[CatalogTemplateDataResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    tenant_path: str,
    catalog_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[CatalogTemplateDataResponse]:
    """Catalog Template Data

     Retrieve standardized product templates from your catalog for quick proposal creation.
    Includes pre-configured pricing, specifications, and terms for consistency. Templates
    accelerate proposal generation while ensuring compliance with approved offerings.
    Customize after adding to proposals for customer-specific requirements.

    Args:
        tenant_path (str):
        catalog_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CatalogTemplateDataResponse]
    """

    kwargs = _get_kwargs(
        tenant_path=tenant_path,
        catalog_id=catalog_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    tenant_path: str,
    catalog_id: str,
    *,
    client: AuthenticatedClient,
) -> CatalogTemplateDataResponse | None:
    """Catalog Template Data

     Retrieve standardized product templates from your catalog for quick proposal creation.
    Includes pre-configured pricing, specifications, and terms for consistency. Templates
    accelerate proposal generation while ensuring compliance with approved offerings.
    Customize after adding to proposals for customer-specific requirements.

    Args:
        tenant_path (str):
        catalog_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CatalogTemplateDataResponse
    """

    return sync_detailed(
        tenant_path=tenant_path,
        catalog_id=catalog_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    tenant_path: str,
    catalog_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[CatalogTemplateDataResponse]:
    """Catalog Template Data

     Retrieve standardized product templates from your catalog for quick proposal creation.
    Includes pre-configured pricing, specifications, and terms for consistency. Templates
    accelerate proposal generation while ensuring compliance with approved offerings.
    Customize after adding to proposals for customer-specific requirements.

    Args:
        tenant_path (str):
        catalog_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CatalogTemplateDataResponse]
    """

    kwargs = _get_kwargs(
        tenant_path=tenant_path,
        catalog_id=catalog_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    tenant_path: str,
    catalog_id: str,
    *,
    client: AuthenticatedClient,
) -> CatalogTemplateDataResponse | None:
    """Catalog Template Data

     Retrieve standardized product templates from your catalog for quick proposal creation.
    Includes pre-configured pricing, specifications, and terms for consistency. Templates
    accelerate proposal generation while ensuring compliance with approved offerings.
    Customize after adding to proposals for customer-specific requirements.

    Args:
        tenant_path (str):
        catalog_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CatalogTemplateDataResponse
    """

    return (
        await asyncio_detailed(
            tenant_path=tenant_path,
            catalog_id=catalog_id,
            client=client,
        )
    ).parsed
