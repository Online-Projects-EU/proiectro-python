from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.output_work_item_type import OutputWorkItemType


T = TypeVar("T", bound="OutputWorkItemTypes")


@_attrs_define
class OutputWorkItemTypes:
    """List of work item types

    Attributes:
        work_item_types (list[OutputWorkItemType]):
    """

    work_item_types: list[OutputWorkItemType]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        work_item_types = []
        for work_item_types_item_data in self.work_item_types:
            work_item_types_item = work_item_types_item_data.to_dict()
            work_item_types.append(work_item_types_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "work_item_types": work_item_types,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.output_work_item_type import OutputWorkItemType

        d = dict(src_dict)
        work_item_types = []
        _work_item_types = d.pop("work_item_types")
        for work_item_types_item_data in _work_item_types:
            work_item_types_item = OutputWorkItemType.from_dict(
                work_item_types_item_data
            )

            work_item_types.append(work_item_types_item)

        output_work_item_types = cls(
            work_item_types=work_item_types,
        )

        output_work_item_types.additional_properties = d
        return output_work_item_types

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
