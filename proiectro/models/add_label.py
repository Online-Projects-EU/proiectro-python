from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.add_label_label_type import AddLabelLabelType
from ..types import UNSET, Unset

T = TypeVar("T", bound="AddLabel")


@_attrs_define
class AddLabel:
    """
    Attributes:
        name (str):
        label_type (AddLabelLabelType | Unset):  Default: AddLabelLabelType.TEXT.
    """

    name: str
    label_type: AddLabelLabelType | Unset = AddLabelLabelType.TEXT
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        label_type: str | Unset = UNSET
        if not isinstance(self.label_type, Unset):
            label_type = self.label_type.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
            }
        )
        if label_type is not UNSET:
            field_dict["label_type"] = label_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        _label_type = d.pop("label_type", UNSET)
        label_type: AddLabelLabelType | Unset
        if isinstance(_label_type, Unset):
            label_type = UNSET
        else:
            label_type = AddLabelLabelType(_label_type)

        add_label = cls(
            name=name,
            label_type=label_type,
        )

        add_label.additional_properties = d
        return add_label

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
