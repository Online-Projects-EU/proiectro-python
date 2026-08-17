from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="KPIUpcomingPaymentsSummary")



@_attrs_define
class KPIUpcomingPaymentsSummary:
    """ 
        Attributes:
            description (str | Unset):  Default: ''.
            count (str | Unset):  Default: '0'.
            total_amount (str | Unset):  Default: '0'.
            due_this_week (str | Unset):  Default: '0'.
     """

    description: str | Unset = ''
    count: str | Unset = '0'
    total_amount: str | Unset = '0'
    due_this_week: str | Unset = '0'
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        description = self.description

        count = self.count

        total_amount = self.total_amount

        due_this_week = self.due_this_week


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if description is not UNSET:
            field_dict["description"] = description
        if count is not UNSET:
            field_dict["count"] = count
        if total_amount is not UNSET:
            field_dict["totalAmount"] = total_amount
        if due_this_week is not UNSET:
            field_dict["dueThisWeek"] = due_this_week

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        description = d.pop("description", UNSET)

        count = d.pop("count", UNSET)

        total_amount = d.pop("totalAmount", UNSET)

        due_this_week = d.pop("dueThisWeek", UNSET)

        kpi_upcoming_payments_summary = cls(
            description=description,
            count=count,
            total_amount=total_amount,
            due_this_week=due_this_week,
        )


        kpi_upcoming_payments_summary.additional_properties = d
        return kpi_upcoming_payments_summary

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
