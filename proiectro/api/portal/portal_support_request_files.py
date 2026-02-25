from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.output_file_names import OutputFileNames
from ...types import Response


def _get_kwargs(
    customer_org_id: str,
    support_request_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/portal/{customer_org_id}/support_requests/{support_request_id}/files".format(
            customer_org_id=quote(str(customer_org_id), safe=""),
            support_request_id=quote(str(support_request_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> OutputFileNames | None:
    if response.status_code == 200:
        response_200 = OutputFileNames.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[OutputFileNames]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    customer_org_id: str,
    support_request_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[OutputFileNames]:
    """Portal Support Request Files

     Get list of files attached to a support request in customer portal.
    Returns file listing for the Files tab on support request detail page.

    Args:
        customer_org_id (str):
        support_request_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OutputFileNames]
    """

    kwargs = _get_kwargs(
        customer_org_id=customer_org_id,
        support_request_id=support_request_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    customer_org_id: str,
    support_request_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> OutputFileNames | None:
    """Portal Support Request Files

     Get list of files attached to a support request in customer portal.
    Returns file listing for the Files tab on support request detail page.

    Args:
        customer_org_id (str):
        support_request_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OutputFileNames
    """

    return sync_detailed(
        customer_org_id=customer_org_id,
        support_request_id=support_request_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    customer_org_id: str,
    support_request_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[OutputFileNames]:
    """Portal Support Request Files

     Get list of files attached to a support request in customer portal.
    Returns file listing for the Files tab on support request detail page.

    Args:
        customer_org_id (str):
        support_request_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OutputFileNames]
    """

    kwargs = _get_kwargs(
        customer_org_id=customer_org_id,
        support_request_id=support_request_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    customer_org_id: str,
    support_request_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> OutputFileNames | None:
    """Portal Support Request Files

     Get list of files attached to a support request in customer portal.
    Returns file listing for the Files tab on support request detail page.

    Args:
        customer_org_id (str):
        support_request_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OutputFileNames
    """

    return (
        await asyncio_detailed(
            customer_org_id=customer_org_id,
            support_request_id=support_request_id,
            client=client,
        )
    ).parsed
