from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.notification_type_option import NotificationTypeOption


T = TypeVar("T", bound="NotificationGroupOption")


@_attrs_define
class NotificationGroupOption:
    """One collapsible section, filtered to what this workspace has enabled.

    Attributes:
        group (str):
        label (str):
        types (list[NotificationTypeOption]):
    """

    group: str
    label: str
    types: list[NotificationTypeOption]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        group = self.group

        label = self.label

        types = []
        for types_item_data in self.types:
            types_item = types_item_data.to_dict()
            types.append(types_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "group": group,
                "label": label,
                "types": types,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.notification_type_option import NotificationTypeOption

        d = dict(src_dict)
        group = d.pop("group")

        label = d.pop("label")

        types = []
        _types = d.pop("types")
        for types_item_data in _types:
            types_item = NotificationTypeOption.from_dict(types_item_data)

            types.append(types_item)

        notification_group_option = cls(
            group=group,
            label=label,
            types=types,
        )

        notification_group_option.additional_properties = d
        return notification_group_option

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
