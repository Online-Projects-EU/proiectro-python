from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="EditTargetBand")


@_attrs_define
class EditTargetBand:
    """
    Attributes:
        name (str):
        threshold_percent (float | None | str | Unset):
        sequence_no (int | None | Unset):
    """

    name: str
    threshold_percent: float | None | str | Unset = UNSET
    sequence_no: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        threshold_percent: float | None | str | Unset
        if isinstance(self.threshold_percent, Unset):
            threshold_percent = UNSET
        else:
            threshold_percent = self.threshold_percent

        sequence_no: int | None | Unset
        if isinstance(self.sequence_no, Unset):
            sequence_no = UNSET
        else:
            sequence_no = self.sequence_no

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
            }
        )
        if threshold_percent is not UNSET:
            field_dict["threshold_percent"] = threshold_percent
        if sequence_no is not UNSET:
            field_dict["sequence_no"] = sequence_no

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        def _parse_threshold_percent(data: object) -> float | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | str | Unset, data)

        threshold_percent = _parse_threshold_percent(d.pop("threshold_percent", UNSET))

        def _parse_sequence_no(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        sequence_no = _parse_sequence_no(d.pop("sequence_no", UNSET))

        edit_target_band = cls(
            name=name,
            threshold_percent=threshold_percent,
            sequence_no=sequence_no,
        )

        edit_target_band.additional_properties = d
        return edit_target_band

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
