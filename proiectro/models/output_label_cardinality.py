from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.label_value_stats import LabelValueStats


T = TypeVar("T", bound="OutputLabelCardinality")


@_attrs_define
class OutputLabelCardinality:
    """
    Attributes:
        label_id (str):
        label_name (str):
        total_entities (int):
        cardinality (int):
        value_distribution (list[LabelValueStats]):
    """

    label_id: str
    label_name: str
    total_entities: int
    cardinality: int
    value_distribution: list[LabelValueStats]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        label_id = self.label_id

        label_name = self.label_name

        total_entities = self.total_entities

        cardinality = self.cardinality

        value_distribution = []
        for value_distribution_item_data in self.value_distribution:
            value_distribution_item = value_distribution_item_data.to_dict()
            value_distribution.append(value_distribution_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "label_id": label_id,
                "label_name": label_name,
                "total_entities": total_entities,
                "cardinality": cardinality,
                "value_distribution": value_distribution,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.label_value_stats import LabelValueStats

        d = dict(src_dict)
        label_id = d.pop("label_id")

        label_name = d.pop("label_name")

        total_entities = d.pop("total_entities")

        cardinality = d.pop("cardinality")

        value_distribution = []
        _value_distribution = d.pop("value_distribution")
        for value_distribution_item_data in _value_distribution:
            value_distribution_item = LabelValueStats.from_dict(
                value_distribution_item_data
            )

            value_distribution.append(value_distribution_item)

        output_label_cardinality = cls(
            label_id=label_id,
            label_name=label_name,
            total_entities=total_entities,
            cardinality=cardinality,
            value_distribution=value_distribution,
        )

        output_label_cardinality.additional_properties = d
        return output_label_cardinality

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
