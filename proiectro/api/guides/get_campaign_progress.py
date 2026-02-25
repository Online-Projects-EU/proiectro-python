from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.output_campaign_progress import OutputCampaignProgress
from ...types import Response


def _get_kwargs(
    tenant_path: str,
    campaign_code: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/{tenant_path}/guide/{campaign_code}".format(
            tenant_path=quote(str(tenant_path), safe=""),
            campaign_code=quote(str(campaign_code), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> OutputCampaignProgress | None:
    if response.status_code == 200:
        response_200 = OutputCampaignProgress.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[OutputCampaignProgress]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    tenant_path: str,
    campaign_code: str,
    *,
    client: AuthenticatedClient,
) -> Response[OutputCampaignProgress]:
    """Get Campaign Progress

     View detailed progress on a specific guidance campaign.
    Shows all steps with their completion status, required actions, and next steps.

    Args:
        tenant_path (str):
        campaign_code (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OutputCampaignProgress]
    """

    kwargs = _get_kwargs(
        tenant_path=tenant_path,
        campaign_code=campaign_code,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    tenant_path: str,
    campaign_code: str,
    *,
    client: AuthenticatedClient,
) -> OutputCampaignProgress | None:
    """Get Campaign Progress

     View detailed progress on a specific guidance campaign.
    Shows all steps with their completion status, required actions, and next steps.

    Args:
        tenant_path (str):
        campaign_code (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OutputCampaignProgress
    """

    return sync_detailed(
        tenant_path=tenant_path,
        campaign_code=campaign_code,
        client=client,
    ).parsed


async def asyncio_detailed(
    tenant_path: str,
    campaign_code: str,
    *,
    client: AuthenticatedClient,
) -> Response[OutputCampaignProgress]:
    """Get Campaign Progress

     View detailed progress on a specific guidance campaign.
    Shows all steps with their completion status, required actions, and next steps.

    Args:
        tenant_path (str):
        campaign_code (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OutputCampaignProgress]
    """

    kwargs = _get_kwargs(
        tenant_path=tenant_path,
        campaign_code=campaign_code,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    tenant_path: str,
    campaign_code: str,
    *,
    client: AuthenticatedClient,
) -> OutputCampaignProgress | None:
    """Get Campaign Progress

     View detailed progress on a specific guidance campaign.
    Shows all steps with their completion status, required actions, and next steps.

    Args:
        tenant_path (str):
        campaign_code (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OutputCampaignProgress
    """

    return (
        await asyncio_detailed(
            tenant_path=tenant_path,
            campaign_code=campaign_code,
            client=client,
        )
    ).parsed
