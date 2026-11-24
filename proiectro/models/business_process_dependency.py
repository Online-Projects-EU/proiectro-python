from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="BusinessProcessDependency")


@_attrs_define
class BusinessProcessDependency:
    """A process that creates something this process uses

    Attributes:
        process_key (str):
        process_name (str):
        group_name (str):
        is_setup (bool):
    """

    process_key: str
    process_name: str
    group_name: str
    is_setup: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        process_key = self.process_key

        process_name = self.process_name

        group_name = self.group_name

        is_setup = self.is_setup

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "process_key": process_key,
                "process_name": process_name,
                "group_name": group_name,
                "is_setup": is_setup,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        process_key = d.pop("process_key")

        process_name = d.pop("process_name")

        group_name = d.pop("group_name")

        is_setup = d.pop("is_setup")

        business_process_dependency = cls(
            process_key=process_key,
            process_name=process_name,
            group_name=group_name,
            is_setup=is_setup,
        )

        business_process_dependency.additional_properties = d
        return business_process_dependency

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
