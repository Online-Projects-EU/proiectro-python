from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="EditWorkItemTemplate")


@_attrs_define
class EditWorkItemTemplate:
    """
    Attributes:
        name (str):
        description (None | str | Unset):
        work_item_type_id (None | str | Unset):
        wbsconfiguration_id (None | str | Unset):
        estimated_work_hours (int | None | Unset):
        estimated_duration_days (int | None | Unset):
        is_active (bool | None | Unset):
    """

    name: str
    description: None | str | Unset = UNSET
    work_item_type_id: None | str | Unset = UNSET
    wbsconfiguration_id: None | str | Unset = UNSET
    estimated_work_hours: int | None | Unset = UNSET
    estimated_duration_days: int | None | Unset = UNSET
    is_active: bool | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        work_item_type_id: None | str | Unset
        if isinstance(self.work_item_type_id, Unset):
            work_item_type_id = UNSET
        else:
            work_item_type_id = self.work_item_type_id

        wbsconfiguration_id: None | str | Unset
        if isinstance(self.wbsconfiguration_id, Unset):
            wbsconfiguration_id = UNSET
        else:
            wbsconfiguration_id = self.wbsconfiguration_id

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

        is_active: bool | None | Unset
        if isinstance(self.is_active, Unset):
            is_active = UNSET
        else:
            is_active = self.is_active

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if work_item_type_id is not UNSET:
            field_dict["work_item_type_id"] = work_item_type_id
        if wbsconfiguration_id is not UNSET:
            field_dict["wbsconfiguration_id"] = wbsconfiguration_id
        if estimated_work_hours is not UNSET:
            field_dict["estimated_work_hours"] = estimated_work_hours
        if estimated_duration_days is not UNSET:
            field_dict["estimated_duration_days"] = estimated_duration_days
        if is_active is not UNSET:
            field_dict["is_active"] = is_active

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_work_item_type_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        work_item_type_id = _parse_work_item_type_id(d.pop("work_item_type_id", UNSET))

        def _parse_wbsconfiguration_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        wbsconfiguration_id = _parse_wbsconfiguration_id(
            d.pop("wbsconfiguration_id", UNSET)
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

        def _parse_is_active(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_active = _parse_is_active(d.pop("is_active", UNSET))

        edit_work_item_template = cls(
            name=name,
            description=description,
            work_item_type_id=work_item_type_id,
            wbsconfiguration_id=wbsconfiguration_id,
            estimated_work_hours=estimated_work_hours,
            estimated_duration_days=estimated_duration_days,
            is_active=is_active,
        )

        edit_work_item_template.additional_properties = d
        return edit_work_item_template

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
