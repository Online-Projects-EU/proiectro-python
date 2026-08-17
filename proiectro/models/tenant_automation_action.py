from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="TenantAutomationAction")



@_attrs_define
class TenantAutomationAction:
    """ An action within a rule, as displayed in the list.

        Attributes:
            action_type (str):
            action_name (str):
            name (str | Unset):  Default: ''.
            condition (list[Any] | Unset):
            stop_on_error (bool | Unset):  Default: False.
            fan_out (bool | Unset):  Default: False.
     """

    action_type: str
    action_name: str
    name: str | Unset = ''
    condition: list[Any] | Unset = UNSET
    stop_on_error: bool | Unset = False
    fan_out: bool | Unset = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        action_type = self.action_type

        action_name = self.action_name

        name = self.name

        condition: list[Any] | Unset = UNSET
        if not isinstance(self.condition, Unset):
            condition = self.condition



        stop_on_error = self.stop_on_error

        fan_out = self.fan_out


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "action_type": action_type,
            "action_name": action_name,
        })
        if name is not UNSET:
            field_dict["name"] = name
        if condition is not UNSET:
            field_dict["condition"] = condition
        if stop_on_error is not UNSET:
            field_dict["stop_on_error"] = stop_on_error
        if fan_out is not UNSET:
            field_dict["fan_out"] = fan_out

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        action_type = d.pop("action_type")

        action_name = d.pop("action_name")

        name = d.pop("name", UNSET)

        condition = cast(list[Any], d.pop("condition", UNSET))


        stop_on_error = d.pop("stop_on_error", UNSET)

        fan_out = d.pop("fan_out", UNSET)

        tenant_automation_action = cls(
            action_type=action_type,
            action_name=action_name,
            name=name,
            condition=condition,
            stop_on_error=stop_on_error,
            fan_out=fan_out,
        )


        tenant_automation_action.additional_properties = d
        return tenant_automation_action

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
