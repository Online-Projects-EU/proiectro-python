from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="AnalyticsIssueTypeItem")


@_attrs_define
class AnalyticsIssueTypeItem:
    """Top issue type

    Attributes:
        issue_type (str):
        count (int):
        percent_of_total (float | str):
    """

    issue_type: str
    count: int
    percent_of_total: float | str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        issue_type = self.issue_type

        count = self.count

        percent_of_total: float | str
        percent_of_total = self.percent_of_total

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "issue_type": issue_type,
                "count": count,
                "percent_of_total": percent_of_total,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        issue_type = d.pop("issue_type")

        count = d.pop("count")

        def _parse_percent_of_total(data: object) -> float | str:
            return cast(float | str, data)

        percent_of_total = _parse_percent_of_total(d.pop("percent_of_total"))

        analytics_issue_type_item = cls(
            issue_type=issue_type,
            count=count,
            percent_of_total=percent_of_total,
        )

        analytics_issue_type_item.additional_properties = d
        return analytics_issue_type_item

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
