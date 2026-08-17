from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_response import APIResponse
from ...models.submit_asset_form_response import SubmitAssetFormResponse
from ...models.submit_custom_form import SubmitCustomForm
from ...types import Response


def _get_kwargs(
    tenant_path: str,
    attachment_id: str,
    *,
    body: SubmitCustomForm,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/{tenant_path}/submit_asset_form/{attachment_id}".format(
            tenant_path=quote(str(tenant_path), safe=""),
            attachment_id=quote(str(attachment_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> APIResponse | SubmitAssetFormResponse | None:
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
        response_422 = SubmitAssetFormResponse.from_dict(response.json())

        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[APIResponse | SubmitAssetFormResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    tenant_path: str,
    attachment_id: str,
    *,
    client: AuthenticatedClient,
    body: SubmitCustomForm,
) -> Response[APIResponse | SubmitAssetFormResponse]:
    """Submit Asset Form

     Submit an asset's attached form. The CustomerAssetForm link id carries the form + asset
    context, so no context query params or payload keys are needed.

    Args:
        tenant_path (str):
        attachment_id (str):
        body (SubmitCustomForm):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[APIResponse | SubmitAssetFormResponse]
    """

    kwargs = _get_kwargs(
        tenant_path=tenant_path,
        attachment_id=attachment_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    tenant_path: str,
    attachment_id: str,
    *,
    client: AuthenticatedClient,
    body: SubmitCustomForm,
) -> APIResponse | SubmitAssetFormResponse | None:
    """Submit Asset Form

     Submit an asset's attached form. The CustomerAssetForm link id carries the form + asset
    context, so no context query params or payload keys are needed.

    Args:
        tenant_path (str):
        attachment_id (str):
        body (SubmitCustomForm):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        APIResponse | SubmitAssetFormResponse
    """

    return sync_detailed(
        tenant_path=tenant_path,
        attachment_id=attachment_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    tenant_path: str,
    attachment_id: str,
    *,
    client: AuthenticatedClient,
    body: SubmitCustomForm,
) -> Response[APIResponse | SubmitAssetFormResponse]:
    """Submit Asset Form

     Submit an asset's attached form. The CustomerAssetForm link id carries the form + asset
    context, so no context query params or payload keys are needed.

    Args:
        tenant_path (str):
        attachment_id (str):
        body (SubmitCustomForm):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[APIResponse | SubmitAssetFormResponse]
    """

    kwargs = _get_kwargs(
        tenant_path=tenant_path,
        attachment_id=attachment_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    tenant_path: str,
    attachment_id: str,
    *,
    client: AuthenticatedClient,
    body: SubmitCustomForm,
) -> APIResponse | SubmitAssetFormResponse | None:
    """Submit Asset Form

     Submit an asset's attached form. The CustomerAssetForm link id carries the form + asset
    context, so no context query params or payload keys are needed.

    Args:
        tenant_path (str):
        attachment_id (str):
        body (SubmitCustomForm):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        APIResponse | SubmitAssetFormResponse
    """

    return (
        await asyncio_detailed(
            tenant_path=tenant_path,
            attachment_id=attachment_id,
            client=client,
            body=body,
        )
    ).parsed
