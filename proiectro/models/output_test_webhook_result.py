from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="OutputTestWebhookResult")


@_attrs_define
class OutputTestWebhookResult:
    """
    Attributes:
        success (bool):
        message (str):
        status_code (int | Unset):  Default: 0.
        duration_ms (int | Unset):  Default: 0.
        response_body (str | Unset):  Default: ''.
        error_type (str | Unset):  Default: ''.
    """

    success: bool
    message: str
    status_code: int | Unset = 0
    duration_ms: int | Unset = 0
    response_body: str | Unset = ""
    error_type: str | Unset = ""
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        success = self.success

        message = self.message

        status_code = self.status_code

        duration_ms = self.duration_ms

        response_body = self.response_body

        error_type = self.error_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "success": success,
                "message": message,
            }
        )
        if status_code is not UNSET:
            field_dict["status_code"] = status_code
        if duration_ms is not UNSET:
            field_dict["duration_ms"] = duration_ms
        if response_body is not UNSET:
            field_dict["response_body"] = response_body
        if error_type is not UNSET:
            field_dict["error_type"] = error_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        success = d.pop("success")

        message = d.pop("message")

        status_code = d.pop("status_code", UNSET)

        duration_ms = d.pop("duration_ms", UNSET)

        response_body = d.pop("response_body", UNSET)

        error_type = d.pop("error_type", UNSET)

        output_test_webhook_result = cls(
            success=success,
            message=message,
            status_code=status_code,
            duration_ms=duration_ms,
            response_body=response_body,
            error_type=error_type,
        )

        output_test_webhook_result.additional_properties = d
        return output_test_webhook_result

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
