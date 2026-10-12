from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.notification_type_option_channels import (
        NotificationTypeOptionChannels,
    )


T = TypeVar("T", bound="NotificationTypeOption")


@_attrs_define
class NotificationTypeOption:
    """One row in the preferences screen.

    Attributes:
        type_ (str):
        label (str):
        description (str):
        icon (str):
        priority (str):
        user_configurable (bool):
        channels (NotificationTypeOptionChannels):
    """

    type_: str
    label: str
    description: str
    icon: str
    priority: str
    user_configurable: bool
    channels: NotificationTypeOptionChannels
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        label = self.label

        description = self.description

        icon = self.icon

        priority = self.priority

        user_configurable = self.user_configurable

        channels = self.channels.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "label": label,
                "description": description,
                "icon": icon,
                "priority": priority,
                "user_configurable": user_configurable,
                "channels": channels,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.notification_type_option_channels import (
            NotificationTypeOptionChannels,
        )

        d = dict(src_dict)
        type_ = d.pop("type")

        label = d.pop("label")

        description = d.pop("description")

        icon = d.pop("icon")

        priority = d.pop("priority")

        user_configurable = d.pop("user_configurable")

        channels = NotificationTypeOptionChannels.from_dict(d.pop("channels"))

        notification_type_option = cls(
            type_=type_,
            label=label,
            description=description,
            icon=icon,
            priority=priority,
            user_configurable=user_configurable,
            channels=channels,
        )

        notification_type_option.additional_properties = d
        return notification_type_option

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
