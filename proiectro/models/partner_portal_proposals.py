from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.partner_portal_proposal_item import PartnerPortalProposalItem


T = TypeVar("T", bound="PartnerPortalProposals")


@_attrs_define
class PartnerPortalProposals:
    """Partner's proposals visible through bridge

    Attributes:
        bridge_id (str):
        partner_tenant_name (str):
        proposals (list[PartnerPortalProposalItem]):
        grant_given_by_partner (bool | Unset):  Default: True.
        grant_label (None | str | Unset):
    """

    bridge_id: str
    partner_tenant_name: str
    proposals: list[PartnerPortalProposalItem]
    grant_given_by_partner: bool | Unset = True
    grant_label: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bridge_id = self.bridge_id

        partner_tenant_name = self.partner_tenant_name

        proposals = []
        for proposals_item_data in self.proposals:
            proposals_item = proposals_item_data.to_dict()
            proposals.append(proposals_item)

        grant_given_by_partner = self.grant_given_by_partner

        grant_label: None | str | Unset
        if isinstance(self.grant_label, Unset):
            grant_label = UNSET
        else:
            grant_label = self.grant_label

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "bridge_id": bridge_id,
                "partner_tenant_name": partner_tenant_name,
                "proposals": proposals,
            }
        )
        if grant_given_by_partner is not UNSET:
            field_dict["grant_given_by_partner"] = grant_given_by_partner
        if grant_label is not UNSET:
            field_dict["grant_label"] = grant_label

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.partner_portal_proposal_item import PartnerPortalProposalItem

        d = dict(src_dict)
        bridge_id = d.pop("bridge_id")

        partner_tenant_name = d.pop("partner_tenant_name")

        proposals = []
        _proposals = d.pop("proposals")
        for proposals_item_data in _proposals:
            proposals_item = PartnerPortalProposalItem.from_dict(proposals_item_data)

            proposals.append(proposals_item)

        grant_given_by_partner = d.pop("grant_given_by_partner", UNSET)

        def _parse_grant_label(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        grant_label = _parse_grant_label(d.pop("grant_label", UNSET))

        partner_portal_proposals = cls(
            bridge_id=bridge_id,
            partner_tenant_name=partner_tenant_name,
            proposals=proposals,
            grant_given_by_partner=grant_given_by_partner,
            grant_label=grant_label,
        )

        partner_portal_proposals.additional_properties = d
        return partner_portal_proposals

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
