from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.output_customer_asset import OutputCustomerAsset


T = TypeVar("T", bound="OutputCustomerAssets")


@_attrs_define
class OutputCustomerAssets:
    """
    Attributes:
        customer_assets (list[OutputCustomerAsset]):
    """

    customer_assets: list[OutputCustomerAsset]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        customer_assets = []
        for customer_assets_item_data in self.customer_assets:
            customer_assets_item = customer_assets_item_data.to_dict()
            customer_assets.append(customer_assets_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "customer_assets": customer_assets,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.output_customer_asset import OutputCustomerAsset

        d = dict(src_dict)
        customer_assets = []
        _customer_assets = d.pop("customer_assets")
        for customer_assets_item_data in _customer_assets:
            customer_assets_item = OutputCustomerAsset.from_dict(
                customer_assets_item_data
            )

            customer_assets.append(customer_assets_item)

        output_customer_assets = cls(
            customer_assets=customer_assets,
        )

        output_customer_assets.additional_properties = d
        return output_customer_assets

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
