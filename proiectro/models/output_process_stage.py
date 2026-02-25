from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.output_process_stage_link import OutputProcessStageLink


T = TypeVar("T", bound="OutputProcessStage")


@_attrs_define
class OutputProcessStage:
    """
    Attributes:
        id (str):
        name (str):
        description (str):
        instructions (str):
        stage_type (str):
        sequence_no (int):
        is_active (bool):
        requires_approval (bool):
        can_link (bool | Unset):  Default: False.
        item_count (int | Unset):  Default: 0.
        linked_stages (list[OutputProcessStageLink] | Unset):
    """

    id: str
    name: str
    description: str
    instructions: str
    stage_type: str
    sequence_no: int
    is_active: bool
    requires_approval: bool
    can_link: bool | Unset = False
    item_count: int | Unset = 0
    linked_stages: list[OutputProcessStageLink] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        description = self.description

        instructions = self.instructions

        stage_type = self.stage_type

        sequence_no = self.sequence_no

        is_active = self.is_active

        requires_approval = self.requires_approval

        can_link = self.can_link

        item_count = self.item_count

        linked_stages: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.linked_stages, Unset):
            linked_stages = []
            for linked_stages_item_data in self.linked_stages:
                linked_stages_item = linked_stages_item_data.to_dict()
                linked_stages.append(linked_stages_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "description": description,
                "instructions": instructions,
                "stage_type": stage_type,
                "sequence_no": sequence_no,
                "is_active": is_active,
                "requires_approval": requires_approval,
            }
        )
        if can_link is not UNSET:
            field_dict["can_link"] = can_link
        if item_count is not UNSET:
            field_dict["item_count"] = item_count
        if linked_stages is not UNSET:
            field_dict["linked_stages"] = linked_stages

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.output_process_stage_link import OutputProcessStageLink

        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        description = d.pop("description")

        instructions = d.pop("instructions")

        stage_type = d.pop("stage_type")

        sequence_no = d.pop("sequence_no")

        is_active = d.pop("is_active")

        requires_approval = d.pop("requires_approval")

        can_link = d.pop("can_link", UNSET)

        item_count = d.pop("item_count", UNSET)

        _linked_stages = d.pop("linked_stages", UNSET)
        linked_stages: list[OutputProcessStageLink] | Unset = UNSET
        if _linked_stages is not UNSET:
            linked_stages = []
            for linked_stages_item_data in _linked_stages:
                linked_stages_item = OutputProcessStageLink.from_dict(
                    linked_stages_item_data
                )

                linked_stages.append(linked_stages_item)

        output_process_stage = cls(
            id=id,
            name=name,
            description=description,
            instructions=instructions,
            stage_type=stage_type,
            sequence_no=sequence_no,
            is_active=is_active,
            requires_approval=requires_approval,
            can_link=can_link,
            item_count=item_count,
            linked_stages=linked_stages,
        )

        output_process_stage.additional_properties = d
        return output_process_stage

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
