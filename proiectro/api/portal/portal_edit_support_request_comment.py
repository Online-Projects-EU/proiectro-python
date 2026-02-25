from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_response import APIResponse
from ...models.edit_external_support_request_comment import (
    EditExternalSupportRequestComment,
)
from ...types import Response


def _get_kwargs(
    customer_org_id: str,
    support_request_id: str,
    comment_id: str,
    *,
    body: EditExternalSupportRequestComment,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/api/v1/portal/{customer_org_id}/support_requests/{support_request_id}/comments/{comment_id}/edit".format(
            customer_org_id=quote(str(customer_org_id), safe=""),
            support_request_id=quote(str(support_request_id), safe=""),
            comment_id=quote(str(comment_id), safe=""),
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
    customer_org_id: str,
    support_request_id: str,
    comment_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: EditExternalSupportRequestComment,
) -> Response[APIResponse]:
    """Portal Edit Support Request Comment

     Edit your own comment on a support request. You can only edit comments that you authored.
    This allows you to correct mistakes or add additional information to your previous comments.

    Args:
        customer_org_id (str):
        support_request_id (str):
        comment_id (str):
        body (EditExternalSupportRequestComment):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[APIResponse]
    """

    kwargs = _get_kwargs(
        customer_org_id=customer_org_id,
        support_request_id=support_request_id,
        comment_id=comment_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    customer_org_id: str,
    support_request_id: str,
    comment_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: EditExternalSupportRequestComment,
) -> APIResponse | None:
    """Portal Edit Support Request Comment

     Edit your own comment on a support request. You can only edit comments that you authored.
    This allows you to correct mistakes or add additional information to your previous comments.

    Args:
        customer_org_id (str):
        support_request_id (str):
        comment_id (str):
        body (EditExternalSupportRequestComment):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        APIResponse
    """

    return sync_detailed(
        customer_org_id=customer_org_id,
        support_request_id=support_request_id,
        comment_id=comment_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    customer_org_id: str,
    support_request_id: str,
    comment_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: EditExternalSupportRequestComment,
) -> Response[APIResponse]:
    """Portal Edit Support Request Comment

     Edit your own comment on a support request. You can only edit comments that you authored.
    This allows you to correct mistakes or add additional information to your previous comments.

    Args:
        customer_org_id (str):
        support_request_id (str):
        comment_id (str):
        body (EditExternalSupportRequestComment):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[APIResponse]
    """

    kwargs = _get_kwargs(
        customer_org_id=customer_org_id,
        support_request_id=support_request_id,
        comment_id=comment_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    customer_org_id: str,
    support_request_id: str,
    comment_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: EditExternalSupportRequestComment,
) -> APIResponse | None:
    """Portal Edit Support Request Comment

     Edit your own comment on a support request. You can only edit comments that you authored.
    This allows you to correct mistakes or add additional information to your previous comments.

    Args:
        customer_org_id (str):
        support_request_id (str):
        comment_id (str):
        body (EditExternalSupportRequestComment):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        APIResponse
    """

    return (
        await asyncio_detailed(
            customer_org_id=customer_org_id,
            support_request_id=support_request_id,
            comment_id=comment_id,
            client=client,
            body=body,
        )
    ).parsed
