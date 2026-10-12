from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="OutputWBSConfigurationRule")


@_attrs_define
class OutputWBSConfigurationRule:
    """
    Attributes:
        id (str):
        parent_type (str):
        child_type (str):
        can_delete (bool):
        parent_scheduling (None | str | Unset):
        child_scheduling (None | str | Unset):
        blocking_templates (list[str] | None | Unset):
    """

    id: str
    parent_type: str
    child_type: str
    can_delete: bool
    parent_scheduling: None | str | Unset = UNSET
    child_scheduling: None | str | Unset = UNSET
    blocking_templates: list[str] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        parent_type = self.parent_type

        child_type = self.child_type

        can_delete = self.can_delete

        parent_scheduling: None | str | Unset
        if isinstance(self.parent_scheduling, Unset):
            parent_scheduling = UNSET
        else:
            parent_scheduling = self.parent_scheduling

        child_scheduling: None | str | Unset
        if isinstance(self.child_scheduling, Unset):
            child_scheduling = UNSET
        else:
            child_scheduling = self.child_scheduling

        blocking_templates: list[str] | None | Unset
        if isinstance(self.blocking_templates, Unset):
            blocking_templates = UNSET
        elif isinstance(self.blocking_templates, list):
            blocking_templates = self.blocking_templates

        else:
            blocking_templates = self.blocking_templates

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "parent_type": parent_type,
                "child_type": child_type,
                "can_delete": can_delete,
            }
        )
        if parent_scheduling is not UNSET:
            field_dict["parent_scheduling"] = parent_scheduling
        if child_scheduling is not UNSET:
            field_dict["child_scheduling"] = child_scheduling
        if blocking_templates is not UNSET:
            field_dict["blocking_templates"] = blocking_templates

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        parent_type = d.pop("parent_type")

        child_type = d.pop("child_type")

        can_delete = d.pop("can_delete")

        def _parse_parent_scheduling(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        parent_scheduling = _parse_parent_scheduling(d.pop("parent_scheduling", UNSET))

        def _parse_child_scheduling(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        child_scheduling = _parse_child_scheduling(d.pop("child_scheduling", UNSET))

        def _parse_blocking_templates(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                blocking_templates_type_0 = cast(list[str], data)

                return blocking_templates_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        blocking_templates = _parse_blocking_templates(
            d.pop("blocking_templates", UNSET)
        )

        output_wbs_configuration_rule = cls(
            id=id,
            parent_type=parent_type,
            child_type=child_type,
            can_delete=can_delete,
            parent_scheduling=parent_scheduling,
            child_scheduling=child_scheduling,
            blocking_templates=blocking_templates,
        )

        output_wbs_configuration_rule.additional_properties = d
        return output_wbs_configuration_rule

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
