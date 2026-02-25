from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.project_team_people_people_item import ProjectTeamPeoplePeopleItem


T = TypeVar("T", bound="ProjectTeamPeople")


@_attrs_define
class ProjectTeamPeople:
    """List of unique people working on a project

    Each person object always contains ALL possible fields:
    - member_id, member_name (always present)
    - Booking fields: total_days, booking_count, earliest_start, latest_end, has_bookings
    - Effort fields: logged_hours, log_count, has_work_logs
    - Ownership fields: owned_items, completed_items, has_owned_items

    The has_* flags indicate which data is actually present for each member.
    Use these flags in templates to conditionally display relevant data.

    Mode flags (booking_mode, effort_mode, ownership_mode) indicate which
    project features are enabled and which data sources were queried.

        Attributes:
            people (list[ProjectTeamPeoplePeopleItem]):
            project_id (str):
            project_name (str):
            total_people (int):
            booking_mode (bool):
            effort_mode (bool):
            ownership_mode (bool):
    """

    people: list[ProjectTeamPeoplePeopleItem]
    project_id: str
    project_name: str
    total_people: int
    booking_mode: bool
    effort_mode: bool
    ownership_mode: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        people = []
        for people_item_data in self.people:
            people_item = people_item_data.to_dict()
            people.append(people_item)

        project_id = self.project_id

        project_name = self.project_name

        total_people = self.total_people

        booking_mode = self.booking_mode

        effort_mode = self.effort_mode

        ownership_mode = self.ownership_mode

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "people": people,
                "project_id": project_id,
                "project_name": project_name,
                "total_people": total_people,
                "booking_mode": booking_mode,
                "effort_mode": effort_mode,
                "ownership_mode": ownership_mode,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.project_team_people_people_item import ProjectTeamPeoplePeopleItem

        d = dict(src_dict)
        people = []
        _people = d.pop("people")
        for people_item_data in _people:
            people_item = ProjectTeamPeoplePeopleItem.from_dict(people_item_data)

            people.append(people_item)

        project_id = d.pop("project_id")

        project_name = d.pop("project_name")

        total_people = d.pop("total_people")

        booking_mode = d.pop("booking_mode")

        effort_mode = d.pop("effort_mode")

        ownership_mode = d.pop("ownership_mode")

        project_team_people = cls(
            people=people,
            project_id=project_id,
            project_name=project_name,
            total_people=total_people,
            booking_mode=booking_mode,
            effort_mode=effort_mode,
            ownership_mode=ownership_mode,
        )

        project_team_people.additional_properties = d
        return project_team_people

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
