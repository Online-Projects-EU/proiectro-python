from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_response import APIResponse
from ...models.submit_custom_form import SubmitCustomForm
from ...models.submit_portal_form_response import SubmitPortalFormResponse
from ...types import Response


def _get_kwargs(
    customer_org_id: str,
    link_id: str,
    *,
    body: SubmitCustomForm,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/portal/{customer_org_id}/submit_portal_form/{link_id}".format(
            customer_org_id=quote(str(customer_org_id), safe=""),
            link_id=quote(str(link_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> APIResponse | SubmitPortalFormResponse | None:
    if response.status_code == 200:
        response_200 = APIResponse.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = APIResponse.from_dict(response.json())

        return response_400

    if response.status_code == 409:
        response_409 = APIResponse.from_dict(response.json())

        return response_409

    if response.status_code == 422:
        response_422 = SubmitPortalFormResponse.from_dict(response.json())

        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[APIResponse | SubmitPortalFormResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    customer_org_id: str,
    link_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: SubmitCustomForm,
) -> Response[APIResponse | SubmitPortalFormResponse]:
    """Submit Portal Form

     Submit a custom form from the customer portal.

    Args:
        customer_org_id (str):
        link_id (str):
        body (SubmitCustomForm):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[APIResponse | SubmitPortalFormResponse]
    """

    kwargs = _get_kwargs(
        customer_org_id=customer_org_id,
        link_id=link_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    customer_org_id: str,
    link_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: SubmitCustomForm,
) -> APIResponse | SubmitPortalFormResponse | None:
    """Submit Portal Form

     Submit a custom form from the customer portal.

    Args:
        customer_org_id (str):
        link_id (str):
        body (SubmitCustomForm):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        APIResponse | SubmitPortalFormResponse
    """

    return sync_detailed(
        customer_org_id=customer_org_id,
        link_id=link_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    customer_org_id: str,
    link_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: SubmitCustomForm,
) -> Response[APIResponse | SubmitPortalFormResponse]:
    """Submit Portal Form

     Submit a custom form from the customer portal.

    Args:
        customer_org_id (str):
        link_id (str):
        body (SubmitCustomForm):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[APIResponse | SubmitPortalFormResponse]
    """

    kwargs = _get_kwargs(
        customer_org_id=customer_org_id,
        link_id=link_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    customer_org_id: str,
    link_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: SubmitCustomForm,
) -> APIResponse | SubmitPortalFormResponse | None:
    """Submit Portal Form

     Submit a custom form from the customer portal.

    Args:
        customer_org_id (str):
        link_id (str):
        body (SubmitCustomForm):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        APIResponse | SubmitPortalFormResponse
    """

    return (
        await asyncio_detailed(
            customer_org_id=customer_org_id,
            link_id=link_id,
            client=client,
            body=body,
        )
    ).parsed
