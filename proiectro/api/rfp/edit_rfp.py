from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_response import APIResponse
from ...models.edit_rfp import EditRFP
from ...types import Response


def _get_kwargs(
    tenant_path: str,
    rfp_id: str,
    *,
    body: EditRFP,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/api/v1/{tenant_path}/edit_rfp/{rfp_id}".format(
            tenant_path=quote(str(tenant_path), safe=""),
            rfp_id=quote(str(rfp_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> APIResponse | None:
    if response.status_code == 200:
        response_200 = APIResponse.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = APIResponse.from_dict(response.json())

        return response_400

    if response.status_code == 422:
        response_422 = APIResponse.from_dict(response.json())

        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[APIResponse]:
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
    body: EditRFP,
) -> Response[APIResponse]:
    """Edit Rfp

     Edit an RFP. Full editing in DRAFT, limited editing in PUBLISHED/CLOSED.

    Args:
        tenant_path (str):
        rfp_id (str):
        body (EditRFP): Input schema for editing an RFP.

            In DRAFT status, all fields can be edited.
            In PUBLISHED/CLOSED status, only description and submission_deadline can be changed.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[APIResponse]
    """

    kwargs = _get_kwargs(
        tenant_path=tenant_path,
        rfp_id=rfp_id,
        body=body,
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
    body: EditRFP,
) -> APIResponse | None:
    """Edit Rfp

     Edit an RFP. Full editing in DRAFT, limited editing in PUBLISHED/CLOSED.

    Args:
        tenant_path (str):
        rfp_id (str):
        body (EditRFP): Input schema for editing an RFP.

            In DRAFT status, all fields can be edited.
            In PUBLISHED/CLOSED status, only description and submission_deadline can be changed.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        APIResponse
    """

    return sync_detailed(
        tenant_path=tenant_path,
        rfp_id=rfp_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    tenant_path: str,
    rfp_id: str,
    *,
    client: AuthenticatedClient,
    body: EditRFP,
) -> Response[APIResponse]:
    """Edit Rfp

     Edit an RFP. Full editing in DRAFT, limited editing in PUBLISHED/CLOSED.

    Args:
        tenant_path (str):
        rfp_id (str):
        body (EditRFP): Input schema for editing an RFP.

            In DRAFT status, all fields can be edited.
            In PUBLISHED/CLOSED status, only description and submission_deadline can be changed.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[APIResponse]
    """

    kwargs = _get_kwargs(
        tenant_path=tenant_path,
        rfp_id=rfp_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    tenant_path: str,
    rfp_id: str,
    *,
    client: AuthenticatedClient,
    body: EditRFP,
) -> APIResponse | None:
    """Edit Rfp

     Edit an RFP. Full editing in DRAFT, limited editing in PUBLISHED/CLOSED.

    Args:
        tenant_path (str):
        rfp_id (str):
        body (EditRFP): Input schema for editing an RFP.

            In DRAFT status, all fields can be edited.
            In PUBLISHED/CLOSED status, only description and submission_deadline can be changed.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        APIResponse
    """

    return (
        await asyncio_detailed(
            tenant_path=tenant_path,
            rfp_id=rfp_id,
            client=client,
            body=body,
        )
    ).parsed
