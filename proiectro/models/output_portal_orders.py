from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.output_portal_orders_org import OutputPortalOrdersOrg
    from ..models.portal_order import PortalOrder


T = TypeVar("T", bound="OutputPortalOrders")


@_attrs_define
class OutputPortalOrders:
    """
    Attributes:
        orders (list[PortalOrder]):
        org (OutputPortalOrdersOrg):
    """

    orders: list[PortalOrder]
    org: OutputPortalOrdersOrg
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        orders = []
        for orders_item_data in self.orders:
            orders_item = orders_item_data.to_dict()
            orders.append(orders_item)

        org = self.org.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "orders": orders,
                "org": org,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.output_portal_orders_org import OutputPortalOrdersOrg
        from ..models.portal_order import PortalOrder

        d = dict(src_dict)
        orders = []
        _orders = d.pop("orders")
        for orders_item_data in _orders:
            orders_item = PortalOrder.from_dict(orders_item_data)

            orders.append(orders_item)

        org = OutputPortalOrdersOrg.from_dict(d.pop("org"))

        output_portal_orders = cls(
            orders=orders,
            org=org,
        )

        output_portal_orders.additional_properties = d
        return output_portal_orders

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
