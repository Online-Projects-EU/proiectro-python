from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.key_project_activity_item import KeyProjectActivityItem


T = TypeVar("T", bound="OutputKeyProjectActivities")


@_attrs_define
class OutputKeyProjectActivities:
    """List of key project activities based on schedule management setting

    Attributes:
        activities (list[KeyProjectActivityItem]):
        project_id (str):
        project_name (str):
        total_activities (int):
        schedule_mode (bool):
    """

    activities: list[KeyProjectActivityItem]
    project_id: str
    project_name: str
    total_activities: int
    schedule_mode: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        activities = []
        for activities_item_data in self.activities:
            activities_item = activities_item_data.to_dict()
            activities.append(activities_item)

        project_id = self.project_id

        project_name = self.project_name

        total_activities = self.total_activities

        schedule_mode = self.schedule_mode

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "activities": activities,
                "project_id": project_id,
                "project_name": project_name,
                "total_activities": total_activities,
                "schedule_mode": schedule_mode,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.key_project_activity_item import KeyProjectActivityItem

        d = dict(src_dict)
        activities = []
        _activities = d.pop("activities")
        for activities_item_data in _activities:
            activities_item = KeyProjectActivityItem.from_dict(activities_item_data)

            activities.append(activities_item)

        project_id = d.pop("project_id")

        project_name = d.pop("project_name")

        total_activities = d.pop("total_activities")

        schedule_mode = d.pop("schedule_mode")

        output_key_project_activities = cls(
            activities=activities,
            project_id=project_id,
            project_name=project_name,
            total_activities=total_activities,
            schedule_mode=schedule_mode,
        )

        output_key_project_activities.additional_properties = d
        return output_key_project_activities

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
