from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="KPIQueueHealthSummary")



@_attrs_define
class KPIQueueHealthSummary:
    """ 
        Attributes:
            description (str | Unset):  Default: ''.
            queue_count (str | Unset):  Default: '0'.
            total_open_tickets (str | Unset):  Default: '0'.
            total_unassigned (str | Unset):  Default: '0'.
            busiest_queue (str | Unset):  Default: ''.
            busiest_queue_count (str | Unset):  Default: '0'.
     """

    description: str | Unset = ''
    queue_count: str | Unset = '0'
    total_open_tickets: str | Unset = '0'
    total_unassigned: str | Unset = '0'
    busiest_queue: str | Unset = ''
    busiest_queue_count: str | Unset = '0'
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        description = self.description

        queue_count = self.queue_count

        total_open_tickets = self.total_open_tickets

        total_unassigned = self.total_unassigned

        busiest_queue = self.busiest_queue

        busiest_queue_count = self.busiest_queue_count


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if description is not UNSET:
            field_dict["description"] = description
        if queue_count is not UNSET:
            field_dict["queueCount"] = queue_count
        if total_open_tickets is not UNSET:
            field_dict["totalOpenTickets"] = total_open_tickets
        if total_unassigned is not UNSET:
            field_dict["totalUnassigned"] = total_unassigned
        if busiest_queue is not UNSET:
            field_dict["busiestQueue"] = busiest_queue
        if busiest_queue_count is not UNSET:
            field_dict["busiestQueueCount"] = busiest_queue_count

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        description = d.pop("description", UNSET)

        queue_count = d.pop("queueCount", UNSET)

        total_open_tickets = d.pop("totalOpenTickets", UNSET)

        total_unassigned = d.pop("totalUnassigned", UNSET)

        busiest_queue = d.pop("busiestQueue", UNSET)

        busiest_queue_count = d.pop("busiestQueueCount", UNSET)

        kpi_queue_health_summary = cls(
            description=description,
            queue_count=queue_count,
            total_open_tickets=total_open_tickets,
            total_unassigned=total_unassigned,
            busiest_queue=busiest_queue,
            busiest_queue_count=busiest_queue_count,
        )


        kpi_queue_health_summary.additional_properties = d
        return kpi_queue_health_summary

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
