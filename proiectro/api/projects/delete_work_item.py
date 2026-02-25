from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_response import APIResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    tenant_path: str,
    work_item_id: str,
    *,
    delete_descendants: bool | Unset = False,
    reparent_id: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["delete_descendants"] = delete_descendants

    params["reparent_id"] = reparent_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/api/v1/{tenant_path}/delete_work_item/{work_item_id}".format(
            tenant_path=quote(str(tenant_path), safe=""),
            work_item_id=quote(str(work_item_id), safe=""),
        ),
        "params": params,
    }

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
    work_item_id: str,
    *,
    client: AuthenticatedClient,
    delete_descendants: bool | Unset = False,
    reparent_id: str | Unset = UNSET,
) -> Response[APIResponse]:
    """Delete Work Item

     Delete a work item with options for handling children.
    Blocks deletion if the work item has dependencies, costs, expenses, work logs, or resource usages.
    Children can be deleted or reparented to another work item of the same type within the same project.

    Args:
        tenant_path (str):
        work_item_id (str):
        delete_descendants (bool | Unset):  Default: False.
        reparent_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[APIResponse]
    """

    kwargs = _get_kwargs(
        tenant_path=tenant_path,
        work_item_id=work_item_id,
        delete_descendants=delete_descendants,
        reparent_id=reparent_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    tenant_path: str,
    work_item_id: str,
    *,
    client: AuthenticatedClient,
    delete_descendants: bool | Unset = False,
    reparent_id: str | Unset = UNSET,
) -> APIResponse | None:
    """Delete Work Item

     Delete a work item with options for handling children.
    Blocks deletion if the work item has dependencies, costs, expenses, work logs, or resource usages.
    Children can be deleted or reparented to another work item of the same type within the same project.

    Args:
        tenant_path (str):
        work_item_id (str):
        delete_descendants (bool | Unset):  Default: False.
        reparent_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        APIResponse
    """

    return sync_detailed(
        tenant_path=tenant_path,
        work_item_id=work_item_id,
        client=client,
        delete_descendants=delete_descendants,
        reparent_id=reparent_id,
    ).parsed


async def asyncio_detailed(
    tenant_path: str,
    work_item_id: str,
    *,
    client: AuthenticatedClient,
    delete_descendants: bool | Unset = False,
    reparent_id: str | Unset = UNSET,
) -> Response[APIResponse]:
    """Delete Work Item

     Delete a work item with options for handling children.
    Blocks deletion if the work item has dependencies, costs, expenses, work logs, or resource usages.
    Children can be deleted or reparented to another work item of the same type within the same project.

    Args:
        tenant_path (str):
        work_item_id (str):
        delete_descendants (bool | Unset):  Default: False.
        reparent_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[APIResponse]
    """

    kwargs = _get_kwargs(
        tenant_path=tenant_path,
        work_item_id=work_item_id,
        delete_descendants=delete_descendants,
        reparent_id=reparent_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    tenant_path: str,
    work_item_id: str,
    *,
    client: AuthenticatedClient,
    delete_descendants: bool | Unset = False,
    reparent_id: str | Unset = UNSET,
) -> APIResponse | None:
    """Delete Work Item

     Delete a work item with options for handling children.
    Blocks deletion if the work item has dependencies, costs, expenses, work logs, or resource usages.
    Children can be deleted or reparented to another work item of the same type within the same project.

    Args:
        tenant_path (str):
        work_item_id (str):
        delete_descendants (bool | Unset):  Default: False.
        reparent_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        APIResponse
    """

    return (
        await asyncio_detailed(
            tenant_path=tenant_path,
            work_item_id=work_item_id,
            client=client,
            delete_descendants=delete_descendants,
            reparent_id=reparent_id,
        )
    ).parsed
