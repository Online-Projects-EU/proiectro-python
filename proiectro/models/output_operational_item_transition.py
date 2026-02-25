from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="OutputOperationalItemTransition")


@_attrs_define
class OutputOperationalItemTransition:
    """
    Attributes:
        action (str):
        stage_id (str):
        stage_name (str):
        icon (str):
        process_name (str | Unset):  Default: ''.
    """

    action: str
    stage_id: str
    stage_name: str
    icon: str
    process_name: str | Unset = ""
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        action = self.action

        stage_id = self.stage_id

        stage_name = self.stage_name

        icon = self.icon

        process_name = self.process_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "action": action,
                "stage_id": stage_id,
                "stage_name": stage_name,
                "icon": icon,
            }
        )
        if process_name is not UNSET:
            field_dict["process_name"] = process_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        action = d.pop("action")

        stage_id = d.pop("stage_id")

        stage_name = d.pop("stage_name")

        icon = d.pop("icon")

        process_name = d.pop("process_name", UNSET)

        output_operational_item_transition = cls(
            action=action,
            stage_id=stage_id,
            stage_name=stage_name,
            icon=icon,
            process_name=process_name,
        )

        output_operational_item_transition.additional_properties = d
        return output_operational_item_transition

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
