from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.automation_action_input import AutomationActionInput
    from ..models.automation_filter import AutomationFilter


T = TypeVar("T", bound="EditAutomation")


@_attrs_define
class EditAutomation:
    """Input: update an existing automation rule.

    Attributes:
        name (None | str | Unset):
        trigger_event (None | str | Unset):
        filters (list[AutomationFilter] | None | Unset):
        actions (list[AutomationActionInput] | None | Unset):
        is_active (bool | None | Unset):
    """

    name: None | str | Unset = UNSET
    trigger_event: None | str | Unset = UNSET
    filters: list[AutomationFilter] | None | Unset = UNSET
    actions: list[AutomationActionInput] | None | Unset = UNSET
    is_active: bool | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        trigger_event: None | str | Unset
        if isinstance(self.trigger_event, Unset):
            trigger_event = UNSET
        else:
            trigger_event = self.trigger_event

        filters: list[dict[str, Any]] | None | Unset
        if isinstance(self.filters, Unset):
            filters = UNSET
        elif isinstance(self.filters, list):
            filters = []
            for filters_type_0_item_data in self.filters:
                filters_type_0_item = filters_type_0_item_data.to_dict()
                filters.append(filters_type_0_item)

        else:
            filters = self.filters

        actions: list[dict[str, Any]] | None | Unset
        if isinstance(self.actions, Unset):
            actions = UNSET
        elif isinstance(self.actions, list):
            actions = []
            for actions_type_0_item_data in self.actions:
                actions_type_0_item = actions_type_0_item_data.to_dict()
                actions.append(actions_type_0_item)

        else:
            actions = self.actions

        is_active: bool | None | Unset
        if isinstance(self.is_active, Unset):
            is_active = UNSET
        else:
            is_active = self.is_active

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if trigger_event is not UNSET:
            field_dict["trigger_event"] = trigger_event
        if filters is not UNSET:
            field_dict["filters"] = filters
        if actions is not UNSET:
            field_dict["actions"] = actions
        if is_active is not UNSET:
            field_dict["is_active"] = is_active

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.automation_action_input import AutomationActionInput
        from ..models.automation_filter import AutomationFilter

        d = dict(src_dict)

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_trigger_event(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        trigger_event = _parse_trigger_event(d.pop("trigger_event", UNSET))

        def _parse_filters(data: object) -> list[AutomationFilter] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                filters_type_0 = []
                _filters_type_0 = data
                for filters_type_0_item_data in _filters_type_0:
                    filters_type_0_item = AutomationFilter.from_dict(
                        filters_type_0_item_data
                    )

                    filters_type_0.append(filters_type_0_item)

                return filters_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[AutomationFilter] | None | Unset, data)

        filters = _parse_filters(d.pop("filters", UNSET))

        def _parse_actions(data: object) -> list[AutomationActionInput] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                actions_type_0 = []
                _actions_type_0 = data
                for actions_type_0_item_data in _actions_type_0:
                    actions_type_0_item = AutomationActionInput.from_dict(
                        actions_type_0_item_data
                    )

                    actions_type_0.append(actions_type_0_item)

                return actions_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[AutomationActionInput] | None | Unset, data)

        actions = _parse_actions(d.pop("actions", UNSET))

        def _parse_is_active(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_active = _parse_is_active(d.pop("is_active", UNSET))

        edit_automation = cls(
            name=name,
            trigger_event=trigger_event,
            filters=filters,
            actions=actions,
            is_active=is_active,
        )

        edit_automation.additional_properties = d
        return edit_automation

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
