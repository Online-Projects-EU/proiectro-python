from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="OutputResourceBooking")


@_attrs_define
class OutputResourceBooking:
    """Output schema for a single resource booking

    Attributes:
        id (str):
        resource_id (str):
        resource_name (str):
        project_id (str):
        project_name (str):
        start_date (str):
        end_date (str):
        hours_per_day (int):
        name (str):
        product_id (None | str | Unset):
        product_name (None | str | Unset):
    """

    id: str
    resource_id: str
    resource_name: str
    project_id: str
    project_name: str
    start_date: str
    end_date: str
    hours_per_day: int
    name: str
    product_id: None | str | Unset = UNSET
    product_name: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        resource_id = self.resource_id

        resource_name = self.resource_name

        project_id = self.project_id

        project_name = self.project_name

        start_date = self.start_date

        end_date = self.end_date

        hours_per_day = self.hours_per_day

        name = self.name

        product_id: None | str | Unset
        if isinstance(self.product_id, Unset):
            product_id = UNSET
        else:
            product_id = self.product_id

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
                "resource_id": resource_id,
                "resource_name": resource_name,
                "project_id": project_id,
                "project_name": project_name,
                "start_date": start_date,
                "end_date": end_date,
                "hours_per_day": hours_per_day,
                "name": name,
            }
        )
        if product_id is not UNSET:
            field_dict["product_id"] = product_id
        if product_name is not UNSET:
            field_dict["product_name"] = product_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        resource_id = d.pop("resource_id")

        resource_name = d.pop("resource_name")

        project_id = d.pop("project_id")

        project_name = d.pop("project_name")

        start_date = d.pop("start_date")

        end_date = d.pop("end_date")

        hours_per_day = d.pop("hours_per_day")

        name = d.pop("name")

        def _parse_product_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        product_id = _parse_product_id(d.pop("product_id", UNSET))

        def _parse_product_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        product_name = _parse_product_name(d.pop("product_name", UNSET))

        output_resource_booking = cls(
            id=id,
            resource_id=resource_id,
            resource_name=resource_name,
            project_id=project_id,
            project_name=project_name,
            start_date=start_date,
            end_date=end_date,
            hours_per_day=hours_per_day,
            name=name,
            product_id=product_id,
            product_name=product_name,
        )

        output_resource_booking.additional_properties = d
        return output_resource_booking

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
