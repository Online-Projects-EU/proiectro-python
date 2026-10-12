from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PriceListEntry")


@_attrs_define
class PriceListEntry:
    """
    Attributes:
        catalog_id (str):
        override_price (float | None | str | Unset):
        override_currency (None | str | Unset):
    """

    catalog_id: str
    override_price: float | None | str | Unset = UNSET
    override_currency: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        catalog_id = self.catalog_id

        override_price: float | None | str | Unset
        if isinstance(self.override_price, Unset):
            override_price = UNSET
        else:
            override_price = self.override_price

        override_currency: None | str | Unset
        if isinstance(self.override_currency, Unset):
            override_currency = UNSET
        else:
            override_currency = self.override_currency

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "catalog_id": catalog_id,
            }
        )
        if override_price is not UNSET:
            field_dict["override_price"] = override_price
        if override_currency is not UNSET:
            field_dict["override_currency"] = override_currency

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        catalog_id = d.pop("catalog_id")

        def _parse_override_price(data: object) -> float | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | str | Unset, data)

        override_price = _parse_override_price(d.pop("override_price", UNSET))

        def _parse_override_currency(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        override_currency = _parse_override_currency(d.pop("override_currency", UNSET))

        price_list_entry = cls(
            catalog_id=catalog_id,
            override_price=override_price,
            override_currency=override_currency,
        )

        price_list_entry.additional_properties = d
        return price_list_entry

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
