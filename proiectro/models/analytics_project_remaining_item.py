from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AnalyticsProjectRemainingItem")


@_attrs_define
class AnalyticsProjectRemainingItem:
    """Remaining work for a single project

    Attributes:
        project_id (str):
        project_name (str):
        remaining_hours (float):
        pending_items (int):
        overdue_items (int):
        progress_pct (float):
        customer_name (None | str | Unset):
    """

    project_id: str
    project_name: str
    remaining_hours: float
    pending_items: int
    overdue_items: int
    progress_pct: float
    customer_name: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        project_id = self.project_id

        project_name = self.project_name

        remaining_hours = self.remaining_hours

        pending_items = self.pending_items

        overdue_items = self.overdue_items

        progress_pct = self.progress_pct

        customer_name: None | str | Unset
        if isinstance(self.customer_name, Unset):
            customer_name = UNSET
        else:
            customer_name = self.customer_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "project_id": project_id,
                "project_name": project_name,
                "remaining_hours": remaining_hours,
                "pending_items": pending_items,
                "overdue_items": overdue_items,
                "progress_pct": progress_pct,
            }
        )
        if customer_name is not UNSET:
            field_dict["customer_name"] = customer_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        project_id = d.pop("project_id")

        project_name = d.pop("project_name")

        remaining_hours = d.pop("remaining_hours")

        pending_items = d.pop("pending_items")

        overdue_items = d.pop("overdue_items")

        progress_pct = d.pop("progress_pct")

        def _parse_customer_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        customer_name = _parse_customer_name(d.pop("customer_name", UNSET))

        analytics_project_remaining_item = cls(
            project_id=project_id,
            project_name=project_name,
            remaining_hours=remaining_hours,
            pending_items=pending_items,
            overdue_items=overdue_items,
            progress_pct=progress_pct,
            customer_name=customer_name,
        )

        analytics_project_remaining_item.additional_properties = d
        return analytics_project_remaining_item

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
