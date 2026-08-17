from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_response import APIResponse
from ...models.validate_form_step import ValidateFormStep
from ...models.validate_form_step_response import ValidateFormStepResponse
from ...types import Response


def _get_kwargs(
    tenant_path: str,
    form_id: str,
    *,
    body: ValidateFormStep,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/{tenant_path}/validate_form_step/{form_id}".format(
            tenant_path=quote(str(tenant_path), safe=""),
            form_id=quote(str(form_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> APIResponse | ValidateFormStepResponse | None:
    if response.status_code == 200:
        response_200 = APIResponse.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = APIResponse.from_dict(response.json())

        return response_400

    if response.status_code == 409:
        response_409 = APIResponse.from_dict(response.json())

        return response_409

    if response.status_code == 422:
        response_422 = ValidateFormStepResponse.from_dict(response.json())

        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[APIResponse | ValidateFormStepResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    tenant_path: str,
    form_id: str,
    *,
    client: AuthenticatedClient,
    body: ValidateFormStep,
) -> Response[APIResponse | ValidateFormStepResponse]:
    """Validate Form Step

     Stateless per-step validation for the multi-step submission UI (stores nothing).

    Args:
        tenant_path (str):
        form_id (str):
        body (ValidateFormStep):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[APIResponse | ValidateFormStepResponse]
    """

    kwargs = _get_kwargs(
        tenant_path=tenant_path,
        form_id=form_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    tenant_path: str,
    form_id: str,
    *,
    client: AuthenticatedClient,
    body: ValidateFormStep,
) -> APIResponse | ValidateFormStepResponse | None:
    """Validate Form Step

     Stateless per-step validation for the multi-step submission UI (stores nothing).

    Args:
        tenant_path (str):
        form_id (str):
        body (ValidateFormStep):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        APIResponse | ValidateFormStepResponse
    """

    return sync_detailed(
        tenant_path=tenant_path,
        form_id=form_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    tenant_path: str,
    form_id: str,
    *,
    client: AuthenticatedClient,
    body: ValidateFormStep,
) -> Response[APIResponse | ValidateFormStepResponse]:
    """Validate Form Step

     Stateless per-step validation for the multi-step submission UI (stores nothing).

    Args:
        tenant_path (str):
        form_id (str):
        body (ValidateFormStep):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[APIResponse | ValidateFormStepResponse]
    """

    kwargs = _get_kwargs(
        tenant_path=tenant_path,
        form_id=form_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    tenant_path: str,
    form_id: str,
    *,
    client: AuthenticatedClient,
    body: ValidateFormStep,
) -> APIResponse | ValidateFormStepResponse | None:
    """Validate Form Step

     Stateless per-step validation for the multi-step submission UI (stores nothing).

    Args:
        tenant_path (str):
        form_id (str):
        body (ValidateFormStep):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        APIResponse | ValidateFormStepResponse
    """

    return (
        await asyncio_detailed(
            tenant_path=tenant_path,
            form_id=form_id,
            client=client,
            body=body,
        )
    ).parsed
