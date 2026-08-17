from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="OutputProcessStageForm")



@_attrs_define
class OutputProcessStageForm:
    """ One form attached to a process stage (Part 7), with its gating policy.

        Attributes:
            id (str):
            form_id (str):
            form_name (str):
            is_required (bool | Unset):  Default: False.
            block_advancement (bool | Unset):  Default: True.
            completion_deadline_hours (int | None | Unset):
            sequence (int | Unset):  Default: 0.
            has_active_version (bool | Unset):  Default: False.
     """

    id: str
    form_id: str
    form_name: str
    is_required: bool | Unset = False
    block_advancement: bool | Unset = True
    completion_deadline_hours: int | None | Unset = UNSET
    sequence: int | Unset = 0
    has_active_version: bool | Unset = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        id = self.id

        form_id = self.form_id

        form_name = self.form_name

        is_required = self.is_required

        block_advancement = self.block_advancement

        completion_deadline_hours: int | None | Unset
        if isinstance(self.completion_deadline_hours, Unset):
            completion_deadline_hours = UNSET
        else:
            completion_deadline_hours = self.completion_deadline_hours

        sequence = self.sequence

        has_active_version = self.has_active_version


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "id": id,
            "form_id": form_id,
            "form_name": form_name,
        })
        if is_required is not UNSET:
            field_dict["is_required"] = is_required
        if block_advancement is not UNSET:
            field_dict["block_advancement"] = block_advancement
        if completion_deadline_hours is not UNSET:
            field_dict["completion_deadline_hours"] = completion_deadline_hours
        if sequence is not UNSET:
            field_dict["sequence"] = sequence
        if has_active_version is not UNSET:
            field_dict["has_active_version"] = has_active_version

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        form_id = d.pop("form_id")

        form_name = d.pop("form_name")

        is_required = d.pop("is_required", UNSET)

        block_advancement = d.pop("block_advancement", UNSET)

        def _parse_completion_deadline_hours(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        completion_deadline_hours = _parse_completion_deadline_hours(d.pop("completion_deadline_hours", UNSET))


        sequence = d.pop("sequence", UNSET)

        has_active_version = d.pop("has_active_version", UNSET)

        output_process_stage_form = cls(
            id=id,
            form_id=form_id,
            form_name=form_name,
            is_required=is_required,
            block_advancement=block_advancement,
            completion_deadline_hours=completion_deadline_hours,
            sequence=sequence,
            has_active_version=has_active_version,
        )


        output_process_stage_form.additional_properties = d
        return output_process_stage_form

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
