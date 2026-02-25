from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.output_stage_with_tasks import OutputStageWithTasks


T = TypeVar("T", bound="OutputProcessStagesWithTasks")


@_attrs_define
class OutputProcessStagesWithTasks:
    """
    Attributes:
        process_id (str):
        process_name (str):
        stages (list[OutputStageWithTasks]):
    """

    process_id: str
    process_name: str
    stages: list[OutputStageWithTasks]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        process_id = self.process_id

        process_name = self.process_name

        stages = []
        for stages_item_data in self.stages:
            stages_item = stages_item_data.to_dict()
            stages.append(stages_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "process_id": process_id,
                "process_name": process_name,
                "stages": stages,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.output_stage_with_tasks import OutputStageWithTasks

        d = dict(src_dict)
        process_id = d.pop("process_id")

        process_name = d.pop("process_name")

        stages = []
        _stages = d.pop("stages")
        for stages_item_data in _stages:
            stages_item = OutputStageWithTasks.from_dict(stages_item_data)

            stages.append(stages_item)

        output_process_stages_with_tasks = cls(
            process_id=process_id,
            process_name=process_name,
            stages=stages,
        )

        output_process_stages_with_tasks.additional_properties = d
        return output_process_stages_with_tasks

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
