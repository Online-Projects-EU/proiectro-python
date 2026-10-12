from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.proposal_history_entry import ProposalHistoryEntry


T = TypeVar("T", bound="ProposalHistoryOutput")


@_attrs_define
class ProposalHistoryOutput:
    """Complete history for a proposal

    Attributes:
        proposal_id (str):
        proposal_name (str):
        customer_name (None | str):
        current_stage (str):
        history (list[ProposalHistoryEntry]):
        total_duration_days (int):
    """

    proposal_id: str
    proposal_name: str
    customer_name: None | str
    current_stage: str
    history: list[ProposalHistoryEntry]
    total_duration_days: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        proposal_id = self.proposal_id

        proposal_name = self.proposal_name

        customer_name: None | str
        customer_name = self.customer_name

        current_stage = self.current_stage

        history = []
        for history_item_data in self.history:
            history_item = history_item_data.to_dict()
            history.append(history_item)

        total_duration_days = self.total_duration_days

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "proposal_id": proposal_id,
                "proposal_name": proposal_name,
                "customer_name": customer_name,
                "current_stage": current_stage,
                "history": history,
                "total_duration_days": total_duration_days,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.proposal_history_entry import ProposalHistoryEntry

        d = dict(src_dict)
        proposal_id = d.pop("proposal_id")

        proposal_name = d.pop("proposal_name")

        def _parse_customer_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        customer_name = _parse_customer_name(d.pop("customer_name"))

        current_stage = d.pop("current_stage")

        history = []
        _history = d.pop("history")
        for history_item_data in _history:
            history_item = ProposalHistoryEntry.from_dict(history_item_data)

            history.append(history_item)

        total_duration_days = d.pop("total_duration_days")

        proposal_history_output = cls(
            proposal_id=proposal_id,
            proposal_name=proposal_name,
            customer_name=customer_name,
            current_stage=current_stage,
            history=history,
            total_duration_days=total_duration_days,
        )

        proposal_history_output.additional_properties = d
        return proposal_history_output

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
