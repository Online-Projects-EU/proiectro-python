from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.wbs_config_reference import WBSConfigReference


T = TypeVar("T", bound="OutputWorkItemType")


@_attrs_define
class OutputWorkItemType:
    """Individual work item type details

    Attributes:
        id (str):
        name (str):
        description (str):
        active (bool):
        scheduling_behaviour (str):
        scheduling_behaviour_display (str):
        scheduling_behaviour_description (str):
        wbs_configurations (list[WBSConfigReference] | Unset):
    """

    id: str
    name: str
    description: str
    active: bool
    scheduling_behaviour: str
    scheduling_behaviour_display: str
    scheduling_behaviour_description: str
    wbs_configurations: list[WBSConfigReference] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        description = self.description

        active = self.active

        scheduling_behaviour = self.scheduling_behaviour

        scheduling_behaviour_display = self.scheduling_behaviour_display

        scheduling_behaviour_description = self.scheduling_behaviour_description

        wbs_configurations: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.wbs_configurations, Unset):
            wbs_configurations = []
            for wbs_configurations_item_data in self.wbs_configurations:
                wbs_configurations_item = wbs_configurations_item_data.to_dict()
                wbs_configurations.append(wbs_configurations_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "description": description,
                "active": active,
                "scheduling_behaviour": scheduling_behaviour,
                "scheduling_behaviour_display": scheduling_behaviour_display,
                "scheduling_behaviour_description": scheduling_behaviour_description,
            }
        )
        if wbs_configurations is not UNSET:
            field_dict["wbs_configurations"] = wbs_configurations

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.wbs_config_reference import WBSConfigReference

        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        description = d.pop("description")

        active = d.pop("active")

        scheduling_behaviour = d.pop("scheduling_behaviour")

        scheduling_behaviour_display = d.pop("scheduling_behaviour_display")

        scheduling_behaviour_description = d.pop("scheduling_behaviour_description")

        _wbs_configurations = d.pop("wbs_configurations", UNSET)
        wbs_configurations: list[WBSConfigReference] | Unset = UNSET
        if _wbs_configurations is not UNSET:
            wbs_configurations = []
            for wbs_configurations_item_data in _wbs_configurations:
                wbs_configurations_item = WBSConfigReference.from_dict(
                    wbs_configurations_item_data
                )

                wbs_configurations.append(wbs_configurations_item)

        output_work_item_type = cls(
            id=id,
            name=name,
            description=description,
            active=active,
            scheduling_behaviour=scheduling_behaviour,
            scheduling_behaviour_display=scheduling_behaviour_display,
            scheduling_behaviour_description=scheduling_behaviour_description,
            wbs_configurations=wbs_configurations,
        )

        output_work_item_type.additional_properties = d
        return output_work_item_type

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
