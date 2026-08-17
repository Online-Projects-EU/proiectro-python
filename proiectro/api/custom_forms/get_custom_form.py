from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.output_custom_form import OutputCustomForm
from ...types import Response


def _get_kwargs(
    tenant_path: str,
    form_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/{tenant_path}/custom_form/{form_id}".format(
            tenant_path=quote(str(tenant_path), safe=""),
            form_id=quote(str(form_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> OutputCustomForm | None:
    if response.status_code == 200:
        response_200 = OutputCustomForm.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[OutputCustomForm]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    tenant_path: str,
    form_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[OutputCustomForm]:
    """Get Custom Form

    Args:
        tenant_path (str):
        form_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OutputCustomForm]
    """

    kwargs = _get_kwargs(
        tenant_path=tenant_path,
        form_id=form_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    tenant_path: str,
    form_id: str,
    *,
    client: AuthenticatedClient,
) -> OutputCustomForm | None:
    """Get Custom Form

    Args:
        tenant_path (str):
        form_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OutputCustomForm
    """

    return sync_detailed(
        tenant_path=tenant_path,
        form_id=form_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    tenant_path: str,
    form_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[OutputCustomForm]:
    """Get Custom Form

    Args:
        tenant_path (str):
        form_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OutputCustomForm]
    """

    kwargs = _get_kwargs(
        tenant_path=tenant_path,
        form_id=form_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    tenant_path: str,
    form_id: str,
    *,
    client: AuthenticatedClient,
) -> OutputCustomForm | None:
    """Get Custom Form

    Args:
        tenant_path (str):
        form_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OutputCustomForm
    """

    return (
        await asyncio_detailed(
            tenant_path=tenant_path,
            form_id=form_id,
            client=client,
        )
    ).parsed
