from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.my_work_item import MyWorkItem


T = TypeVar("T", bound="OutputMyWorkItems")


@_attrs_define
class OutputMyWorkItems:
    """Cross-tenant work items assigned to the current user

    Attributes:
        work_items (list[MyWorkItem]):
        total_count (int):
        overdue_count (int):
        due_today_count (int):
        due_this_week_count (int):
        upcoming_count (int):
        no_date_count (int):
    """

    work_items: list[MyWorkItem]
    total_count: int
    overdue_count: int
    due_today_count: int
    due_this_week_count: int
    upcoming_count: int
    no_date_count: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        work_items = []
        for work_items_item_data in self.work_items:
            work_items_item = work_items_item_data.to_dict()
            work_items.append(work_items_item)

        total_count = self.total_count

        overdue_count = self.overdue_count

        due_today_count = self.due_today_count

        due_this_week_count = self.due_this_week_count

        upcoming_count = self.upcoming_count

        no_date_count = self.no_date_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "work_items": work_items,
                "total_count": total_count,
                "overdue_count": overdue_count,
                "due_today_count": due_today_count,
                "due_this_week_count": due_this_week_count,
                "upcoming_count": upcoming_count,
                "no_date_count": no_date_count,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.my_work_item import MyWorkItem

        d = dict(src_dict)
        work_items = []
        _work_items = d.pop("work_items")
        for work_items_item_data in _work_items:
            work_items_item = MyWorkItem.from_dict(work_items_item_data)

            work_items.append(work_items_item)

        total_count = d.pop("total_count")

        overdue_count = d.pop("overdue_count")

        due_today_count = d.pop("due_today_count")

        due_this_week_count = d.pop("due_this_week_count")

        upcoming_count = d.pop("upcoming_count")

        no_date_count = d.pop("no_date_count")

        output_my_work_items = cls(
            work_items=work_items,
            total_count=total_count,
            overdue_count=overdue_count,
            due_today_count=due_today_count,
            due_this_week_count=due_this_week_count,
            upcoming_count=upcoming_count,
            no_date_count=no_date_count,
        )

        output_my_work_items.additional_properties = d
        return output_my_work_items

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
