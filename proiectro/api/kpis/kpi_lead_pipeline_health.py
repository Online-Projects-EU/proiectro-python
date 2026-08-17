from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.output_kpi_lead_pipeline_health import OutputKPILeadPipelineHealth
from ...types import UNSET, Response, Unset


def _get_kwargs(
    tenant_path: str,
    *,
    stale_days: int | None | Unset = UNSET,
    conversion_window_days: int | None | Unset = UNSET,
    include_items: bool | Unset = False,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_stale_days: int | None | Unset
    if isinstance(stale_days, Unset):
        json_stale_days = UNSET
    else:
        json_stale_days = stale_days
    params["stale_days"] = json_stale_days

    json_conversion_window_days: int | None | Unset
    if isinstance(conversion_window_days, Unset):
        json_conversion_window_days = UNSET
    else:
        json_conversion_window_days = conversion_window_days
    params["conversion_window_days"] = json_conversion_window_days

    params["include_items"] = include_items

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/{tenant_path}/kpi/lead_pipeline_health".format(
            tenant_path=quote(str(tenant_path), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> OutputKPILeadPipelineHealth | None:
    if response.status_code == 200:
        response_200 = OutputKPILeadPipelineHealth.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[OutputKPILeadPipelineHealth]:
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
    stale_days: int | None | Unset = UNSET,
    conversion_window_days: int | None | Unset = UNSET,
    include_items: bool | Unset = False,
) -> Response[OutputKPILeadPipelineHealth]:
    """Kpi Lead Pipeline Health

    Args:
        tenant_path (str):
        stale_days (int | None | Unset):
        conversion_window_days (int | None | Unset):
        include_items (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OutputKPILeadPipelineHealth]
    """

    kwargs = _get_kwargs(
        tenant_path=tenant_path,
        stale_days=stale_days,
        conversion_window_days=conversion_window_days,
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
    stale_days: int | None | Unset = UNSET,
    conversion_window_days: int | None | Unset = UNSET,
    include_items: bool | Unset = False,
) -> OutputKPILeadPipelineHealth | None:
    """Kpi Lead Pipeline Health

    Args:
        tenant_path (str):
        stale_days (int | None | Unset):
        conversion_window_days (int | None | Unset):
        include_items (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OutputKPILeadPipelineHealth
    """

    return sync_detailed(
        tenant_path=tenant_path,
        client=client,
        stale_days=stale_days,
        conversion_window_days=conversion_window_days,
        include_items=include_items,
    ).parsed


async def asyncio_detailed(
    tenant_path: str,
    *,
    client: AuthenticatedClient,
    stale_days: int | None | Unset = UNSET,
    conversion_window_days: int | None | Unset = UNSET,
    include_items: bool | Unset = False,
) -> Response[OutputKPILeadPipelineHealth]:
    """Kpi Lead Pipeline Health

    Args:
        tenant_path (str):
        stale_days (int | None | Unset):
        conversion_window_days (int | None | Unset):
        include_items (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OutputKPILeadPipelineHealth]
    """

    kwargs = _get_kwargs(
        tenant_path=tenant_path,
        stale_days=stale_days,
        conversion_window_days=conversion_window_days,
        include_items=include_items,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    tenant_path: str,
    *,
    client: AuthenticatedClient,
    stale_days: int | None | Unset = UNSET,
    conversion_window_days: int | None | Unset = UNSET,
    include_items: bool | Unset = False,
) -> OutputKPILeadPipelineHealth | None:
    """Kpi Lead Pipeline Health

    Args:
        tenant_path (str):
        stale_days (int | None | Unset):
        conversion_window_days (int | None | Unset):
        include_items (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OutputKPILeadPipelineHealth
    """

    return (
        await asyncio_detailed(
            tenant_path=tenant_path,
            client=client,
            stale_days=stale_days,
            conversion_window_days=conversion_window_days,
            include_items=include_items,
        )
    ).parsed
