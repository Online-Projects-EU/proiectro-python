from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.output_support_request_queue import OutputSupportRequestQueue


T = TypeVar("T", bound="OutputSupportRequestQueues")


@_attrs_define
class OutputSupportRequestQueues:
    """Output schema for listing support request queues

    Attributes:
        external_queues (list[OutputSupportRequestQueue]):
        internal_queues (list[OutputSupportRequestQueue]):
        total_external_queues (int):
        total_internal_queues (int):
        total_queues (int):
        assigned_open_count (int):
    """

    external_queues: list[OutputSupportRequestQueue]
    internal_queues: list[OutputSupportRequestQueue]
    total_external_queues: int
    total_internal_queues: int
    total_queues: int
    assigned_open_count: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        external_queues = []
        for external_queues_item_data in self.external_queues:
            external_queues_item = external_queues_item_data.to_dict()
            external_queues.append(external_queues_item)

        internal_queues = []
        for internal_queues_item_data in self.internal_queues:
            internal_queues_item = internal_queues_item_data.to_dict()
            internal_queues.append(internal_queues_item)

        total_external_queues = self.total_external_queues

        total_internal_queues = self.total_internal_queues

        total_queues = self.total_queues

        assigned_open_count = self.assigned_open_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "external_queues": external_queues,
                "internal_queues": internal_queues,
                "total_external_queues": total_external_queues,
                "total_internal_queues": total_internal_queues,
                "total_queues": total_queues,
                "assigned_open_count": assigned_open_count,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.output_support_request_queue import OutputSupportRequestQueue

        d = dict(src_dict)
        external_queues = []
        _external_queues = d.pop("external_queues")
        for external_queues_item_data in _external_queues:
            external_queues_item = OutputSupportRequestQueue.from_dict(
                external_queues_item_data
            )

            external_queues.append(external_queues_item)

        internal_queues = []
        _internal_queues = d.pop("internal_queues")
        for internal_queues_item_data in _internal_queues:
            internal_queues_item = OutputSupportRequestQueue.from_dict(
                internal_queues_item_data
            )

            internal_queues.append(internal_queues_item)

        total_external_queues = d.pop("total_external_queues")

        total_internal_queues = d.pop("total_internal_queues")

        total_queues = d.pop("total_queues")

        assigned_open_count = d.pop("assigned_open_count")

        output_support_request_queues = cls(
            external_queues=external_queues,
            internal_queues=internal_queues,
            total_external_queues=total_external_queues,
            total_internal_queues=total_internal_queues,
            total_queues=total_queues,
            assigned_open_count=assigned_open_count,
        )

        output_support_request_queues.additional_properties = d
        return output_support_request_queues

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
