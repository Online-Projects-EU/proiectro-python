from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AnalyticsTeamWorkloadItem")


@_attrs_define
class AnalyticsTeamWorkloadItem:
    """Workload for a single team member

    Attributes:
        remaining_hours (float):
        pending_items (int):
        overdue_items (int):
        status (str):
        member_id (None | str | Unset):
        member_name (None | str | Unset):
        booked_capacity (float | None | Unset):
        utilization_pct (float | None | Unset):
    """

    remaining_hours: float
    pending_items: int
    overdue_items: int
    status: str
    member_id: None | str | Unset = UNSET
    member_name: None | str | Unset = UNSET
    booked_capacity: float | None | Unset = UNSET
    utilization_pct: float | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        remaining_hours = self.remaining_hours

        pending_items = self.pending_items

        overdue_items = self.overdue_items

        status = self.status

        member_id: None | str | Unset
        if isinstance(self.member_id, Unset):
            member_id = UNSET
        else:
            member_id = self.member_id

        member_name: None | str | Unset
        if isinstance(self.member_name, Unset):
            member_name = UNSET
        else:
            member_name = self.member_name

        booked_capacity: float | None | Unset
        if isinstance(self.booked_capacity, Unset):
            booked_capacity = UNSET
        else:
            booked_capacity = self.booked_capacity

        utilization_pct: float | None | Unset
        if isinstance(self.utilization_pct, Unset):
            utilization_pct = UNSET
        else:
            utilization_pct = self.utilization_pct

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "remaining_hours": remaining_hours,
                "pending_items": pending_items,
                "overdue_items": overdue_items,
                "status": status,
            }
        )
        if member_id is not UNSET:
            field_dict["member_id"] = member_id
        if member_name is not UNSET:
            field_dict["member_name"] = member_name
        if booked_capacity is not UNSET:
            field_dict["booked_capacity"] = booked_capacity
        if utilization_pct is not UNSET:
            field_dict["utilization_pct"] = utilization_pct

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        remaining_hours = d.pop("remaining_hours")

        pending_items = d.pop("pending_items")

        overdue_items = d.pop("overdue_items")

        status = d.pop("status")

        def _parse_member_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        member_id = _parse_member_id(d.pop("member_id", UNSET))

        def _parse_member_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        member_name = _parse_member_name(d.pop("member_name", UNSET))

        def _parse_booked_capacity(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        booked_capacity = _parse_booked_capacity(d.pop("booked_capacity", UNSET))

        def _parse_utilization_pct(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        utilization_pct = _parse_utilization_pct(d.pop("utilization_pct", UNSET))

        analytics_team_workload_item = cls(
            remaining_hours=remaining_hours,
            pending_items=pending_items,
            overdue_items=overdue_items,
            status=status,
            member_id=member_id,
            member_name=member_name,
            booked_capacity=booked_capacity,
            utilization_pct=utilization_pct,
        )

        analytics_team_workload_item.additional_properties = d
        return analytics_team_workload_item

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
