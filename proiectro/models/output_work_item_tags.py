from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.output_tag import OutputTag


T = TypeVar("T", bound="OutputWorkItemTags")


@_attrs_define
class OutputWorkItemTags:
    """
    Attributes:
        work_item (str):
        tags (list[OutputTag]):
        unassigned_tags (list[OutputTag]):
        has_project (bool):
    """

    work_item: str
    tags: list[OutputTag]
    unassigned_tags: list[OutputTag]
    has_project: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        work_item = self.work_item

        tags = []
        for tags_item_data in self.tags:
            tags_item = tags_item_data.to_dict()
            tags.append(tags_item)

        unassigned_tags = []
        for unassigned_tags_item_data in self.unassigned_tags:
            unassigned_tags_item = unassigned_tags_item_data.to_dict()
            unassigned_tags.append(unassigned_tags_item)

        has_project = self.has_project

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "work_item": work_item,
                "tags": tags,
                "unassigned_tags": unassigned_tags,
                "has_project": has_project,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.output_tag import OutputTag

        d = dict(src_dict)
        work_item = d.pop("work_item")

        tags = []
        _tags = d.pop("tags")
        for tags_item_data in _tags:
            tags_item = OutputTag.from_dict(tags_item_data)

            tags.append(tags_item)

        unassigned_tags = []
        _unassigned_tags = d.pop("unassigned_tags")
        for unassigned_tags_item_data in _unassigned_tags:
            unassigned_tags_item = OutputTag.from_dict(unassigned_tags_item_data)

            unassigned_tags.append(unassigned_tags_item)

        has_project = d.pop("has_project")

        output_work_item_tags = cls(
            work_item=work_item,
            tags=tags,
            unassigned_tags=unassigned_tags,
            has_project=has_project,
        )

        output_work_item_tags.additional_properties = d
        return output_work_item_tags

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
