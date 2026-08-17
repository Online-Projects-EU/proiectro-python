from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="KPIRevenueAtRiskSummary")



@_attrs_define
class KPIRevenueAtRiskSummary:
    """ 
        Attributes:
            description (str | Unset):  Default: ''.
            customer_count (str | Unset):  Default: '0'.
            total_overdue_amount (str | Unset):  Default: '0'.
            total_proposal_value_at_risk (str | Unset):  Default: '0'.
            combined_at_risk (str | Unset):  Default: '0'.
     """

    description: str | Unset = ''
    customer_count: str | Unset = '0'
    total_overdue_amount: str | Unset = '0'
    total_proposal_value_at_risk: str | Unset = '0'
    combined_at_risk: str | Unset = '0'
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        description = self.description

        customer_count = self.customer_count

        total_overdue_amount = self.total_overdue_amount

        total_proposal_value_at_risk = self.total_proposal_value_at_risk

        combined_at_risk = self.combined_at_risk


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if description is not UNSET:
            field_dict["description"] = description
        if customer_count is not UNSET:
            field_dict["customerCount"] = customer_count
        if total_overdue_amount is not UNSET:
            field_dict["totalOverdueAmount"] = total_overdue_amount
        if total_proposal_value_at_risk is not UNSET:
            field_dict["totalProposalValueAtRisk"] = total_proposal_value_at_risk
        if combined_at_risk is not UNSET:
            field_dict["combinedAtRisk"] = combined_at_risk

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        description = d.pop("description", UNSET)

        customer_count = d.pop("customerCount", UNSET)

        total_overdue_amount = d.pop("totalOverdueAmount", UNSET)

        total_proposal_value_at_risk = d.pop("totalProposalValueAtRisk", UNSET)

        combined_at_risk = d.pop("combinedAtRisk", UNSET)

        kpi_revenue_at_risk_summary = cls(
            description=description,
            customer_count=customer_count,
            total_overdue_amount=total_overdue_amount,
            total_proposal_value_at_risk=total_proposal_value_at_risk,
            combined_at_risk=combined_at_risk,
        )


        kpi_revenue_at_risk_summary.additional_properties = d
        return kpi_revenue_at_risk_summary

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
