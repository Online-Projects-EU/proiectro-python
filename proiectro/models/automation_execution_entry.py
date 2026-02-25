from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.automation_action_log_entry import AutomationActionLogEntry


T = TypeVar("T", bound="AutomationExecutionEntry")


@_attrs_define
class AutomationExecutionEntry:
    """A single execution log entry.

    Attributes:
        id (str):
        event_id (str):
        event_type (str):
        created_at (str):
        action_count (int | Unset):  Default: 0.
        success_count (int | Unset):  Default: 0.
        failure_count (int | Unset):  Default: 0.
        duration_ms (int | None | Unset):
        action_logs (list[AutomationActionLogEntry] | Unset):
    """

    id: str
    event_id: str
    event_type: str
    created_at: str
    action_count: int | Unset = 0
    success_count: int | Unset = 0
    failure_count: int | Unset = 0
    duration_ms: int | None | Unset = UNSET
    action_logs: list[AutomationActionLogEntry] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        event_id = self.event_id

        event_type = self.event_type

        created_at = self.created_at

        action_count = self.action_count

        success_count = self.success_count

        failure_count = self.failure_count

        duration_ms: int | None | Unset
        if isinstance(self.duration_ms, Unset):
            duration_ms = UNSET
        else:
            duration_ms = self.duration_ms

        action_logs: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.action_logs, Unset):
            action_logs = []
            for action_logs_item_data in self.action_logs:
                action_logs_item = action_logs_item_data.to_dict()
                action_logs.append(action_logs_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "event_id": event_id,
                "event_type": event_type,
                "created_at": created_at,
            }
        )
        if action_count is not UNSET:
            field_dict["action_count"] = action_count
        if success_count is not UNSET:
            field_dict["success_count"] = success_count
        if failure_count is not UNSET:
            field_dict["failure_count"] = failure_count
        if duration_ms is not UNSET:
            field_dict["duration_ms"] = duration_ms
        if action_logs is not UNSET:
            field_dict["action_logs"] = action_logs

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.automation_action_log_entry import AutomationActionLogEntry

        d = dict(src_dict)
        id = d.pop("id")

        event_id = d.pop("event_id")

        event_type = d.pop("event_type")

        created_at = d.pop("created_at")

        action_count = d.pop("action_count", UNSET)

        success_count = d.pop("success_count", UNSET)

        failure_count = d.pop("failure_count", UNSET)

        def _parse_duration_ms(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        duration_ms = _parse_duration_ms(d.pop("duration_ms", UNSET))

        _action_logs = d.pop("action_logs", UNSET)
        action_logs: list[AutomationActionLogEntry] | Unset = UNSET
        if _action_logs is not UNSET:
            action_logs = []
            for action_logs_item_data in _action_logs:
                action_logs_item = AutomationActionLogEntry.from_dict(
                    action_logs_item_data
                )

                action_logs.append(action_logs_item)

        automation_execution_entry = cls(
            id=id,
            event_id=event_id,
            event_type=event_type,
            created_at=created_at,
            action_count=action_count,
            success_count=success_count,
            failure_count=failure_count,
            duration_ms=duration_ms,
            action_logs=action_logs,
        )

        automation_execution_entry.additional_properties = d
        return automation_execution_entry

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
