from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.add_process_stage_stage_type import AddProcessStageStageType
from ..types import UNSET, Unset

T = TypeVar("T", bound="AddProcessStage")


@_attrs_define
class AddProcessStage:
    """
    Attributes:
        process (str):
        name (str):
        stage_type (AddProcessStageStageType):
        sequence_no (int):
        description (str | Unset):  Default: ''.
        instructions (str | Unset):  Default: ''.
        is_active (bool | None | Unset):  Default: False.
        requires_approval (bool | None | Unset):  Default: False.
    """

    process: str
    name: str
    stage_type: AddProcessStageStageType
    sequence_no: int
    description: str | Unset = ""
    instructions: str | Unset = ""
    is_active: bool | None | Unset = False
    requires_approval: bool | None | Unset = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        process = self.process

        name = self.name

        stage_type = self.stage_type.value

        sequence_no = self.sequence_no

        description = self.description

        instructions = self.instructions

        is_active: bool | None | Unset
        if isinstance(self.is_active, Unset):
            is_active = UNSET
        else:
            is_active = self.is_active

        requires_approval: bool | None | Unset
        if isinstance(self.requires_approval, Unset):
            requires_approval = UNSET
        else:
            requires_approval = self.requires_approval

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "process": process,
                "name": name,
                "stage_type": stage_type,
                "sequence_no": sequence_no,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if instructions is not UNSET:
            field_dict["instructions"] = instructions
        if is_active is not UNSET:
            field_dict["is_active"] = is_active
        if requires_approval is not UNSET:
            field_dict["requires_approval"] = requires_approval

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        process = d.pop("process")

        name = d.pop("name")

        stage_type = AddProcessStageStageType(d.pop("stage_type"))

        sequence_no = d.pop("sequence_no")

        description = d.pop("description", UNSET)

        instructions = d.pop("instructions", UNSET)

        def _parse_is_active(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_active = _parse_is_active(d.pop("is_active", UNSET))

        def _parse_requires_approval(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        requires_approval = _parse_requires_approval(d.pop("requires_approval", UNSET))

        add_process_stage = cls(
            process=process,
            name=name,
            stage_type=stage_type,
            sequence_no=sequence_no,
            description=description,
            instructions=instructions,
            is_active=is_active,
            requires_approval=requires_approval,
        )

        add_process_stage.additional_properties = d
        return add_process_stage

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
