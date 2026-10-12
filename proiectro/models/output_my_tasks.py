from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.output_operational_item import OutputOperationalItem


T = TypeVar("T", bound="OutputMyTasks")


@_attrs_define
class OutputMyTasks:
    """
    Attributes:
        pending_approval (list[OutputOperationalItem]):
        active (list[OutputOperationalItem]):
        pending_approval_count (int | Unset):  Default: 0.
        active_count (int | Unset):  Default: 0.
    """

    pending_approval: list[OutputOperationalItem]
    active: list[OutputOperationalItem]
    pending_approval_count: int | Unset = 0
    active_count: int | Unset = 0
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        pending_approval = []
        for pending_approval_item_data in self.pending_approval:
            pending_approval_item = pending_approval_item_data.to_dict()
            pending_approval.append(pending_approval_item)

        active = []
        for active_item_data in self.active:
            active_item = active_item_data.to_dict()
            active.append(active_item)

        pending_approval_count = self.pending_approval_count

        active_count = self.active_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "pending_approval": pending_approval,
                "active": active,
            }
        )
        if pending_approval_count is not UNSET:
            field_dict["pending_approval_count"] = pending_approval_count
        if active_count is not UNSET:
            field_dict["active_count"] = active_count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.output_operational_item import OutputOperationalItem

        d = dict(src_dict)
        pending_approval = []
        _pending_approval = d.pop("pending_approval")
        for pending_approval_item_data in _pending_approval:
            pending_approval_item = OutputOperationalItem.from_dict(
                pending_approval_item_data
            )

            pending_approval.append(pending_approval_item)

        active = []
        _active = d.pop("active")
        for active_item_data in _active:
            active_item = OutputOperationalItem.from_dict(active_item_data)

            active.append(active_item)

        pending_approval_count = d.pop("pending_approval_count", UNSET)

        active_count = d.pop("active_count", UNSET)

        output_my_tasks = cls(
            pending_approval=pending_approval,
            active=active,
            pending_approval_count=pending_approval_count,
            active_count=active_count,
        )

        output_my_tasks.additional_properties = d
        return output_my_tasks

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
