from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.automation_action_log_entry_output_type_0 import AutomationActionLogEntryOutputType0





T = TypeVar("T", bound="AutomationActionLogEntry")



@_attrs_define
class AutomationActionLogEntry:
    """ A single action execution within an automation run.

        Attributes:
            action_type (str):
            status (str | Unset):  Default: 'failure'.
            error_message (str | Unset):  Default: ''.
            output (AutomationActionLogEntryOutputType0 | None | Unset):
            fan_out_index (int | None | Unset):
     """

    action_type: str
    status: str | Unset = 'failure'
    error_message: str | Unset = ''
    output: AutomationActionLogEntryOutputType0 | None | Unset = UNSET
    fan_out_index: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.automation_action_log_entry_output_type_0 import AutomationActionLogEntryOutputType0
        action_type = self.action_type

        status = self.status

        error_message = self.error_message

        output: dict[str, Any] | None | Unset
        if isinstance(self.output, Unset):
            output = UNSET
        elif isinstance(self.output, AutomationActionLogEntryOutputType0):
            output = self.output.to_dict()
        else:
            output = self.output

        fan_out_index: int | None | Unset
        if isinstance(self.fan_out_index, Unset):
            fan_out_index = UNSET
        else:
            fan_out_index = self.fan_out_index


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "action_type": action_type,
        })
        if status is not UNSET:
            field_dict["status"] = status
        if error_message is not UNSET:
            field_dict["error_message"] = error_message
        if output is not UNSET:
            field_dict["output"] = output
        if fan_out_index is not UNSET:
            field_dict["fan_out_index"] = fan_out_index

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.automation_action_log_entry_output_type_0 import AutomationActionLogEntryOutputType0
        d = dict(src_dict)
        action_type = d.pop("action_type")

        status = d.pop("status", UNSET)

        error_message = d.pop("error_message", UNSET)

        def _parse_output(data: object) -> AutomationActionLogEntryOutputType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                output_type_0 = AutomationActionLogEntryOutputType0.from_dict(data)



                return output_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(AutomationActionLogEntryOutputType0 | None | Unset, data)

        output = _parse_output(d.pop("output", UNSET))


        def _parse_fan_out_index(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        fan_out_index = _parse_fan_out_index(d.pop("fan_out_index", UNSET))


        automation_action_log_entry = cls(
            action_type=action_type,
            status=status,
            error_message=error_message,
            output=output,
            fan_out_index=fan_out_index,
        )


        automation_action_log_entry.additional_properties = d
        return automation_action_log_entry

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
