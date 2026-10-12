from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.partner_portal_asset_item import PartnerPortalAssetItem


T = TypeVar("T", bound="PartnerPortalLocationWithAssets")


@_attrs_define
class PartnerPortalLocationWithAssets:
    """Location with its assets for partner portal

    Attributes:
        id (str):
        name (str):
        assets (list[PartnerPortalAssetItem]):
        description (None | str | Unset):
    """

    id: str
    name: str
    assets: list[PartnerPortalAssetItem]
    description: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        assets = []
        for assets_item_data in self.assets:
            assets_item = assets_item_data.to_dict()
            assets.append(assets_item)

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "assets": assets,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.partner_portal_asset_item import PartnerPortalAssetItem

        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        assets = []
        _assets = d.pop("assets")
        for assets_item_data in _assets:
            assets_item = PartnerPortalAssetItem.from_dict(assets_item_data)

            assets.append(assets_item)

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        partner_portal_location_with_assets = cls(
            id=id,
            name=name,
            assets=assets,
            description=description,
        )

        partner_portal_location_with_assets.additional_properties = d
        return partner_portal_location_with_assets

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
