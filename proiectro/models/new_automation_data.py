from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.automation_action_input import AutomationActionInput
    from ..models.automation_filter import AutomationFilter
    from ..models.automation_rule_info import AutomationRuleInfo


T = TypeVar("T", bound="NewAutomationData")


@_attrs_define
class NewAutomationData:
    """The full payload for creating a new automation rule.

    Attributes:
        event (str):
        filters (list[AutomationFilter]):
        actions (list[AutomationActionInput]):
        automation (AutomationRuleInfo): The name and active state of a rule.
    """

    event: str
    filters: list[AutomationFilter]
    actions: list[AutomationActionInput]
    automation: AutomationRuleInfo
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        event = self.event

        filters = []
        for filters_item_data in self.filters:
            filters_item = filters_item_data.to_dict()
            filters.append(filters_item)

        actions = []
        for actions_item_data in self.actions:
            actions_item = actions_item_data.to_dict()
            actions.append(actions_item)

        automation = self.automation.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "event": event,
                "filters": filters,
                "actions": actions,
                "automation": automation,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.automation_action_input import AutomationActionInput
        from ..models.automation_filter import AutomationFilter
        from ..models.automation_rule_info import AutomationRuleInfo

        d = dict(src_dict)
        event = d.pop("event")

        filters = []
        _filters = d.pop("filters")
        for filters_item_data in _filters:
            filters_item = AutomationFilter.from_dict(filters_item_data)

            filters.append(filters_item)

        actions = []
        _actions = d.pop("actions")
        for actions_item_data in _actions:
            actions_item = AutomationActionInput.from_dict(actions_item_data)

            actions.append(actions_item)

        automation = AutomationRuleInfo.from_dict(d.pop("automation"))

        new_automation_data = cls(
            event=event,
            filters=filters,
            actions=actions,
            automation=automation,
        )

        new_automation_data.additional_properties = d
        return new_automation_data

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
