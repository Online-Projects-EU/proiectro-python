from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TenantFunnelConfigurationStage")


@_attrs_define
class TenantFunnelConfigurationStage:
    """
    Attributes:
        id (str):
        sequence (str):
        name (str):
        description (str):
        is_active (bool):
        stage_type (str):
        transitions (list[str] | None | Unset):
    """

    id: str
    sequence: str
    name: str
    description: str
    is_active: bool
    stage_type: str
    transitions: list[str] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        sequence = self.sequence

        name = self.name

        description = self.description

        is_active = self.is_active

        stage_type = self.stage_type

        transitions: list[str] | None | Unset
        if isinstance(self.transitions, Unset):
            transitions = UNSET
        elif isinstance(self.transitions, list):
            transitions = self.transitions

        else:
            transitions = self.transitions

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "sequence": sequence,
                "name": name,
                "description": description,
                "is_active": is_active,
                "stage_type": stage_type,
            }
        )
        if transitions is not UNSET:
            field_dict["transitions"] = transitions

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        sequence = d.pop("sequence")

        name = d.pop("name")

        description = d.pop("description")

        is_active = d.pop("is_active")

        stage_type = d.pop("stage_type")

        def _parse_transitions(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                transitions_type_0 = cast(list[str], data)

                return transitions_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        transitions = _parse_transitions(d.pop("transitions", UNSET))

        tenant_funnel_configuration_stage = cls(
            id=id,
            sequence=sequence,
            name=name,
            description=description,
            is_active=is_active,
            stage_type=stage_type,
            transitions=transitions,
        )

        tenant_funnel_configuration_stage.additional_properties = d
        return tenant_funnel_configuration_stage

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
