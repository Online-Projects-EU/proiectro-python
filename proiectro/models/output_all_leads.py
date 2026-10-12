from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.output_lead_summary import OutputLeadSummary


T = TypeVar("T", bound="OutputAllLeads")


@_attrs_define
class OutputAllLeads:
    """All leads in the workspace, with their total count.

    Attributes:
        leads (list[OutputLeadSummary]):
        total_count (int):
    """

    leads: list[OutputLeadSummary]
    total_count: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        leads = []
        for leads_item_data in self.leads:
            leads_item = leads_item_data.to_dict()
            leads.append(leads_item)

        total_count = self.total_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "leads": leads,
                "total_count": total_count,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.output_lead_summary import OutputLeadSummary

        d = dict(src_dict)
        leads = []
        _leads = d.pop("leads")
        for leads_item_data in _leads:
            leads_item = OutputLeadSummary.from_dict(leads_item_data)

            leads.append(leads_item)

        total_count = d.pop("total_count")

        output_all_leads = cls(
            leads=leads,
            total_count=total_count,
        )

        output_all_leads.additional_properties = d
        return output_all_leads

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
