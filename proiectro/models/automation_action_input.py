from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.automation_action_input_action_config import (
        AutomationActionInputActionConfig,
    )


T = TypeVar("T", bound="AutomationActionInput")


@_attrs_define
class AutomationActionInput:
    """An action definition within a rule.

    Attributes:
        action_type (str):
        action_config (AutomationActionInputActionConfig):
        name (None | str | Unset):
        condition (list[Any] | Unset):
        stop_on_error (bool | Unset):  Default: False.
        fan_out (bool | Unset):  Default: False.
    """

    action_type: str
    action_config: AutomationActionInputActionConfig
    name: None | str | Unset = UNSET
    condition: list[Any] | Unset = UNSET
    stop_on_error: bool | Unset = False
    fan_out: bool | Unset = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        action_type = self.action_type

        action_config = self.action_config.to_dict()

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        condition: list[Any] | Unset = UNSET
        if not isinstance(self.condition, Unset):
            condition = self.condition

        stop_on_error = self.stop_on_error

        fan_out = self.fan_out

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "action_type": action_type,
                "action_config": action_config,
            }
        )
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
        from ..models.automation_action_input_action_config import (
            AutomationActionInputActionConfig,
        )

        d = dict(src_dict)
        action_type = d.pop("action_type")

        action_config = AutomationActionInputActionConfig.from_dict(
            d.pop("action_config")
        )

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        condition = cast(list[Any], d.pop("condition", UNSET))

        stop_on_error = d.pop("stop_on_error", UNSET)

        fan_out = d.pop("fan_out", UNSET)

        automation_action_input = cls(
            action_type=action_type,
            action_config=action_config,
            name=name,
            condition=condition,
            stop_on_error=stop_on_error,
            fan_out=fan_out,
        )

        automation_action_input.additional_properties = d
        return automation_action_input

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
