from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.output_sales_target import OutputSalesTarget


T = TypeVar("T", bound="OutputSalesTargets")


@_attrs_define
class OutputSalesTargets:
    """
    Attributes:
        sales_targets (list[OutputSalesTarget]):
    """

    sales_targets: list[OutputSalesTarget]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        sales_targets = []
        for sales_targets_item_data in self.sales_targets:
            sales_targets_item = sales_targets_item_data.to_dict()
            sales_targets.append(sales_targets_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "sales_targets": sales_targets,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.output_sales_target import OutputSalesTarget

        d = dict(src_dict)
        sales_targets = []
        _sales_targets = d.pop("sales_targets")
        for sales_targets_item_data in _sales_targets:
            sales_targets_item = OutputSalesTarget.from_dict(sales_targets_item_data)

            sales_targets.append(sales_targets_item)

        output_sales_targets = cls(
            sales_targets=sales_targets,
        )

        output_sales_targets.additional_properties = d
        return output_sales_targets

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
