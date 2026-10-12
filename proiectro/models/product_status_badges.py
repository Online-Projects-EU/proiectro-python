from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.product_status_detail import ProductStatusDetail


T = TypeVar("T", bound="ProductStatusBadges")


@_attrs_define
class ProductStatusBadges:
    """Product status badges for dynamic updates

    Attributes:
        product_id (str):
        product_name (str):
        is_active (bool):
        current_status (ProductStatusDetail): Product status for lifecycle display.
            Used in status dropdowns to show current status and all available lifecycle stages.
            Use lifecycle_type with templatetags for styling (status_bg, status_text, status_icon, etc.)
        lifecycle_statuses (list[ProductStatusDetail]):
    """

    product_id: str
    product_name: str
    is_active: bool
    current_status: ProductStatusDetail
    lifecycle_statuses: list[ProductStatusDetail]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        product_id = self.product_id

        product_name = self.product_name

        is_active = self.is_active

        current_status = self.current_status.to_dict()

        lifecycle_statuses = []
        for lifecycle_statuses_item_data in self.lifecycle_statuses:
            lifecycle_statuses_item = lifecycle_statuses_item_data.to_dict()
            lifecycle_statuses.append(lifecycle_statuses_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "product_id": product_id,
                "product_name": product_name,
                "is_active": is_active,
                "current_status": current_status,
                "lifecycle_statuses": lifecycle_statuses,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.product_status_detail import ProductStatusDetail

        d = dict(src_dict)
        product_id = d.pop("product_id")

        product_name = d.pop("product_name")

        is_active = d.pop("is_active")

        current_status = ProductStatusDetail.from_dict(d.pop("current_status"))

        lifecycle_statuses = []
        _lifecycle_statuses = d.pop("lifecycle_statuses")
        for lifecycle_statuses_item_data in _lifecycle_statuses:
            lifecycle_statuses_item = ProductStatusDetail.from_dict(
                lifecycle_statuses_item_data
            )

            lifecycle_statuses.append(lifecycle_statuses_item)

        product_status_badges = cls(
            product_id=product_id,
            product_name=product_name,
            is_active=is_active,
            current_status=current_status,
            lifecycle_statuses=lifecycle_statuses,
        )

        product_status_badges.additional_properties = d
        return product_status_badges

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
