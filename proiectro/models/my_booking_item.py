from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="MyBookingItem")


@_attrs_define
class MyBookingItem:
    """Individual booking for cross-tenant My Schedule view

    Attributes:
        id (str):
        name (str):
        project_name (str):
        start_date (str):
        end_date (str):
        hours_per_day (int):
        tenant_name (str):
        tenant_path (str):
        schedule_group (str):
        project_id (None | str | Unset):
        product_name (None | str | Unset):
    """

    id: str
    name: str
    project_name: str
    start_date: str
    end_date: str
    hours_per_day: int
    tenant_name: str
    tenant_path: str
    schedule_group: str
    project_id: None | str | Unset = UNSET
    product_name: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        project_name = self.project_name

        start_date = self.start_date

        end_date = self.end_date

        hours_per_day = self.hours_per_day

        tenant_name = self.tenant_name

        tenant_path = self.tenant_path

        schedule_group = self.schedule_group

        project_id: None | str | Unset
        if isinstance(self.project_id, Unset):
            project_id = UNSET
        else:
            project_id = self.project_id

        product_name: None | str | Unset
        if isinstance(self.product_name, Unset):
            product_name = UNSET
        else:
            product_name = self.product_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "project_name": project_name,
                "start_date": start_date,
                "end_date": end_date,
                "hours_per_day": hours_per_day,
                "tenant_name": tenant_name,
                "tenant_path": tenant_path,
                "schedule_group": schedule_group,
            }
        )
        if project_id is not UNSET:
            field_dict["project_id"] = project_id
        if product_name is not UNSET:
            field_dict["product_name"] = product_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        project_name = d.pop("project_name")

        start_date = d.pop("start_date")

        end_date = d.pop("end_date")

        hours_per_day = d.pop("hours_per_day")

        tenant_name = d.pop("tenant_name")

        tenant_path = d.pop("tenant_path")

        schedule_group = d.pop("schedule_group")

        def _parse_project_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        project_id = _parse_project_id(d.pop("project_id", UNSET))

        def _parse_product_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        product_name = _parse_product_name(d.pop("product_name", UNSET))

        my_booking_item = cls(
            id=id,
            name=name,
            project_name=project_name,
            start_date=start_date,
            end_date=end_date,
            hours_per_day=hours_per_day,
            tenant_name=tenant_name,
            tenant_path=tenant_path,
            schedule_group=schedule_group,
            project_id=project_id,
            product_name=product_name,
        )

        my_booking_item.additional_properties = d
        return my_booking_item

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
