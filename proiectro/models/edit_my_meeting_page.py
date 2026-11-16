from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="EditMyMeetingPage")


@_attrs_define
class EditMyMeetingPage:
    """Your own meeting page (plans/PUBLIC_INBOUND.md D1). Created on first save. The address is the
    last part of the link, lowercase letters, digits and dashes; left empty, it is made from your
    name. Duration is 15, 30, 45, 60 or 90 minutes; the buffer 0, 5, 10 or 15, kept free before and
    after each meeting. An omitted key keeps the stored value.

        Attributes:
            slug (None | str | Unset):
            title (None | str | Unset):
            duration_minutes (int | None | Unset):
            buffer_minutes (int | None | Unset):
            location (None | str | Unset):
            is_active (bool | None | Unset):
    """

    slug: None | str | Unset = UNSET
    title: None | str | Unset = UNSET
    duration_minutes: int | None | Unset = UNSET
    buffer_minutes: int | None | Unset = UNSET
    location: None | str | Unset = UNSET
    is_active: bool | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        slug: None | str | Unset
        if isinstance(self.slug, Unset):
            slug = UNSET
        else:
            slug = self.slug

        title: None | str | Unset
        if isinstance(self.title, Unset):
            title = UNSET
        else:
            title = self.title

        duration_minutes: int | None | Unset
        if isinstance(self.duration_minutes, Unset):
            duration_minutes = UNSET
        else:
            duration_minutes = self.duration_minutes

        buffer_minutes: int | None | Unset
        if isinstance(self.buffer_minutes, Unset):
            buffer_minutes = UNSET
        else:
            buffer_minutes = self.buffer_minutes

        location: None | str | Unset
        if isinstance(self.location, Unset):
            location = UNSET
        else:
            location = self.location

        is_active: bool | None | Unset
        if isinstance(self.is_active, Unset):
            is_active = UNSET
        else:
            is_active = self.is_active

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if slug is not UNSET:
            field_dict["slug"] = slug
        if title is not UNSET:
            field_dict["title"] = title
        if duration_minutes is not UNSET:
            field_dict["duration_minutes"] = duration_minutes
        if buffer_minutes is not UNSET:
            field_dict["buffer_minutes"] = buffer_minutes
        if location is not UNSET:
            field_dict["location"] = location
        if is_active is not UNSET:
            field_dict["is_active"] = is_active

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_slug(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        slug = _parse_slug(d.pop("slug", UNSET))

        def _parse_title(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        title = _parse_title(d.pop("title", UNSET))

        def _parse_duration_minutes(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        duration_minutes = _parse_duration_minutes(d.pop("duration_minutes", UNSET))

        def _parse_buffer_minutes(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        buffer_minutes = _parse_buffer_minutes(d.pop("buffer_minutes", UNSET))

        def _parse_location(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        location = _parse_location(d.pop("location", UNSET))

        def _parse_is_active(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_active = _parse_is_active(d.pop("is_active", UNSET))

        edit_my_meeting_page = cls(
            slug=slug,
            title=title,
            duration_minutes=duration_minutes,
            buffer_minutes=buffer_minutes,
            location=location,
            is_active=is_active,
        )

        edit_my_meeting_page.additional_properties = d
        return edit_my_meeting_page

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
