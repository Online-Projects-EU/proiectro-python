from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.work_log_item import WorkLogItem


T = TypeVar("T", bound="WorkItemWorkLogsOutput")


@_attrs_define
class WorkItemWorkLogsOutput:
    """
    Attributes:
        work_logs (list[WorkLogItem]):
        total_hours (int):
        log_count (int):
        work_item_id (str):
        work_item_name (str):
        project_id (str):
    """

    work_logs: list[WorkLogItem]
    total_hours: int
    log_count: int
    work_item_id: str
    work_item_name: str
    project_id: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        work_logs = []
        for work_logs_item_data in self.work_logs:
            work_logs_item = work_logs_item_data.to_dict()
            work_logs.append(work_logs_item)

        total_hours = self.total_hours

        log_count = self.log_count

        work_item_id = self.work_item_id

        work_item_name = self.work_item_name

        project_id = self.project_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "work_logs": work_logs,
                "total_hours": total_hours,
                "log_count": log_count,
                "work_item_id": work_item_id,
                "work_item_name": work_item_name,
                "project_id": project_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.work_log_item import WorkLogItem

        d = dict(src_dict)
        work_logs = []
        _work_logs = d.pop("work_logs")
        for work_logs_item_data in _work_logs:
            work_logs_item = WorkLogItem.from_dict(work_logs_item_data)

            work_logs.append(work_logs_item)

        total_hours = d.pop("total_hours")

        log_count = d.pop("log_count")

        work_item_id = d.pop("work_item_id")

        work_item_name = d.pop("work_item_name")

        project_id = d.pop("project_id")

        work_item_work_logs_output = cls(
            work_logs=work_logs,
            total_hours=total_hours,
            log_count=log_count,
            work_item_id=work_item_id,
            work_item_name=work_item_name,
            project_id=project_id,
        )

        work_item_work_logs_output.additional_properties = d
        return work_item_work_logs_output

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
