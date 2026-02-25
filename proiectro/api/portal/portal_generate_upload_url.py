from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_error import APIError
from ...models.api_response import APIResponse
from ...models.request_upload_url_gcs import RequestUploadUrlGCS
from ...models.upload_url_gcs import UploadUrlGCS
from ...types import Response


def _get_kwargs(
    customer_org_id: str,
    support_request_id: str,
    *,
    body: RequestUploadUrlGCS,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/portal/{customer_org_id}/support_requests/{support_request_id}/generate_upload_url".format(
            customer_org_id=quote(str(customer_org_id), safe=""),
            support_request_id=quote(str(support_request_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> APIError | APIResponse | UploadUrlGCS | None:
    if response.status_code == 200:
        response_200 = UploadUrlGCS.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = APIResponse.from_dict(response.json())

        return response_400

    if response.status_code == 409:
        response_409 = APIError.from_dict(response.json())

        return response_409

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[APIError | APIResponse | UploadUrlGCS]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    customer_org_id: str,
    support_request_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: RequestUploadUrlGCS,
) -> Response[APIError | APIResponse | UploadUrlGCS]:
    """Portal Generate Upload Url

     Generate signed upload URL for attaching files to support request.
    Org-level access: any team member from customer org can upload files.

    Args:
        customer_org_id (str):
        support_request_id (str):
        body (RequestUploadUrlGCS):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[APIError | APIResponse | UploadUrlGCS]
    """

    kwargs = _get_kwargs(
        customer_org_id=customer_org_id,
        support_request_id=support_request_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    customer_org_id: str,
    support_request_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: RequestUploadUrlGCS,
) -> APIError | APIResponse | UploadUrlGCS | None:
    """Portal Generate Upload Url

     Generate signed upload URL for attaching files to support request.
    Org-level access: any team member from customer org can upload files.

    Args:
        customer_org_id (str):
        support_request_id (str):
        body (RequestUploadUrlGCS):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        APIError | APIResponse | UploadUrlGCS
    """

    return sync_detailed(
        customer_org_id=customer_org_id,
        support_request_id=support_request_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    customer_org_id: str,
    support_request_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: RequestUploadUrlGCS,
) -> Response[APIError | APIResponse | UploadUrlGCS]:
    """Portal Generate Upload Url

     Generate signed upload URL for attaching files to support request.
    Org-level access: any team member from customer org can upload files.

    Args:
        customer_org_id (str):
        support_request_id (str):
        body (RequestUploadUrlGCS):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[APIError | APIResponse | UploadUrlGCS]
    """

    kwargs = _get_kwargs(
        customer_org_id=customer_org_id,
        support_request_id=support_request_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    customer_org_id: str,
    support_request_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: RequestUploadUrlGCS,
) -> APIError | APIResponse | UploadUrlGCS | None:
    """Portal Generate Upload Url

     Generate signed upload URL for attaching files to support request.
    Org-level access: any team member from customer org can upload files.

    Args:
        customer_org_id (str):
        support_request_id (str):
        body (RequestUploadUrlGCS):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        APIError | APIResponse | UploadUrlGCS
    """

    return (
        await asyncio_detailed(
            customer_org_id=customer_org_id,
            support_request_id=support_request_id,
            client=client,
            body=body,
        )
    ).parsed
