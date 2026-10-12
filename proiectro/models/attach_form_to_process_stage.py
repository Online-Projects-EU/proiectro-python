from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AttachFormToProcessStage")


@_attrs_define
class AttachFormToProcessStage:
    """
    Attributes:
        custom_form_id (str):
        is_required (bool | Unset):  Default: False.
        block_advancement (bool | Unset):  Default: False.
        completion_deadline_hours (int | None | Unset):
        sequence (int | Unset):  Default: 0.
    """

    custom_form_id: str
    is_required: bool | Unset = False
    block_advancement: bool | Unset = False
    completion_deadline_hours: int | None | Unset = UNSET
    sequence: int | Unset = 0
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        custom_form_id = self.custom_form_id

        is_required = self.is_required

        block_advancement = self.block_advancement

        completion_deadline_hours: int | None | Unset
        if isinstance(self.completion_deadline_hours, Unset):
            completion_deadline_hours = UNSET
        else:
            completion_deadline_hours = self.completion_deadline_hours

        sequence = self.sequence

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "custom_form_id": custom_form_id,
            }
        )
        if is_required is not UNSET:
            field_dict["is_required"] = is_required
        if block_advancement is not UNSET:
            field_dict["block_advancement"] = block_advancement
        if completion_deadline_hours is not UNSET:
            field_dict["completion_deadline_hours"] = completion_deadline_hours
        if sequence is not UNSET:
            field_dict["sequence"] = sequence

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        custom_form_id = d.pop("custom_form_id")

        is_required = d.pop("is_required", UNSET)

        block_advancement = d.pop("block_advancement", UNSET)

        def _parse_completion_deadline_hours(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        completion_deadline_hours = _parse_completion_deadline_hours(
            d.pop("completion_deadline_hours", UNSET)
        )

        sequence = d.pop("sequence", UNSET)

        attach_form_to_process_stage = cls(
            custom_form_id=custom_form_id,
            is_required=is_required,
            block_advancement=block_advancement,
            completion_deadline_hours=completion_deadline_hours,
            sequence=sequence,
        )

        attach_form_to_process_stage.additional_properties = d
        return attach_form_to_process_stage

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
