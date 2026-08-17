from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.output_document_tags import OutputDocumentTags
from ...types import Response


def _get_kwargs(
    tenant_path: str,
    document_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/{tenant_path}/document_tags/{document_id}".format(
            tenant_path=quote(str(tenant_path), safe=""),
            document_id=quote(str(document_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> OutputDocumentTags | None:
    if response.status_code == 200:
        response_200 = OutputDocumentTags.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[OutputDocumentTags]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    tenant_path: str,
    document_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[OutputDocumentTags]:
    """Document Tags

     Show the tags applied to a document, and the tags still available to apply. Tags group
    documents by kind, department or confidentiality so the list can be sliced without
    remembering where a file was put.

    Args:
        tenant_path (str):
        document_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OutputDocumentTags]
    """

    kwargs = _get_kwargs(
        tenant_path=tenant_path,
        document_id=document_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    tenant_path: str,
    document_id: str,
    *,
    client: AuthenticatedClient,
) -> OutputDocumentTags | None:
    """Document Tags

     Show the tags applied to a document, and the tags still available to apply. Tags group
    documents by kind, department or confidentiality so the list can be sliced without
    remembering where a file was put.

    Args:
        tenant_path (str):
        document_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OutputDocumentTags
    """

    return sync_detailed(
        tenant_path=tenant_path,
        document_id=document_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    tenant_path: str,
    document_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[OutputDocumentTags]:
    """Document Tags

     Show the tags applied to a document, and the tags still available to apply. Tags group
    documents by kind, department or confidentiality so the list can be sliced without
    remembering where a file was put.

    Args:
        tenant_path (str):
        document_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OutputDocumentTags]
    """

    kwargs = _get_kwargs(
        tenant_path=tenant_path,
        document_id=document_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    tenant_path: str,
    document_id: str,
    *,
    client: AuthenticatedClient,
) -> OutputDocumentTags | None:
    """Document Tags

     Show the tags applied to a document, and the tags still available to apply. Tags group
    documents by kind, department or confidentiality so the list can be sliced without
    remembering where a file was put.

    Args:
        tenant_path (str):
        document_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OutputDocumentTags
    """

    return (
        await asyncio_detailed(
            tenant_path=tenant_path,
            document_id=document_id,
            client=client,
        )
    ).parsed
