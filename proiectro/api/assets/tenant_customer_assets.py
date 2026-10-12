from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.output_customer_assets import OutputCustomerAssets
from ...types import UNSET, Response, Unset


def _get_kwargs(
    tenant_path: str,
    *,
    exclude_mode: bool | None | Unset = UNSET,
    search: None | str | Unset = UNSET,
    name: None | str | Unset = UNSET,
    serial_number_or_uri: None | str | Unset = UNSET,
    customer: None | str | Unset = UNSET,
    category: None | str | Unset = UNSET,
    status: None | str | Unset = UNSET,
    placement: None | str | Unset = UNSET,
    root_only: bool | None | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_exclude_mode: bool | None | Unset
    if isinstance(exclude_mode, Unset):
        json_exclude_mode = UNSET
    else:
        json_exclude_mode = exclude_mode
    params["exclude_mode"] = json_exclude_mode

    json_search: None | str | Unset
    if isinstance(search, Unset):
        json_search = UNSET
    else:
        json_search = search
    params["search"] = json_search

    json_name: None | str | Unset
    if isinstance(name, Unset):
        json_name = UNSET
    else:
        json_name = name
    params["name"] = json_name

    json_serial_number_or_uri: None | str | Unset
    if isinstance(serial_number_or_uri, Unset):
        json_serial_number_or_uri = UNSET
    else:
        json_serial_number_or_uri = serial_number_or_uri
    params["serial_number_or_uri"] = json_serial_number_or_uri

    json_customer: None | str | Unset
    if isinstance(customer, Unset):
        json_customer = UNSET
    else:
        json_customer = customer
    params["customer"] = json_customer

    json_category: None | str | Unset
    if isinstance(category, Unset):
        json_category = UNSET
    else:
        json_category = category
    params["category"] = json_category

    json_status: None | str | Unset
    if isinstance(status, Unset):
        json_status = UNSET
    else:
        json_status = status
    params["status"] = json_status

    json_placement: None | str | Unset
    if isinstance(placement, Unset):
        json_placement = UNSET
    else:
        json_placement = placement
    params["placement"] = json_placement

    json_root_only: bool | None | Unset
    if isinstance(root_only, Unset):
        json_root_only = UNSET
    else:
        json_root_only = root_only
    params["root_only"] = json_root_only

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/{tenant_path}/tenant_customer_assets".format(
            tenant_path=quote(str(tenant_path), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> OutputCustomerAssets | None:
    if response.status_code == 200:
        response_200 = OutputCustomerAssets.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[OutputCustomerAssets]:
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
    exclude_mode: bool | None | Unset = UNSET,
    search: None | str | Unset = UNSET,
    name: None | str | Unset = UNSET,
    serial_number_or_uri: None | str | Unset = UNSET,
    customer: None | str | Unset = UNSET,
    category: None | str | Unset = UNSET,
    status: None | str | Unset = UNSET,
    placement: None | str | Unset = UNSET,
    root_only: bool | None | Unset = UNSET,
) -> Response[OutputCustomerAssets]:
    """Tenant Customer Assets

     List every customer asset in your workspace, across all customers and locations.
    Search by name, serial number or internal code, and narrow by customer, category
    or lifecycle status. Set placement to 'unplaced' to find equipment that is not yet
    assigned to any customer location, or 'placed' for the rest.

    Args:
        tenant_path (str):
        exclude_mode (bool | None | Unset): Invert filter logic to exclude matching results
        search (None | str | Unset): Search by asset name, serial number / URI, or internal code
        name (None | str | Unset): Filter by asset name
        serial_number_or_uri (None | str | Unset): Filter by serial number or URI
        customer (None | str | Unset): Filter by customer organization (external id)
        category (None | str | Unset): Filter by asset category (external id)
        status (None | str | Unset): Filter by lifecycle status (planned, active, maintenance,
            retired)
        placement (None | str | Unset): Filter by placement: 'placed' or 'unplaced'
        root_only (bool | None | Unset): Return only root-level assets (depth=0) instead of every
            depth

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OutputCustomerAssets]
    """

    kwargs = _get_kwargs(
        tenant_path=tenant_path,
        exclude_mode=exclude_mode,
        search=search,
        name=name,
        serial_number_or_uri=serial_number_or_uri,
        customer=customer,
        category=category,
        status=status,
        placement=placement,
        root_only=root_only,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    tenant_path: str,
    *,
    client: AuthenticatedClient,
    exclude_mode: bool | None | Unset = UNSET,
    search: None | str | Unset = UNSET,
    name: None | str | Unset = UNSET,
    serial_number_or_uri: None | str | Unset = UNSET,
    customer: None | str | Unset = UNSET,
    category: None | str | Unset = UNSET,
    status: None | str | Unset = UNSET,
    placement: None | str | Unset = UNSET,
    root_only: bool | None | Unset = UNSET,
) -> OutputCustomerAssets | None:
    """Tenant Customer Assets

     List every customer asset in your workspace, across all customers and locations.
    Search by name, serial number or internal code, and narrow by customer, category
    or lifecycle status. Set placement to 'unplaced' to find equipment that is not yet
    assigned to any customer location, or 'placed' for the rest.

    Args:
        tenant_path (str):
        exclude_mode (bool | None | Unset): Invert filter logic to exclude matching results
        search (None | str | Unset): Search by asset name, serial number / URI, or internal code
        name (None | str | Unset): Filter by asset name
        serial_number_or_uri (None | str | Unset): Filter by serial number or URI
        customer (None | str | Unset): Filter by customer organization (external id)
        category (None | str | Unset): Filter by asset category (external id)
        status (None | str | Unset): Filter by lifecycle status (planned, active, maintenance,
            retired)
        placement (None | str | Unset): Filter by placement: 'placed' or 'unplaced'
        root_only (bool | None | Unset): Return only root-level assets (depth=0) instead of every
            depth

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OutputCustomerAssets
    """

    return sync_detailed(
        tenant_path=tenant_path,
        client=client,
        exclude_mode=exclude_mode,
        search=search,
        name=name,
        serial_number_or_uri=serial_number_or_uri,
        customer=customer,
        category=category,
        status=status,
        placement=placement,
        root_only=root_only,
    ).parsed


async def asyncio_detailed(
    tenant_path: str,
    *,
    client: AuthenticatedClient,
    exclude_mode: bool | None | Unset = UNSET,
    search: None | str | Unset = UNSET,
    name: None | str | Unset = UNSET,
    serial_number_or_uri: None | str | Unset = UNSET,
    customer: None | str | Unset = UNSET,
    category: None | str | Unset = UNSET,
    status: None | str | Unset = UNSET,
    placement: None | str | Unset = UNSET,
    root_only: bool | None | Unset = UNSET,
) -> Response[OutputCustomerAssets]:
    """Tenant Customer Assets

     List every customer asset in your workspace, across all customers and locations.
    Search by name, serial number or internal code, and narrow by customer, category
    or lifecycle status. Set placement to 'unplaced' to find equipment that is not yet
    assigned to any customer location, or 'placed' for the rest.

    Args:
        tenant_path (str):
        exclude_mode (bool | None | Unset): Invert filter logic to exclude matching results
        search (None | str | Unset): Search by asset name, serial number / URI, or internal code
        name (None | str | Unset): Filter by asset name
        serial_number_or_uri (None | str | Unset): Filter by serial number or URI
        customer (None | str | Unset): Filter by customer organization (external id)
        category (None | str | Unset): Filter by asset category (external id)
        status (None | str | Unset): Filter by lifecycle status (planned, active, maintenance,
            retired)
        placement (None | str | Unset): Filter by placement: 'placed' or 'unplaced'
        root_only (bool | None | Unset): Return only root-level assets (depth=0) instead of every
            depth

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OutputCustomerAssets]
    """

    kwargs = _get_kwargs(
        tenant_path=tenant_path,
        exclude_mode=exclude_mode,
        search=search,
        name=name,
        serial_number_or_uri=serial_number_or_uri,
        customer=customer,
        category=category,
        status=status,
        placement=placement,
        root_only=root_only,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    tenant_path: str,
    *,
    client: AuthenticatedClient,
    exclude_mode: bool | None | Unset = UNSET,
    search: None | str | Unset = UNSET,
    name: None | str | Unset = UNSET,
    serial_number_or_uri: None | str | Unset = UNSET,
    customer: None | str | Unset = UNSET,
    category: None | str | Unset = UNSET,
    status: None | str | Unset = UNSET,
    placement: None | str | Unset = UNSET,
    root_only: bool | None | Unset = UNSET,
) -> OutputCustomerAssets | None:
    """Tenant Customer Assets

     List every customer asset in your workspace, across all customers and locations.
    Search by name, serial number or internal code, and narrow by customer, category
    or lifecycle status. Set placement to 'unplaced' to find equipment that is not yet
    assigned to any customer location, or 'placed' for the rest.

    Args:
        tenant_path (str):
        exclude_mode (bool | None | Unset): Invert filter logic to exclude matching results
        search (None | str | Unset): Search by asset name, serial number / URI, or internal code
        name (None | str | Unset): Filter by asset name
        serial_number_or_uri (None | str | Unset): Filter by serial number or URI
        customer (None | str | Unset): Filter by customer organization (external id)
        category (None | str | Unset): Filter by asset category (external id)
        status (None | str | Unset): Filter by lifecycle status (planned, active, maintenance,
            retired)
        placement (None | str | Unset): Filter by placement: 'placed' or 'unplaced'
        root_only (bool | None | Unset): Return only root-level assets (depth=0) instead of every
            depth

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OutputCustomerAssets
    """

    return (
        await asyncio_detailed(
            tenant_path=tenant_path,
            client=client,
            exclude_mode=exclude_mode,
            search=search,
            name=name,
            serial_number_or_uri=serial_number_or_uri,
            customer=customer,
            category=category,
            status=status,
            placement=placement,
            root_only=root_only,
        )
    ).parsed
