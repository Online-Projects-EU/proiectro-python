from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.product_status_detail import ProductStatusDetail


T = TypeVar("T", bound="ProposalProduct")


@_attrs_define
class ProposalProduct:
    """
    Attributes:
        id (str):
        name (str):
        description (str):
        product_type (str):
        pricing_type (str):
        pricing_type_display (str):
        pricing_value (float | str):
        pricing_currency (str):
        pricing_currency_symbol (str):
        product_count (int):
        total_price (float | str):
        is_active (bool):
        created_at (datetime.datetime):
        original_value (float | str):
        original_currency (str):
        is_converted (bool):
        current_status (ProductStatusDetail): Product status for lifecycle display.
            Used in status dropdowns to show current status and all available lifecycle stages.
            Use lifecycle_type with templatetags for styling (status_bg, status_text, status_icon, etc.)
        lifecycle_statuses (list[ProductStatusDetail]):
        catalog_name (None | str | Unset):
        exchange_rate (float | None | str | Unset):
        cost_value (float | None | str | Unset):
        cost_currency (None | str | Unset):
        proposal_cost (float | None | str | Unset):
        margin_percent (float | None | str | Unset):
        total_margin (float | None | str | Unset):
        total_cost (float | None | str | Unset):
    """

    id: str
    name: str
    description: str
    product_type: str
    pricing_type: str
    pricing_type_display: str
    pricing_value: float | str
    pricing_currency: str
    pricing_currency_symbol: str
    product_count: int
    total_price: float | str
    is_active: bool
    created_at: datetime.datetime
    original_value: float | str
    original_currency: str
    is_converted: bool
    current_status: ProductStatusDetail
    lifecycle_statuses: list[ProductStatusDetail]
    catalog_name: None | str | Unset = UNSET
    exchange_rate: float | None | str | Unset = UNSET
    cost_value: float | None | str | Unset = UNSET
    cost_currency: None | str | Unset = UNSET
    proposal_cost: float | None | str | Unset = UNSET
    margin_percent: float | None | str | Unset = UNSET
    total_margin: float | None | str | Unset = UNSET
    total_cost: float | None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        description = self.description

        product_type = self.product_type

        pricing_type = self.pricing_type

        pricing_type_display = self.pricing_type_display

        pricing_value: float | str
        pricing_value = self.pricing_value

        pricing_currency = self.pricing_currency

        pricing_currency_symbol = self.pricing_currency_symbol

        product_count = self.product_count

        total_price: float | str
        total_price = self.total_price

        is_active = self.is_active

        created_at = self.created_at.isoformat()

        original_value: float | str
        original_value = self.original_value

        original_currency = self.original_currency

        is_converted = self.is_converted

        current_status = self.current_status.to_dict()

        lifecycle_statuses = []
        for lifecycle_statuses_item_data in self.lifecycle_statuses:
            lifecycle_statuses_item = lifecycle_statuses_item_data.to_dict()
            lifecycle_statuses.append(lifecycle_statuses_item)

        catalog_name: None | str | Unset
        if isinstance(self.catalog_name, Unset):
            catalog_name = UNSET
        else:
            catalog_name = self.catalog_name

        exchange_rate: float | None | str | Unset
        if isinstance(self.exchange_rate, Unset):
            exchange_rate = UNSET
        else:
            exchange_rate = self.exchange_rate

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

        proposal_cost: float | None | str | Unset
        if isinstance(self.proposal_cost, Unset):
            proposal_cost = UNSET
        else:
            proposal_cost = self.proposal_cost

        margin_percent: float | None | str | Unset
        if isinstance(self.margin_percent, Unset):
            margin_percent = UNSET
        else:
            margin_percent = self.margin_percent

        total_margin: float | None | str | Unset
        if isinstance(self.total_margin, Unset):
            total_margin = UNSET
        else:
            total_margin = self.total_margin

        total_cost: float | None | str | Unset
        if isinstance(self.total_cost, Unset):
            total_cost = UNSET
        else:
            total_cost = self.total_cost

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "description": description,
                "product_type": product_type,
                "pricing_type": pricing_type,
                "pricing_type_display": pricing_type_display,
                "pricing_value": pricing_value,
                "pricing_currency": pricing_currency,
                "pricing_currency_symbol": pricing_currency_symbol,
                "product_count": product_count,
                "total_price": total_price,
                "is_active": is_active,
                "created_at": created_at,
                "original_value": original_value,
                "original_currency": original_currency,
                "is_converted": is_converted,
                "current_status": current_status,
                "lifecycle_statuses": lifecycle_statuses,
            }
        )
        if catalog_name is not UNSET:
            field_dict["catalog_name"] = catalog_name
        if exchange_rate is not UNSET:
            field_dict["exchange_rate"] = exchange_rate
        if cost_value is not UNSET:
            field_dict["cost_value"] = cost_value
        if cost_currency is not UNSET:
            field_dict["cost_currency"] = cost_currency
        if proposal_cost is not UNSET:
            field_dict["proposal_cost"] = proposal_cost
        if margin_percent is not UNSET:
            field_dict["margin_percent"] = margin_percent
        if total_margin is not UNSET:
            field_dict["total_margin"] = total_margin
        if total_cost is not UNSET:
            field_dict["total_cost"] = total_cost

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.product_status_detail import ProductStatusDetail

        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        description = d.pop("description")

        product_type = d.pop("product_type")

        pricing_type = d.pop("pricing_type")

        pricing_type_display = d.pop("pricing_type_display")

        def _parse_pricing_value(data: object) -> float | str:
            return cast(float | str, data)

        pricing_value = _parse_pricing_value(d.pop("pricing_value"))

        pricing_currency = d.pop("pricing_currency")

        pricing_currency_symbol = d.pop("pricing_currency_symbol")

        product_count = d.pop("product_count")

        def _parse_total_price(data: object) -> float | str:
            return cast(float | str, data)

        total_price = _parse_total_price(d.pop("total_price"))

        is_active = d.pop("is_active")

        created_at = isoparse(d.pop("created_at"))

        def _parse_original_value(data: object) -> float | str:
            return cast(float | str, data)

        original_value = _parse_original_value(d.pop("original_value"))

        original_currency = d.pop("original_currency")

        is_converted = d.pop("is_converted")

        current_status = ProductStatusDetail.from_dict(d.pop("current_status"))

        lifecycle_statuses = []
        _lifecycle_statuses = d.pop("lifecycle_statuses")
        for lifecycle_statuses_item_data in _lifecycle_statuses:
            lifecycle_statuses_item = ProductStatusDetail.from_dict(
                lifecycle_statuses_item_data
            )

            lifecycle_statuses.append(lifecycle_statuses_item)

        def _parse_catalog_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        catalog_name = _parse_catalog_name(d.pop("catalog_name", UNSET))

        def _parse_exchange_rate(data: object) -> float | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | str | Unset, data)

        exchange_rate = _parse_exchange_rate(d.pop("exchange_rate", UNSET))

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

        def _parse_proposal_cost(data: object) -> float | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | str | Unset, data)

        proposal_cost = _parse_proposal_cost(d.pop("proposal_cost", UNSET))

        def _parse_margin_percent(data: object) -> float | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | str | Unset, data)

        margin_percent = _parse_margin_percent(d.pop("margin_percent", UNSET))

        def _parse_total_margin(data: object) -> float | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | str | Unset, data)

        total_margin = _parse_total_margin(d.pop("total_margin", UNSET))

        def _parse_total_cost(data: object) -> float | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | str | Unset, data)

        total_cost = _parse_total_cost(d.pop("total_cost", UNSET))

        proposal_product = cls(
            id=id,
            name=name,
            description=description,
            product_type=product_type,
            pricing_type=pricing_type,
            pricing_type_display=pricing_type_display,
            pricing_value=pricing_value,
            pricing_currency=pricing_currency,
            pricing_currency_symbol=pricing_currency_symbol,
            product_count=product_count,
            total_price=total_price,
            is_active=is_active,
            created_at=created_at,
            original_value=original_value,
            original_currency=original_currency,
            is_converted=is_converted,
            current_status=current_status,
            lifecycle_statuses=lifecycle_statuses,
            catalog_name=catalog_name,
            exchange_rate=exchange_rate,
            cost_value=cost_value,
            cost_currency=cost_currency,
            proposal_cost=proposal_cost,
            margin_percent=margin_percent,
            total_margin=total_margin,
            total_cost=total_cost,
        )

        proposal_product.additional_properties = d
        return proposal_product

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
