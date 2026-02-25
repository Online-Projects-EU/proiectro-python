from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.add_sales_activity import AddSalesActivity
from ...models.api_response import APIResponse
from ...types import Response


def _get_kwargs(
    tenant_path: str,
    *,
    body: AddSalesActivity,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/{tenant_path}/add_sales_activity".format(
            tenant_path=quote(str(tenant_path), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> APIResponse | None:
    if response.status_code == 200:
        response_200 = APIResponse.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = APIResponse.from_dict(response.json())

        return response_400

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[APIResponse]:
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
    body: AddSalesActivity,
) -> Response[APIResponse]:
    """Add Sales Activity

     Log customer interactions, meeting notes, and deal progress for complete activity
    history. Creates searchable record of all sales touches for handoffs and reviews.
    Essential for CRM hygiene and team collaboration. Activities drive engagement
    scoring and next-best-action recommendations.

    Args:
        tenant_path (str):
        body (AddSalesActivity):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[APIResponse]
    """

    kwargs = _get_kwargs(
        tenant_path=tenant_path,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    tenant_path: str,
    *,
    client: AuthenticatedClient,
    body: AddSalesActivity,
) -> APIResponse | None:
    """Add Sales Activity

     Log customer interactions, meeting notes, and deal progress for complete activity
    history. Creates searchable record of all sales touches for handoffs and reviews.
    Essential for CRM hygiene and team collaboration. Activities drive engagement
    scoring and next-best-action recommendations.

    Args:
        tenant_path (str):
        body (AddSalesActivity):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        APIResponse
    """

    return sync_detailed(
        tenant_path=tenant_path,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    tenant_path: str,
    *,
    client: AuthenticatedClient,
    body: AddSalesActivity,
) -> Response[APIResponse]:
    """Add Sales Activity

     Log customer interactions, meeting notes, and deal progress for complete activity
    history. Creates searchable record of all sales touches for handoffs and reviews.
    Essential for CRM hygiene and team collaboration. Activities drive engagement
    scoring and next-best-action recommendations.

    Args:
        tenant_path (str):
        body (AddSalesActivity):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[APIResponse]
    """

    kwargs = _get_kwargs(
        tenant_path=tenant_path,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    tenant_path: str,
    *,
    client: AuthenticatedClient,
    body: AddSalesActivity,
) -> APIResponse | None:
    """Add Sales Activity

     Log customer interactions, meeting notes, and deal progress for complete activity
    history. Creates searchable record of all sales touches for handoffs and reviews.
    Essential for CRM hygiene and team collaboration. Activities drive engagement
    scoring and next-best-action recommendations.

    Args:
        tenant_path (str):
        body (AddSalesActivity):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        APIResponse
    """

    return (
        await asyncio_detailed(
            tenant_path=tenant_path,
            client=client,
            body=body,
        )
    ).parsed
