from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.work_item_reference import WorkItemReference


T = TypeVar("T", bound="ScheduleWarning")


@_attrs_define
class ScheduleWarning:
    """Single warning from preflight checks

    Attributes:
        warning_type (str):
        severity (str):
        message (str):
        affected_count (int):
        work_items (list[WorkItemReference] | Unset):
    """

    warning_type: str
    severity: str
    message: str
    affected_count: int
    work_items: list[WorkItemReference] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        warning_type = self.warning_type

        severity = self.severity

        message = self.message

        affected_count = self.affected_count

        work_items: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.work_items, Unset):
            work_items = []
            for work_items_item_data in self.work_items:
                work_items_item = work_items_item_data.to_dict()
                work_items.append(work_items_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "warning_type": warning_type,
                "severity": severity,
                "message": message,
                "affected_count": affected_count,
            }
        )
        if work_items is not UNSET:
            field_dict["work_items"] = work_items

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.work_item_reference import WorkItemReference

        d = dict(src_dict)
        warning_type = d.pop("warning_type")

        severity = d.pop("severity")

        message = d.pop("message")

        affected_count = d.pop("affected_count")

        _work_items = d.pop("work_items", UNSET)
        work_items: list[WorkItemReference] | Unset = UNSET
        if _work_items is not UNSET:
            work_items = []
            for work_items_item_data in _work_items:
                work_items_item = WorkItemReference.from_dict(work_items_item_data)

                work_items.append(work_items_item)

        schedule_warning = cls(
            warning_type=warning_type,
            severity=severity,
            message=message,
            affected_count=affected_count,
            work_items=work_items,
        )

        schedule_warning.additional_properties = d
        return schedule_warning

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
