from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AddExchange")


@_attrs_define
class AddExchange:
    """
    Attributes:
        base_currency (str):
        target_currency (str):
        rate (float | str):
        valid_from (str):
        source (None | str | Unset):  Default: 'Manual'.
    """

    base_currency: str
    target_currency: str
    rate: float | str
    valid_from: str
    source: None | str | Unset = "Manual"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        base_currency = self.base_currency

        target_currency = self.target_currency

        rate: float | str
        rate = self.rate

        valid_from = self.valid_from

        source: None | str | Unset
        if isinstance(self.source, Unset):
            source = UNSET
        else:
            source = self.source

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "base_currency": base_currency,
                "target_currency": target_currency,
                "rate": rate,
                "valid_from": valid_from,
            }
        )
        if source is not UNSET:
            field_dict["source"] = source

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        base_currency = d.pop("base_currency")

        target_currency = d.pop("target_currency")

        def _parse_rate(data: object) -> float | str:
            return cast(float | str, data)

        rate = _parse_rate(d.pop("rate"))

        valid_from = d.pop("valid_from")

        def _parse_source(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        source = _parse_source(d.pop("source", UNSET))

        add_exchange = cls(
            base_currency=base_currency,
            target_currency=target_currency,
            rate=rate,
            valid_from=valid_from,
            source=source,
        )

        add_exchange.additional_properties = d
        return add_exchange

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
