from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.output_label_details import OutputLabelDetails
from ...types import Response


def _get_kwargs(
    tenant_path: str,
    label_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/{tenant_path}/label_details/{label_id}".format(
            tenant_path=quote(str(tenant_path), safe=""),
            label_id=quote(str(label_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> OutputLabelDetails | None:
    if response.status_code == 200:
        response_200 = OutputLabelDetails.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[OutputLabelDetails]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    tenant_path: str,
    label_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[OutputLabelDetails]:
    """Label Details

     Examine comprehensive label metadata including creation date, usage statistics, and
    complete description. Useful for understanding label purpose and adoption patterns.
    Review before editing or deleting to assess workspace-wide impact. Helps identify
    underutilized or redundant labels for taxonomy optimization.

    Args:
        tenant_path (str):
        label_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OutputLabelDetails]
    """

    kwargs = _get_kwargs(
        tenant_path=tenant_path,
        label_id=label_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    tenant_path: str,
    label_id: str,
    *,
    client: AuthenticatedClient,
) -> OutputLabelDetails | None:
    """Label Details

     Examine comprehensive label metadata including creation date, usage statistics, and
    complete description. Useful for understanding label purpose and adoption patterns.
    Review before editing or deleting to assess workspace-wide impact. Helps identify
    underutilized or redundant labels for taxonomy optimization.

    Args:
        tenant_path (str):
        label_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OutputLabelDetails
    """

    return sync_detailed(
        tenant_path=tenant_path,
        label_id=label_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    tenant_path: str,
    label_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[OutputLabelDetails]:
    """Label Details

     Examine comprehensive label metadata including creation date, usage statistics, and
    complete description. Useful for understanding label purpose and adoption patterns.
    Review before editing or deleting to assess workspace-wide impact. Helps identify
    underutilized or redundant labels for taxonomy optimization.

    Args:
        tenant_path (str):
        label_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OutputLabelDetails]
    """

    kwargs = _get_kwargs(
        tenant_path=tenant_path,
        label_id=label_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    tenant_path: str,
    label_id: str,
    *,
    client: AuthenticatedClient,
) -> OutputLabelDetails | None:
    """Label Details

     Examine comprehensive label metadata including creation date, usage statistics, and
    complete description. Useful for understanding label purpose and adoption patterns.
    Review before editing or deleting to assess workspace-wide impact. Helps identify
    underutilized or redundant labels for taxonomy optimization.

    Args:
        tenant_path (str):
        label_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OutputLabelDetails
    """

    return (
        await asyncio_detailed(
            tenant_path=tenant_path,
            label_id=label_id,
            client=client,
        )
    ).parsed
