from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="AnalyticsSalesFunnel")


@_attrs_define
class AnalyticsSalesFunnel:
    """Summary info for a single funnel (used in tabs)

    Attributes:
        funnel_id (str):
        funnel_name (str):
        deal_count (int):
        total_value (float | str):
    """

    funnel_id: str
    funnel_name: str
    deal_count: int
    total_value: float | str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        funnel_id = self.funnel_id

        funnel_name = self.funnel_name

        deal_count = self.deal_count

        total_value: float | str
        total_value = self.total_value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "funnel_id": funnel_id,
                "funnel_name": funnel_name,
                "deal_count": deal_count,
                "total_value": total_value,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        funnel_id = d.pop("funnel_id")

        funnel_name = d.pop("funnel_name")

        deal_count = d.pop("deal_count")

        def _parse_total_value(data: object) -> float | str:
            return cast(float | str, data)

        total_value = _parse_total_value(d.pop("total_value"))

        analytics_sales_funnel = cls(
            funnel_id=funnel_id,
            funnel_name=funnel_name,
            deal_count=deal_count,
            total_value=total_value,
        )

        analytics_sales_funnel.additional_properties = d
        return analytics_sales_funnel

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
