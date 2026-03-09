from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.customer_asset_ticket_item import CustomerAssetTicketItem


T = TypeVar("T", bound="OutputCustomerAssetTickets")


@_attrs_define
class OutputCustomerAssetTickets:
    """Tickets linked to a customer asset (both ISR and ESR)

    Attributes:
        tickets (list[CustomerAssetTicketItem]):
        ticket_count (int):
    """

    tickets: list[CustomerAssetTicketItem]
    ticket_count: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        tickets = []
        for tickets_item_data in self.tickets:
            tickets_item = tickets_item_data.to_dict()
            tickets.append(tickets_item)

        ticket_count = self.ticket_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "tickets": tickets,
                "ticket_count": ticket_count,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.customer_asset_ticket_item import CustomerAssetTicketItem

        d = dict(src_dict)
        tickets = []
        _tickets = d.pop("tickets")
        for tickets_item_data in _tickets:
            tickets_item = CustomerAssetTicketItem.from_dict(tickets_item_data)

            tickets.append(tickets_item)

        ticket_count = d.pop("ticket_count")

        output_customer_asset_tickets = cls(
            tickets=tickets,
            ticket_count=ticket_count,
        )

        output_customer_asset_tickets.additional_properties = d
        return output_customer_asset_tickets

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
