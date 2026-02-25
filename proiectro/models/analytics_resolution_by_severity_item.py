from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="AnalyticsResolutionBySeverityItem")


@_attrs_define
class AnalyticsResolutionBySeverityItem:
    """Resolution time by severity

    Attributes:
        severity (str):
        ticket_type (str):
        count (int):
        avg_resolution_hours (float | str):
    """

    severity: str
    ticket_type: str
    count: int
    avg_resolution_hours: float | str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        severity = self.severity

        ticket_type = self.ticket_type

        count = self.count

        avg_resolution_hours: float | str
        avg_resolution_hours = self.avg_resolution_hours

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "severity": severity,
                "ticket_type": ticket_type,
                "count": count,
                "avg_resolution_hours": avg_resolution_hours,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        severity = d.pop("severity")

        ticket_type = d.pop("ticket_type")

        count = d.pop("count")

        def _parse_avg_resolution_hours(data: object) -> float | str:
            return cast(float | str, data)

        avg_resolution_hours = _parse_avg_resolution_hours(
            d.pop("avg_resolution_hours")
        )

        analytics_resolution_by_severity_item = cls(
            severity=severity,
            ticket_type=ticket_type,
            count=count,
            avg_resolution_hours=avg_resolution_hours,
        )

        analytics_resolution_by_severity_item.additional_properties = d
        return analytics_resolution_by_severity_item

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
