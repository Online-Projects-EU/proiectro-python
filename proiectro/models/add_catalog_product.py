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
        description (str):
        description_for_customer (str):
        product_type (AddCatalogProductProductType):
        default_lifecycle (str):
        pricing_type (AddCatalogProductPricingType):
        cost_value (float | str):
        cost_currency (str):
        internal_code (None | str | Unset):
        is_active (bool | None | Unset):  Default: False.
        payment_integration_id (None | str | Unset):
        pricing_currency (None | str | Unset):
        pricing_value (float | None | str | Unset):
        unit_of_measure (None | str | Unset):
        track_stock (bool | None | Unset):  Default: False.
        stock_quantity (int | None | Unset):
        available_in_customer_portal (bool | None | Unset):  Default: False.
        available_in_partner_portals (bool | None | Unset):  Default: False.
        price_lists (list[str] | None | Unset):
    """

    name: str
    description: str
    description_for_customer: str
    product_type: AddCatalogProductProductType
    default_lifecycle: str
    pricing_type: AddCatalogProductPricingType
    cost_value: float | str
    cost_currency: str
    internal_code: None | str | Unset = UNSET
    is_active: bool | None | Unset = False
    payment_integration_id: None | str | Unset = UNSET
    pricing_currency: None | str | Unset = UNSET
    pricing_value: float | None | str | Unset = UNSET
    unit_of_measure: None | str | Unset = UNSET
    track_stock: bool | None | Unset = False
    stock_quantity: int | None | Unset = UNSET
    available_in_customer_portal: bool | None | Unset = False
    available_in_partner_portals: bool | None | Unset = False
    price_lists: list[str] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        description = self.description

        description_for_customer = self.description_for_customer

        product_type = self.product_type.value

        default_lifecycle = self.default_lifecycle

        pricing_type = self.pricing_type.value

        cost_value: float | str
        cost_value = self.cost_value

        cost_currency = self.cost_currency

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

        unit_of_measure: None | str | Unset
        if isinstance(self.unit_of_measure, Unset):
            unit_of_measure = UNSET
        else:
            unit_of_measure = self.unit_of_measure

        track_stock: bool | None | Unset
        if isinstance(self.track_stock, Unset):
            track_stock = UNSET
        else:
            track_stock = self.track_stock

        stock_quantity: int | None | Unset
        if isinstance(self.stock_quantity, Unset):
            stock_quantity = UNSET
        else:
            stock_quantity = self.stock_quantity

        available_in_customer_portal: bool | None | Unset
        if isinstance(self.available_in_customer_portal, Unset):
            available_in_customer_portal = UNSET
        else:
            available_in_customer_portal = self.available_in_customer_portal

        available_in_partner_portals: bool | None | Unset
        if isinstance(self.available_in_partner_portals, Unset):
            available_in_partner_portals = UNSET
        else:
            available_in_partner_portals = self.available_in_partner_portals

        price_lists: list[str] | None | Unset
        if isinstance(self.price_lists, Unset):
            price_lists = UNSET
        elif isinstance(self.price_lists, list):
            price_lists = self.price_lists

        else:
            price_lists = self.price_lists

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "description": description,
                "description_for_customer": description_for_customer,
                "product_type": product_type,
                "default_lifecycle": default_lifecycle,
                "pricing_type": pricing_type,
                "cost_value": cost_value,
                "cost_currency": cost_currency,
            }
        )
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
        if unit_of_measure is not UNSET:
            field_dict["unit_of_measure"] = unit_of_measure
        if track_stock is not UNSET:
            field_dict["track_stock"] = track_stock
        if stock_quantity is not UNSET:
            field_dict["stock_quantity"] = stock_quantity
        if available_in_customer_portal is not UNSET:
            field_dict["available_in_customer_portal"] = available_in_customer_portal
        if available_in_partner_portals is not UNSET:
            field_dict["available_in_partner_portals"] = available_in_partner_portals
        if price_lists is not UNSET:
            field_dict["price_lists"] = price_lists

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        description = d.pop("description")

        description_for_customer = d.pop("description_for_customer")

        product_type = AddCatalogProductProductType(d.pop("product_type"))

        default_lifecycle = d.pop("default_lifecycle")

        pricing_type = AddCatalogProductPricingType(d.pop("pricing_type"))

        def _parse_cost_value(data: object) -> float | str:
            return cast(float | str, data)

        cost_value = _parse_cost_value(d.pop("cost_value"))

        cost_currency = d.pop("cost_currency")

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

        def _parse_unit_of_measure(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        unit_of_measure = _parse_unit_of_measure(d.pop("unit_of_measure", UNSET))

        def _parse_track_stock(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        track_stock = _parse_track_stock(d.pop("track_stock", UNSET))

        def _parse_stock_quantity(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        stock_quantity = _parse_stock_quantity(d.pop("stock_quantity", UNSET))

        def _parse_available_in_customer_portal(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        available_in_customer_portal = _parse_available_in_customer_portal(
            d.pop("available_in_customer_portal", UNSET)
        )

        def _parse_available_in_partner_portals(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        available_in_partner_portals = _parse_available_in_partner_portals(
            d.pop("available_in_partner_portals", UNSET)
        )

        def _parse_price_lists(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                price_lists_type_0 = cast(list[str], data)

                return price_lists_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        price_lists = _parse_price_lists(d.pop("price_lists", UNSET))

        add_catalog_product = cls(
            name=name,
            description=description,
            description_for_customer=description_for_customer,
            product_type=product_type,
            default_lifecycle=default_lifecycle,
            pricing_type=pricing_type,
            cost_value=cost_value,
            cost_currency=cost_currency,
            internal_code=internal_code,
            is_active=is_active,
            payment_integration_id=payment_integration_id,
            pricing_currency=pricing_currency,
            pricing_value=pricing_value,
            unit_of_measure=unit_of_measure,
            track_stock=track_stock,
            stock_quantity=stock_quantity,
            available_in_customer_portal=available_in_customer_portal,
            available_in_partner_portals=available_in_partner_portals,
            price_lists=price_lists,
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
