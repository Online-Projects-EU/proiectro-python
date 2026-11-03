from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PortalOrderLineOutput")


@_attrs_define
class PortalOrderLineOutput:
    """One line of a portal order as the customer sees it: the price agreed, never costs.

    Attributes:
        id (str):
        name (str):
        quantity (int):
        unit_price (float | str):
        total (float | str):
        unit_of_measure (str | Unset):  Default: ''.
        status_name (None | str | Unset):
        status_type (None | str | Unset):
        image_url (None | str | Unset):
    """

    id: str
    name: str
    quantity: int
    unit_price: float | str
    total: float | str
    unit_of_measure: str | Unset = ""
    status_name: None | str | Unset = UNSET
    status_type: None | str | Unset = UNSET
    image_url: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        quantity = self.quantity

        unit_price: float | str
        unit_price = self.unit_price

        total: float | str
        total = self.total

        unit_of_measure = self.unit_of_measure

        status_name: None | str | Unset
        if isinstance(self.status_name, Unset):
            status_name = UNSET
        else:
            status_name = self.status_name

        status_type: None | str | Unset
        if isinstance(self.status_type, Unset):
            status_type = UNSET
        else:
            status_type = self.status_type

        image_url: None | str | Unset
        if isinstance(self.image_url, Unset):
            image_url = UNSET
        else:
            image_url = self.image_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "quantity": quantity,
                "unit_price": unit_price,
                "total": total,
            }
        )
        if unit_of_measure is not UNSET:
            field_dict["unit_of_measure"] = unit_of_measure
        if status_name is not UNSET:
            field_dict["status_name"] = status_name
        if status_type is not UNSET:
            field_dict["status_type"] = status_type
        if image_url is not UNSET:
            field_dict["image_url"] = image_url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        quantity = d.pop("quantity")

        def _parse_unit_price(data: object) -> float | str:
            return cast(float | str, data)

        unit_price = _parse_unit_price(d.pop("unit_price"))

        def _parse_total(data: object) -> float | str:
            return cast(float | str, data)

        total = _parse_total(d.pop("total"))

        unit_of_measure = d.pop("unit_of_measure", UNSET)

        def _parse_status_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        status_name = _parse_status_name(d.pop("status_name", UNSET))

        def _parse_status_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        status_type = _parse_status_type(d.pop("status_type", UNSET))

        def _parse_image_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        image_url = _parse_image_url(d.pop("image_url", UNSET))

        portal_order_line_output = cls(
            id=id,
            name=name,
            quantity=quantity,
            unit_price=unit_price,
            total=total,
            unit_of_measure=unit_of_measure,
            status_name=status_name,
            status_type=status_type,
            image_url=image_url,
        )

        portal_order_line_output.additional_properties = d
        return portal_order_line_output

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
