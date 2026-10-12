from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TargetBandSegment")


@_attrs_define
class TargetBandSegment:
    """One stretch of the attainment bar, already measured as a share of the track.

    The arithmetic is done here rather than in the template: widths depend on where the ladder ends
    and on whether the person went past it, and a template cannot divide.

        Attributes:
            width_pct (float | str):
            achieved (bool):
            name (None | str | Unset):
    """

    width_pct: float | str
    achieved: bool
    name: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        width_pct: float | str
        width_pct = self.width_pct

        achieved = self.achieved

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "width_pct": width_pct,
                "achieved": achieved,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_width_pct(data: object) -> float | str:
            return cast(float | str, data)

        width_pct = _parse_width_pct(d.pop("width_pct"))

        achieved = d.pop("achieved")

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        target_band_segment = cls(
            width_pct=width_pct,
            achieved=achieved,
            name=name,
        )

        target_band_segment.additional_properties = d
        return target_band_segment

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
