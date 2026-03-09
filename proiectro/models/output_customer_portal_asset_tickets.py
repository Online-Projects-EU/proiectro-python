from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.output_customer_portal_asset_tickets_org import (
        OutputCustomerPortalAssetTicketsOrg,
    )
    from ..models.output_customer_portal_asset_tickets_tickets_item import (
        OutputCustomerPortalAssetTicketsTicketsItem,
    )


T = TypeVar("T", bound="OutputCustomerPortalAssetTickets")


@_attrs_define
class OutputCustomerPortalAssetTickets:
    """Customer portal asset linked tickets (ESRs with reported_asset)

    Attributes:
        tickets (list[OutputCustomerPortalAssetTicketsTicketsItem]):
        asset_id (str):
        org (OutputCustomerPortalAssetTicketsOrg):
    """

    tickets: list[OutputCustomerPortalAssetTicketsTicketsItem]
    asset_id: str
    org: OutputCustomerPortalAssetTicketsOrg
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        tickets = []
        for tickets_item_data in self.tickets:
            tickets_item = tickets_item_data.to_dict()
            tickets.append(tickets_item)

        asset_id = self.asset_id

        org = self.org.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "tickets": tickets,
                "asset_id": asset_id,
                "org": org,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.output_customer_portal_asset_tickets_org import (
            OutputCustomerPortalAssetTicketsOrg,
        )
        from ..models.output_customer_portal_asset_tickets_tickets_item import (
            OutputCustomerPortalAssetTicketsTicketsItem,
        )

        d = dict(src_dict)
        tickets = []
        _tickets = d.pop("tickets")
        for tickets_item_data in _tickets:
            tickets_item = OutputCustomerPortalAssetTicketsTicketsItem.from_dict(
                tickets_item_data
            )

            tickets.append(tickets_item)

        asset_id = d.pop("asset_id")

        org = OutputCustomerPortalAssetTicketsOrg.from_dict(d.pop("org"))

        output_customer_portal_asset_tickets = cls(
            tickets=tickets,
            asset_id=asset_id,
            org=org,
        )

        output_customer_portal_asset_tickets.additional_properties = d
        return output_customer_portal_asset_tickets

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
