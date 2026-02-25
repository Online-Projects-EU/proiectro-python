from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ScheduleTaskItem")


@_attrs_define
class ScheduleTaskItem:
    """Single task in project schedule with critical path data

    Attributes:
        id (str):
        name (str):
        hierarchy_id (str):
        total_float_days (int):
        free_float_days (int):
        is_critical (bool):
        duration_days (int):
        early_start (None | str | Unset):
        early_finish (None | str | Unset):
        late_start (None | str | Unset):
        late_finish (None | str | Unset):
    """

    id: str
    name: str
    hierarchy_id: str
    total_float_days: int
    free_float_days: int
    is_critical: bool
    duration_days: int
    early_start: None | str | Unset = UNSET
    early_finish: None | str | Unset = UNSET
    late_start: None | str | Unset = UNSET
    late_finish: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        hierarchy_id = self.hierarchy_id

        total_float_days = self.total_float_days

        free_float_days = self.free_float_days

        is_critical = self.is_critical

        duration_days = self.duration_days

        early_start: None | str | Unset
        if isinstance(self.early_start, Unset):
            early_start = UNSET
        else:
            early_start = self.early_start

        early_finish: None | str | Unset
        if isinstance(self.early_finish, Unset):
            early_finish = UNSET
        else:
            early_finish = self.early_finish

        late_start: None | str | Unset
        if isinstance(self.late_start, Unset):
            late_start = UNSET
        else:
            late_start = self.late_start

        late_finish: None | str | Unset
        if isinstance(self.late_finish, Unset):
            late_finish = UNSET
        else:
            late_finish = self.late_finish

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "hierarchy_id": hierarchy_id,
                "total_float_days": total_float_days,
                "free_float_days": free_float_days,
                "is_critical": is_critical,
                "duration_days": duration_days,
            }
        )
        if early_start is not UNSET:
            field_dict["early_start"] = early_start
        if early_finish is not UNSET:
            field_dict["early_finish"] = early_finish
        if late_start is not UNSET:
            field_dict["late_start"] = late_start
        if late_finish is not UNSET:
            field_dict["late_finish"] = late_finish

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        hierarchy_id = d.pop("hierarchy_id")

        total_float_days = d.pop("total_float_days")

        free_float_days = d.pop("free_float_days")

        is_critical = d.pop("is_critical")

        duration_days = d.pop("duration_days")

        def _parse_early_start(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        early_start = _parse_early_start(d.pop("early_start", UNSET))

        def _parse_early_finish(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        early_finish = _parse_early_finish(d.pop("early_finish", UNSET))

        def _parse_late_start(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        late_start = _parse_late_start(d.pop("late_start", UNSET))

        def _parse_late_finish(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        late_finish = _parse_late_finish(d.pop("late_finish", UNSET))

        schedule_task_item = cls(
            id=id,
            name=name,
            hierarchy_id=hierarchy_id,
            total_float_days=total_float_days,
            free_float_days=free_float_days,
            is_critical=is_critical,
            duration_days=duration_days,
            early_start=early_start,
            early_finish=early_finish,
            late_start=late_start,
            late_finish=late_finish,
        )

        schedule_task_item.additional_properties = d
        return schedule_task_item

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
