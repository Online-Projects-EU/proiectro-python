from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.output_label import OutputLabel


T = TypeVar("T", bound="OutputResourceLabels")


@_attrs_define
class OutputResourceLabels:
    """
    Attributes:
        resource (str):
        labels (list[OutputLabel]):
    """

    resource: str
    labels: list[OutputLabel]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        resource = self.resource

        labels = []
        for labels_item_data in self.labels:
            labels_item = labels_item_data.to_dict()
            labels.append(labels_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "resource": resource,
                "labels": labels,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.output_label import OutputLabel

        d = dict(src_dict)
        resource = d.pop("resource")

        labels = []
        _labels = d.pop("labels")
        for labels_item_data in _labels:
            labels_item = OutputLabel.from_dict(labels_item_data)

            labels.append(labels_item)

        output_resource_labels = cls(
            resource=resource,
            labels=labels,
        )

        output_resource_labels.additional_properties = d
        return output_resource_labels

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
