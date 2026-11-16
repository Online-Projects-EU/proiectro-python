from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_response import APIResponse
from ...models.edit_belief import EditBelief
from ...models.pydantic_detail import PydanticDetail
from ...types import Response


def _get_kwargs(
    tenant_path: str,
    belief_id: str,
    *,
    body: EditBelief,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/api/v1/{tenant_path}/edit_belief/{belief_id}".format(
            tenant_path=quote(str(tenant_path), safe=""),
            belief_id=quote(str(belief_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> APIResponse | PydanticDetail | None:
    if response.status_code == 200:
        response_200 = APIResponse.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = APIResponse.from_dict(response.json())

        return response_400

    if response.status_code == 404:
        response_404 = APIResponse.from_dict(response.json())

        return response_404

    if response.status_code == 422:
        response_422 = PydanticDetail.from_dict(response.json())

        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[APIResponse | PydanticDetail]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    tenant_path: str,
    belief_id: str,
    *,
    client: AuthenticatedClient,
    body: EditBelief,
) -> Response[APIResponse | PydanticDetail]:
    """Edit Belief

     Reword a belief, or change its starting guess, decision bar, split or the date it counts from. What
    it
    counts as evidence stays as it was added.

    Args:
        tenant_path (str):
        belief_id (str):
        body (EditBelief): Only what you send changes. What a belief counts as evidence is fixed
            when it is added: a different
            question is a different belief. Send `guess`, `bar` or `split_by` empty to remove it.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[APIResponse | PydanticDetail]
    """

    kwargs = _get_kwargs(
        tenant_path=tenant_path,
        belief_id=belief_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    tenant_path: str,
    belief_id: str,
    *,
    client: AuthenticatedClient,
    body: EditBelief,
) -> APIResponse | PydanticDetail | None:
    """Edit Belief

     Reword a belief, or change its starting guess, decision bar, split or the date it counts from. What
    it
    counts as evidence stays as it was added.

    Args:
        tenant_path (str):
        belief_id (str):
        body (EditBelief): Only what you send changes. What a belief counts as evidence is fixed
            when it is added: a different
            question is a different belief. Send `guess`, `bar` or `split_by` empty to remove it.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        APIResponse | PydanticDetail
    """

    return sync_detailed(
        tenant_path=tenant_path,
        belief_id=belief_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    tenant_path: str,
    belief_id: str,
    *,
    client: AuthenticatedClient,
    body: EditBelief,
) -> Response[APIResponse | PydanticDetail]:
    """Edit Belief

     Reword a belief, or change its starting guess, decision bar, split or the date it counts from. What
    it
    counts as evidence stays as it was added.

    Args:
        tenant_path (str):
        belief_id (str):
        body (EditBelief): Only what you send changes. What a belief counts as evidence is fixed
            when it is added: a different
            question is a different belief. Send `guess`, `bar` or `split_by` empty to remove it.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[APIResponse | PydanticDetail]
    """

    kwargs = _get_kwargs(
        tenant_path=tenant_path,
        belief_id=belief_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    tenant_path: str,
    belief_id: str,
    *,
    client: AuthenticatedClient,
    body: EditBelief,
) -> APIResponse | PydanticDetail | None:
    """Edit Belief

     Reword a belief, or change its starting guess, decision bar, split or the date it counts from. What
    it
    counts as evidence stays as it was added.

    Args:
        tenant_path (str):
        belief_id (str):
        body (EditBelief): Only what you send changes. What a belief counts as evidence is fixed
            when it is added: a different
            question is a different belief. Send `guess`, `bar` or `split_by` empty to remove it.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        APIResponse | PydanticDetail
    """

    return (
        await asyncio_detailed(
            tenant_path=tenant_path,
            belief_id=belief_id,
            client=client,
            body=body,
        )
    ).parsed
