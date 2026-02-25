from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.sales_feed_activity import SalesFeedActivity


T = TypeVar("T", bound="SalesActivityFeed")


@_attrs_define
class SalesActivityFeed:
    """
    Attributes:
        activities (list[SalesFeedActivity]):
        per_page (int):
        next_page (int):
        node_type (str):
        node_id (str):
    """

    activities: list[SalesFeedActivity]
    per_page: int
    next_page: int
    node_type: str
    node_id: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        activities = []
        for activities_item_data in self.activities:
            activities_item = activities_item_data.to_dict()
            activities.append(activities_item)

        per_page = self.per_page

        next_page = self.next_page

        node_type = self.node_type

        node_id = self.node_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "activities": activities,
                "per_page": per_page,
                "next_page": next_page,
                "node_type": node_type,
                "node_id": node_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.sales_feed_activity import SalesFeedActivity

        d = dict(src_dict)
        activities = []
        _activities = d.pop("activities")
        for activities_item_data in _activities:
            activities_item = SalesFeedActivity.from_dict(activities_item_data)

            activities.append(activities_item)

        per_page = d.pop("per_page")

        next_page = d.pop("next_page")

        node_type = d.pop("node_type")

        node_id = d.pop("node_id")

        sales_activity_feed = cls(
            activities=activities,
            per_page=per_page,
            next_page=next_page,
            node_type=node_type,
            node_id=node_id,
        )

        sales_activity_feed.additional_properties = d
        return sales_activity_feed

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
