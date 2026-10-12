from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="TenantWBSConfiguration")


@_attrs_define
class TenantWBSConfiguration:
    """
    Attributes:
        id (str):
        name (str):
        active (bool):
        description (str):
        rules (int):
        default_for_new_projects (bool):
    """

    id: str
    name: str
    active: bool
    description: str
    rules: int
    default_for_new_projects: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        active = self.active

        description = self.description

        rules = self.rules

        default_for_new_projects = self.default_for_new_projects

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "active": active,
                "description": description,
                "rules": rules,
                "default_for_new_projects": default_for_new_projects,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        active = d.pop("active")

        description = d.pop("description")

        rules = d.pop("rules")

        default_for_new_projects = d.pop("default_for_new_projects")

        tenant_wbs_configuration = cls(
            id=id,
            name=name,
            active=active,
            description=description,
            rules=rules,
            default_for_new_projects=default_for_new_projects,
        )

        tenant_wbs_configuration.additional_properties = d
        return tenant_wbs_configuration

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
