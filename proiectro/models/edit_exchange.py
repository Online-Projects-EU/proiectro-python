from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="EditExchange")


@_attrs_define
class EditExchange:
    """
    Attributes:
        rate (float | str):
        valid_from (str):
        source (None | str):
        valid_until (None | str | Unset):
    """

    rate: float | str
    valid_from: str
    source: None | str
    valid_until: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        rate: float | str
        rate = self.rate

        valid_from = self.valid_from

        source: None | str
        source = self.source

        valid_until: None | str | Unset
        if isinstance(self.valid_until, Unset):
            valid_until = UNSET
        else:
            valid_until = self.valid_until

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "rate": rate,
                "valid_from": valid_from,
                "source": source,
            }
        )
        if valid_until is not UNSET:
            field_dict["valid_until"] = valid_until

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_rate(data: object) -> float | str:
            return cast(float | str, data)

        rate = _parse_rate(d.pop("rate"))

        valid_from = d.pop("valid_from")

        def _parse_source(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        source = _parse_source(d.pop("source"))

        def _parse_valid_until(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        valid_until = _parse_valid_until(d.pop("valid_until", UNSET))

        edit_exchange = cls(
            rate=rate,
            valid_from=valid_from,
            source=source,
            valid_until=valid_until,
        )

        edit_exchange.additional_properties = d
        return edit_exchange

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
