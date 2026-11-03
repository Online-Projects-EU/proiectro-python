from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_response import APIResponse
from ...models.import_orgs_multi_part_body_params import ImportOrgsMultiPartBodyParams
from ...models.output_csv_import_summary import OutputCsvImportSummary
from ...models.pydantic_detail import PydanticDetail
from ...types import Response


def _get_kwargs(
    tenant_path: str,
    *,
    body: ImportOrgsMultiPartBodyParams,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/{tenant_path}/import_orgs".format(
            tenant_path=quote(str(tenant_path), safe=""),
        ),
    }

    _kwargs["files"] = body.to_multipart()

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> APIResponse | OutputCsvImportSummary | PydanticDetail | None:
    if response.status_code == 200:
        response_200 = OutputCsvImportSummary.from_dict(response.json())

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

    if response.status_code == 413:
        response_413 = APIResponse.from_dict(response.json())

        return response_413

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
) -> Response[APIResponse | OutputCsvImportSummary | PydanticDetail]:
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
    body: ImportOrgsMultiPartBodyParams,
) -> Response[APIResponse | OutputCsvImportSummary | PydanticDetail]:
    """Import Orgs

     Import customers from a CSV, or from the upload token of a preview. A row matches a customer by
    tax ID, or by a name only one customer has, and an empty cell keeps the stored value; any other
    row adds a customer, with its legal details and one contact. Rows with errors are skipped.

    Args:
        tenant_path (str):
        body (ImportOrgsMultiPartBodyParams):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[APIResponse | OutputCsvImportSummary | PydanticDetail]
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
    body: ImportOrgsMultiPartBodyParams,
) -> APIResponse | OutputCsvImportSummary | PydanticDetail | None:
    """Import Orgs

     Import customers from a CSV, or from the upload token of a preview. A row matches a customer by
    tax ID, or by a name only one customer has, and an empty cell keeps the stored value; any other
    row adds a customer, with its legal details and one contact. Rows with errors are skipped.

    Args:
        tenant_path (str):
        body (ImportOrgsMultiPartBodyParams):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        APIResponse | OutputCsvImportSummary | PydanticDetail
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
    body: ImportOrgsMultiPartBodyParams,
) -> Response[APIResponse | OutputCsvImportSummary | PydanticDetail]:
    """Import Orgs

     Import customers from a CSV, or from the upload token of a preview. A row matches a customer by
    tax ID, or by a name only one customer has, and an empty cell keeps the stored value; any other
    row adds a customer, with its legal details and one contact. Rows with errors are skipped.

    Args:
        tenant_path (str):
        body (ImportOrgsMultiPartBodyParams):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[APIResponse | OutputCsvImportSummary | PydanticDetail]
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
    body: ImportOrgsMultiPartBodyParams,
) -> APIResponse | OutputCsvImportSummary | PydanticDetail | None:
    """Import Orgs

     Import customers from a CSV, or from the upload token of a preview. A row matches a customer by
    tax ID, or by a name only one customer has, and an empty cell keeps the stored value; any other
    row adds a customer, with its legal details and one contact. Rows with errors are skipped.

    Args:
        tenant_path (str):
        body (ImportOrgsMultiPartBodyParams):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        APIResponse | OutputCsvImportSummary | PydanticDetail
    """

    return (
        await asyncio_detailed(
            tenant_path=tenant_path,
            client=client,
            body=body,
        )
    ).parsed
