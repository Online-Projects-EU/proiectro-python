from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CostItem")


@_attrs_define
class CostItem:
    """
    Attributes:
        external_id (str):
        cost_type_name (str):
        cost_type_id (str):
        expected_amount (str):
        currency_symbol (str):
        expected_date (str):
        units (int):
        uom (str):
        note (str):
        resource_name (None | str | Unset):
        resource_id (None | str | Unset):
        booking_name (None | str | Unset):
        booking_id (None | str | Unset):
        member_full_name (None | str | Unset):
        member_id (None | str | Unset):
        work_item_name (None | str | Unset):
        work_item_id (None | str | Unset):
    """

    external_id: str
    cost_type_name: str
    cost_type_id: str
    expected_amount: str
    currency_symbol: str
    expected_date: str
    units: int
    uom: str
    note: str
    resource_name: None | str | Unset = UNSET
    resource_id: None | str | Unset = UNSET
    booking_name: None | str | Unset = UNSET
    booking_id: None | str | Unset = UNSET
    member_full_name: None | str | Unset = UNSET
    member_id: None | str | Unset = UNSET
    work_item_name: None | str | Unset = UNSET
    work_item_id: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        external_id = self.external_id

        cost_type_name = self.cost_type_name

        cost_type_id = self.cost_type_id

        expected_amount = self.expected_amount

        currency_symbol = self.currency_symbol

        expected_date = self.expected_date

        units = self.units

        uom = self.uom

        note = self.note

        resource_name: None | str | Unset
        if isinstance(self.resource_name, Unset):
            resource_name = UNSET
        else:
            resource_name = self.resource_name

        resource_id: None | str | Unset
        if isinstance(self.resource_id, Unset):
            resource_id = UNSET
        else:
            resource_id = self.resource_id

        booking_name: None | str | Unset
        if isinstance(self.booking_name, Unset):
            booking_name = UNSET
        else:
            booking_name = self.booking_name

        booking_id: None | str | Unset
        if isinstance(self.booking_id, Unset):
            booking_id = UNSET
        else:
            booking_id = self.booking_id

        member_full_name: None | str | Unset
        if isinstance(self.member_full_name, Unset):
            member_full_name = UNSET
        else:
            member_full_name = self.member_full_name

        member_id: None | str | Unset
        if isinstance(self.member_id, Unset):
            member_id = UNSET
        else:
            member_id = self.member_id

        work_item_name: None | str | Unset
        if isinstance(self.work_item_name, Unset):
            work_item_name = UNSET
        else:
            work_item_name = self.work_item_name

        work_item_id: None | str | Unset
        if isinstance(self.work_item_id, Unset):
            work_item_id = UNSET
        else:
            work_item_id = self.work_item_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "external_id": external_id,
                "cost_type_name": cost_type_name,
                "cost_type_id": cost_type_id,
                "expected_amount": expected_amount,
                "currency_symbol": currency_symbol,
                "expected_date": expected_date,
                "units": units,
                "uom": uom,
                "note": note,
            }
        )
        if resource_name is not UNSET:
            field_dict["resource_name"] = resource_name
        if resource_id is not UNSET:
            field_dict["resource_id"] = resource_id
        if booking_name is not UNSET:
            field_dict["booking_name"] = booking_name
        if booking_id is not UNSET:
            field_dict["booking_id"] = booking_id
        if member_full_name is not UNSET:
            field_dict["member_full_name"] = member_full_name
        if member_id is not UNSET:
            field_dict["member_id"] = member_id
        if work_item_name is not UNSET:
            field_dict["work_item_name"] = work_item_name
        if work_item_id is not UNSET:
            field_dict["work_item_id"] = work_item_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        external_id = d.pop("external_id")

        cost_type_name = d.pop("cost_type_name")

        cost_type_id = d.pop("cost_type_id")

        expected_amount = d.pop("expected_amount")

        currency_symbol = d.pop("currency_symbol")

        expected_date = d.pop("expected_date")

        units = d.pop("units")

        uom = d.pop("uom")

        note = d.pop("note")

        def _parse_resource_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        resource_name = _parse_resource_name(d.pop("resource_name", UNSET))

        def _parse_resource_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        resource_id = _parse_resource_id(d.pop("resource_id", UNSET))

        def _parse_booking_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        booking_name = _parse_booking_name(d.pop("booking_name", UNSET))

        def _parse_booking_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        booking_id = _parse_booking_id(d.pop("booking_id", UNSET))

        def _parse_member_full_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        member_full_name = _parse_member_full_name(d.pop("member_full_name", UNSET))

        def _parse_member_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        member_id = _parse_member_id(d.pop("member_id", UNSET))

        def _parse_work_item_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        work_item_name = _parse_work_item_name(d.pop("work_item_name", UNSET))

        def _parse_work_item_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        work_item_id = _parse_work_item_id(d.pop("work_item_id", UNSET))

        cost_item = cls(
            external_id=external_id,
            cost_type_name=cost_type_name,
            cost_type_id=cost_type_id,
            expected_amount=expected_amount,
            currency_symbol=currency_symbol,
            expected_date=expected_date,
            units=units,
            uom=uom,
            note=note,
            resource_name=resource_name,
            resource_id=resource_id,
            booking_name=booking_name,
            booking_id=booking_id,
            member_full_name=member_full_name,
            member_id=member_id,
            work_item_name=work_item_name,
            work_item_id=work_item_id,
        )

        cost_item.additional_properties = d
        return cost_item

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
