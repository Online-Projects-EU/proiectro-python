from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.add_belief import AddBelief
from ...models.api_response import APIResponse
from ...models.pydantic_detail import PydanticDetail
from ...types import Response


def _get_kwargs(
    tenant_path: str,
    *,
    body: AddBelief,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/{tenant_path}/add_belief".format(
            tenant_path=quote(str(tenant_path), safe=""),
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
    *,
    client: AuthenticatedClient,
    body: AddBelief,
) -> Response[APIResponse | PydanticDetail]:
    """Add Belief

     State a belief about your sales or operations: a reply rate, a win rate, or the answer to a question
    on one of your forms. Add your own starting guess and a decision bar if you have them.

    Args:
        tenant_path (str):
        body (AddBelief): A belief names what is counted as evidence and, optionally, your own
            starting guess. For evidence
            `form`, name the form and one of its questions: a yes/no question is counted as it is, a
            choice question
            by one `option`, and a number either against a `threshold` or, with none, as an average.
            `guess` and
            `bar` are a percentage from 0 to 100 for a share and a plain number for an average.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[APIResponse | PydanticDetail]
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
    body: AddBelief,
) -> APIResponse | PydanticDetail | None:
    """Add Belief

     State a belief about your sales or operations: a reply rate, a win rate, or the answer to a question
    on one of your forms. Add your own starting guess and a decision bar if you have them.

    Args:
        tenant_path (str):
        body (AddBelief): A belief names what is counted as evidence and, optionally, your own
            starting guess. For evidence
            `form`, name the form and one of its questions: a yes/no question is counted as it is, a
            choice question
            by one `option`, and a number either against a `threshold` or, with none, as an average.
            `guess` and
            `bar` are a percentage from 0 to 100 for a share and a plain number for an average.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        APIResponse | PydanticDetail
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
    body: AddBelief,
) -> Response[APIResponse | PydanticDetail]:
    """Add Belief

     State a belief about your sales or operations: a reply rate, a win rate, or the answer to a question
    on one of your forms. Add your own starting guess and a decision bar if you have them.

    Args:
        tenant_path (str):
        body (AddBelief): A belief names what is counted as evidence and, optionally, your own
            starting guess. For evidence
            `form`, name the form and one of its questions: a yes/no question is counted as it is, a
            choice question
            by one `option`, and a number either against a `threshold` or, with none, as an average.
            `guess` and
            `bar` are a percentage from 0 to 100 for a share and a plain number for an average.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[APIResponse | PydanticDetail]
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
    body: AddBelief,
) -> APIResponse | PydanticDetail | None:
    """Add Belief

     State a belief about your sales or operations: a reply rate, a win rate, or the answer to a question
    on one of your forms. Add your own starting guess and a decision bar if you have them.

    Args:
        tenant_path (str):
        body (AddBelief): A belief names what is counted as evidence and, optionally, your own
            starting guess. For evidence
            `form`, name the form and one of its questions: a yes/no question is counted as it is, a
            choice question
            by one `option`, and a number either against a `threshold` or, with none, as an average.
            `guess` and
            `bar` are a percentage from 0 to 100 for a share and a plain number for an average.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        APIResponse | PydanticDetail
    """

    return (
        await asyncio_detailed(
            tenant_path=tenant_path,
            client=client,
            body=body,
        )
    ).parsed
