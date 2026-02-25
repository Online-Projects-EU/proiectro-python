from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

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
    """

    action_type: str
    action_config: AutomationActionInputActionConfig
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        action_type = self.action_type

        action_config = self.action_config.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "action_type": action_type,
                "action_config": action_config,
            }
        )

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

        automation_action_input = cls(
            action_type=action_type,
            action_config=action_config,
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
