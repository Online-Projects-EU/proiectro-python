from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AddProductFromCatalog")


@_attrs_define
class AddProductFromCatalog:
    """
    Attributes:
        proposal_id (str):
        catalog_id (str):
        product_count (int | Unset):  Default: 1.
    """

    proposal_id: str
    catalog_id: str
    product_count: int | Unset = 1
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        proposal_id = self.proposal_id

        catalog_id = self.catalog_id

        product_count = self.product_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "proposal_id": proposal_id,
                "catalog_id": catalog_id,
            }
        )
        if product_count is not UNSET:
            field_dict["product_count"] = product_count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        proposal_id = d.pop("proposal_id")

        catalog_id = d.pop("catalog_id")

        product_count = d.pop("product_count", UNSET)

        add_product_from_catalog = cls(
            proposal_id=proposal_id,
            catalog_id=catalog_id,
            product_count=product_count,
        )

        add_product_from_catalog.additional_properties = d
        return add_product_from_catalog

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
