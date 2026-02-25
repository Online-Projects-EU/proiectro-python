from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.guide_step import GuideStep


T = TypeVar("T", bound="GuideCampaign")


@_attrs_define
class GuideCampaign:
    """A guidance campaign with progress information.

    Attributes:
        code (str):
        name (str):
        description (str):
        type_ (str):
        priority (int):
        presentation (str):
        placement (str):
        dismissible (bool):
        completion_percentage (int):
        steps (list[GuideStep]):
    """

    code: str
    name: str
    description: str
    type_: str
    priority: int
    presentation: str
    placement: str
    dismissible: bool
    completion_percentage: int
    steps: list[GuideStep]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        code = self.code

        name = self.name

        description = self.description

        type_ = self.type_

        priority = self.priority

        presentation = self.presentation

        placement = self.placement

        dismissible = self.dismissible

        completion_percentage = self.completion_percentage

        steps = []
        for steps_item_data in self.steps:
            steps_item = steps_item_data.to_dict()
            steps.append(steps_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "code": code,
                "name": name,
                "description": description,
                "type": type_,
                "priority": priority,
                "presentation": presentation,
                "placement": placement,
                "dismissible": dismissible,
                "completion_percentage": completion_percentage,
                "steps": steps,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.guide_step import GuideStep

        d = dict(src_dict)
        code = d.pop("code")

        name = d.pop("name")

        description = d.pop("description")

        type_ = d.pop("type")

        priority = d.pop("priority")

        presentation = d.pop("presentation")

        placement = d.pop("placement")

        dismissible = d.pop("dismissible")

        completion_percentage = d.pop("completion_percentage")

        steps = []
        _steps = d.pop("steps")
        for steps_item_data in _steps:
            steps_item = GuideStep.from_dict(steps_item_data)

            steps.append(steps_item)

        guide_campaign = cls(
            code=code,
            name=name,
            description=description,
            type_=type_,
            priority=priority,
            presentation=presentation,
            placement=placement,
            dismissible=dismissible,
            completion_percentage=completion_percentage,
            steps=steps,
        )

        guide_campaign.additional_properties = d
        return guide_campaign

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
