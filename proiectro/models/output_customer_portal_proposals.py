from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.output_customer_portal_proposals_org import (
        OutputCustomerPortalProposalsOrg,
    )
    from ..models.output_customer_portal_proposals_proposals_item import (
        OutputCustomerPortalProposalsProposalsItem,
    )


T = TypeVar("T", bound="OutputCustomerPortalProposals")


@_attrs_define
class OutputCustomerPortalProposals:
    """Customer portal proposals view with individual costs

    Attributes:
        proposals (list[OutputCustomerPortalProposalsProposalsItem]):
        currency_symbol (str):
        org (OutputCustomerPortalProposalsOrg):
    """

    proposals: list[OutputCustomerPortalProposalsProposalsItem]
    currency_symbol: str
    org: OutputCustomerPortalProposalsOrg
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        proposals = []
        for proposals_item_data in self.proposals:
            proposals_item = proposals_item_data.to_dict()
            proposals.append(proposals_item)

        currency_symbol = self.currency_symbol

        org = self.org.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "proposals": proposals,
                "currency_symbol": currency_symbol,
                "org": org,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.output_customer_portal_proposals_org import (
            OutputCustomerPortalProposalsOrg,
        )
        from ..models.output_customer_portal_proposals_proposals_item import (
            OutputCustomerPortalProposalsProposalsItem,
        )

        d = dict(src_dict)
        proposals = []
        _proposals = d.pop("proposals")
        for proposals_item_data in _proposals:
            proposals_item = OutputCustomerPortalProposalsProposalsItem.from_dict(
                proposals_item_data
            )

            proposals.append(proposals_item)

        currency_symbol = d.pop("currency_symbol")

        org = OutputCustomerPortalProposalsOrg.from_dict(d.pop("org"))

        output_customer_portal_proposals = cls(
            proposals=proposals,
            currency_symbol=currency_symbol,
            org=org,
        )

        output_customer_portal_proposals.additional_properties = d
        return output_customer_portal_proposals

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
