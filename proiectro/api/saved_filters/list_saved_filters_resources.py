from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.output_saved_filters_list import OutputSavedFiltersList
from ...types import Response


def _get_kwargs(
    tenant_path: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/{tenant_path}/list_saved_filters_resources".format(
            tenant_path=quote(str(tenant_path), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> OutputSavedFiltersList | None:
    if response.status_code == 200:
        response_200 = OutputSavedFiltersList.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[OutputSavedFiltersList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    tenant_path: str,
    *,
    client: AuthenticatedClient,
) -> Response[OutputSavedFiltersList]:
    """List Saved Filters Resources

     List all available saved filters for the resources list. Returns filters you created
    (personal) and filters shared by your team members. Use these saved filters to quickly
    apply complex filter combinations without manually rebuilding criteria. Personal filters
    are only visible to you, while shared filters help teams maintain consistent views.

    Args:
        tenant_path (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OutputSavedFiltersList]
    """

    kwargs = _get_kwargs(
        tenant_path=tenant_path,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    tenant_path: str,
    *,
    client: AuthenticatedClient,
) -> OutputSavedFiltersList | None:
    """List Saved Filters Resources

     List all available saved filters for the resources list. Returns filters you created
    (personal) and filters shared by your team members. Use these saved filters to quickly
    apply complex filter combinations without manually rebuilding criteria. Personal filters
    are only visible to you, while shared filters help teams maintain consistent views.

    Args:
        tenant_path (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OutputSavedFiltersList
    """

    return sync_detailed(
        tenant_path=tenant_path,
        client=client,
    ).parsed


async def asyncio_detailed(
    tenant_path: str,
    *,
    client: AuthenticatedClient,
) -> Response[OutputSavedFiltersList]:
    """List Saved Filters Resources

     List all available saved filters for the resources list. Returns filters you created
    (personal) and filters shared by your team members. Use these saved filters to quickly
    apply complex filter combinations without manually rebuilding criteria. Personal filters
    are only visible to you, while shared filters help teams maintain consistent views.

    Args:
        tenant_path (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OutputSavedFiltersList]
    """

    kwargs = _get_kwargs(
        tenant_path=tenant_path,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    tenant_path: str,
    *,
    client: AuthenticatedClient,
) -> OutputSavedFiltersList | None:
    """List Saved Filters Resources

     List all available saved filters for the resources list. Returns filters you created
    (personal) and filters shared by your team members. Use these saved filters to quickly
    apply complex filter combinations without manually rebuilding criteria. Personal filters
    are only visible to you, while shared filters help teams maintain consistent views.

    Args:
        tenant_path (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OutputSavedFiltersList
    """

    return (
        await asyncio_detailed(
            tenant_path=tenant_path,
            client=client,
        )
    ).parsed
