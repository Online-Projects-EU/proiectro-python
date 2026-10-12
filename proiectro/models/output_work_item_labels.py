from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.output_label import OutputLabel


T = TypeVar("T", bound="OutputWorkItemLabels")


@_attrs_define
class OutputWorkItemLabels:
    """
    Attributes:
        work_item (str):
        labels (list[OutputLabel]):
        has_project (bool):
    """

    work_item: str
    labels: list[OutputLabel]
    has_project: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        work_item = self.work_item

        labels = []
        for labels_item_data in self.labels:
            labels_item = labels_item_data.to_dict()
            labels.append(labels_item)

        has_project = self.has_project

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "work_item": work_item,
                "labels": labels,
                "has_project": has_project,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.output_label import OutputLabel

        d = dict(src_dict)
        work_item = d.pop("work_item")

        labels = []
        _labels = d.pop("labels")
        for labels_item_data in _labels:
            labels_item = OutputLabel.from_dict(labels_item_data)

            labels.append(labels_item)

        has_project = d.pop("has_project")

        output_work_item_labels = cls(
            work_item=work_item,
            labels=labels,
            has_project=has_project,
        )

        output_work_item_labels.additional_properties = d
        return output_work_item_labels

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
