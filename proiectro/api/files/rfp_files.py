from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.output_file_names import OutputFileNames
from ...types import Response


def _get_kwargs(
    tenant_path: str,
    rfp_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/{tenant_path}/rfp_files/{rfp_id}".format(
            tenant_path=quote(str(tenant_path), safe=""),
            rfp_id=quote(str(rfp_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> OutputFileNames | None:
    if response.status_code == 200:
        response_200 = OutputFileNames.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[OutputFileNames]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    tenant_path: str,
    rfp_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[OutputFileNames]:
    """Rfp Files

     Access all documents attached to an RFP including specifications, requirements,
    and supporting materials. Returns secure signed URLs valid for limited time.
    Files are shared with partners who have received this RFP as a solicitation.

    Args:
        tenant_path (str):
        rfp_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OutputFileNames]
    """

    kwargs = _get_kwargs(
        tenant_path=tenant_path,
        rfp_id=rfp_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    tenant_path: str,
    rfp_id: str,
    *,
    client: AuthenticatedClient,
) -> OutputFileNames | None:
    """Rfp Files

     Access all documents attached to an RFP including specifications, requirements,
    and supporting materials. Returns secure signed URLs valid for limited time.
    Files are shared with partners who have received this RFP as a solicitation.

    Args:
        tenant_path (str):
        rfp_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OutputFileNames
    """

    return sync_detailed(
        tenant_path=tenant_path,
        rfp_id=rfp_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    tenant_path: str,
    rfp_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[OutputFileNames]:
    """Rfp Files

     Access all documents attached to an RFP including specifications, requirements,
    and supporting materials. Returns secure signed URLs valid for limited time.
    Files are shared with partners who have received this RFP as a solicitation.

    Args:
        tenant_path (str):
        rfp_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OutputFileNames]
    """

    kwargs = _get_kwargs(
        tenant_path=tenant_path,
        rfp_id=rfp_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    tenant_path: str,
    rfp_id: str,
    *,
    client: AuthenticatedClient,
) -> OutputFileNames | None:
    """Rfp Files

     Access all documents attached to an RFP including specifications, requirements,
    and supporting materials. Returns secure signed URLs valid for limited time.
    Files are shared with partners who have received this RFP as a solicitation.

    Args:
        tenant_path (str):
        rfp_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OutputFileNames
    """

    return (
        await asyncio_detailed(
            tenant_path=tenant_path,
            rfp_id=rfp_id,
            client=client,
        )
    ).parsed
