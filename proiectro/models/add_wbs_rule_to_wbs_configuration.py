from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AddWBSRuleToWBSConfiguration")


@_attrs_define
class AddWBSRuleToWBSConfiguration:
    """
    Attributes:
        wbsconfiguration (str):
        child_work_item_type (str):
        parent_work_item_type (None | str | Unset):
    """

    wbsconfiguration: str
    child_work_item_type: str
    parent_work_item_type: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        wbsconfiguration = self.wbsconfiguration

        child_work_item_type = self.child_work_item_type

        parent_work_item_type: None | str | Unset
        if isinstance(self.parent_work_item_type, Unset):
            parent_work_item_type = UNSET
        else:
            parent_work_item_type = self.parent_work_item_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "wbsconfiguration": wbsconfiguration,
                "child_work_item_type": child_work_item_type,
            }
        )
        if parent_work_item_type is not UNSET:
            field_dict["parent_work_item_type"] = parent_work_item_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        wbsconfiguration = d.pop("wbsconfiguration")

        child_work_item_type = d.pop("child_work_item_type")

        def _parse_parent_work_item_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        parent_work_item_type = _parse_parent_work_item_type(
            d.pop("parent_work_item_type", UNSET)
        )

        add_wbs_rule_to_wbs_configuration = cls(
            wbsconfiguration=wbsconfiguration,
            child_work_item_type=child_work_item_type,
            parent_work_item_type=parent_work_item_type,
        )

        add_wbs_rule_to_wbs_configuration.additional_properties = d
        return add_wbs_rule_to_wbs_configuration

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
