from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.edit_product_pricing_type import EditProductPricingType
from ..models.edit_product_product_type import EditProductProductType
from ..types import UNSET, Unset

T = TypeVar("T", bound="EditProduct")


@_attrs_define
class EditProduct:
    """
    Attributes:
        name (str):
        description (str):
        description_for_customer (str):
        product_type (EditProductProductType):
        pricing_type (EditProductPricingType):
        pricing_currency (str):
        pricing_value (float | None | str | Unset):
        cost_value (float | None | str | Unset):
        cost_currency (None | str | Unset):
        product_count (int | Unset):  Default: 1.
        planned_start (None | str | Unset):
        planned_end (None | str | Unset):
        tracks_project (None | str | Unset):
    """

    name: str
    description: str
    description_for_customer: str
    product_type: EditProductProductType
    pricing_type: EditProductPricingType
    pricing_currency: str
    pricing_value: float | None | str | Unset = UNSET
    cost_value: float | None | str | Unset = UNSET
    cost_currency: None | str | Unset = UNSET
    product_count: int | Unset = 1
    planned_start: None | str | Unset = UNSET
    planned_end: None | str | Unset = UNSET
    tracks_project: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        description = self.description

        description_for_customer = self.description_for_customer

        product_type = self.product_type.value

        pricing_type = self.pricing_type.value

        pricing_currency = self.pricing_currency

        pricing_value: float | None | str | Unset
        if isinstance(self.pricing_value, Unset):
            pricing_value = UNSET
        else:
            pricing_value = self.pricing_value

        cost_value: float | None | str | Unset
        if isinstance(self.cost_value, Unset):
            cost_value = UNSET
        else:
            cost_value = self.cost_value

        cost_currency: None | str | Unset
        if isinstance(self.cost_currency, Unset):
            cost_currency = UNSET
        else:
            cost_currency = self.cost_currency

        product_count = self.product_count

        planned_start: None | str | Unset
        if isinstance(self.planned_start, Unset):
            planned_start = UNSET
        else:
            planned_start = self.planned_start

        planned_end: None | str | Unset
        if isinstance(self.planned_end, Unset):
            planned_end = UNSET
        else:
            planned_end = self.planned_end

        tracks_project: None | str | Unset
        if isinstance(self.tracks_project, Unset):
            tracks_project = UNSET
        else:
            tracks_project = self.tracks_project

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "description": description,
                "description_for_customer": description_for_customer,
                "product_type": product_type,
                "pricing_type": pricing_type,
                "pricing_currency": pricing_currency,
            }
        )
        if pricing_value is not UNSET:
            field_dict["pricing_value"] = pricing_value
        if cost_value is not UNSET:
            field_dict["cost_value"] = cost_value
        if cost_currency is not UNSET:
            field_dict["cost_currency"] = cost_currency
        if product_count is not UNSET:
            field_dict["product_count"] = product_count
        if planned_start is not UNSET:
            field_dict["planned_start"] = planned_start
        if planned_end is not UNSET:
            field_dict["planned_end"] = planned_end
        if tracks_project is not UNSET:
            field_dict["tracks_project"] = tracks_project

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        description = d.pop("description")

        description_for_customer = d.pop("description_for_customer")

        product_type = EditProductProductType(d.pop("product_type"))

        pricing_type = EditProductPricingType(d.pop("pricing_type"))

        pricing_currency = d.pop("pricing_currency")

        def _parse_pricing_value(data: object) -> float | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | str | Unset, data)

        pricing_value = _parse_pricing_value(d.pop("pricing_value", UNSET))

        def _parse_cost_value(data: object) -> float | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | str | Unset, data)

        cost_value = _parse_cost_value(d.pop("cost_value", UNSET))

        def _parse_cost_currency(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        cost_currency = _parse_cost_currency(d.pop("cost_currency", UNSET))

        product_count = d.pop("product_count", UNSET)

        def _parse_planned_start(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        planned_start = _parse_planned_start(d.pop("planned_start", UNSET))

        def _parse_planned_end(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        planned_end = _parse_planned_end(d.pop("planned_end", UNSET))

        def _parse_tracks_project(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        tracks_project = _parse_tracks_project(d.pop("tracks_project", UNSET))

        edit_product = cls(
            name=name,
            description=description,
            description_for_customer=description_for_customer,
            product_type=product_type,
            pricing_type=pricing_type,
            pricing_currency=pricing_currency,
            pricing_value=pricing_value,
            cost_value=cost_value,
            cost_currency=cost_currency,
            product_count=product_count,
            planned_start=planned_start,
            planned_end=planned_end,
            tracks_project=tracks_project,
        )

        edit_product.additional_properties = d
        return edit_product

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
