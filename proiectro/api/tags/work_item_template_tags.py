from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.output_work_item_template_tags import OutputWorkItemTemplateTags
from ...types import Response


def _get_kwargs(
    tenant_path: str,
    template_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/{tenant_path}/work_item_template_tags/{template_id}".format(
            tenant_path=quote(str(tenant_path), safe=""),
            template_id=quote(str(template_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> OutputWorkItemTemplateTags | None:
    if response.status_code == 200:
        response_200 = OutputWorkItemTemplateTags.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[OutputWorkItemTemplateTags]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    tenant_path: str,
    template_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[OutputWorkItemTemplateTags]:
    """Work Item Template Tags

     View all tags assigned to a work item template for categorization and filtering.
    Shows the complete classification profile for template organization.
    Essential for understanding template purposes and finding relevant templates.

    Args:
        tenant_path (str):
        template_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OutputWorkItemTemplateTags]
    """

    kwargs = _get_kwargs(
        tenant_path=tenant_path,
        template_id=template_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    tenant_path: str,
    template_id: str,
    *,
    client: AuthenticatedClient,
) -> OutputWorkItemTemplateTags | None:
    """Work Item Template Tags

     View all tags assigned to a work item template for categorization and filtering.
    Shows the complete classification profile for template organization.
    Essential for understanding template purposes and finding relevant templates.

    Args:
        tenant_path (str):
        template_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OutputWorkItemTemplateTags
    """

    return sync_detailed(
        tenant_path=tenant_path,
        template_id=template_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    tenant_path: str,
    template_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[OutputWorkItemTemplateTags]:
    """Work Item Template Tags

     View all tags assigned to a work item template for categorization and filtering.
    Shows the complete classification profile for template organization.
    Essential for understanding template purposes and finding relevant templates.

    Args:
        tenant_path (str):
        template_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OutputWorkItemTemplateTags]
    """

    kwargs = _get_kwargs(
        tenant_path=tenant_path,
        template_id=template_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    tenant_path: str,
    template_id: str,
    *,
    client: AuthenticatedClient,
) -> OutputWorkItemTemplateTags | None:
    """Work Item Template Tags

     View all tags assigned to a work item template for categorization and filtering.
    Shows the complete classification profile for template organization.
    Essential for understanding template purposes and finding relevant templates.

    Args:
        tenant_path (str):
        template_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OutputWorkItemTemplateTags
    """

    return (
        await asyncio_detailed(
            tenant_path=tenant_path,
            template_id=template_id,
            client=client,
        )
    ).parsed
