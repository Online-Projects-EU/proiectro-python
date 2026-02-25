from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.output_top_entities_by_storage import OutputTopEntitiesByStorage
from ...types import UNSET, Response, Unset


def _get_kwargs(
    tenant_path: str,
    *,
    top: int | Unset = 10,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["top"] = top

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/{tenant_path}/top_proposals_by_storage".format(
            tenant_path=quote(str(tenant_path), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> OutputTopEntitiesByStorage | None:
    if response.status_code == 200:
        response_200 = OutputTopEntitiesByStorage.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[OutputTopEntitiesByStorage]:
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
    top: int | Unset = 10,
) -> Response[OutputTopEntitiesByStorage]:
    """Top Proposals By Storage

     Find proposals with largest document collections to understand sales documentation
    patterns. High storage proposals might indicate complex deals requiring extensive
    supporting materials. Useful for identifying proposals that need archival after
    decision or conversion to project documentation.

    Args:
        tenant_path (str):
        top (int | Unset):  Default: 10.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OutputTopEntitiesByStorage]
    """

    kwargs = _get_kwargs(
        tenant_path=tenant_path,
        top=top,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    tenant_path: str,
    *,
    client: AuthenticatedClient,
    top: int | Unset = 10,
) -> OutputTopEntitiesByStorage | None:
    """Top Proposals By Storage

     Find proposals with largest document collections to understand sales documentation
    patterns. High storage proposals might indicate complex deals requiring extensive
    supporting materials. Useful for identifying proposals that need archival after
    decision or conversion to project documentation.

    Args:
        tenant_path (str):
        top (int | Unset):  Default: 10.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OutputTopEntitiesByStorage
    """

    return sync_detailed(
        tenant_path=tenant_path,
        client=client,
        top=top,
    ).parsed


async def asyncio_detailed(
    tenant_path: str,
    *,
    client: AuthenticatedClient,
    top: int | Unset = 10,
) -> Response[OutputTopEntitiesByStorage]:
    """Top Proposals By Storage

     Find proposals with largest document collections to understand sales documentation
    patterns. High storage proposals might indicate complex deals requiring extensive
    supporting materials. Useful for identifying proposals that need archival after
    decision or conversion to project documentation.

    Args:
        tenant_path (str):
        top (int | Unset):  Default: 10.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OutputTopEntitiesByStorage]
    """

    kwargs = _get_kwargs(
        tenant_path=tenant_path,
        top=top,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    tenant_path: str,
    *,
    client: AuthenticatedClient,
    top: int | Unset = 10,
) -> OutputTopEntitiesByStorage | None:
    """Top Proposals By Storage

     Find proposals with largest document collections to understand sales documentation
    patterns. High storage proposals might indicate complex deals requiring extensive
    supporting materials. Useful for identifying proposals that need archival after
    decision or conversion to project documentation.

    Args:
        tenant_path (str):
        top (int | Unset):  Default: 10.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OutputTopEntitiesByStorage
    """

    return (
        await asyncio_detailed(
            tenant_path=tenant_path,
            client=client,
            top=top,
        )
    ).parsed
