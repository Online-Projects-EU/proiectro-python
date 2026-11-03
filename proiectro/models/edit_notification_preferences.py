from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.edit_notification_preferences_scope import (
    EditNotificationPreferencesScope,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.edit_notification_preferences_preferences import (
        EditNotificationPreferencesPreferences,
    )


T = TypeVar("T", bound="EditNotificationPreferences")


@_attrs_define
class EditNotificationPreferences:
    """A **sparse** notification-preference edit.

    `preferences` maps a notification type or group key to the channels the user expressed an
    opinion about: `{"support": {"web": false}, "support_assigned": {"mobile": true}}`.

    Only the keys sent are written. An absent key keeps whatever was stored, and a stored key
    that is absent here is not cleared, matching how every other edit in this codebase
    behaves. To go back to following the product default, send the key with an empty object
    and it is removed.

        Attributes:
            scope (EditNotificationPreferencesScope | Unset):  Default: EditNotificationPreferencesScope.USER.
            preferences (EditNotificationPreferencesPreferences | Unset):
    """

    scope: EditNotificationPreferencesScope | Unset = (
        EditNotificationPreferencesScope.USER
    )
    preferences: EditNotificationPreferencesPreferences | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        scope: str | Unset = UNSET
        if not isinstance(self.scope, Unset):
            scope = self.scope.value

        preferences: dict[str, Any] | Unset = UNSET
        if not isinstance(self.preferences, Unset):
            preferences = self.preferences.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if scope is not UNSET:
            field_dict["scope"] = scope
        if preferences is not UNSET:
            field_dict["preferences"] = preferences

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.edit_notification_preferences_preferences import (
            EditNotificationPreferencesPreferences,
        )

        d = dict(src_dict)
        _scope = d.pop("scope", UNSET)
        scope: EditNotificationPreferencesScope | Unset
        if isinstance(_scope, Unset):
            scope = UNSET
        else:
            scope = EditNotificationPreferencesScope(_scope)

        _preferences = d.pop("preferences", UNSET)
        preferences: EditNotificationPreferencesPreferences | Unset
        if isinstance(_preferences, Unset):
            preferences = UNSET
        else:
            preferences = EditNotificationPreferencesPreferences.from_dict(_preferences)

        edit_notification_preferences = cls(
            scope=scope,
            preferences=preferences,
        )

        edit_notification_preferences.additional_properties = d
        return edit_notification_preferences

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
