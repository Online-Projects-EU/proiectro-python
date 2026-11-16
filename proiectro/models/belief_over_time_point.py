from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="BeliefOverTimePoint")


@_attrs_define
class BeliefOverTimePoint:
    """
    Attributes:
        at (datetime.datetime):
        value (float | None | str | Unset):
        low (float | None | str | Unset):
        high (float | None | str | Unset):
        observed (int | Unset):  Default: 0.
    """

    at: datetime.datetime
    value: float | None | str | Unset = UNSET
    low: float | None | str | Unset = UNSET
    high: float | None | str | Unset = UNSET
    observed: int | Unset = 0
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        at = self.at.isoformat()

        value: float | None | str | Unset
        if isinstance(self.value, Unset):
            value = UNSET
        else:
            value = self.value

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

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "at": at,
            }
        )
        if value is not UNSET:
            field_dict["value"] = value
        if low is not UNSET:
            field_dict["low"] = low
        if high is not UNSET:
            field_dict["high"] = high
        if observed is not UNSET:
            field_dict["observed"] = observed

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        at = isoparse(d.pop("at"))

        def _parse_value(data: object) -> float | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | str | Unset, data)

        value = _parse_value(d.pop("value", UNSET))

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

        belief_over_time_point = cls(
            at=at,
            value=value,
            low=low,
            high=high,
            observed=observed,
        )

        belief_over_time_point.additional_properties = d
        return belief_over_time_point

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
