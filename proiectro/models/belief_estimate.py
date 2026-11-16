from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BeliefEstimate")


@_attrs_define
class BeliefEstimate:
    """A figure with what it rests on. A share carries `rate` and `successes`; an average carries `average`
    and `middle`. `low` and `high` are the two ends of the likely range. Everything is empty while `needed`
    cases are still missing.

        Attributes:
            rate (float | None | str | Unset):
            average (float | None | str | Unset):
            middle (float | None | str | Unset):
            low (float | None | str | Unset):
            high (float | None | str | Unset):
            observed (int | Unset):  Default: 0.
            successes (int | None | Unset):
            needed (int | Unset):  Default: 0.
    """

    rate: float | None | str | Unset = UNSET
    average: float | None | str | Unset = UNSET
    middle: float | None | str | Unset = UNSET
    low: float | None | str | Unset = UNSET
    high: float | None | str | Unset = UNSET
    observed: int | Unset = 0
    successes: int | None | Unset = UNSET
    needed: int | Unset = 0
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        rate: float | None | str | Unset
        if isinstance(self.rate, Unset):
            rate = UNSET
        else:
            rate = self.rate

        average: float | None | str | Unset
        if isinstance(self.average, Unset):
            average = UNSET
        else:
            average = self.average

        middle: float | None | str | Unset
        if isinstance(self.middle, Unset):
            middle = UNSET
        else:
            middle = self.middle

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

        observed = self.observed

        successes: int | None | Unset
        if isinstance(self.successes, Unset):
            successes = UNSET
        else:
            successes = self.successes

        needed = self.needed

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if rate is not UNSET:
            field_dict["rate"] = rate
        if average is not UNSET:
            field_dict["average"] = average
        if middle is not UNSET:
            field_dict["middle"] = middle
        if low is not UNSET:
            field_dict["low"] = low
        if high is not UNSET:
            field_dict["high"] = high
        if observed is not UNSET:
            field_dict["observed"] = observed
        if successes is not UNSET:
            field_dict["successes"] = successes
        if needed is not UNSET:
            field_dict["needed"] = needed

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_rate(data: object) -> float | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | str | Unset, data)

        rate = _parse_rate(d.pop("rate", UNSET))

        def _parse_average(data: object) -> float | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | str | Unset, data)

        average = _parse_average(d.pop("average", UNSET))

        def _parse_middle(data: object) -> float | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | str | Unset, data)

        middle = _parse_middle(d.pop("middle", UNSET))

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

        observed = d.pop("observed", UNSET)

        def _parse_successes(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        successes = _parse_successes(d.pop("successes", UNSET))

        needed = d.pop("needed", UNSET)

        belief_estimate = cls(
            rate=rate,
            average=average,
            middle=middle,
            low=low,
            high=high,
            observed=observed,
            successes=successes,
            needed=needed,
        )

        belief_estimate.additional_properties = d
        return belief_estimate

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
