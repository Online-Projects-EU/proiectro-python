from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.output_tag_details import OutputTagDetails
from ...types import Response


def _get_kwargs(
    tenant_path: str,
    tag_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/{tenant_path}/tag_details/{tag_id}".format(
            tenant_path=quote(str(tenant_path), safe=""),
            tag_id=quote(str(tag_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> OutputTagDetails | None:
    if response.status_code == 200:
        response_200 = OutputTagDetails.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[OutputTagDetails]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    tenant_path: str,
    tag_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[OutputTagDetails]:
    """Tag Details

     Examine detailed tag usage across all entity types with specific counts.
    Shows which members, roles, organizations, resources, and proposals use this tag.
    Critical for understanding tag impact before editing or deletion.
    Helps identify over-used or under-utilized categorizations.

    Args:
        tenant_path (str):
        tag_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OutputTagDetails]
    """

    kwargs = _get_kwargs(
        tenant_path=tenant_path,
        tag_id=tag_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    tenant_path: str,
    tag_id: str,
    *,
    client: AuthenticatedClient,
) -> OutputTagDetails | None:
    """Tag Details

     Examine detailed tag usage across all entity types with specific counts.
    Shows which members, roles, organizations, resources, and proposals use this tag.
    Critical for understanding tag impact before editing or deletion.
    Helps identify over-used or under-utilized categorizations.

    Args:
        tenant_path (str):
        tag_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OutputTagDetails
    """

    return sync_detailed(
        tenant_path=tenant_path,
        tag_id=tag_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    tenant_path: str,
    tag_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[OutputTagDetails]:
    """Tag Details

     Examine detailed tag usage across all entity types with specific counts.
    Shows which members, roles, organizations, resources, and proposals use this tag.
    Critical for understanding tag impact before editing or deletion.
    Helps identify over-used or under-utilized categorizations.

    Args:
        tenant_path (str):
        tag_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OutputTagDetails]
    """

    kwargs = _get_kwargs(
        tenant_path=tenant_path,
        tag_id=tag_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    tenant_path: str,
    tag_id: str,
    *,
    client: AuthenticatedClient,
) -> OutputTagDetails | None:
    """Tag Details

     Examine detailed tag usage across all entity types with specific counts.
    Shows which members, roles, organizations, resources, and proposals use this tag.
    Critical for understanding tag impact before editing or deletion.
    Helps identify over-used or under-utilized categorizations.

    Args:
        tenant_path (str):
        tag_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OutputTagDetails
    """

    return (
        await asyncio_detailed(
            tenant_path=tenant_path,
            tag_id=tag_id,
            client=client,
        )
    ).parsed
