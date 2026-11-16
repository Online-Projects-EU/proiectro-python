from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_response import APIResponse
from ...models.pydantic_detail import PydanticDetail
from ...models.set_email_template_default import SetEmailTemplateDefault
from ...types import Response


def _get_kwargs(
    tenant_path: str,
    purpose: str,
    *,
    body: SetEmailTemplateDefault,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/{tenant_path}/set_email_template_default/{purpose}".format(
            tenant_path=quote(str(tenant_path), safe=""),
            purpose=quote(str(purpose), safe=""),
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

    if response.status_code == 403:
        response_403 = APIResponse.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = APIResponse.from_dict(response.json())

        return response_404

    if response.status_code == 409:
        response_409 = APIResponse.from_dict(response.json())

        return response_409

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
    purpose: str,
    *,
    client: AuthenticatedClient,
    body: SetEmailTemplateDefault,
) -> Response[APIResponse | PydanticDetail]:
    """Set Email Template Default

     Choose the template a kind of email uses by default, or none, so whoever sends it chooses.

    Args:
        tenant_path (str):
        purpose (str):
        body (SetEmailTemplateDefault): `template_id`: the email template this kind of email uses
            by default; empty, none, and the person sending
            chooses each time.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[APIResponse | PydanticDetail]
    """

    kwargs = _get_kwargs(
        tenant_path=tenant_path,
        purpose=purpose,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    tenant_path: str,
    purpose: str,
    *,
    client: AuthenticatedClient,
    body: SetEmailTemplateDefault,
) -> APIResponse | PydanticDetail | None:
    """Set Email Template Default

     Choose the template a kind of email uses by default, or none, so whoever sends it chooses.

    Args:
        tenant_path (str):
        purpose (str):
        body (SetEmailTemplateDefault): `template_id`: the email template this kind of email uses
            by default; empty, none, and the person sending
            chooses each time.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        APIResponse | PydanticDetail
    """

    return sync_detailed(
        tenant_path=tenant_path,
        purpose=purpose,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    tenant_path: str,
    purpose: str,
    *,
    client: AuthenticatedClient,
    body: SetEmailTemplateDefault,
) -> Response[APIResponse | PydanticDetail]:
    """Set Email Template Default

     Choose the template a kind of email uses by default, or none, so whoever sends it chooses.

    Args:
        tenant_path (str):
        purpose (str):
        body (SetEmailTemplateDefault): `template_id`: the email template this kind of email uses
            by default; empty, none, and the person sending
            chooses each time.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[APIResponse | PydanticDetail]
    """

    kwargs = _get_kwargs(
        tenant_path=tenant_path,
        purpose=purpose,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    tenant_path: str,
    purpose: str,
    *,
    client: AuthenticatedClient,
    body: SetEmailTemplateDefault,
) -> APIResponse | PydanticDetail | None:
    """Set Email Template Default

     Choose the template a kind of email uses by default, or none, so whoever sends it chooses.

    Args:
        tenant_path (str):
        purpose (str):
        body (SetEmailTemplateDefault): `template_id`: the email template this kind of email uses
            by default; empty, none, and the person sending
            chooses each time.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        APIResponse | PydanticDetail
    """

    return (
        await asyncio_detailed(
            tenant_path=tenant_path,
            purpose=purpose,
            client=client,
            body=body,
        )
    ).parsed
