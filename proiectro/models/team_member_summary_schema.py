from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.team_member_summary_schema_daily_data import (
        TeamMemberSummarySchemaDailyData,
    )


T = TypeVar("T", bound="TeamMemberSummarySchema")


@_attrs_define
class TeamMemberSummarySchema:
    """Team member with their weekly load data

    Attributes:
        id (str):
        name (str):
        daily_data (TeamMemberSummarySchemaDailyData):
        total_booked (float):
        total_available (float):
        total_display (str):
        load_percentage (float):
    """

    id: str
    name: str
    daily_data: TeamMemberSummarySchemaDailyData
    total_booked: float
    total_available: float
    total_display: str
    load_percentage: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        daily_data = self.daily_data.to_dict()

        total_booked = self.total_booked

        total_available = self.total_available

        total_display = self.total_display

        load_percentage = self.load_percentage

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "daily_data": daily_data,
                "total_booked": total_booked,
                "total_available": total_available,
                "total_display": total_display,
                "load_percentage": load_percentage,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.team_member_summary_schema_daily_data import (
            TeamMemberSummarySchemaDailyData,
        )

        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        daily_data = TeamMemberSummarySchemaDailyData.from_dict(d.pop("daily_data"))

        total_booked = d.pop("total_booked")

        total_available = d.pop("total_available")

        total_display = d.pop("total_display")

        load_percentage = d.pop("load_percentage")

        team_member_summary_schema = cls(
            id=id,
            name=name,
            daily_data=daily_data,
            total_booked=total_booked,
            total_available=total_available,
            total_display=total_display,
            load_percentage=load_percentage,
        )

        team_member_summary_schema.additional_properties = d
        return team_member_summary_schema

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
