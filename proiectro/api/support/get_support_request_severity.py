from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.output_support_request_severity import OutputSupportRequestSeverity
from ...types import Response


def _get_kwargs(
    tenant_path: str,
    severity_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/{tenant_path}/support_request_severity/{severity_id}".format(
            tenant_path=quote(str(tenant_path), safe=""),
            severity_id=quote(str(severity_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> OutputSupportRequestSeverity | None:
    if response.status_code == 200:
        response_200 = OutputSupportRequestSeverity.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[OutputSupportRequestSeverity]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    tenant_path: str,
    severity_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[OutputSupportRequestSeverity]:
    """Get Support Request Severity

     Examine specific severity configuration including response times and escalation.
    Shows SLA requirements, notification rules, and priority settings.
    Critical for understanding support commitments and resource needs.

    Args:
        tenant_path (str):
        severity_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OutputSupportRequestSeverity]
    """

    kwargs = _get_kwargs(
        tenant_path=tenant_path,
        severity_id=severity_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    tenant_path: str,
    severity_id: str,
    *,
    client: AuthenticatedClient,
) -> OutputSupportRequestSeverity | None:
    """Get Support Request Severity

     Examine specific severity configuration including response times and escalation.
    Shows SLA requirements, notification rules, and priority settings.
    Critical for understanding support commitments and resource needs.

    Args:
        tenant_path (str):
        severity_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OutputSupportRequestSeverity
    """

    return sync_detailed(
        tenant_path=tenant_path,
        severity_id=severity_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    tenant_path: str,
    severity_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[OutputSupportRequestSeverity]:
    """Get Support Request Severity

     Examine specific severity configuration including response times and escalation.
    Shows SLA requirements, notification rules, and priority settings.
    Critical for understanding support commitments and resource needs.

    Args:
        tenant_path (str):
        severity_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OutputSupportRequestSeverity]
    """

    kwargs = _get_kwargs(
        tenant_path=tenant_path,
        severity_id=severity_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    tenant_path: str,
    severity_id: str,
    *,
    client: AuthenticatedClient,
) -> OutputSupportRequestSeverity | None:
    """Get Support Request Severity

     Examine specific severity configuration including response times and escalation.
    Shows SLA requirements, notification rules, and priority settings.
    Critical for understanding support commitments and resource needs.

    Args:
        tenant_path (str):
        severity_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OutputSupportRequestSeverity
    """

    return (
        await asyncio_detailed(
            tenant_path=tenant_path,
            severity_id=severity_id,
            client=client,
        )
    ).parsed
