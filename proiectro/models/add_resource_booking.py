from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AddResourceBooking")


@_attrs_define
class AddResourceBooking:
    """Input schema for adding a resource booking

    Attributes:
        project (str):
        resource (str):
        start_date (str):
        end_date (str):
        name (str):
        product (None | str | Unset):
        hours_per_day (int | None | Unset):  Default: 0.
    """

    project: str
    resource: str
    start_date: str
    end_date: str
    name: str
    product: None | str | Unset = UNSET
    hours_per_day: int | None | Unset = 0
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        project = self.project

        resource = self.resource

        start_date = self.start_date

        end_date = self.end_date

        name = self.name

        product: None | str | Unset
        if isinstance(self.product, Unset):
            product = UNSET
        else:
            product = self.product

        hours_per_day: int | None | Unset
        if isinstance(self.hours_per_day, Unset):
            hours_per_day = UNSET
        else:
            hours_per_day = self.hours_per_day

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "project": project,
                "resource": resource,
                "start_date": start_date,
                "end_date": end_date,
                "name": name,
            }
        )
        if product is not UNSET:
            field_dict["product"] = product
        if hours_per_day is not UNSET:
            field_dict["hours_per_day"] = hours_per_day

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        project = d.pop("project")

        resource = d.pop("resource")

        start_date = d.pop("start_date")

        end_date = d.pop("end_date")

        name = d.pop("name")

        def _parse_product(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        product = _parse_product(d.pop("product", UNSET))

        def _parse_hours_per_day(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        hours_per_day = _parse_hours_per_day(d.pop("hours_per_day", UNSET))

        add_resource_booking = cls(
            project=project,
            resource=resource,
            start_date=start_date,
            end_date=end_date,
            name=name,
            product=product,
            hours_per_day=hours_per_day,
        )

        add_resource_booking.additional_properties = d
        return add_resource_booking

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
