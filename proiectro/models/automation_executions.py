from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.automation_execution_entry import AutomationExecutionEntry


T = TypeVar("T", bound="AutomationExecutions")


@_attrs_define
class AutomationExecutions:
    """Output: execution log list for one automation rule.

    Attributes:
        executions (list[AutomationExecutionEntry]):
        total (int | Unset):  Default: 0.
    """

    executions: list[AutomationExecutionEntry]
    total: int | Unset = 0
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        executions = []
        for executions_item_data in self.executions:
            executions_item = executions_item_data.to_dict()
            executions.append(executions_item)

        total = self.total

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "executions": executions,
            }
        )
        if total is not UNSET:
            field_dict["total"] = total

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.automation_execution_entry import AutomationExecutionEntry

        d = dict(src_dict)
        executions = []
        _executions = d.pop("executions")
        for executions_item_data in _executions:
            executions_item = AutomationExecutionEntry.from_dict(executions_item_data)

            executions.append(executions_item)

        total = d.pop("total", UNSET)

        automation_executions = cls(
            executions=executions,
            total=total,
        )

        automation_executions.additional_properties = d
        return automation_executions

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
