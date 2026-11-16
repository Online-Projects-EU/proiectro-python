from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.chain_waiting_on import ChainWaitingOn


T = TypeVar("T", bound="ChainFinish")


@_attrs_define
class ChainFinish:
    """
    Attributes:
        key (str):
        name (str):
        rate (float | None | str | Unset):
        low (float | None | str | Unset):
        high (float | None | str | Unset):
        waiting_on (list[ChainWaitingOn] | Unset):
    """

    key: str
    name: str
    rate: float | None | str | Unset = UNSET
    low: float | None | str | Unset = UNSET
    high: float | None | str | Unset = UNSET
    waiting_on: list[ChainWaitingOn] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        key = self.key

        name = self.name

        rate: float | None | str | Unset
        if isinstance(self.rate, Unset):
            rate = UNSET
        else:
            rate = self.rate

        low: float | None | str | Unset
        if isinstance(self.low, Unset):
            low = UNSET
        else:
            low = self.low

        high: float | None | str | Unset
        if isinstance(self.high, Unset):
            high = UNSET
        else:
            high = self.high

        waiting_on: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.waiting_on, Unset):
            waiting_on = []
            for waiting_on_item_data in self.waiting_on:
                waiting_on_item = waiting_on_item_data.to_dict()
                waiting_on.append(waiting_on_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "key": key,
                "name": name,
            }
        )
        if rate is not UNSET:
            field_dict["rate"] = rate
        if low is not UNSET:
            field_dict["low"] = low
        if high is not UNSET:
            field_dict["high"] = high
        if waiting_on is not UNSET:
            field_dict["waiting_on"] = waiting_on

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.chain_waiting_on import ChainWaitingOn

        d = dict(src_dict)
        key = d.pop("key")

        name = d.pop("name")

        def _parse_rate(data: object) -> float | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | str | Unset, data)

        rate = _parse_rate(d.pop("rate", UNSET))

        def _parse_low(data: object) -> float | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | str | Unset, data)

        low = _parse_low(d.pop("low", UNSET))

        def _parse_high(data: object) -> float | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | str | Unset, data)

        high = _parse_high(d.pop("high", UNSET))

        _waiting_on = d.pop("waiting_on", UNSET)
        waiting_on: list[ChainWaitingOn] | Unset = UNSET
        if _waiting_on is not UNSET:
            waiting_on = []
            for waiting_on_item_data in _waiting_on:
                waiting_on_item = ChainWaitingOn.from_dict(waiting_on_item_data)

                waiting_on.append(waiting_on_item)

        chain_finish = cls(
            key=key,
            name=name,
            rate=rate,
            low=low,
            high=high,
            waiting_on=waiting_on,
        )

        chain_finish.additional_properties = d
        return chain_finish

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
