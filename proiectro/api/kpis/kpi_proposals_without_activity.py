from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.output_kpi_proposals_without_activity import (
    OutputKPIProposalsWithoutActivity,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    tenant_path: str,
    *,
    no_activity_days: int | Unset = 14,
    min_value: None | str | Unset = UNSET,
    include_items: bool | Unset = False,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["no_activity_days"] = no_activity_days

    json_min_value: None | str | Unset
    if isinstance(min_value, Unset):
        json_min_value = UNSET
    else:
        json_min_value = min_value
    params["min_value"] = json_min_value

    params["include_items"] = include_items

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/{tenant_path}/kpi/proposals_without_activity".format(
            tenant_path=quote(str(tenant_path), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> OutputKPIProposalsWithoutActivity | None:
    if response.status_code == 200:
        response_200 = OutputKPIProposalsWithoutActivity.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[OutputKPIProposalsWithoutActivity]:
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
    no_activity_days: int | Unset = 14,
    min_value: None | str | Unset = UNSET,
    include_items: bool | Unset = False,
) -> Response[OutputKPIProposalsWithoutActivity]:
    """Kpi Proposals Without Activity

    Args:
        tenant_path (str):
        no_activity_days (int | Unset):  Default: 14.
        min_value (None | str | Unset):
        include_items (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OutputKPIProposalsWithoutActivity]
    """

    kwargs = _get_kwargs(
        tenant_path=tenant_path,
        no_activity_days=no_activity_days,
        min_value=min_value,
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
    no_activity_days: int | Unset = 14,
    min_value: None | str | Unset = UNSET,
    include_items: bool | Unset = False,
) -> OutputKPIProposalsWithoutActivity | None:
    """Kpi Proposals Without Activity

    Args:
        tenant_path (str):
        no_activity_days (int | Unset):  Default: 14.
        min_value (None | str | Unset):
        include_items (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OutputKPIProposalsWithoutActivity
    """

    return sync_detailed(
        tenant_path=tenant_path,
        client=client,
        no_activity_days=no_activity_days,
        min_value=min_value,
        include_items=include_items,
    ).parsed


async def asyncio_detailed(
    tenant_path: str,
    *,
    client: AuthenticatedClient,
    no_activity_days: int | Unset = 14,
    min_value: None | str | Unset = UNSET,
    include_items: bool | Unset = False,
) -> Response[OutputKPIProposalsWithoutActivity]:
    """Kpi Proposals Without Activity

    Args:
        tenant_path (str):
        no_activity_days (int | Unset):  Default: 14.
        min_value (None | str | Unset):
        include_items (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OutputKPIProposalsWithoutActivity]
    """

    kwargs = _get_kwargs(
        tenant_path=tenant_path,
        no_activity_days=no_activity_days,
        min_value=min_value,
        include_items=include_items,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    tenant_path: str,
    *,
    client: AuthenticatedClient,
    no_activity_days: int | Unset = 14,
    min_value: None | str | Unset = UNSET,
    include_items: bool | Unset = False,
) -> OutputKPIProposalsWithoutActivity | None:
    """Kpi Proposals Without Activity

    Args:
        tenant_path (str):
        no_activity_days (int | Unset):  Default: 14.
        min_value (None | str | Unset):
        include_items (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OutputKPIProposalsWithoutActivity
    """

    return (
        await asyncio_detailed(
            tenant_path=tenant_path,
            client=client,
            no_activity_days=no_activity_days,
            min_value=min_value,
            include_items=include_items,
        )
    ).parsed
