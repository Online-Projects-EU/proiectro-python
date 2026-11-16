from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.output_lead_history_entry import OutputLeadHistoryEntry


T = TypeVar("T", bound="OutputLeadHistory")


@_attrs_define
class OutputLeadHistory:
    """A lead's statuses and sales activities in one timeline, newest first.

    Attributes:
        lead_id (str):
        lead_name (str):
        history (list[OutputLeadHistoryEntry]):
        total_duration_days (int | Unset):  Default: 0.
    """

    lead_id: str
    lead_name: str
    history: list[OutputLeadHistoryEntry]
    total_duration_days: int | Unset = 0
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        lead_id = self.lead_id

        lead_name = self.lead_name

        history = []
        for history_item_data in self.history:
            history_item = history_item_data.to_dict()
            history.append(history_item)

        total_duration_days = self.total_duration_days

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "lead_id": lead_id,
                "lead_name": lead_name,
                "history": history,
            }
        )
        if total_duration_days is not UNSET:
            field_dict["total_duration_days"] = total_duration_days

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.output_lead_history_entry import OutputLeadHistoryEntry

        d = dict(src_dict)
        lead_id = d.pop("lead_id")

        lead_name = d.pop("lead_name")

        history = []
        _history = d.pop("history")
        for history_item_data in _history:
            history_item = OutputLeadHistoryEntry.from_dict(history_item_data)

            history.append(history_item)

        total_duration_days = d.pop("total_duration_days", UNSET)

        output_lead_history = cls(
            lead_id=lead_id,
            lead_name=lead_name,
            history=history,
            total_duration_days=total_duration_days,
        )

        output_lead_history.additional_properties = d
        return output_lead_history

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
