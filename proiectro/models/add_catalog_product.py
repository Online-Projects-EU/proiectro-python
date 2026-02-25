from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.add_catalog_product_pricing_type import AddCatalogProductPricingType
from ..models.add_catalog_product_product_type import AddCatalogProductProductType
from ..types import UNSET, Unset

T = TypeVar("T", bound="AddCatalogProduct")


@_attrs_define
class AddCatalogProduct:
    """
    Attributes:
        name (str):
        description_for_customer (str):
        product_type (AddCatalogProductProductType):
        default_lifecycle (str):
        pricing_type (AddCatalogProductPricingType):
        cost_value (float | str):
        cost_currency (str):
        description (None | str | Unset):
        internal_code (None | str | Unset):
        is_active (bool | None | Unset):  Default: False.
        payment_integration_id (None | str | Unset):
        pricing_currency (None | str | Unset):
        pricing_value (float | None | str | Unset):
    """

    name: str
    description_for_customer: str
    product_type: AddCatalogProductProductType
    default_lifecycle: str
    pricing_type: AddCatalogProductPricingType
    cost_value: float | str
    cost_currency: str
    description: None | str | Unset = UNSET
    internal_code: None | str | Unset = UNSET
    is_active: bool | None | Unset = False
    payment_integration_id: None | str | Unset = UNSET
    pricing_currency: None | str | Unset = UNSET
    pricing_value: float | None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        description_for_customer = self.description_for_customer

        product_type = self.product_type.value

        default_lifecycle = self.default_lifecycle

        pricing_type = self.pricing_type.value

        cost_value: float | str
        cost_value = self.cost_value

        cost_currency = self.cost_currency

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

        is_active: bool | None | Unset
        if isinstance(self.is_active, Unset):
            is_active = UNSET
        else:
            is_active = self.is_active

        payment_integration_id: None | str | Unset
        if isinstance(self.payment_integration_id, Unset):
            payment_integration_id = UNSET
        else:
            payment_integration_id = self.payment_integration_id

        pricing_currency: None | str | Unset
        if isinstance(self.pricing_currency, Unset):
            pricing_currency = UNSET
        else:
            pricing_currency = self.pricing_currency

        pricing_value: float | None | str | Unset
        if isinstance(self.pricing_value, Unset):
            pricing_value = UNSET
        else:
            pricing_value = self.pricing_value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "description_for_customer": description_for_customer,
                "product_type": product_type,
                "default_lifecycle": default_lifecycle,
                "pricing_type": pricing_type,
                "cost_value": cost_value,
                "cost_currency": cost_currency,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if internal_code is not UNSET:
            field_dict["internal_code"] = internal_code
        if is_active is not UNSET:
            field_dict["is_active"] = is_active
        if payment_integration_id is not UNSET:
            field_dict["payment_integration_id"] = payment_integration_id
        if pricing_currency is not UNSET:
            field_dict["pricing_currency"] = pricing_currency
        if pricing_value is not UNSET:
            field_dict["pricing_value"] = pricing_value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        description_for_customer = d.pop("description_for_customer")

        product_type = AddCatalogProductProductType(d.pop("product_type"))

        default_lifecycle = d.pop("default_lifecycle")

        pricing_type = AddCatalogProductPricingType(d.pop("pricing_type"))

        def _parse_cost_value(data: object) -> float | str:
            return cast(float | str, data)

        cost_value = _parse_cost_value(d.pop("cost_value"))

        cost_currency = d.pop("cost_currency")

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

        def _parse_is_active(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_active = _parse_is_active(d.pop("is_active", UNSET))

        def _parse_payment_integration_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        payment_integration_id = _parse_payment_integration_id(
            d.pop("payment_integration_id", UNSET)
        )

        def _parse_pricing_currency(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        pricing_currency = _parse_pricing_currency(d.pop("pricing_currency", UNSET))

        def _parse_pricing_value(data: object) -> float | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | str | Unset, data)

        pricing_value = _parse_pricing_value(d.pop("pricing_value", UNSET))

        add_catalog_product = cls(
            name=name,
            description_for_customer=description_for_customer,
            product_type=product_type,
            default_lifecycle=default_lifecycle,
            pricing_type=pricing_type,
            cost_value=cost_value,
            cost_currency=cost_currency,
            description=description,
            internal_code=internal_code,
            is_active=is_active,
            payment_integration_id=payment_integration_id,
            pricing_currency=pricing_currency,
            pricing_value=pricing_value,
        )

        add_catalog_product.additional_properties = d
        return add_catalog_product

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
