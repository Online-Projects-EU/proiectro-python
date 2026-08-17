from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_response import APIResponse
from ...models.submit_custom_form import SubmitCustomForm
from ...models.submit_work_item_form_response import SubmitWorkItemFormResponse
from ...types import Response


def _get_kwargs(
    tenant_path: str,
    item_id: str,
    form_id: str,
    *,
    body: SubmitCustomForm,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/{tenant_path}/submit_work_item_form/{item_id}/{form_id}".format(
            tenant_path=quote(str(tenant_path), safe=""),
            item_id=quote(str(item_id), safe=""),
            form_id=quote(str(form_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> APIResponse | SubmitWorkItemFormResponse | None:
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
        response_422 = SubmitWorkItemFormResponse.from_dict(response.json())

        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[APIResponse | SubmitWorkItemFormResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    tenant_path: str,
    item_id: str,
    form_id: str,
    *,
    client: AuthenticatedClient,
    body: SubmitCustomForm,
) -> Response[APIResponse | SubmitWorkItemFormResponse]:
    """Submit Work Item Form

     Submit a stage-gated form for a work item. Both ids are required: the form is attached to
    a shared stage but filled per work item (the gate identity is per (work item, form)).

    Args:
        tenant_path (str):
        item_id (str):
        form_id (str):
        body (SubmitCustomForm):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[APIResponse | SubmitWorkItemFormResponse]
    """

    kwargs = _get_kwargs(
        tenant_path=tenant_path,
        item_id=item_id,
        form_id=form_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    tenant_path: str,
    item_id: str,
    form_id: str,
    *,
    client: AuthenticatedClient,
    body: SubmitCustomForm,
) -> APIResponse | SubmitWorkItemFormResponse | None:
    """Submit Work Item Form

     Submit a stage-gated form for a work item. Both ids are required: the form is attached to
    a shared stage but filled per work item (the gate identity is per (work item, form)).

    Args:
        tenant_path (str):
        item_id (str):
        form_id (str):
        body (SubmitCustomForm):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        APIResponse | SubmitWorkItemFormResponse
    """

    return sync_detailed(
        tenant_path=tenant_path,
        item_id=item_id,
        form_id=form_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    tenant_path: str,
    item_id: str,
    form_id: str,
    *,
    client: AuthenticatedClient,
    body: SubmitCustomForm,
) -> Response[APIResponse | SubmitWorkItemFormResponse]:
    """Submit Work Item Form

     Submit a stage-gated form for a work item. Both ids are required: the form is attached to
    a shared stage but filled per work item (the gate identity is per (work item, form)).

    Args:
        tenant_path (str):
        item_id (str):
        form_id (str):
        body (SubmitCustomForm):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[APIResponse | SubmitWorkItemFormResponse]
    """

    kwargs = _get_kwargs(
        tenant_path=tenant_path,
        item_id=item_id,
        form_id=form_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    tenant_path: str,
    item_id: str,
    form_id: str,
    *,
    client: AuthenticatedClient,
    body: SubmitCustomForm,
) -> APIResponse | SubmitWorkItemFormResponse | None:
    """Submit Work Item Form

     Submit a stage-gated form for a work item. Both ids are required: the form is attached to
    a shared stage but filled per work item (the gate identity is per (work item, form)).

    Args:
        tenant_path (str):
        item_id (str):
        form_id (str):
        body (SubmitCustomForm):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        APIResponse | SubmitWorkItemFormResponse
    """

    return (
        await asyncio_detailed(
            tenant_path=tenant_path,
            item_id=item_id,
            form_id=form_id,
            client=client,
            body=body,
        )
    ).parsed
