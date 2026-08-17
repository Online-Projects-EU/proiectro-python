from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.company_enrichment_result_schema import CompanyEnrichmentResultSchema
from ...types import Response


def _get_kwargs(
    tenant_path: str,
    cui: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/{tenant_path}/enrich_company/{cui}".format(
            tenant_path=quote(str(tenant_path), safe=""),
            cui=quote(str(cui), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> CompanyEnrichmentResultSchema | None:
    if response.status_code == 200:
        response_200 = CompanyEnrichmentResultSchema.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[CompanyEnrichmentResultSchema]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    tenant_path: str,
    cui: str,
    *,
    client: AuthenticatedClient,
) -> Response[CompanyEnrichmentResultSchema]:
    """Enrich Company

     Look up a Romanian company by CUI via the ANAF public API.
    Returns company name, registration number, VAT status, and address.
    Used to auto-fill legal entity forms.

    Args:
        tenant_path (str):
        cui (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CompanyEnrichmentResultSchema]
    """

    kwargs = _get_kwargs(
        tenant_path=tenant_path,
        cui=cui,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    tenant_path: str,
    cui: str,
    *,
    client: AuthenticatedClient,
) -> CompanyEnrichmentResultSchema | None:
    """Enrich Company

     Look up a Romanian company by CUI via the ANAF public API.
    Returns company name, registration number, VAT status, and address.
    Used to auto-fill legal entity forms.

    Args:
        tenant_path (str):
        cui (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CompanyEnrichmentResultSchema
    """

    return sync_detailed(
        tenant_path=tenant_path,
        cui=cui,
        client=client,
    ).parsed


async def asyncio_detailed(
    tenant_path: str,
    cui: str,
    *,
    client: AuthenticatedClient,
) -> Response[CompanyEnrichmentResultSchema]:
    """Enrich Company

     Look up a Romanian company by CUI via the ANAF public API.
    Returns company name, registration number, VAT status, and address.
    Used to auto-fill legal entity forms.

    Args:
        tenant_path (str):
        cui (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CompanyEnrichmentResultSchema]
    """

    kwargs = _get_kwargs(
        tenant_path=tenant_path,
        cui=cui,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    tenant_path: str,
    cui: str,
    *,
    client: AuthenticatedClient,
) -> CompanyEnrichmentResultSchema | None:
    """Enrich Company

     Look up a Romanian company by CUI via the ANAF public API.
    Returns company name, registration number, VAT status, and address.
    Used to auto-fill legal entity forms.

    Args:
        tenant_path (str):
        cui (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CompanyEnrichmentResultSchema
    """

    return (
        await asyncio_detailed(
            tenant_path=tenant_path,
            cui=cui,
            client=client,
        )
    ).parsed
