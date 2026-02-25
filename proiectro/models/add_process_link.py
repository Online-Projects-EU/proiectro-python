from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="AddProcessLink")


@_attrs_define
class AddProcessLink:
    """
    Attributes:
        source_stage (str):
        target_stage (str):
    """

    source_stage: str
    target_stage: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        source_stage = self.source_stage

        target_stage = self.target_stage

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "source_stage": source_stage,
                "target_stage": target_stage,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        source_stage = d.pop("source_stage")

        target_stage = d.pop("target_stage")

        add_process_link = cls(
            source_stage=source_stage,
            target_stage=target_stage,
        )

        add_process_link.additional_properties = d
        return add_process_link

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
