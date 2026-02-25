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
        preference_mentions (bool | None | Unset):
        preference_feed (bool | None | Unset):
        preference_ownership (bool | None | Unset):
        preference_my_string (None | str | Unset):
        preference_my_number (int | None | Unset):
        preference_theme (None | str | Unset):
    """

    preference_mentions: bool | None | Unset = UNSET
    preference_feed: bool | None | Unset = UNSET
    preference_ownership: bool | None | Unset = UNSET
    preference_my_string: None | str | Unset = UNSET
    preference_my_number: int | None | Unset = UNSET
    preference_theme: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        preference_mentions: bool | None | Unset
        if isinstance(self.preference_mentions, Unset):
            preference_mentions = UNSET
        else:
            preference_mentions = self.preference_mentions

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

        preference_my_string: None | str | Unset
        if isinstance(self.preference_my_string, Unset):
            preference_my_string = UNSET
        else:
            preference_my_string = self.preference_my_string

        preference_my_number: int | None | Unset
        if isinstance(self.preference_my_number, Unset):
            preference_my_number = UNSET
        else:
            preference_my_number = self.preference_my_number

        preference_theme: None | str | Unset
        if isinstance(self.preference_theme, Unset):
            preference_theme = UNSET
        else:
            preference_theme = self.preference_theme

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if preference_mentions is not UNSET:
            field_dict["preference_mentions"] = preference_mentions
        if preference_feed is not UNSET:
            field_dict["preference_feed"] = preference_feed
        if preference_ownership is not UNSET:
            field_dict["preference_ownership"] = preference_ownership
        if preference_my_string is not UNSET:
            field_dict["preference_my_string"] = preference_my_string
        if preference_my_number is not UNSET:
            field_dict["preference_my_number"] = preference_my_number
        if preference_theme is not UNSET:
            field_dict["preference_theme"] = preference_theme

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_preference_mentions(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        preference_mentions = _parse_preference_mentions(
            d.pop("preference_mentions", UNSET)
        )

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

        def _parse_preference_my_string(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        preference_my_string = _parse_preference_my_string(
            d.pop("preference_my_string", UNSET)
        )

        def _parse_preference_my_number(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        preference_my_number = _parse_preference_my_number(
            d.pop("preference_my_number", UNSET)
        )

        def _parse_preference_theme(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        preference_theme = _parse_preference_theme(d.pop("preference_theme", UNSET))

        edit_member_misc_preferences = cls(
            preference_mentions=preference_mentions,
            preference_feed=preference_feed,
            preference_ownership=preference_ownership,
            preference_my_string=preference_my_string,
            preference_my_number=preference_my_number,
            preference_theme=preference_theme,
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
