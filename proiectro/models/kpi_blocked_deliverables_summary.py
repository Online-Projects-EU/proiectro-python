from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="KPIBlockedDeliverablesSummary")



@_attrs_define
class KPIBlockedDeliverablesSummary:
    """ 
        Attributes:
            description (str | Unset):  Default: ''.
            count (str | Unset):  Default: '0'.
            blocked_count (str | Unset):  Default: '0'.
            customer_pending_count (str | Unset):  Default: '0'.
            rejected_count (str | Unset):  Default: '0'.
     """

    description: str | Unset = ''
    count: str | Unset = '0'
    blocked_count: str | Unset = '0'
    customer_pending_count: str | Unset = '0'
    rejected_count: str | Unset = '0'
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        description = self.description

        count = self.count

        blocked_count = self.blocked_count

        customer_pending_count = self.customer_pending_count

        rejected_count = self.rejected_count


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if description is not UNSET:
            field_dict["description"] = description
        if count is not UNSET:
            field_dict["count"] = count
        if blocked_count is not UNSET:
            field_dict["blockedCount"] = blocked_count
        if customer_pending_count is not UNSET:
            field_dict["customerPendingCount"] = customer_pending_count
        if rejected_count is not UNSET:
            field_dict["rejectedCount"] = rejected_count

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        description = d.pop("description", UNSET)

        count = d.pop("count", UNSET)

        blocked_count = d.pop("blockedCount", UNSET)

        customer_pending_count = d.pop("customerPendingCount", UNSET)

        rejected_count = d.pop("rejectedCount", UNSET)

        kpi_blocked_deliverables_summary = cls(
            description=description,
            count=count,
            blocked_count=blocked_count,
            customer_pending_count=customer_pending_count,
            rejected_count=rejected_count,
        )


        kpi_blocked_deliverables_summary.additional_properties = d
        return kpi_blocked_deliverables_summary

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
