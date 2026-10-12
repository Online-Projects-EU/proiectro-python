from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.resource_cost_type import ResourceCostType


T = TypeVar("T", bound="ResourceCostTypes")


@_attrs_define
class ResourceCostTypes:
    """
    Attributes:
        resource (str):
        cost_types (list[ResourceCostType]):
    """

    resource: str
    cost_types: list[ResourceCostType]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        resource = self.resource

        cost_types = []
        for cost_types_item_data in self.cost_types:
            cost_types_item = cost_types_item_data.to_dict()
            cost_types.append(cost_types_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "resource": resource,
                "cost_types": cost_types,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.resource_cost_type import ResourceCostType

        d = dict(src_dict)
        resource = d.pop("resource")

        cost_types = []
        _cost_types = d.pop("cost_types")
        for cost_types_item_data in _cost_types:
            cost_types_item = ResourceCostType.from_dict(cost_types_item_data)

            cost_types.append(cost_types_item)

        resource_cost_types = cls(
            resource=resource,
            cost_types=cost_types,
        )

        resource_cost_types.additional_properties = d
        return resource_cost_types

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
