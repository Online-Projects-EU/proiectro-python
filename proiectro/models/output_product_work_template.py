from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="OutputProductWorkTemplate")


@_attrs_define
class OutputProductWorkTemplate:
    """Individual template data for product templates tab

    Attributes:
        id (str):
        name (str):
        work_item_type_name (str):
        work_item_type_scheduling_behaviour (str):
        is_active (bool):
        wbsconfiguration_name (None | str | Unset):
        wbsconfiguration_matches_project (bool | Unset):  Default: False.
        estimated_work_hours (int | None | Unset):
        estimated_duration_days (int | None | Unset):
        total_hours (int | Unset):  Default: 0.
        total_days (int | Unset):  Default: 0.
    """

    id: str
    name: str
    work_item_type_name: str
    work_item_type_scheduling_behaviour: str
    is_active: bool
    wbsconfiguration_name: None | str | Unset = UNSET
    wbsconfiguration_matches_project: bool | Unset = False
    estimated_work_hours: int | None | Unset = UNSET
    estimated_duration_days: int | None | Unset = UNSET
    total_hours: int | Unset = 0
    total_days: int | Unset = 0
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        work_item_type_name = self.work_item_type_name

        work_item_type_scheduling_behaviour = self.work_item_type_scheduling_behaviour

        is_active = self.is_active

        wbsconfiguration_name: None | str | Unset
        if isinstance(self.wbsconfiguration_name, Unset):
            wbsconfiguration_name = UNSET
        else:
            wbsconfiguration_name = self.wbsconfiguration_name

        wbsconfiguration_matches_project = self.wbsconfiguration_matches_project

        estimated_work_hours: int | None | Unset
        if isinstance(self.estimated_work_hours, Unset):
            estimated_work_hours = UNSET
        else:
            estimated_work_hours = self.estimated_work_hours

        estimated_duration_days: int | None | Unset
        if isinstance(self.estimated_duration_days, Unset):
            estimated_duration_days = UNSET
        else:
            estimated_duration_days = self.estimated_duration_days

        total_hours = self.total_hours

        total_days = self.total_days

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "work_item_type_name": work_item_type_name,
                "work_item_type_scheduling_behaviour": work_item_type_scheduling_behaviour,
                "is_active": is_active,
            }
        )
        if wbsconfiguration_name is not UNSET:
            field_dict["wbsconfiguration_name"] = wbsconfiguration_name
        if wbsconfiguration_matches_project is not UNSET:
            field_dict["wbsconfiguration_matches_project"] = (
                wbsconfiguration_matches_project
            )
        if estimated_work_hours is not UNSET:
            field_dict["estimated_work_hours"] = estimated_work_hours
        if estimated_duration_days is not UNSET:
            field_dict["estimated_duration_days"] = estimated_duration_days
        if total_hours is not UNSET:
            field_dict["total_hours"] = total_hours
        if total_days is not UNSET:
            field_dict["total_days"] = total_days

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        work_item_type_name = d.pop("work_item_type_name")

        work_item_type_scheduling_behaviour = d.pop(
            "work_item_type_scheduling_behaviour"
        )

        is_active = d.pop("is_active")

        def _parse_wbsconfiguration_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        wbsconfiguration_name = _parse_wbsconfiguration_name(
            d.pop("wbsconfiguration_name", UNSET)
        )

        wbsconfiguration_matches_project = d.pop(
            "wbsconfiguration_matches_project", UNSET
        )

        def _parse_estimated_work_hours(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        estimated_work_hours = _parse_estimated_work_hours(
            d.pop("estimated_work_hours", UNSET)
        )

        def _parse_estimated_duration_days(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        estimated_duration_days = _parse_estimated_duration_days(
            d.pop("estimated_duration_days", UNSET)
        )

        total_hours = d.pop("total_hours", UNSET)

        total_days = d.pop("total_days", UNSET)

        output_product_work_template = cls(
            id=id,
            name=name,
            work_item_type_name=work_item_type_name,
            work_item_type_scheduling_behaviour=work_item_type_scheduling_behaviour,
            is_active=is_active,
            wbsconfiguration_name=wbsconfiguration_name,
            wbsconfiguration_matches_project=wbsconfiguration_matches_project,
            estimated_work_hours=estimated_work_hours,
            estimated_duration_days=estimated_duration_days,
            total_hours=total_hours,
            total_days=total_days,
        )

        output_product_work_template.additional_properties = d
        return output_product_work_template

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
