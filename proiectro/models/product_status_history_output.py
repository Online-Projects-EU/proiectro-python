from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.product_status_history_entry import ProductStatusHistoryEntry


T = TypeVar("T", bound="ProductStatusHistoryOutput")


@_attrs_define
class ProductStatusHistoryOutput:
    """Complete status history for a product

    Attributes:
        product_id (str):
        product_name (str):
        history (list[ProductStatusHistoryEntry]):
        total_duration_days (int):
    """

    product_id: str
    product_name: str
    history: list[ProductStatusHistoryEntry]
    total_duration_days: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        product_id = self.product_id

        product_name = self.product_name

        history = []
        for history_item_data in self.history:
            history_item = history_item_data.to_dict()
            history.append(history_item)

        total_duration_days = self.total_duration_days

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "product_id": product_id,
                "product_name": product_name,
                "history": history,
                "total_duration_days": total_duration_days,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.product_status_history_entry import ProductStatusHistoryEntry

        d = dict(src_dict)
        product_id = d.pop("product_id")

        product_name = d.pop("product_name")

        history = []
        _history = d.pop("history")
        for history_item_data in _history:
            history_item = ProductStatusHistoryEntry.from_dict(history_item_data)

            history.append(history_item)

        total_duration_days = d.pop("total_duration_days")

        product_status_history_output = cls(
            product_id=product_id,
            product_name=product_name,
            history=history,
            total_duration_days=total_duration_days,
        )

        product_status_history_output.additional_properties = d
        return product_status_history_output

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
