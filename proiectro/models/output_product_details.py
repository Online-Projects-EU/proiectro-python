from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.product_sales_time_series import ProductSalesTimeSeries


T = TypeVar("T", bound="OutputProductDetails")


@_attrs_define
class OutputProductDetails:
    """Product details with sales analytics

    Attributes:
        id (str):
        name (str):
        pricing_type (str):
        pricing_type_display (str):
        pricing_value (float | str):
        currency (str):
        currency_symbol (str):
        is_active (bool):
        owner_name (str):
        payment_integration_id (str):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        times_sold (int):
        won_proposals_percent (float | str):
        lost_proposals_percent (float | str):
        sales_time_series (list[ProductSalesTimeSeries]):
        description (None | str | Unset):
        internal_code (None | str | Unset):
    """

    id: str
    name: str
    pricing_type: str
    pricing_type_display: str
    pricing_value: float | str
    currency: str
    currency_symbol: str
    is_active: bool
    owner_name: str
    payment_integration_id: str
    created_at: datetime.datetime
    updated_at: datetime.datetime
    times_sold: int
    won_proposals_percent: float | str
    lost_proposals_percent: float | str
    sales_time_series: list[ProductSalesTimeSeries]
    description: None | str | Unset = UNSET
    internal_code: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        pricing_type = self.pricing_type

        pricing_type_display = self.pricing_type_display

        pricing_value: float | str
        pricing_value = self.pricing_value

        currency = self.currency

        currency_symbol = self.currency_symbol

        is_active = self.is_active

        owner_name = self.owner_name

        payment_integration_id = self.payment_integration_id

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        times_sold = self.times_sold

        won_proposals_percent: float | str
        won_proposals_percent = self.won_proposals_percent

        lost_proposals_percent: float | str
        lost_proposals_percent = self.lost_proposals_percent

        sales_time_series = []
        for sales_time_series_item_data in self.sales_time_series:
            sales_time_series_item = sales_time_series_item_data.to_dict()
            sales_time_series.append(sales_time_series_item)

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

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "pricing_type": pricing_type,
                "pricing_type_display": pricing_type_display,
                "pricing_value": pricing_value,
                "currency": currency,
                "currency_symbol": currency_symbol,
                "is_active": is_active,
                "owner_name": owner_name,
                "payment_integration_id": payment_integration_id,
                "created_at": created_at,
                "updated_at": updated_at,
                "times_sold": times_sold,
                "won_proposals_percent": won_proposals_percent,
                "lost_proposals_percent": lost_proposals_percent,
                "sales_time_series": sales_time_series,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if internal_code is not UNSET:
            field_dict["internal_code"] = internal_code

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.product_sales_time_series import ProductSalesTimeSeries

        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        pricing_type = d.pop("pricing_type")

        pricing_type_display = d.pop("pricing_type_display")

        def _parse_pricing_value(data: object) -> float | str:
            return cast(float | str, data)

        pricing_value = _parse_pricing_value(d.pop("pricing_value"))

        currency = d.pop("currency")

        currency_symbol = d.pop("currency_symbol")

        is_active = d.pop("is_active")

        owner_name = d.pop("owner_name")

        payment_integration_id = d.pop("payment_integration_id")

        created_at = isoparse(d.pop("created_at"))

        updated_at = isoparse(d.pop("updated_at"))

        times_sold = d.pop("times_sold")

        def _parse_won_proposals_percent(data: object) -> float | str:
            return cast(float | str, data)

        won_proposals_percent = _parse_won_proposals_percent(
            d.pop("won_proposals_percent")
        )

        def _parse_lost_proposals_percent(data: object) -> float | str:
            return cast(float | str, data)

        lost_proposals_percent = _parse_lost_proposals_percent(
            d.pop("lost_proposals_percent")
        )

        sales_time_series = []
        _sales_time_series = d.pop("sales_time_series")
        for sales_time_series_item_data in _sales_time_series:
            sales_time_series_item = ProductSalesTimeSeries.from_dict(
                sales_time_series_item_data
            )

            sales_time_series.append(sales_time_series_item)

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

        output_product_details = cls(
            id=id,
            name=name,
            pricing_type=pricing_type,
            pricing_type_display=pricing_type_display,
            pricing_value=pricing_value,
            currency=currency,
            currency_symbol=currency_symbol,
            is_active=is_active,
            owner_name=owner_name,
            payment_integration_id=payment_integration_id,
            created_at=created_at,
            updated_at=updated_at,
            times_sold=times_sold,
            won_proposals_percent=won_proposals_percent,
            lost_proposals_percent=lost_proposals_percent,
            sales_time_series=sales_time_series,
            description=description,
            internal_code=internal_code,
        )

        output_product_details.additional_properties = d
        return output_product_details

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
