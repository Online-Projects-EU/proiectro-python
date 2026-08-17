from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="AutomationActionConditionInput")



@_attrs_define
class AutomationActionConditionInput:
    """ Input: get condition fields for an action in the pipeline.

        Attributes:
            trigger_event (str):
            preceding_actions (list[Any] | Unset):
            action_idx (int | Unset):  Default: 0.
     """

    trigger_event: str
    preceding_actions: list[Any] | Unset = UNSET
    action_idx: int | Unset = 0
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        trigger_event = self.trigger_event

        preceding_actions: list[Any] | Unset = UNSET
        if not isinstance(self.preceding_actions, Unset):
            preceding_actions = self.preceding_actions



        action_idx = self.action_idx


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "trigger_event": trigger_event,
        })
        if preceding_actions is not UNSET:
            field_dict["preceding_actions"] = preceding_actions
        if action_idx is not UNSET:
            field_dict["action_idx"] = action_idx

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        trigger_event = d.pop("trigger_event")

        preceding_actions = cast(list[Any], d.pop("preceding_actions", UNSET))


        action_idx = d.pop("action_idx", UNSET)

        automation_action_condition_input = cls(
            trigger_event=trigger_event,
            preceding_actions=preceding_actions,
            action_idx=action_idx,
        )


        automation_action_condition_input.additional_properties = d
        return automation_action_condition_input

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
