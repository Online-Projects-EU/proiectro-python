from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.output_customer_portal_asset_detail_asset import (
        OutputCustomerPortalAssetDetailAsset,
    )
    from ..models.output_customer_portal_asset_detail_org import (
        OutputCustomerPortalAssetDetailOrg,
    )


T = TypeVar("T", bound="OutputCustomerPortalAssetDetail")


@_attrs_define
class OutputCustomerPortalAssetDetail:
    """Customer portal asset detail view

    Attributes:
        asset (OutputCustomerPortalAssetDetailAsset):
        org (OutputCustomerPortalAssetDetailOrg):
    """

    asset: OutputCustomerPortalAssetDetailAsset
    org: OutputCustomerPortalAssetDetailOrg
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        asset = self.asset.to_dict()

        org = self.org.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "asset": asset,
                "org": org,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.output_customer_portal_asset_detail_asset import (
            OutputCustomerPortalAssetDetailAsset,
        )
        from ..models.output_customer_portal_asset_detail_org import (
            OutputCustomerPortalAssetDetailOrg,
        )

        d = dict(src_dict)
        asset = OutputCustomerPortalAssetDetailAsset.from_dict(d.pop("asset"))

        org = OutputCustomerPortalAssetDetailOrg.from_dict(d.pop("org"))

        output_customer_portal_asset_detail = cls(
            asset=asset,
            org=org,
        )

        output_customer_portal_asset_detail.additional_properties = d
        return output_customer_portal_asset_detail

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
