from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="AnalyticsCashflowSourceItem")


@_attrs_define
class AnalyticsCashflowSourceItem:
    """Cash flow by source

    Attributes:
        source (str):
        amount_scheduled (float | str):
        amount_realized (float | str):
    """

    source: str
    amount_scheduled: float | str
    amount_realized: float | str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        source = self.source

        amount_scheduled: float | str
        amount_scheduled = self.amount_scheduled

        amount_realized: float | str
        amount_realized = self.amount_realized

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "source": source,
                "amount_scheduled": amount_scheduled,
                "amount_realized": amount_realized,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        source = d.pop("source")

        def _parse_amount_scheduled(data: object) -> float | str:
            return cast(float | str, data)

        amount_scheduled = _parse_amount_scheduled(d.pop("amount_scheduled"))

        def _parse_amount_realized(data: object) -> float | str:
            return cast(float | str, data)

        amount_realized = _parse_amount_realized(d.pop("amount_realized"))

        analytics_cashflow_source_item = cls(
            source=source,
            amount_scheduled=amount_scheduled,
            amount_realized=amount_realized,
        )

        analytics_cashflow_source_item.additional_properties = d
        return analytics_cashflow_source_item

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
