from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.my_operational_item import MyOperationalItem


T = TypeVar("T", bound="OutputMyOperationalItems")


@_attrs_define
class OutputMyOperationalItems:
    """
    Attributes:
        approvals (list[MyOperationalItem]):
        pending_approval (list[MyOperationalItem]):
        active (list[MyOperationalItem]):
        approvals_count (int | Unset):  Default: 0.
        pending_approval_count (int | Unset):  Default: 0.
        active_count (int | Unset):  Default: 0.
    """

    approvals: list[MyOperationalItem]
    pending_approval: list[MyOperationalItem]
    active: list[MyOperationalItem]
    approvals_count: int | Unset = 0
    pending_approval_count: int | Unset = 0
    active_count: int | Unset = 0
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        approvals = []
        for approvals_item_data in self.approvals:
            approvals_item = approvals_item_data.to_dict()
            approvals.append(approvals_item)

        pending_approval = []
        for pending_approval_item_data in self.pending_approval:
            pending_approval_item = pending_approval_item_data.to_dict()
            pending_approval.append(pending_approval_item)

        active = []
        for active_item_data in self.active:
            active_item = active_item_data.to_dict()
            active.append(active_item)

        approvals_count = self.approvals_count

        pending_approval_count = self.pending_approval_count

        active_count = self.active_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "approvals": approvals,
                "pending_approval": pending_approval,
                "active": active,
            }
        )
        if approvals_count is not UNSET:
            field_dict["approvals_count"] = approvals_count
        if pending_approval_count is not UNSET:
            field_dict["pending_approval_count"] = pending_approval_count
        if active_count is not UNSET:
            field_dict["active_count"] = active_count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.my_operational_item import MyOperationalItem

        d = dict(src_dict)
        approvals = []
        _approvals = d.pop("approvals")
        for approvals_item_data in _approvals:
            approvals_item = MyOperationalItem.from_dict(approvals_item_data)

            approvals.append(approvals_item)

        pending_approval = []
        _pending_approval = d.pop("pending_approval")
        for pending_approval_item_data in _pending_approval:
            pending_approval_item = MyOperationalItem.from_dict(
                pending_approval_item_data
            )

            pending_approval.append(pending_approval_item)

        active = []
        _active = d.pop("active")
        for active_item_data in _active:
            active_item = MyOperationalItem.from_dict(active_item_data)

            active.append(active_item)

        approvals_count = d.pop("approvals_count", UNSET)

        pending_approval_count = d.pop("pending_approval_count", UNSET)

        active_count = d.pop("active_count", UNSET)

        output_my_operational_items = cls(
            approvals=approvals,
            pending_approval=pending_approval,
            active=active,
            approvals_count=approvals_count,
            pending_approval_count=pending_approval_count,
            active_count=active_count,
        )

        output_my_operational_items.additional_properties = d
        return output_my_operational_items

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
