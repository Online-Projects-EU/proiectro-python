from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.output_label_cardinality import OutputLabelCardinality
from ...types import Response


def _get_kwargs(
    tenant_path: str,
    label_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/{tenant_path}/label_cardinality/{label_id}".format(
            tenant_path=quote(str(tenant_path), safe=""),
            label_id=quote(str(label_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> OutputLabelCardinality | None:
    if response.status_code == 200:
        response_200 = OutputLabelCardinality.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[OutputLabelCardinality]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    tenant_path: str,
    label_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[OutputLabelCardinality]:
    """Label Cardinality

     Analyze label distribution across different entity types to understand usage patterns.
    Shows counts for members, roles, organizations, resources, and proposals. Essential
    for impact analysis before label modifications. Identifies cross-functional labels
    that span multiple entity types versus specialized classifications.

    Args:
        tenant_path (str):
        label_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OutputLabelCardinality]
    """

    kwargs = _get_kwargs(
        tenant_path=tenant_path,
        label_id=label_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    tenant_path: str,
    label_id: str,
    *,
    client: AuthenticatedClient,
) -> OutputLabelCardinality | None:
    """Label Cardinality

     Analyze label distribution across different entity types to understand usage patterns.
    Shows counts for members, roles, organizations, resources, and proposals. Essential
    for impact analysis before label modifications. Identifies cross-functional labels
    that span multiple entity types versus specialized classifications.

    Args:
        tenant_path (str):
        label_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OutputLabelCardinality
    """

    return sync_detailed(
        tenant_path=tenant_path,
        label_id=label_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    tenant_path: str,
    label_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[OutputLabelCardinality]:
    """Label Cardinality

     Analyze label distribution across different entity types to understand usage patterns.
    Shows counts for members, roles, organizations, resources, and proposals. Essential
    for impact analysis before label modifications. Identifies cross-functional labels
    that span multiple entity types versus specialized classifications.

    Args:
        tenant_path (str):
        label_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OutputLabelCardinality]
    """

    kwargs = _get_kwargs(
        tenant_path=tenant_path,
        label_id=label_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    tenant_path: str,
    label_id: str,
    *,
    client: AuthenticatedClient,
) -> OutputLabelCardinality | None:
    """Label Cardinality

     Analyze label distribution across different entity types to understand usage patterns.
    Shows counts for members, roles, organizations, resources, and proposals. Essential
    for impact analysis before label modifications. Identifies cross-functional labels
    that span multiple entity types versus specialized classifications.

    Args:
        tenant_path (str):
        label_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OutputLabelCardinality
    """

    return (
        await asyncio_detailed(
            tenant_path=tenant_path,
            label_id=label_id,
            client=client,
        )
    ).parsed
