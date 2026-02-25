from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.gantt_task import GanttTask
    from ..models.schedule_warning import ScheduleWarning


T = TypeVar("T", bound="OutputProjectGanttData")


@_attrs_define
class OutputProjectGanttData:
    """Frappe Gantt data for project visualization

    Attributes:
        tasks (list[GanttTask]):
        project_id (str):
        project_name (str):
        has_data (bool):
        warnings (list[ScheduleWarning] | Unset):
    """

    tasks: list[GanttTask]
    project_id: str
    project_name: str
    has_data: bool
    warnings: list[ScheduleWarning] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        tasks = []
        for tasks_item_data in self.tasks:
            tasks_item = tasks_item_data.to_dict()
            tasks.append(tasks_item)

        project_id = self.project_id

        project_name = self.project_name

        has_data = self.has_data

        warnings: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.warnings, Unset):
            warnings = []
            for warnings_item_data in self.warnings:
                warnings_item = warnings_item_data.to_dict()
                warnings.append(warnings_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "tasks": tasks,
                "project_id": project_id,
                "project_name": project_name,
                "has_data": has_data,
            }
        )
        if warnings is not UNSET:
            field_dict["warnings"] = warnings

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.gantt_task import GanttTask
        from ..models.schedule_warning import ScheduleWarning

        d = dict(src_dict)
        tasks = []
        _tasks = d.pop("tasks")
        for tasks_item_data in _tasks:
            tasks_item = GanttTask.from_dict(tasks_item_data)

            tasks.append(tasks_item)

        project_id = d.pop("project_id")

        project_name = d.pop("project_name")

        has_data = d.pop("has_data")

        _warnings = d.pop("warnings", UNSET)
        warnings: list[ScheduleWarning] | Unset = UNSET
        if _warnings is not UNSET:
            warnings = []
            for warnings_item_data in _warnings:
                warnings_item = ScheduleWarning.from_dict(warnings_item_data)

                warnings.append(warnings_item)

        output_project_gantt_data = cls(
            tasks=tasks,
            project_id=project_id,
            project_name=project_name,
            has_data=has_data,
            warnings=warnings,
        )

        output_project_gantt_data.additional_properties = d
        return output_project_gantt_data

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
