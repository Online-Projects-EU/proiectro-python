from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.output_customer_portal_assets_customer_locations_item import (
        OutputCustomerPortalAssetsCustomerLocationsItem,
    )
    from ..models.output_customer_portal_assets_org import OutputCustomerPortalAssetsOrg
    from ..models.output_customer_portal_assets_unlocated_assets_item import (
        OutputCustomerPortalAssetsUnlocatedAssetsItem,
    )


T = TypeVar("T", bound="OutputCustomerPortalAssets")


@_attrs_define
class OutputCustomerPortalAssets:
    """Customer portal assets view with customer locations and nested assets

    Attributes:
        customer_locations (list[OutputCustomerPortalAssetsCustomerLocationsItem]):
        unlocated_assets (list[OutputCustomerPortalAssetsUnlocatedAssetsItem]):
        org (OutputCustomerPortalAssetsOrg):
    """

    customer_locations: list[OutputCustomerPortalAssetsCustomerLocationsItem]
    unlocated_assets: list[OutputCustomerPortalAssetsUnlocatedAssetsItem]
    org: OutputCustomerPortalAssetsOrg
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        customer_locations = []
        for customer_locations_item_data in self.customer_locations:
            customer_locations_item = customer_locations_item_data.to_dict()
            customer_locations.append(customer_locations_item)

        unlocated_assets = []
        for unlocated_assets_item_data in self.unlocated_assets:
            unlocated_assets_item = unlocated_assets_item_data.to_dict()
            unlocated_assets.append(unlocated_assets_item)

        org = self.org.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "customer_locations": customer_locations,
                "unlocated_assets": unlocated_assets,
                "org": org,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.output_customer_portal_assets_customer_locations_item import (
            OutputCustomerPortalAssetsCustomerLocationsItem,
        )
        from ..models.output_customer_portal_assets_org import (
            OutputCustomerPortalAssetsOrg,
        )
        from ..models.output_customer_portal_assets_unlocated_assets_item import (
            OutputCustomerPortalAssetsUnlocatedAssetsItem,
        )

        d = dict(src_dict)
        customer_locations = []
        _customer_locations = d.pop("customer_locations")
        for customer_locations_item_data in _customer_locations:
            customer_locations_item = (
                OutputCustomerPortalAssetsCustomerLocationsItem.from_dict(
                    customer_locations_item_data
                )
            )

            customer_locations.append(customer_locations_item)

        unlocated_assets = []
        _unlocated_assets = d.pop("unlocated_assets")
        for unlocated_assets_item_data in _unlocated_assets:
            unlocated_assets_item = (
                OutputCustomerPortalAssetsUnlocatedAssetsItem.from_dict(
                    unlocated_assets_item_data
                )
            )

            unlocated_assets.append(unlocated_assets_item)

        org = OutputCustomerPortalAssetsOrg.from_dict(d.pop("org"))

        output_customer_portal_assets = cls(
            customer_locations=customer_locations,
            unlocated_assets=unlocated_assets,
            org=org,
        )

        output_customer_portal_assets.additional_properties = d
        return output_customer_portal_assets

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
