from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="AnalyticsSalesConversionFunnelSummary")


@_attrs_define
class AnalyticsSalesConversionFunnelSummary:
    """Summary info for a single funnel (used in tabs)

    Attributes:
        funnel_id (str):
        funnel_name (str):
        deals_created (int):
        deals_won (int):
        deals_lost (int):
        funnel_conversion_rate (float | str):
    """

    funnel_id: str
    funnel_name: str
    deals_created: int
    deals_won: int
    deals_lost: int
    funnel_conversion_rate: float | str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        funnel_id = self.funnel_id

        funnel_name = self.funnel_name

        deals_created = self.deals_created

        deals_won = self.deals_won

        deals_lost = self.deals_lost

        funnel_conversion_rate: float | str
        funnel_conversion_rate = self.funnel_conversion_rate

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "funnel_id": funnel_id,
                "funnel_name": funnel_name,
                "deals_created": deals_created,
                "deals_won": deals_won,
                "deals_lost": deals_lost,
                "funnel_conversion_rate": funnel_conversion_rate,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        funnel_id = d.pop("funnel_id")

        funnel_name = d.pop("funnel_name")

        deals_created = d.pop("deals_created")

        deals_won = d.pop("deals_won")

        deals_lost = d.pop("deals_lost")

        def _parse_funnel_conversion_rate(data: object) -> float | str:
            return cast(float | str, data)

        funnel_conversion_rate = _parse_funnel_conversion_rate(
            d.pop("funnel_conversion_rate")
        )

        analytics_sales_conversion_funnel_summary = cls(
            funnel_id=funnel_id,
            funnel_name=funnel_name,
            deals_created=deals_created,
            deals_won=deals_won,
            deals_lost=deals_lost,
            funnel_conversion_rate=funnel_conversion_rate,
        )

        analytics_sales_conversion_funnel_summary.additional_properties = d
        return analytics_sales_conversion_funnel_summary

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
