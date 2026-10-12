from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AvailabilityHours")


@_attrs_define
class AvailabilityHours:
    """
    Attributes:
        external_id (None | str | Unset):
        start_time (None | str | Unset):
        end_time (None | str | Unset):
        member_tz_start_time (None | str | Unset):
        member_tz_end_time (None | str | Unset):
        viewer_tz_start_time (None | str | Unset):
        viewer_tz_end_time (None | str | Unset):
        hour_range (list[int] | Unset):
        hour_range_member_tz (list[int] | Unset):
        hour_range_viewer_tz (list[int] | Unset):
        total (int | Unset):  Default: 0.
    """

    external_id: None | str | Unset = UNSET
    start_time: None | str | Unset = UNSET
    end_time: None | str | Unset = UNSET
    member_tz_start_time: None | str | Unset = UNSET
    member_tz_end_time: None | str | Unset = UNSET
    viewer_tz_start_time: None | str | Unset = UNSET
    viewer_tz_end_time: None | str | Unset = UNSET
    hour_range: list[int] | Unset = UNSET
    hour_range_member_tz: list[int] | Unset = UNSET
    hour_range_viewer_tz: list[int] | Unset = UNSET
    total: int | Unset = 0
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        external_id: None | str | Unset
        if isinstance(self.external_id, Unset):
            external_id = UNSET
        else:
            external_id = self.external_id

        start_time: None | str | Unset
        if isinstance(self.start_time, Unset):
            start_time = UNSET
        else:
            start_time = self.start_time

        end_time: None | str | Unset
        if isinstance(self.end_time, Unset):
            end_time = UNSET
        else:
            end_time = self.end_time

        member_tz_start_time: None | str | Unset
        if isinstance(self.member_tz_start_time, Unset):
            member_tz_start_time = UNSET
        else:
            member_tz_start_time = self.member_tz_start_time

        member_tz_end_time: None | str | Unset
        if isinstance(self.member_tz_end_time, Unset):
            member_tz_end_time = UNSET
        else:
            member_tz_end_time = self.member_tz_end_time

        viewer_tz_start_time: None | str | Unset
        if isinstance(self.viewer_tz_start_time, Unset):
            viewer_tz_start_time = UNSET
        else:
            viewer_tz_start_time = self.viewer_tz_start_time

        viewer_tz_end_time: None | str | Unset
        if isinstance(self.viewer_tz_end_time, Unset):
            viewer_tz_end_time = UNSET
        else:
            viewer_tz_end_time = self.viewer_tz_end_time

        hour_range: list[int] | Unset = UNSET
        if not isinstance(self.hour_range, Unset):
            hour_range = self.hour_range

        hour_range_member_tz: list[int] | Unset = UNSET
        if not isinstance(self.hour_range_member_tz, Unset):
            hour_range_member_tz = self.hour_range_member_tz

        hour_range_viewer_tz: list[int] | Unset = UNSET
        if not isinstance(self.hour_range_viewer_tz, Unset):
            hour_range_viewer_tz = self.hour_range_viewer_tz

        total = self.total

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if external_id is not UNSET:
            field_dict["external_id"] = external_id
        if start_time is not UNSET:
            field_dict["start_time"] = start_time
        if end_time is not UNSET:
            field_dict["end_time"] = end_time
        if member_tz_start_time is not UNSET:
            field_dict["member_tz_start_time"] = member_tz_start_time
        if member_tz_end_time is not UNSET:
            field_dict["member_tz_end_time"] = member_tz_end_time
        if viewer_tz_start_time is not UNSET:
            field_dict["viewer_tz_start_time"] = viewer_tz_start_time
        if viewer_tz_end_time is not UNSET:
            field_dict["viewer_tz_end_time"] = viewer_tz_end_time
        if hour_range is not UNSET:
            field_dict["hour_range"] = hour_range
        if hour_range_member_tz is not UNSET:
            field_dict["hour_range_member_tz"] = hour_range_member_tz
        if hour_range_viewer_tz is not UNSET:
            field_dict["hour_range_viewer_tz"] = hour_range_viewer_tz
        if total is not UNSET:
            field_dict["total"] = total

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_external_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        external_id = _parse_external_id(d.pop("external_id", UNSET))

        def _parse_start_time(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        start_time = _parse_start_time(d.pop("start_time", UNSET))

        def _parse_end_time(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        end_time = _parse_end_time(d.pop("end_time", UNSET))

        def _parse_member_tz_start_time(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        member_tz_start_time = _parse_member_tz_start_time(
            d.pop("member_tz_start_time", UNSET)
        )

        def _parse_member_tz_end_time(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        member_tz_end_time = _parse_member_tz_end_time(
            d.pop("member_tz_end_time", UNSET)
        )

        def _parse_viewer_tz_start_time(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        viewer_tz_start_time = _parse_viewer_tz_start_time(
            d.pop("viewer_tz_start_time", UNSET)
        )

        def _parse_viewer_tz_end_time(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        viewer_tz_end_time = _parse_viewer_tz_end_time(
            d.pop("viewer_tz_end_time", UNSET)
        )

        hour_range = cast(list[int], d.pop("hour_range", UNSET))

        hour_range_member_tz = cast(list[int], d.pop("hour_range_member_tz", UNSET))

        hour_range_viewer_tz = cast(list[int], d.pop("hour_range_viewer_tz", UNSET))

        total = d.pop("total", UNSET)

        availability_hours = cls(
            external_id=external_id,
            start_time=start_time,
            end_time=end_time,
            member_tz_start_time=member_tz_start_time,
            member_tz_end_time=member_tz_end_time,
            viewer_tz_start_time=viewer_tz_start_time,
            viewer_tz_end_time=viewer_tz_end_time,
            hour_range=hour_range,
            hour_range_member_tz=hour_range_member_tz,
            hour_range_viewer_tz=hour_range_viewer_tz,
            total=total,
        )

        availability_hours.additional_properties = d
        return availability_hours

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
