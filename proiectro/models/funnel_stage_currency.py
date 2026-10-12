from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="FunnelStageCurrency")


@_attrs_define
class FunnelStageCurrency:
    """One currency's deals in a funnel stage, in that currency.

    Attributes:
        count (int):
        value (float | str):
        symbol (str):
    """

    count: int
    value: float | str
    symbol: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        count = self.count

        value: float | str
        value = self.value

        symbol = self.symbol

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "count": count,
                "value": value,
                "symbol": symbol,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        count = d.pop("count")

        def _parse_value(data: object) -> float | str:
            return cast(float | str, data)

        value = _parse_value(d.pop("value"))

        symbol = d.pop("symbol")

        funnel_stage_currency = cls(
            count=count,
            value=value,
            symbol=symbol,
        )

        funnel_stage_currency.additional_properties = d
        return funnel_stage_currency

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
