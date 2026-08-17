from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.output_kpi_expiring_warranties import OutputKPIExpiringWarranties
from ...types import UNSET, Response, Unset


def _get_kwargs(
    tenant_path: str,
    *,
    days_until_expiry_lte: int | None | Unset = UNSET,
    customer_id: None | str | Unset = UNSET,
    include_items: bool | Unset = False,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_days_until_expiry_lte: int | None | Unset
    if isinstance(days_until_expiry_lte, Unset):
        json_days_until_expiry_lte = UNSET
    else:
        json_days_until_expiry_lte = days_until_expiry_lte
    params["days_until_expiry_lte"] = json_days_until_expiry_lte

    json_customer_id: None | str | Unset
    if isinstance(customer_id, Unset):
        json_customer_id = UNSET
    else:
        json_customer_id = customer_id
    params["customer_id"] = json_customer_id

    params["include_items"] = include_items

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/{tenant_path}/kpi/expiring_warranties".format(
            tenant_path=quote(str(tenant_path), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> OutputKPIExpiringWarranties | None:
    if response.status_code == 200:
        response_200 = OutputKPIExpiringWarranties.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[OutputKPIExpiringWarranties]:
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
    days_until_expiry_lte: int | None | Unset = UNSET,
    customer_id: None | str | Unset = UNSET,
    include_items: bool | Unset = False,
) -> Response[OutputKPIExpiringWarranties]:
    """Kpi Expiring Warranties

    Args:
        tenant_path (str):
        days_until_expiry_lte (int | None | Unset):
        customer_id (None | str | Unset):
        include_items (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OutputKPIExpiringWarranties]
    """

    kwargs = _get_kwargs(
        tenant_path=tenant_path,
        days_until_expiry_lte=days_until_expiry_lte,
        customer_id=customer_id,
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
    days_until_expiry_lte: int | None | Unset = UNSET,
    customer_id: None | str | Unset = UNSET,
    include_items: bool | Unset = False,
) -> OutputKPIExpiringWarranties | None:
    """Kpi Expiring Warranties

    Args:
        tenant_path (str):
        days_until_expiry_lte (int | None | Unset):
        customer_id (None | str | Unset):
        include_items (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OutputKPIExpiringWarranties
    """

    return sync_detailed(
        tenant_path=tenant_path,
        client=client,
        days_until_expiry_lte=days_until_expiry_lte,
        customer_id=customer_id,
        include_items=include_items,
    ).parsed


async def asyncio_detailed(
    tenant_path: str,
    *,
    client: AuthenticatedClient,
    days_until_expiry_lte: int | None | Unset = UNSET,
    customer_id: None | str | Unset = UNSET,
    include_items: bool | Unset = False,
) -> Response[OutputKPIExpiringWarranties]:
    """Kpi Expiring Warranties

    Args:
        tenant_path (str):
        days_until_expiry_lte (int | None | Unset):
        customer_id (None | str | Unset):
        include_items (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OutputKPIExpiringWarranties]
    """

    kwargs = _get_kwargs(
        tenant_path=tenant_path,
        days_until_expiry_lte=days_until_expiry_lte,
        customer_id=customer_id,
        include_items=include_items,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    tenant_path: str,
    *,
    client: AuthenticatedClient,
    days_until_expiry_lte: int | None | Unset = UNSET,
    customer_id: None | str | Unset = UNSET,
    include_items: bool | Unset = False,
) -> OutputKPIExpiringWarranties | None:
    """Kpi Expiring Warranties

    Args:
        tenant_path (str):
        days_until_expiry_lte (int | None | Unset):
        customer_id (None | str | Unset):
        include_items (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OutputKPIExpiringWarranties
    """

    return (
        await asyncio_detailed(
            tenant_path=tenant_path,
            client=client,
            days_until_expiry_lte=days_until_expiry_lte,
            customer_id=customer_id,
            include_items=include_items,
        )
    ).parsed
