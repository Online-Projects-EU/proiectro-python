from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.work_template import WorkTemplate


T = TypeVar("T", bound="WorkScheduleItem")


@_attrs_define
class WorkScheduleItem:
    """
    Attributes:
        product_id (str):
        name (str):
        is_asap (bool):
        planned_start (datetime.datetime | None | Unset):
        planned_end (datetime.datetime | None | Unset):
        duration_days (int | None | Unset):
        work_templates (list[WorkTemplate] | None | Unset):
        total_template_hours (int | None | Unset):
    """

    product_id: str
    name: str
    is_asap: bool
    planned_start: datetime.datetime | None | Unset = UNSET
    planned_end: datetime.datetime | None | Unset = UNSET
    duration_days: int | None | Unset = UNSET
    work_templates: list[WorkTemplate] | None | Unset = UNSET
    total_template_hours: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        product_id = self.product_id

        name = self.name

        is_asap = self.is_asap

        planned_start: None | str | Unset
        if isinstance(self.planned_start, Unset):
            planned_start = UNSET
        elif isinstance(self.planned_start, datetime.datetime):
            planned_start = self.planned_start.isoformat()
        else:
            planned_start = self.planned_start

        planned_end: None | str | Unset
        if isinstance(self.planned_end, Unset):
            planned_end = UNSET
        elif isinstance(self.planned_end, datetime.datetime):
            planned_end = self.planned_end.isoformat()
        else:
            planned_end = self.planned_end

        duration_days: int | None | Unset
        if isinstance(self.duration_days, Unset):
            duration_days = UNSET
        else:
            duration_days = self.duration_days

        work_templates: list[dict[str, Any]] | None | Unset
        if isinstance(self.work_templates, Unset):
            work_templates = UNSET
        elif isinstance(self.work_templates, list):
            work_templates = []
            for work_templates_type_0_item_data in self.work_templates:
                work_templates_type_0_item = work_templates_type_0_item_data.to_dict()
                work_templates.append(work_templates_type_0_item)

        else:
            work_templates = self.work_templates

        total_template_hours: int | None | Unset
        if isinstance(self.total_template_hours, Unset):
            total_template_hours = UNSET
        else:
            total_template_hours = self.total_template_hours

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "product_id": product_id,
                "name": name,
                "is_asap": is_asap,
            }
        )
        if planned_start is not UNSET:
            field_dict["planned_start"] = planned_start
        if planned_end is not UNSET:
            field_dict["planned_end"] = planned_end
        if duration_days is not UNSET:
            field_dict["duration_days"] = duration_days
        if work_templates is not UNSET:
            field_dict["work_templates"] = work_templates
        if total_template_hours is not UNSET:
            field_dict["total_template_hours"] = total_template_hours

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.work_template import WorkTemplate

        d = dict(src_dict)
        product_id = d.pop("product_id")

        name = d.pop("name")

        is_asap = d.pop("is_asap")

        def _parse_planned_start(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                planned_start_type_0 = isoparse(data)

                return planned_start_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        planned_start = _parse_planned_start(d.pop("planned_start", UNSET))

        def _parse_planned_end(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                planned_end_type_0 = isoparse(data)

                return planned_end_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        planned_end = _parse_planned_end(d.pop("planned_end", UNSET))

        def _parse_duration_days(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        duration_days = _parse_duration_days(d.pop("duration_days", UNSET))

        def _parse_work_templates(data: object) -> list[WorkTemplate] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                work_templates_type_0 = []
                _work_templates_type_0 = data
                for work_templates_type_0_item_data in _work_templates_type_0:
                    work_templates_type_0_item = WorkTemplate.from_dict(
                        work_templates_type_0_item_data
                    )

                    work_templates_type_0.append(work_templates_type_0_item)

                return work_templates_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[WorkTemplate] | None | Unset, data)

        work_templates = _parse_work_templates(d.pop("work_templates", UNSET))

        def _parse_total_template_hours(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        total_template_hours = _parse_total_template_hours(
            d.pop("total_template_hours", UNSET)
        )

        work_schedule_item = cls(
            product_id=product_id,
            name=name,
            is_asap=is_asap,
            planned_start=planned_start,
            planned_end=planned_end,
            duration_days=duration_days,
            work_templates=work_templates,
            total_template_hours=total_template_hours,
        )

        work_schedule_item.additional_properties = d
        return work_schedule_item

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
