from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="LeadMilestoneRate")


@_attrs_define
class LeadMilestoneRate:
    """How many of the contacted leads reached a milestone, as a count and as a share with its likely range.

    Attributes:
        reached (int):
        percent (float | None | str | Unset):
        low (float | None | str | Unset):
        high (float | None | str | Unset):
        verdict (str | Unset):  Default: 'cannot_tell'.
    """

    reached: int
    percent: float | None | str | Unset = UNSET
    low: float | None | str | Unset = UNSET
    high: float | None | str | Unset = UNSET
    verdict: str | Unset = "cannot_tell"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        reached = self.reached

        percent: float | None | str | Unset
        if isinstance(self.percent, Unset):
            percent = UNSET
        else:
            percent = self.percent

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

        verdict = self.verdict

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "reached": reached,
            }
        )
        if percent is not UNSET:
            field_dict["percent"] = percent
        if low is not UNSET:
            field_dict["low"] = low
        if high is not UNSET:
            field_dict["high"] = high
        if verdict is not UNSET:
            field_dict["verdict"] = verdict

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        reached = d.pop("reached")

        def _parse_percent(data: object) -> float | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | str | Unset, data)

        percent = _parse_percent(d.pop("percent", UNSET))

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

        verdict = d.pop("verdict", UNSET)

        lead_milestone_rate = cls(
            reached=reached,
            percent=percent,
            low=low,
            high=high,
            verdict=verdict,
        )

        lead_milestone_rate.additional_properties = d
        return lead_milestone_rate

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
