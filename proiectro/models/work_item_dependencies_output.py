from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.dependency_item import DependencyItem


T = TypeVar("T", bound="WorkItemDependenciesOutput")


@_attrs_define
class WorkItemDependenciesOutput:
    """Output for displaying work item dependencies grouped by predecessors/successors

    Attributes:
        predecessors (list[DependencyItem]):
        successors (list[DependencyItem]):
        dependency_types (list[list[str]]):
    """

    predecessors: list[DependencyItem]
    successors: list[DependencyItem]
    dependency_types: list[list[str]]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        predecessors = []
        for predecessors_item_data in self.predecessors:
            predecessors_item = predecessors_item_data.to_dict()
            predecessors.append(predecessors_item)

        successors = []
        for successors_item_data in self.successors:
            successors_item = successors_item_data.to_dict()
            successors.append(successors_item)

        dependency_types = []
        for dependency_types_item_data in self.dependency_types:
            dependency_types_item = []
            for dependency_types_item_item_data in dependency_types_item_data:
                dependency_types_item_item: str
                dependency_types_item_item = dependency_types_item_item_data
                dependency_types_item.append(dependency_types_item_item)

            dependency_types.append(dependency_types_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "predecessors": predecessors,
                "successors": successors,
                "dependency_types": dependency_types,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dependency_item import DependencyItem

        d = dict(src_dict)
        predecessors = []
        _predecessors = d.pop("predecessors")
        for predecessors_item_data in _predecessors:
            predecessors_item = DependencyItem.from_dict(predecessors_item_data)

            predecessors.append(predecessors_item)

        successors = []
        _successors = d.pop("successors")
        for successors_item_data in _successors:
            successors_item = DependencyItem.from_dict(successors_item_data)

            successors.append(successors_item)

        dependency_types = []
        _dependency_types = d.pop("dependency_types")
        for dependency_types_item_data in _dependency_types:
            dependency_types_item = []
            _dependency_types_item = dependency_types_item_data
            for dependency_types_item_item_data in _dependency_types_item:

                def _parse_dependency_types_item_item(data: object) -> str:
                    return cast(str, data)

                dependency_types_item_item = _parse_dependency_types_item_item(
                    dependency_types_item_item_data
                )

                dependency_types_item.append(dependency_types_item_item)

            dependency_types.append(dependency_types_item)

        work_item_dependencies_output = cls(
            predecessors=predecessors,
            successors=successors,
            dependency_types=dependency_types,
        )

        work_item_dependencies_output.additional_properties = d
        return work_item_dependencies_output

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
