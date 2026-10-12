from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.my_ticket_item import MyTicketItem


T = TypeVar("T", bound="OutputMyTickets")


@_attrs_define
class OutputMyTickets:
    """Cross-tenant support tickets assigned to the current user

    Attributes:
        tickets (list[MyTicketItem]):
        total_count (int):
        internal_count (int):
        external_count (int):
    """

    tickets: list[MyTicketItem]
    total_count: int
    internal_count: int
    external_count: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        tickets = []
        for tickets_item_data in self.tickets:
            tickets_item = tickets_item_data.to_dict()
            tickets.append(tickets_item)

        total_count = self.total_count

        internal_count = self.internal_count

        external_count = self.external_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "tickets": tickets,
                "total_count": total_count,
                "internal_count": internal_count,
                "external_count": external_count,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.my_ticket_item import MyTicketItem

        d = dict(src_dict)
        tickets = []
        _tickets = d.pop("tickets")
        for tickets_item_data in _tickets:
            tickets_item = MyTicketItem.from_dict(tickets_item_data)

            tickets.append(tickets_item)

        total_count = d.pop("total_count")

        internal_count = d.pop("internal_count")

        external_count = d.pop("external_count")

        output_my_tickets = cls(
            tickets=tickets,
            total_count=total_count,
            internal_count=internal_count,
            external_count=external_count,
        )

        output_my_tickets.additional_properties = d
        return output_my_tickets

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
