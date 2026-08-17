from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.output_kpi_process_bottlenecks import OutputKPIProcessBottlenecks
from ...types import UNSET, Response, Unset


def _get_kwargs(
    tenant_path: str,
    *,
    process_id: None | str | Unset = UNSET,
    threshold_count: int | Unset = 5,
    include_items: bool | Unset = False,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_process_id: None | str | Unset
    if isinstance(process_id, Unset):
        json_process_id = UNSET
    else:
        json_process_id = process_id
    params["process_id"] = json_process_id

    params["threshold_count"] = threshold_count

    params["include_items"] = include_items

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/{tenant_path}/kpi/process_bottlenecks".format(
            tenant_path=quote(str(tenant_path), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> OutputKPIProcessBottlenecks | None:
    if response.status_code == 200:
        response_200 = OutputKPIProcessBottlenecks.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[OutputKPIProcessBottlenecks]:
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
    process_id: None | str | Unset = UNSET,
    threshold_count: int | Unset = 5,
    include_items: bool | Unset = False,
) -> Response[OutputKPIProcessBottlenecks]:
    """Kpi Process Bottlenecks

    Args:
        tenant_path (str):
        process_id (None | str | Unset):
        threshold_count (int | Unset):  Default: 5.
        include_items (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OutputKPIProcessBottlenecks]
    """

    kwargs = _get_kwargs(
        tenant_path=tenant_path,
        process_id=process_id,
        threshold_count=threshold_count,
        include_items=include_items,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    tenant_path: str,
    *,
    client: AuthenticatedClient,
    process_id: None | str | Unset = UNSET,
    threshold_count: int | Unset = 5,
    include_items: bool | Unset = False,
) -> OutputKPIProcessBottlenecks | None:
    """Kpi Process Bottlenecks

    Args:
        tenant_path (str):
        process_id (None | str | Unset):
        threshold_count (int | Unset):  Default: 5.
        include_items (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OutputKPIProcessBottlenecks
    """

    return sync_detailed(
        tenant_path=tenant_path,
        client=client,
        process_id=process_id,
        threshold_count=threshold_count,
        include_items=include_items,
    ).parsed


async def asyncio_detailed(
    tenant_path: str,
    *,
    client: AuthenticatedClient,
    process_id: None | str | Unset = UNSET,
    threshold_count: int | Unset = 5,
    include_items: bool | Unset = False,
) -> Response[OutputKPIProcessBottlenecks]:
    """Kpi Process Bottlenecks

    Args:
        tenant_path (str):
        process_id (None | str | Unset):
        threshold_count (int | Unset):  Default: 5.
        include_items (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OutputKPIProcessBottlenecks]
    """

    kwargs = _get_kwargs(
        tenant_path=tenant_path,
        process_id=process_id,
        threshold_count=threshold_count,
        include_items=include_items,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    tenant_path: str,
    *,
    client: AuthenticatedClient,
    process_id: None | str | Unset = UNSET,
    threshold_count: int | Unset = 5,
    include_items: bool | Unset = False,
) -> OutputKPIProcessBottlenecks | None:
    """Kpi Process Bottlenecks

    Args:
        tenant_path (str):
        process_id (None | str | Unset):
        threshold_count (int | Unset):  Default: 5.
        include_items (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OutputKPIProcessBottlenecks
    """

    return (
        await asyncio_detailed(
            tenant_path=tenant_path,
            client=client,
            process_id=process_id,
            threshold_count=threshold_count,
            include_items=include_items,
        )
    ).parsed
