from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.automation_action import AutomationAction
    from ..models.template_variable import TemplateVariable


T = TypeVar("T", bound="AutomationActionsResponse")


@_attrs_define
class AutomationActionsResponse:
    """Output: list of available actions from the registry.

    Attributes:
        actions (list[AutomationAction]):
        template_vars (list[TemplateVariable] | Unset):
    """

    actions: list[AutomationAction]
    template_vars: list[TemplateVariable] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        actions = []
        for actions_item_data in self.actions:
            actions_item = actions_item_data.to_dict()
            actions.append(actions_item)

        template_vars: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.template_vars, Unset):
            template_vars = []
            for template_vars_item_data in self.template_vars:
                template_vars_item = template_vars_item_data.to_dict()
                template_vars.append(template_vars_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "actions": actions,
            }
        )
        if template_vars is not UNSET:
            field_dict["template_vars"] = template_vars

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.automation_action import AutomationAction
        from ..models.template_variable import TemplateVariable

        d = dict(src_dict)
        actions = []
        _actions = d.pop("actions")
        for actions_item_data in _actions:
            actions_item = AutomationAction.from_dict(actions_item_data)

            actions.append(actions_item)

        _template_vars = d.pop("template_vars", UNSET)
        template_vars: list[TemplateVariable] | Unset = UNSET
        if _template_vars is not UNSET:
            template_vars = []
            for template_vars_item_data in _template_vars:
                template_vars_item = TemplateVariable.from_dict(template_vars_item_data)

                template_vars.append(template_vars_item)

        automation_actions_response = cls(
            actions=actions,
            template_vars=template_vars,
        )

        automation_actions_response.additional_properties = d
        return automation_actions_response

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
