from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.proposal_list_item import ProposalListItem


T = TypeVar("T", bound="OutputProposalList")


@_attrs_define
class OutputProposalList:
    """
    Attributes:
        proposals (list[ProposalListItem]):
        node_type (str):
        node_id (str):
        node_name (str):
        total_internal_cost (float | str):
        total_external_value (float | str):
        currency (str):
        currency_symbol (str):
        empty_message (str):
        total_count (int):
    """

    proposals: list[ProposalListItem]
    node_type: str
    node_id: str
    node_name: str
    total_internal_cost: float | str
    total_external_value: float | str
    currency: str
    currency_symbol: str
    empty_message: str
    total_count: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        proposals = []
        for proposals_item_data in self.proposals:
            proposals_item = proposals_item_data.to_dict()
            proposals.append(proposals_item)

        node_type = self.node_type

        node_id = self.node_id

        node_name = self.node_name

        total_internal_cost: float | str
        total_internal_cost = self.total_internal_cost

        total_external_value: float | str
        total_external_value = self.total_external_value

        currency = self.currency

        currency_symbol = self.currency_symbol

        empty_message = self.empty_message

        total_count = self.total_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "proposals": proposals,
                "node_type": node_type,
                "node_id": node_id,
                "node_name": node_name,
                "total_internal_cost": total_internal_cost,
                "total_external_value": total_external_value,
                "currency": currency,
                "currency_symbol": currency_symbol,
                "empty_message": empty_message,
                "total_count": total_count,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.proposal_list_item import ProposalListItem

        d = dict(src_dict)
        proposals = []
        _proposals = d.pop("proposals")
        for proposals_item_data in _proposals:
            proposals_item = ProposalListItem.from_dict(proposals_item_data)

            proposals.append(proposals_item)

        node_type = d.pop("node_type")

        node_id = d.pop("node_id")

        node_name = d.pop("node_name")

        def _parse_total_internal_cost(data: object) -> float | str:
            return cast(float | str, data)

        total_internal_cost = _parse_total_internal_cost(d.pop("total_internal_cost"))

        def _parse_total_external_value(data: object) -> float | str:
            return cast(float | str, data)

        total_external_value = _parse_total_external_value(
            d.pop("total_external_value")
        )

        currency = d.pop("currency")

        currency_symbol = d.pop("currency_symbol")

        empty_message = d.pop("empty_message")

        total_count = d.pop("total_count")

        output_proposal_list = cls(
            proposals=proposals,
            node_type=node_type,
            node_id=node_id,
            node_name=node_name,
            total_internal_cost=total_internal_cost,
            total_external_value=total_external_value,
            currency=currency,
            currency_symbol=currency_symbol,
            empty_message=empty_message,
            total_count=total_count,
        )

        output_proposal_list.additional_properties = d
        return output_proposal_list

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
