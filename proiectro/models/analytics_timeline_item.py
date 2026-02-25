from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="AnalyticsTimelineItem")


@_attrs_define
class AnalyticsTimelineItem:
    """Work item in timeline view

    Attributes:
        id (str):
        name (str):
        remaining_hours (float):
        percent_complete (int):
        project_name (None | str | Unset):
        project_id (None | str | Unset):
        owner_name (None | str | Unset):
        owner_id (None | str | Unset):
        due_date (datetime.date | None | Unset):
        type_name (None | str | Unset):
        days_overdue (int | None | Unset):
    """

    id: str
    name: str
    remaining_hours: float
    percent_complete: int
    project_name: None | str | Unset = UNSET
    project_id: None | str | Unset = UNSET
    owner_name: None | str | Unset = UNSET
    owner_id: None | str | Unset = UNSET
    due_date: datetime.date | None | Unset = UNSET
    type_name: None | str | Unset = UNSET
    days_overdue: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        remaining_hours = self.remaining_hours

        percent_complete = self.percent_complete

        project_name: None | str | Unset
        if isinstance(self.project_name, Unset):
            project_name = UNSET
        else:
            project_name = self.project_name

        project_id: None | str | Unset
        if isinstance(self.project_id, Unset):
            project_id = UNSET
        else:
            project_id = self.project_id

        owner_name: None | str | Unset
        if isinstance(self.owner_name, Unset):
            owner_name = UNSET
        else:
            owner_name = self.owner_name

        owner_id: None | str | Unset
        if isinstance(self.owner_id, Unset):
            owner_id = UNSET
        else:
            owner_id = self.owner_id

        due_date: None | str | Unset
        if isinstance(self.due_date, Unset):
            due_date = UNSET
        elif isinstance(self.due_date, datetime.date):
            due_date = self.due_date.isoformat()
        else:
            due_date = self.due_date

        type_name: None | str | Unset
        if isinstance(self.type_name, Unset):
            type_name = UNSET
        else:
            type_name = self.type_name

        days_overdue: int | None | Unset
        if isinstance(self.days_overdue, Unset):
            days_overdue = UNSET
        else:
            days_overdue = self.days_overdue

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "remaining_hours": remaining_hours,
                "percent_complete": percent_complete,
            }
        )
        if project_name is not UNSET:
            field_dict["project_name"] = project_name
        if project_id is not UNSET:
            field_dict["project_id"] = project_id
        if owner_name is not UNSET:
            field_dict["owner_name"] = owner_name
        if owner_id is not UNSET:
            field_dict["owner_id"] = owner_id
        if due_date is not UNSET:
            field_dict["due_date"] = due_date
        if type_name is not UNSET:
            field_dict["type_name"] = type_name
        if days_overdue is not UNSET:
            field_dict["days_overdue"] = days_overdue

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        remaining_hours = d.pop("remaining_hours")

        percent_complete = d.pop("percent_complete")

        def _parse_project_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        project_name = _parse_project_name(d.pop("project_name", UNSET))

        def _parse_project_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        project_id = _parse_project_id(d.pop("project_id", UNSET))

        def _parse_owner_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        owner_name = _parse_owner_name(d.pop("owner_name", UNSET))

        def _parse_owner_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        owner_id = _parse_owner_id(d.pop("owner_id", UNSET))

        def _parse_due_date(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                due_date_type_0 = isoparse(data).date()

                return due_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None | Unset, data)

        due_date = _parse_due_date(d.pop("due_date", UNSET))

        def _parse_type_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        type_name = _parse_type_name(d.pop("type_name", UNSET))

        def _parse_days_overdue(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        days_overdue = _parse_days_overdue(d.pop("days_overdue", UNSET))

        analytics_timeline_item = cls(
            id=id,
            name=name,
            remaining_hours=remaining_hours,
            percent_complete=percent_complete,
            project_name=project_name,
            project_id=project_id,
            owner_name=owner_name,
            owner_id=owner_id,
            due_date=due_date,
            type_name=type_name,
            days_overdue=days_overdue,
        )

        analytics_timeline_item.additional_properties = d
        return analytics_timeline_item

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
