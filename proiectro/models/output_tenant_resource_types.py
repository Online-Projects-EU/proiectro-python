from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.output_tenant_resource_types_resources import (
        OutputTenantResourceTypesResources,
    )


T = TypeVar("T", bound="OutputTenantResourceTypes")


@_attrs_define
class OutputTenantResourceTypes:
    """
    Attributes:
        resources (OutputTenantResourceTypesResources):
        root_id (str):
    """

    resources: OutputTenantResourceTypesResources
    root_id: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        resources = self.resources.to_dict()

        root_id = self.root_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "resources": resources,
                "root_id": root_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.output_tenant_resource_types_resources import (
            OutputTenantResourceTypesResources,
        )

        d = dict(src_dict)
        resources = OutputTenantResourceTypesResources.from_dict(d.pop("resources"))

        root_id = d.pop("root_id")

        output_tenant_resource_types = cls(
            resources=resources,
            root_id=root_id,
        )

        output_tenant_resource_types.additional_properties = d
        return output_tenant_resource_types

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
