from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="KPIExpiringWarrantiesSummary")



@_attrs_define
class KPIExpiringWarrantiesSummary:
    """ 
        Attributes:
            description (str | Unset):  Default: ''.
            count (str | Unset):  Default: '0'.
            customer_count (str | Unset):  Default: '0'.
            expiring_this_week (str | Unset):  Default: '0'.
     """

    description: str | Unset = ''
    count: str | Unset = '0'
    customer_count: str | Unset = '0'
    expiring_this_week: str | Unset = '0'
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        description = self.description

        count = self.count

        customer_count = self.customer_count

        expiring_this_week = self.expiring_this_week


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if description is not UNSET:
            field_dict["description"] = description
        if count is not UNSET:
            field_dict["count"] = count
        if customer_count is not UNSET:
            field_dict["customerCount"] = customer_count
        if expiring_this_week is not UNSET:
            field_dict["expiringThisWeek"] = expiring_this_week

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        description = d.pop("description", UNSET)

        count = d.pop("count", UNSET)

        customer_count = d.pop("customerCount", UNSET)

        expiring_this_week = d.pop("expiringThisWeek", UNSET)

        kpi_expiring_warranties_summary = cls(
            description=description,
            count=count,
            customer_count=customer_count,
            expiring_this_week=expiring_this_week,
        )


        kpi_expiring_warranties_summary.additional_properties = d
        return kpi_expiring_warranties_summary

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
