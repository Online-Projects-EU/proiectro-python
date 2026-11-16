from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.lead_milestone_rate import LeadMilestoneRate


T = TypeVar("T", bound="AnalyticsSalesLeadsRow")


@_attrs_define
class AnalyticsSalesLeadsRow:
    """What the leads of one list, or from one source, produced.

    Attributes:
        key (str):
        name (str):
        contacted (int):
        replied (LeadMilestoneRate): How many of the contacted leads reached a milestone, as a count and as a share with
            its likely range.
        qualified (LeadMilestoneRate): How many of the contacted leads reached a milestone, as a count and as a share
            with its likely range.
        opportunity (LeadMilestoneRate): How many of the contacted leads reached a milestone, as a count and as a share
            with its likely range.
    """

    key: str
    name: str
    contacted: int
    replied: LeadMilestoneRate
    qualified: LeadMilestoneRate
    opportunity: LeadMilestoneRate
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        key = self.key

        name = self.name

        contacted = self.contacted

        replied = self.replied.to_dict()

        qualified = self.qualified.to_dict()

        opportunity = self.opportunity.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "key": key,
                "name": name,
                "contacted": contacted,
                "replied": replied,
                "qualified": qualified,
                "opportunity": opportunity,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.lead_milestone_rate import LeadMilestoneRate

        d = dict(src_dict)
        key = d.pop("key")

        name = d.pop("name")

        contacted = d.pop("contacted")

        replied = LeadMilestoneRate.from_dict(d.pop("replied"))

        qualified = LeadMilestoneRate.from_dict(d.pop("qualified"))

        opportunity = LeadMilestoneRate.from_dict(d.pop("opportunity"))

        analytics_sales_leads_row = cls(
            key=key,
            name=name,
            contacted=contacted,
            replied=replied,
            qualified=qualified,
            opportunity=opportunity,
        )

        analytics_sales_leads_row.additional_properties = d
        return analytics_sales_leads_row

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
