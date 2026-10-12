from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.tagged_entity_stats import TaggedEntityStats


T = TypeVar("T", bound="OutputTagDetails")


@_attrs_define
class OutputTagDetails:
    """
    Attributes:
        tag_id (str):
        tag_name (str):
        tag_color (str):
        entity_stats (list[TaggedEntityStats]):
        total_usage_count (int):
    """

    tag_id: str
    tag_name: str
    tag_color: str
    entity_stats: list[TaggedEntityStats]
    total_usage_count: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        tag_id = self.tag_id

        tag_name = self.tag_name

        tag_color = self.tag_color

        entity_stats = []
        for entity_stats_item_data in self.entity_stats:
            entity_stats_item = entity_stats_item_data.to_dict()
            entity_stats.append(entity_stats_item)

        total_usage_count = self.total_usage_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "tag_id": tag_id,
                "tag_name": tag_name,
                "tag_color": tag_color,
                "entity_stats": entity_stats,
                "total_usage_count": total_usage_count,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.tagged_entity_stats import TaggedEntityStats

        d = dict(src_dict)
        tag_id = d.pop("tag_id")

        tag_name = d.pop("tag_name")

        tag_color = d.pop("tag_color")

        entity_stats = []
        _entity_stats = d.pop("entity_stats")
        for entity_stats_item_data in _entity_stats:
            entity_stats_item = TaggedEntityStats.from_dict(entity_stats_item_data)

            entity_stats.append(entity_stats_item)

        total_usage_count = d.pop("total_usage_count")

        output_tag_details = cls(
            tag_id=tag_id,
            tag_name=tag_name,
            tag_color=tag_color,
            entity_stats=entity_stats,
            total_usage_count=total_usage_count,
        )

        output_tag_details.additional_properties = d
        return output_tag_details

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
