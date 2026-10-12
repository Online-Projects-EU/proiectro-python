from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.notification_group_option import NotificationGroupOption


T = TypeVar("T", bound="OutputNotificationPreferences")


@_attrs_define
class OutputNotificationPreferences:
    """The preferences screen's whole state: what can be tuned, and how it currently resolves.

    Attributes:
        scope (str):
        edit_url (str):
        channels (list[str]):
        editable_channels (list[str]):
        groups (list[NotificationGroupOption]):
    """

    scope: str
    edit_url: str
    channels: list[str]
    editable_channels: list[str]
    groups: list[NotificationGroupOption]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        scope = self.scope

        edit_url = self.edit_url

        channels = self.channels

        editable_channels = self.editable_channels

        groups = []
        for groups_item_data in self.groups:
            groups_item = groups_item_data.to_dict()
            groups.append(groups_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "scope": scope,
                "edit_url": edit_url,
                "channels": channels,
                "editable_channels": editable_channels,
                "groups": groups,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.notification_group_option import NotificationGroupOption

        d = dict(src_dict)
        scope = d.pop("scope")

        edit_url = d.pop("edit_url")

        channels = cast(list[str], d.pop("channels"))

        editable_channels = cast(list[str], d.pop("editable_channels"))

        groups = []
        _groups = d.pop("groups")
        for groups_item_data in _groups:
            groups_item = NotificationGroupOption.from_dict(groups_item_data)

            groups.append(groups_item)

        output_notification_preferences = cls(
            scope=scope,
            edit_url=edit_url,
            channels=channels,
            editable_channels=editable_channels,
            groups=groups,
        )

        output_notification_preferences.additional_properties = d
        return output_notification_preferences

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
