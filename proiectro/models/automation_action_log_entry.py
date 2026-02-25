from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AutomationActionLogEntry")


@_attrs_define
class AutomationActionLogEntry:
    """A single action execution within an automation run.

    Attributes:
        action_type (str):
        success (bool | Unset):  Default: False.
        error_message (str | Unset):  Default: ''.
    """

    action_type: str
    success: bool | Unset = False
    error_message: str | Unset = ""
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        action_type = self.action_type

        success = self.success

        error_message = self.error_message

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "action_type": action_type,
            }
        )
        if success is not UNSET:
            field_dict["success"] = success
        if error_message is not UNSET:
            field_dict["error_message"] = error_message

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        action_type = d.pop("action_type")

        success = d.pop("success", UNSET)

        error_message = d.pop("error_message", UNSET)

        automation_action_log_entry = cls(
            action_type=action_type,
            success=success,
            error_message=error_message,
        )

        automation_action_log_entry.additional_properties = d
        return automation_action_log_entry

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
