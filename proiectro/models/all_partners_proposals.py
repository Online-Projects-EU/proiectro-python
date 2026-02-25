from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.all_partners_proposal_item import AllPartnersProposalItem


T = TypeVar("T", bound="AllPartnersProposals")


@_attrs_define
class AllPartnersProposals:
    """Aggregated proposals from all active partnerships

    Attributes:
        proposals (list[AllPartnersProposalItem]):
        total (int):
    """

    proposals: list[AllPartnersProposalItem]
    total: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        proposals = []
        for proposals_item_data in self.proposals:
            proposals_item = proposals_item_data.to_dict()
            proposals.append(proposals_item)

        total = self.total

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "proposals": proposals,
                "total": total,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.all_partners_proposal_item import AllPartnersProposalItem

        d = dict(src_dict)
        proposals = []
        _proposals = d.pop("proposals")
        for proposals_item_data in _proposals:
            proposals_item = AllPartnersProposalItem.from_dict(proposals_item_data)

            proposals.append(proposals_item)

        total = d.pop("total")

        all_partners_proposals = cls(
            proposals=proposals,
            total=total,
        )

        all_partners_proposals.additional_properties = d
        return all_partners_proposals

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
