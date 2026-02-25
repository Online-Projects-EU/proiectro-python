from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CatalogProduct")


@_attrs_define
class CatalogProduct:
    """
    Attributes:
        id (str):
        name (str):
        product_type (str):
        is_active (bool):
        owner_id (str):
        owner_name (str):
        pricing_type (str):
        pricing_currency (str):
        pricing_value (float | str):
        description (None | str | Unset):
        internal_code (None | str | Unset):
        payment_integration_id (None | str | Unset):
    """

    id: str
    name: str
    product_type: str
    is_active: bool
    owner_id: str
    owner_name: str
    pricing_type: str
    pricing_currency: str
    pricing_value: float | str
    description: None | str | Unset = UNSET
    internal_code: None | str | Unset = UNSET
    payment_integration_id: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        product_type = self.product_type

        is_active = self.is_active

        owner_id = self.owner_id

        owner_name = self.owner_name

        pricing_type = self.pricing_type

        pricing_currency = self.pricing_currency

        pricing_value: float | str
        pricing_value = self.pricing_value

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        internal_code: None | str | Unset
        if isinstance(self.internal_code, Unset):
            internal_code = UNSET
        else:
            internal_code = self.internal_code

        payment_integration_id: None | str | Unset
        if isinstance(self.payment_integration_id, Unset):
            payment_integration_id = UNSET
        else:
            payment_integration_id = self.payment_integration_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "product_type": product_type,
                "is_active": is_active,
                "owner_id": owner_id,
                "owner_name": owner_name,
                "pricing_type": pricing_type,
                "pricing_currency": pricing_currency,
                "pricing_value": pricing_value,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if internal_code is not UNSET:
            field_dict["internal_code"] = internal_code
        if payment_integration_id is not UNSET:
            field_dict["payment_integration_id"] = payment_integration_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        product_type = d.pop("product_type")

        is_active = d.pop("is_active")

        owner_id = d.pop("owner_id")

        owner_name = d.pop("owner_name")

        pricing_type = d.pop("pricing_type")

        pricing_currency = d.pop("pricing_currency")

        def _parse_pricing_value(data: object) -> float | str:
            return cast(float | str, data)

        pricing_value = _parse_pricing_value(d.pop("pricing_value"))

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_internal_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        internal_code = _parse_internal_code(d.pop("internal_code", UNSET))

        def _parse_payment_integration_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        payment_integration_id = _parse_payment_integration_id(
            d.pop("payment_integration_id", UNSET)
        )

        catalog_product = cls(
            id=id,
            name=name,
            product_type=product_type,
            is_active=is_active,
            owner_id=owner_id,
            owner_name=owner_name,
            pricing_type=pricing_type,
            pricing_currency=pricing_currency,
            pricing_value=pricing_value,
            description=description,
            internal_code=internal_code,
            payment_integration_id=payment_integration_id,
        )

        catalog_product.additional_properties = d
        return catalog_product

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
