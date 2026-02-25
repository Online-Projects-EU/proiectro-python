from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.output_team_member_booking_heatmap_data import (
        OutputTeamMemberBookingHeatmapData,
    )
    from ..models.output_team_member_booking_heatmap_week_labels import (
        OutputTeamMemberBookingHeatmapWeekLabels,
    )


T = TypeVar("T", bound="OutputTeamMemberBookingHeatmap")


@_attrs_define
class OutputTeamMemberBookingHeatmap:
    """Heatmap data for team member bookings in a project

    Shows three metrics per cell:
    - activity: Actual logged work hours from WorkLog records
    - booking: Allocated hours from TeamBooking (cumulative if overlapping)
    - availability: Weekly availability hours from Availability records (+1 bonus if > 0)

        Attributes:
            team_member_id (str):
            team_member_name (str):
            project_id (str):
            project_name (str):
            total_weeks (int):
            weeks (list[str]):
            week_labels (OutputTeamMemberBookingHeatmapWeekLabels):
            data (OutputTeamMemberBookingHeatmapData):
            total_bookings (int):
            avg_activity (float):
            avg_booking (float):
            avg_availability (float):
            has_booking_data (bool):
            has_effort_data (bool):
            earliest_booking_date (None | str | Unset):
            latest_booking_date (None | str | Unset):
            weekdays (list[int] | Unset):
    """

    team_member_id: str
    team_member_name: str
    project_id: str
    project_name: str
    total_weeks: int
    weeks: list[str]
    week_labels: OutputTeamMemberBookingHeatmapWeekLabels
    data: OutputTeamMemberBookingHeatmapData
    total_bookings: int
    avg_activity: float
    avg_booking: float
    avg_availability: float
    has_booking_data: bool
    has_effort_data: bool
    earliest_booking_date: None | str | Unset = UNSET
    latest_booking_date: None | str | Unset = UNSET
    weekdays: list[int] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        team_member_id = self.team_member_id

        team_member_name = self.team_member_name

        project_id = self.project_id

        project_name = self.project_name

        total_weeks = self.total_weeks

        weeks = self.weeks

        week_labels = self.week_labels.to_dict()

        data = self.data.to_dict()

        total_bookings = self.total_bookings

        avg_activity = self.avg_activity

        avg_booking = self.avg_booking

        avg_availability = self.avg_availability

        has_booking_data = self.has_booking_data

        has_effort_data = self.has_effort_data

        earliest_booking_date: None | str | Unset
        if isinstance(self.earliest_booking_date, Unset):
            earliest_booking_date = UNSET
        else:
            earliest_booking_date = self.earliest_booking_date

        latest_booking_date: None | str | Unset
        if isinstance(self.latest_booking_date, Unset):
            latest_booking_date = UNSET
        else:
            latest_booking_date = self.latest_booking_date

        weekdays: list[int] | Unset = UNSET
        if not isinstance(self.weekdays, Unset):
            weekdays = self.weekdays

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "team_member_id": team_member_id,
                "team_member_name": team_member_name,
                "project_id": project_id,
                "project_name": project_name,
                "total_weeks": total_weeks,
                "weeks": weeks,
                "week_labels": week_labels,
                "data": data,
                "total_bookings": total_bookings,
                "avg_activity": avg_activity,
                "avg_booking": avg_booking,
                "avg_availability": avg_availability,
                "has_booking_data": has_booking_data,
                "has_effort_data": has_effort_data,
            }
        )
        if earliest_booking_date is not UNSET:
            field_dict["earliest_booking_date"] = earliest_booking_date
        if latest_booking_date is not UNSET:
            field_dict["latest_booking_date"] = latest_booking_date
        if weekdays is not UNSET:
            field_dict["weekdays"] = weekdays

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.output_team_member_booking_heatmap_data import (
            OutputTeamMemberBookingHeatmapData,
        )
        from ..models.output_team_member_booking_heatmap_week_labels import (
            OutputTeamMemberBookingHeatmapWeekLabels,
        )

        d = dict(src_dict)
        team_member_id = d.pop("team_member_id")

        team_member_name = d.pop("team_member_name")

        project_id = d.pop("project_id")

        project_name = d.pop("project_name")

        total_weeks = d.pop("total_weeks")

        weeks = cast(list[str], d.pop("weeks"))

        week_labels = OutputTeamMemberBookingHeatmapWeekLabels.from_dict(
            d.pop("week_labels")
        )

        data = OutputTeamMemberBookingHeatmapData.from_dict(d.pop("data"))

        total_bookings = d.pop("total_bookings")

        avg_activity = d.pop("avg_activity")

        avg_booking = d.pop("avg_booking")

        avg_availability = d.pop("avg_availability")

        has_booking_data = d.pop("has_booking_data")

        has_effort_data = d.pop("has_effort_data")

        def _parse_earliest_booking_date(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        earliest_booking_date = _parse_earliest_booking_date(
            d.pop("earliest_booking_date", UNSET)
        )

        def _parse_latest_booking_date(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        latest_booking_date = _parse_latest_booking_date(
            d.pop("latest_booking_date", UNSET)
        )

        weekdays = cast(list[int], d.pop("weekdays", UNSET))

        output_team_member_booking_heatmap = cls(
            team_member_id=team_member_id,
            team_member_name=team_member_name,
            project_id=project_id,
            project_name=project_name,
            total_weeks=total_weeks,
            weeks=weeks,
            week_labels=week_labels,
            data=data,
            total_bookings=total_bookings,
            avg_activity=avg_activity,
            avg_booking=avg_booking,
            avg_availability=avg_availability,
            has_booking_data=has_booking_data,
            has_effort_data=has_effort_data,
            earliest_booking_date=earliest_booking_date,
            latest_booking_date=latest_booking_date,
            weekdays=weekdays,
        )

        output_team_member_booking_heatmap.additional_properties = d
        return output_team_member_booking_heatmap

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
