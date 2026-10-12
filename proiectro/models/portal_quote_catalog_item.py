from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PortalQuoteCatalogItem")


@_attrs_define
class PortalQuoteCatalogItem:
    """An orderable catalog item as the customer sees it: no costs, no internal codes.

    Attributes:
        id (str):
        name (str):
        product_type (str):
        description_for_customer (str | Unset):  Default: ''.
        unit_of_measure (str | Unset):  Default: ''.
        price (float | None | str | Unset):
        currency (str | Unset):  Default: ''.
    """

    id: str
    name: str
    product_type: str
    description_for_customer: str | Unset = ""
    unit_of_measure: str | Unset = ""
    price: float | None | str | Unset = UNSET
    currency: str | Unset = ""
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        product_type = self.product_type

        description_for_customer = self.description_for_customer

        unit_of_measure = self.unit_of_measure

        price: float | None | str | Unset
        if isinstance(self.price, Unset):
            price = UNSET
        else:
            price = self.price

        currency = self.currency

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "product_type": product_type,
            }
        )
        if description_for_customer is not UNSET:
            field_dict["description_for_customer"] = description_for_customer
        if unit_of_measure is not UNSET:
            field_dict["unit_of_measure"] = unit_of_measure
        if price is not UNSET:
            field_dict["price"] = price
        if currency is not UNSET:
            field_dict["currency"] = currency

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        product_type = d.pop("product_type")

        description_for_customer = d.pop("description_for_customer", UNSET)

        unit_of_measure = d.pop("unit_of_measure", UNSET)

        def _parse_price(data: object) -> float | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | str | Unset, data)

        price = _parse_price(d.pop("price", UNSET))

        currency = d.pop("currency", UNSET)

        portal_quote_catalog_item = cls(
            id=id,
            name=name,
            product_type=product_type,
            description_for_customer=description_for_customer,
            unit_of_measure=unit_of_measure,
            price=price,
            currency=currency,
        )

        portal_quote_catalog_item.additional_properties = d
        return portal_quote_catalog_item

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
