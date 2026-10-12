from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="EditMemberMiscPreferences")


@_attrs_define
class EditMemberMiscPreferences:
    """
    Attributes:
        preference_feed (bool | None | Unset):
        preference_ownership (bool | None | Unset):
    """

    preference_feed: bool | None | Unset = UNSET
    preference_ownership: bool | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        preference_feed: bool | None | Unset
        if isinstance(self.preference_feed, Unset):
            preference_feed = UNSET
        else:
            preference_feed = self.preference_feed

        preference_ownership: bool | None | Unset
        if isinstance(self.preference_ownership, Unset):
            preference_ownership = UNSET
        else:
            preference_ownership = self.preference_ownership

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if preference_feed is not UNSET:
            field_dict["preference_feed"] = preference_feed
        if preference_ownership is not UNSET:
            field_dict["preference_ownership"] = preference_ownership

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_preference_feed(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        preference_feed = _parse_preference_feed(d.pop("preference_feed", UNSET))

        def _parse_preference_ownership(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        preference_ownership = _parse_preference_ownership(
            d.pop("preference_ownership", UNSET)
        )

        edit_member_misc_preferences = cls(
            preference_feed=preference_feed,
            preference_ownership=preference_ownership,
        )

        edit_member_misc_preferences.additional_properties = d
        return edit_member_misc_preferences

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
