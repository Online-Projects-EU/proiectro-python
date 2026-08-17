from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_response import APIResponse
from ...models.import_leads_multi_part_body_params import ImportLeadsMultiPartBodyParams
from ...models.output_lead_import_summary import OutputLeadImportSummary
from ...models.pydantic_detail import PydanticDetail
from ...types import Response


def _get_kwargs(
    tenant_path: str,
    *,
    body: ImportLeadsMultiPartBodyParams,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/{tenant_path}/import_leads".format(
            tenant_path=quote(str(tenant_path), safe=""),
        ),
    }

    _kwargs["files"] = body.to_multipart()

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> APIResponse | OutputLeadImportSummary | PydanticDetail | None:
    if response.status_code == 200:
        response_200 = OutputLeadImportSummary.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = APIResponse.from_dict(response.json())

        return response_400

    if response.status_code == 403:
        response_403 = APIResponse.from_dict(response.json())

        return response_403

    if response.status_code == 410:
        response_410 = APIResponse.from_dict(response.json())

        return response_410

    if response.status_code == 422:
        response_422 = PydanticDetail.from_dict(response.json())

        return response_422

    if response.status_code == 429:
        response_429 = APIResponse.from_dict(response.json())

        return response_429

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[APIResponse | OutputLeadImportSummary | PydanticDetail]:
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
    body: ImportLeadsMultiPartBodyParams,
) -> Response[APIResponse | OutputLeadImportSummary | PydanticDetail]:
    """Import Leads

     Accepts EITHER a file (single-step import) OR an upload_token in metadata
    pointing to a cached preview (Confirm-from-preview step). The function
    rejects when neither is present.

    Args:
        tenant_path (str):
        body (ImportLeadsMultiPartBodyParams):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[APIResponse | OutputLeadImportSummary | PydanticDetail]
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
    body: ImportLeadsMultiPartBodyParams,
) -> APIResponse | OutputLeadImportSummary | PydanticDetail | None:
    """Import Leads

     Accepts EITHER a file (single-step import) OR an upload_token in metadata
    pointing to a cached preview (Confirm-from-preview step). The function
    rejects when neither is present.

    Args:
        tenant_path (str):
        body (ImportLeadsMultiPartBodyParams):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        APIResponse | OutputLeadImportSummary | PydanticDetail
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
    body: ImportLeadsMultiPartBodyParams,
) -> Response[APIResponse | OutputLeadImportSummary | PydanticDetail]:
    """Import Leads

     Accepts EITHER a file (single-step import) OR an upload_token in metadata
    pointing to a cached preview (Confirm-from-preview step). The function
    rejects when neither is present.

    Args:
        tenant_path (str):
        body (ImportLeadsMultiPartBodyParams):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[APIResponse | OutputLeadImportSummary | PydanticDetail]
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
    body: ImportLeadsMultiPartBodyParams,
) -> APIResponse | OutputLeadImportSummary | PydanticDetail | None:
    """Import Leads

     Accepts EITHER a file (single-step import) OR an upload_token in metadata
    pointing to a cached preview (Confirm-from-preview step). The function
    rejects when neither is present.

    Args:
        tenant_path (str):
        body (ImportLeadsMultiPartBodyParams):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        APIResponse | OutputLeadImportSummary | PydanticDetail
    """

    return (
        await asyncio_detailed(
            tenant_path=tenant_path,
            client=client,
            body=body,
        )
    ).parsed
