from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.bridge_history_entry import BridgeHistoryEntry


T = TypeVar("T", bound="BridgeHistoryOutput")


@_attrs_define
class BridgeHistoryOutput:
    """Complete audit history for a bridge

    Attributes:
        bridge_id (str):
        history (list[BridgeHistoryEntry]):
    """

    bridge_id: str
    history: list[BridgeHistoryEntry]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bridge_id = self.bridge_id

        history = []
        for history_item_data in self.history:
            history_item = history_item_data.to_dict()
            history.append(history_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "bridge_id": bridge_id,
                "history": history,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bridge_history_entry import BridgeHistoryEntry

        d = dict(src_dict)
        bridge_id = d.pop("bridge_id")

        history = []
        _history = d.pop("history")
        for history_item_data in _history:
            history_item = BridgeHistoryEntry.from_dict(history_item_data)

            history.append(history_item)

        bridge_history_output = cls(
            bridge_id=bridge_id,
            history=history,
        )

        bridge_history_output.additional_properties = d
        return bridge_history_output

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
