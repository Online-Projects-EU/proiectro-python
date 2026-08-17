from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
import datetime

if TYPE_CHECKING:
  from ..models.schedule_task_item import ScheduleTaskItem
  from ..models.schedule_warning import ScheduleWarning





T = TypeVar("T", bound="OutputProjectSchedule")



@_attrs_define
class OutputProjectSchedule:
    """ Project schedule with critical path data

        Attributes:
            tasks (list[ScheduleTaskItem]):
            project_id (str):
            project_name (str):
            total_tasks (int):
            critical_path_tasks (int):
            project_duration_days (int):
            has_schedule_data (bool):
            warnings (list[ScheduleWarning] | Unset):
            schedule_last_computed (datetime.datetime | None | Unset):
            schedule_last_modified (datetime.datetime | None | Unset):
     """

    tasks: list[ScheduleTaskItem]
    project_id: str
    project_name: str
    total_tasks: int
    critical_path_tasks: int
    project_duration_days: int
    has_schedule_data: bool
    warnings: list[ScheduleWarning] | Unset = UNSET
    schedule_last_computed: datetime.datetime | None | Unset = UNSET
    schedule_last_modified: datetime.datetime | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.schedule_warning import ScheduleWarning
        from ..models.schedule_task_item import ScheduleTaskItem
        tasks = []
        for tasks_item_data in self.tasks:
            tasks_item = tasks_item_data.to_dict()
            tasks.append(tasks_item)



        project_id = self.project_id

        project_name = self.project_name

        total_tasks = self.total_tasks

        critical_path_tasks = self.critical_path_tasks

        project_duration_days = self.project_duration_days

        has_schedule_data = self.has_schedule_data

        warnings: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.warnings, Unset):
            warnings = []
            for warnings_item_data in self.warnings:
                warnings_item = warnings_item_data.to_dict()
                warnings.append(warnings_item)



        schedule_last_computed: None | str | Unset
        if isinstance(self.schedule_last_computed, Unset):
            schedule_last_computed = UNSET
        elif isinstance(self.schedule_last_computed, datetime.datetime):
            schedule_last_computed = self.schedule_last_computed.isoformat()
        else:
            schedule_last_computed = self.schedule_last_computed

        schedule_last_modified: None | str | Unset
        if isinstance(self.schedule_last_modified, Unset):
            schedule_last_modified = UNSET
        elif isinstance(self.schedule_last_modified, datetime.datetime):
            schedule_last_modified = self.schedule_last_modified.isoformat()
        else:
            schedule_last_modified = self.schedule_last_modified


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "tasks": tasks,
            "project_id": project_id,
            "project_name": project_name,
            "total_tasks": total_tasks,
            "critical_path_tasks": critical_path_tasks,
            "project_duration_days": project_duration_days,
            "has_schedule_data": has_schedule_data,
        })
        if warnings is not UNSET:
            field_dict["warnings"] = warnings
        if schedule_last_computed is not UNSET:
            field_dict["schedule_last_computed"] = schedule_last_computed
        if schedule_last_modified is not UNSET:
            field_dict["schedule_last_modified"] = schedule_last_modified

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.schedule_task_item import ScheduleTaskItem
        from ..models.schedule_warning import ScheduleWarning
        d = dict(src_dict)
        tasks = []
        _tasks = d.pop("tasks")
        for tasks_item_data in (_tasks):
            tasks_item = ScheduleTaskItem.from_dict(tasks_item_data)



            tasks.append(tasks_item)


        project_id = d.pop("project_id")

        project_name = d.pop("project_name")

        total_tasks = d.pop("total_tasks")

        critical_path_tasks = d.pop("critical_path_tasks")

        project_duration_days = d.pop("project_duration_days")

        has_schedule_data = d.pop("has_schedule_data")

        _warnings = d.pop("warnings", UNSET)
        warnings: list[ScheduleWarning] | Unset = UNSET
        if _warnings is not UNSET:
            warnings = []
            for warnings_item_data in _warnings:
                warnings_item = ScheduleWarning.from_dict(warnings_item_data)



                warnings.append(warnings_item)


        def _parse_schedule_last_computed(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                schedule_last_computed_type_0 = isoparse(data)



                return schedule_last_computed_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        schedule_last_computed = _parse_schedule_last_computed(d.pop("schedule_last_computed", UNSET))


        def _parse_schedule_last_modified(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                schedule_last_modified_type_0 = isoparse(data)



                return schedule_last_modified_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        schedule_last_modified = _parse_schedule_last_modified(d.pop("schedule_last_modified", UNSET))


        output_project_schedule = cls(
            tasks=tasks,
            project_id=project_id,
            project_name=project_name,
            total_tasks=total_tasks,
            critical_path_tasks=critical_path_tasks,
            project_duration_days=project_duration_days,
            has_schedule_data=has_schedule_data,
            warnings=warnings,
            schedule_last_computed=schedule_last_computed,
            schedule_last_modified=schedule_last_modified,
        )


        output_project_schedule.additional_properties = d
        return output_project_schedule

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
