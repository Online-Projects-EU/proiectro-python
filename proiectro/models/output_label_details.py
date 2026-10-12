from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.labeled_entity_stats import LabeledEntityStats


T = TypeVar("T", bound="OutputLabelDetails")


@_attrs_define
class OutputLabelDetails:
    """
    Attributes:
        label_id (str):
        label_name (str):
        security (bool):
        entity_stats (list[LabeledEntityStats]):
        total_usage_count (int):
    """

    label_id: str
    label_name: str
    security: bool
    entity_stats: list[LabeledEntityStats]
    total_usage_count: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        label_id = self.label_id

        label_name = self.label_name

        security = self.security

        entity_stats = []
        for entity_stats_item_data in self.entity_stats:
            entity_stats_item = entity_stats_item_data.to_dict()
            entity_stats.append(entity_stats_item)

        total_usage_count = self.total_usage_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "label_id": label_id,
                "label_name": label_name,
                "security": security,
                "entity_stats": entity_stats,
                "total_usage_count": total_usage_count,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.labeled_entity_stats import LabeledEntityStats

        d = dict(src_dict)
        label_id = d.pop("label_id")

        label_name = d.pop("label_name")

        security = d.pop("security")

        entity_stats = []
        _entity_stats = d.pop("entity_stats")
        for entity_stats_item_data in _entity_stats:
            entity_stats_item = LabeledEntityStats.from_dict(entity_stats_item_data)

            entity_stats.append(entity_stats_item)

        total_usage_count = d.pop("total_usage_count")

        output_label_details = cls(
            label_id=label_id,
            label_name=label_name,
            security=security,
            entity_stats=entity_stats,
            total_usage_count=total_usage_count,
        )

        output_label_details.additional_properties = d
        return output_label_details

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
