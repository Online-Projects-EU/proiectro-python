from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.sale_activity_type_item import SaleActivityTypeItem


T = TypeVar("T", bound="OutputSaleActivityTypes")


@_attrs_define
class OutputSaleActivityTypes:
    """
    Attributes:
        activity_types (list[SaleActivityTypeItem]):
    """

    activity_types: list[SaleActivityTypeItem]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        activity_types = []
        for activity_types_item_data in self.activity_types:
            activity_types_item = activity_types_item_data.to_dict()
            activity_types.append(activity_types_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "activity_types": activity_types,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.sale_activity_type_item import SaleActivityTypeItem

        d = dict(src_dict)
        activity_types = []
        _activity_types = d.pop("activity_types")
        for activity_types_item_data in _activity_types:
            activity_types_item = SaleActivityTypeItem.from_dict(
                activity_types_item_data
            )

            activity_types.append(activity_types_item)

        output_sale_activity_types = cls(
            activity_types=activity_types,
        )

        output_sale_activity_types.additional_properties = d
        return output_sale_activity_types

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
