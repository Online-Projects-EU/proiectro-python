from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AttachFormToAsset")


@_attrs_define
class AttachFormToAsset:
    """
    Attributes:
        custom_form_id (str):
        inspection_interval_days (int | None | Unset):
        sequence (int | Unset):  Default: 0.
    """

    custom_form_id: str
    inspection_interval_days: int | None | Unset = UNSET
    sequence: int | Unset = 0
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        custom_form_id = self.custom_form_id

        inspection_interval_days: int | None | Unset
        if isinstance(self.inspection_interval_days, Unset):
            inspection_interval_days = UNSET
        else:
            inspection_interval_days = self.inspection_interval_days

        sequence = self.sequence

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "custom_form_id": custom_form_id,
            }
        )
        if inspection_interval_days is not UNSET:
            field_dict["inspection_interval_days"] = inspection_interval_days
        if sequence is not UNSET:
            field_dict["sequence"] = sequence

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        custom_form_id = d.pop("custom_form_id")

        def _parse_inspection_interval_days(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        inspection_interval_days = _parse_inspection_interval_days(
            d.pop("inspection_interval_days", UNSET)
        )

        sequence = d.pop("sequence", UNSET)

        attach_form_to_asset = cls(
            custom_form_id=custom_form_id,
            inspection_interval_days=inspection_interval_days,
            sequence=sequence,
        )

        attach_form_to_asset.additional_properties = d
        return attach_form_to_asset

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
