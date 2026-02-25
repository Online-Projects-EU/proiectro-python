from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.tenant_automation_action import TenantAutomationAction


T = TypeVar("T", bound="TenantAutomation")


@_attrs_define
class TenantAutomation:
    """A single automation rule in the list.

    Attributes:
        id (str):
        name (str):
        trigger_event (None | str | Unset):
        trigger_label (None | str | Unset):
        filter_count (int | Unset):  Default: 0.
        actions (list[TenantAutomationAction] | Unset):
        is_active (bool | Unset):  Default: True.
        source (str | Unset):  Default: 'ui'.
        source_webhook_name (None | str | Unset):
    """

    id: str
    name: str
    trigger_event: None | str | Unset = UNSET
    trigger_label: None | str | Unset = UNSET
    filter_count: int | Unset = 0
    actions: list[TenantAutomationAction] | Unset = UNSET
    is_active: bool | Unset = True
    source: str | Unset = "ui"
    source_webhook_name: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        trigger_event: None | str | Unset
        if isinstance(self.trigger_event, Unset):
            trigger_event = UNSET
        else:
            trigger_event = self.trigger_event

        trigger_label: None | str | Unset
        if isinstance(self.trigger_label, Unset):
            trigger_label = UNSET
        else:
            trigger_label = self.trigger_label

        filter_count = self.filter_count

        actions: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.actions, Unset):
            actions = []
            for actions_item_data in self.actions:
                actions_item = actions_item_data.to_dict()
                actions.append(actions_item)

        is_active = self.is_active

        source = self.source

        source_webhook_name: None | str | Unset
        if isinstance(self.source_webhook_name, Unset):
            source_webhook_name = UNSET
        else:
            source_webhook_name = self.source_webhook_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
            }
        )
        if trigger_event is not UNSET:
            field_dict["trigger_event"] = trigger_event
        if trigger_label is not UNSET:
            field_dict["trigger_label"] = trigger_label
        if filter_count is not UNSET:
            field_dict["filter_count"] = filter_count
        if actions is not UNSET:
            field_dict["actions"] = actions
        if is_active is not UNSET:
            field_dict["is_active"] = is_active
        if source is not UNSET:
            field_dict["source"] = source
        if source_webhook_name is not UNSET:
            field_dict["source_webhook_name"] = source_webhook_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.tenant_automation_action import TenantAutomationAction

        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        def _parse_trigger_event(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        trigger_event = _parse_trigger_event(d.pop("trigger_event", UNSET))

        def _parse_trigger_label(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        trigger_label = _parse_trigger_label(d.pop("trigger_label", UNSET))

        filter_count = d.pop("filter_count", UNSET)

        _actions = d.pop("actions", UNSET)
        actions: list[TenantAutomationAction] | Unset = UNSET
        if _actions is not UNSET:
            actions = []
            for actions_item_data in _actions:
                actions_item = TenantAutomationAction.from_dict(actions_item_data)

                actions.append(actions_item)

        is_active = d.pop("is_active", UNSET)

        source = d.pop("source", UNSET)

        def _parse_source_webhook_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        source_webhook_name = _parse_source_webhook_name(
            d.pop("source_webhook_name", UNSET)
        )

        tenant_automation = cls(
            id=id,
            name=name,
            trigger_event=trigger_event,
            trigger_label=trigger_label,
            filter_count=filter_count,
            actions=actions,
            is_active=is_active,
            source=source,
            source_webhook_name=source_webhook_name,
        )

        tenant_automation.additional_properties = d
        return tenant_automation

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
