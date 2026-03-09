from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.output_customer_location import OutputCustomerLocation


T = TypeVar("T", bound="OutputCustomerLocations")


@_attrs_define
class OutputCustomerLocations:
    """
    Attributes:
        customer_locations (list[OutputCustomerLocation]):
    """

    customer_locations: list[OutputCustomerLocation]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        customer_locations = []
        for customer_locations_item_data in self.customer_locations:
            customer_locations_item = customer_locations_item_data.to_dict()
            customer_locations.append(customer_locations_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "customer_locations": customer_locations,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.output_customer_location import OutputCustomerLocation

        d = dict(src_dict)
        customer_locations = []
        _customer_locations = d.pop("customer_locations")
        for customer_locations_item_data in _customer_locations:
            customer_locations_item = OutputCustomerLocation.from_dict(
                customer_locations_item_data
            )

            customer_locations.append(customer_locations_item)

        output_customer_locations = cls(
            customer_locations=customer_locations,
        )

        output_customer_locations.additional_properties = d
        return output_customer_locations

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
