from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.active_proposal_item import ActiveProposalItem


T = TypeVar("T", bound="ActiveProposalsList")


@_attrs_define
class ActiveProposalsList:
    """List of active proposals for projects view

    Attributes:
        proposals (list[ActiveProposalItem]):
        total_count (int):
    """

    proposals: list[ActiveProposalItem]
    total_count: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        proposals = []
        for proposals_item_data in self.proposals:
            proposals_item = proposals_item_data.to_dict()
            proposals.append(proposals_item)

        total_count = self.total_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "proposals": proposals,
                "total_count": total_count,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.active_proposal_item import ActiveProposalItem

        d = dict(src_dict)
        proposals = []
        _proposals = d.pop("proposals")
        for proposals_item_data in _proposals:
            proposals_item = ActiveProposalItem.from_dict(proposals_item_data)

            proposals.append(proposals_item)

        total_count = d.pop("total_count")

        active_proposals_list = cls(
            proposals=proposals,
            total_count=total_count,
        )

        active_proposals_list.additional_properties = d
        return active_proposals_list

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
