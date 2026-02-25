from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.output_stage_history_entry import OutputStageHistoryEntry


T = TypeVar("T", bound="OutputOperationalItemHistory")


@_attrs_define
class OutputOperationalItemHistory:
    """
    Attributes:
        work_item_id (str):
        entries (list[OutputStageHistoryEntry]):
        total_duration_days (int | Unset):  Default: 0.
    """

    work_item_id: str
    entries: list[OutputStageHistoryEntry]
    total_duration_days: int | Unset = 0
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        work_item_id = self.work_item_id

        entries = []
        for entries_item_data in self.entries:
            entries_item = entries_item_data.to_dict()
            entries.append(entries_item)

        total_duration_days = self.total_duration_days

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "work_item_id": work_item_id,
                "entries": entries,
            }
        )
        if total_duration_days is not UNSET:
            field_dict["total_duration_days"] = total_duration_days

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.output_stage_history_entry import OutputStageHistoryEntry

        d = dict(src_dict)
        work_item_id = d.pop("work_item_id")

        entries = []
        _entries = d.pop("entries")
        for entries_item_data in _entries:
            entries_item = OutputStageHistoryEntry.from_dict(entries_item_data)

            entries.append(entries_item)

        total_duration_days = d.pop("total_duration_days", UNSET)

        output_operational_item_history = cls(
            work_item_id=work_item_id,
            entries=entries,
            total_duration_days=total_duration_days,
        )

        output_operational_item_history.additional_properties = d
        return output_operational_item_history

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
