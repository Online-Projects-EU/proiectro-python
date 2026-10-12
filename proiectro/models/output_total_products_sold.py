from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.dashboard_metric import DashboardMetric
    from ..models.output_total_products_sold_breakdown_by_type_item import (
        OutputTotalProductsSoldBreakdownByTypeItem,
    )


T = TypeVar("T", bound="OutputTotalProductsSold")


@_attrs_define
class OutputTotalProductsSold:
    """Total catalog products sold metric

    Attributes:
        metric (DashboardMetric): Individual metric for display with comparison data
        breakdown_by_type (list[OutputTotalProductsSoldBreakdownByTypeItem]):
    """

    metric: DashboardMetric
    breakdown_by_type: list[OutputTotalProductsSoldBreakdownByTypeItem]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        metric = self.metric.to_dict()

        breakdown_by_type = []
        for breakdown_by_type_item_data in self.breakdown_by_type:
            breakdown_by_type_item = breakdown_by_type_item_data.to_dict()
            breakdown_by_type.append(breakdown_by_type_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "metric": metric,
                "breakdown_by_type": breakdown_by_type,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dashboard_metric import DashboardMetric
        from ..models.output_total_products_sold_breakdown_by_type_item import (
            OutputTotalProductsSoldBreakdownByTypeItem,
        )

        d = dict(src_dict)
        metric = DashboardMetric.from_dict(d.pop("metric"))

        breakdown_by_type = []
        _breakdown_by_type = d.pop("breakdown_by_type")
        for breakdown_by_type_item_data in _breakdown_by_type:
            breakdown_by_type_item = (
                OutputTotalProductsSoldBreakdownByTypeItem.from_dict(
                    breakdown_by_type_item_data
                )
            )

            breakdown_by_type.append(breakdown_by_type_item)

        output_total_products_sold = cls(
            metric=metric,
            breakdown_by_type=breakdown_by_type,
        )

        output_total_products_sold.additional_properties = d
        return output_total_products_sold

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
