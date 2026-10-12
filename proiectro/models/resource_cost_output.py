from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.resource_cost_histogram import ResourceCostHistogram
    from ..models.resource_cost_record import ResourceCostRecord


T = TypeVar("T", bound="ResourceCostOutput")


@_attrs_define
class ResourceCostOutput:
    """
    Attributes:
        resource (str):
        current_record (ResourceCostRecord):
        history (list[ResourceCostRecord]):
        histogram (list[ResourceCostHistogram]):
    """

    resource: str
    current_record: ResourceCostRecord
    history: list[ResourceCostRecord]
    histogram: list[ResourceCostHistogram]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        resource = self.resource

        current_record = self.current_record.to_dict()

        history = []
        for history_item_data in self.history:
            history_item = history_item_data.to_dict()
            history.append(history_item)

        histogram = []
        for histogram_item_data in self.histogram:
            histogram_item = histogram_item_data.to_dict()
            histogram.append(histogram_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "resource": resource,
                "current_record": current_record,
                "history": history,
                "histogram": histogram,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.resource_cost_histogram import ResourceCostHistogram
        from ..models.resource_cost_record import ResourceCostRecord

        d = dict(src_dict)
        resource = d.pop("resource")

        current_record = ResourceCostRecord.from_dict(d.pop("current_record"))

        history = []
        _history = d.pop("history")
        for history_item_data in _history:
            history_item = ResourceCostRecord.from_dict(history_item_data)

            history.append(history_item)

        histogram = []
        _histogram = d.pop("histogram")
        for histogram_item_data in _histogram:
            histogram_item = ResourceCostHistogram.from_dict(histogram_item_data)

            histogram.append(histogram_item)

        resource_cost_output = cls(
            resource=resource,
            current_record=current_record,
            history=history,
            histogram=histogram,
        )

        resource_cost_output.additional_properties = d
        return resource_cost_output

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
