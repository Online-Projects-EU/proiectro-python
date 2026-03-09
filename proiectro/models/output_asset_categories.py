from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.output_asset_category import OutputAssetCategory


T = TypeVar("T", bound="OutputAssetCategories")


@_attrs_define
class OutputAssetCategories:
    """
    Attributes:
        asset_categories (list[OutputAssetCategory]):
    """

    asset_categories: list[OutputAssetCategory]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        asset_categories = []
        for asset_categories_item_data in self.asset_categories:
            asset_categories_item = asset_categories_item_data.to_dict()
            asset_categories.append(asset_categories_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "asset_categories": asset_categories,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.output_asset_category import OutputAssetCategory

        d = dict(src_dict)
        asset_categories = []
        _asset_categories = d.pop("asset_categories")
        for asset_categories_item_data in _asset_categories:
            asset_categories_item = OutputAssetCategory.from_dict(
                asset_categories_item_data
            )

            asset_categories.append(asset_categories_item)

        output_asset_categories = cls(
            asset_categories=asset_categories,
        )

        output_asset_categories.additional_properties = d
        return output_asset_categories

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
