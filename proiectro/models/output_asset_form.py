from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="OutputAssetForm")



@_attrs_define
class OutputAssetForm:
    """ One form attached to an asset (Part 6), with this link's submission count.

        Attributes:
            id (str):
            form_id (str):
            form_name (str):
            sequence (int | Unset):  Default: 0.
            inspection_interval_days (int | None | Unset):
            submission_count (int | Unset):  Default: 0.
            has_active_version (bool | Unset):  Default: False.
     """

    id: str
    form_id: str
    form_name: str
    sequence: int | Unset = 0
    inspection_interval_days: int | None | Unset = UNSET
    submission_count: int | Unset = 0
    has_active_version: bool | Unset = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        id = self.id

        form_id = self.form_id

        form_name = self.form_name

        sequence = self.sequence

        inspection_interval_days: int | None | Unset
        if isinstance(self.inspection_interval_days, Unset):
            inspection_interval_days = UNSET
        else:
            inspection_interval_days = self.inspection_interval_days

        submission_count = self.submission_count

        has_active_version = self.has_active_version


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "id": id,
            "form_id": form_id,
            "form_name": form_name,
        })
        if sequence is not UNSET:
            field_dict["sequence"] = sequence
        if inspection_interval_days is not UNSET:
            field_dict["inspection_interval_days"] = inspection_interval_days
        if submission_count is not UNSET:
            field_dict["submission_count"] = submission_count
        if has_active_version is not UNSET:
            field_dict["has_active_version"] = has_active_version

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        form_id = d.pop("form_id")

        form_name = d.pop("form_name")

        sequence = d.pop("sequence", UNSET)

        def _parse_inspection_interval_days(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        inspection_interval_days = _parse_inspection_interval_days(d.pop("inspection_interval_days", UNSET))


        submission_count = d.pop("submission_count", UNSET)

        has_active_version = d.pop("has_active_version", UNSET)

        output_asset_form = cls(
            id=id,
            form_id=form_id,
            form_name=form_name,
            sequence=sequence,
            inspection_interval_days=inspection_interval_days,
            submission_count=submission_count,
            has_active_version=has_active_version,
        )


        output_asset_form.additional_properties = d
        return output_asset_form

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
