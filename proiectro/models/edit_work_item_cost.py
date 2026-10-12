from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="EditWorkItemCost")


@_attrs_define
class EditWorkItemCost:
    """
    Attributes:
        expected_amount (str):
        expected_date (str):
        uom (str):
        cost_type (None | str | Unset):
        resource_cost (None | str | Unset):
        resource_booking (None | str | Unset):
        units (int | None | Unset):  Default: 1.
        note (None | str | Unset):
    """

    expected_amount: str
    expected_date: str
    uom: str
    cost_type: None | str | Unset = UNSET
    resource_cost: None | str | Unset = UNSET
    resource_booking: None | str | Unset = UNSET
    units: int | None | Unset = 1
    note: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        expected_amount = self.expected_amount

        expected_date = self.expected_date

        uom = self.uom

        cost_type: None | str | Unset
        if isinstance(self.cost_type, Unset):
            cost_type = UNSET
        else:
            cost_type = self.cost_type

        resource_cost: None | str | Unset
        if isinstance(self.resource_cost, Unset):
            resource_cost = UNSET
        else:
            resource_cost = self.resource_cost

        resource_booking: None | str | Unset
        if isinstance(self.resource_booking, Unset):
            resource_booking = UNSET
        else:
            resource_booking = self.resource_booking

        units: int | None | Unset
        if isinstance(self.units, Unset):
            units = UNSET
        else:
            units = self.units

        note: None | str | Unset
        if isinstance(self.note, Unset):
            note = UNSET
        else:
            note = self.note

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "expected_amount": expected_amount,
                "expected_date": expected_date,
                "uom": uom,
            }
        )
        if cost_type is not UNSET:
            field_dict["cost_type"] = cost_type
        if resource_cost is not UNSET:
            field_dict["resource_cost"] = resource_cost
        if resource_booking is not UNSET:
            field_dict["resource_booking"] = resource_booking
        if units is not UNSET:
            field_dict["units"] = units
        if note is not UNSET:
            field_dict["note"] = note

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        expected_amount = d.pop("expected_amount")

        expected_date = d.pop("expected_date")

        uom = d.pop("uom")

        def _parse_cost_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        cost_type = _parse_cost_type(d.pop("cost_type", UNSET))

        def _parse_resource_cost(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        resource_cost = _parse_resource_cost(d.pop("resource_cost", UNSET))

        def _parse_resource_booking(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        resource_booking = _parse_resource_booking(d.pop("resource_booking", UNSET))

        def _parse_units(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        units = _parse_units(d.pop("units", UNSET))

        def _parse_note(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        note = _parse_note(d.pop("note", UNSET))

        edit_work_item_cost = cls(
            expected_amount=expected_amount,
            expected_date=expected_date,
            uom=uom,
            cost_type=cost_type,
            resource_cost=resource_cost,
            resource_booking=resource_booking,
            units=units,
            note=note,
        )

        edit_work_item_cost.additional_properties = d
        return edit_work_item_cost

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
