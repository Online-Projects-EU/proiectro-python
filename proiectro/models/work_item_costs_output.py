from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.cost_item import CostItem


T = TypeVar("T", bound="WorkItemCostsOutput")


@_attrs_define
class WorkItemCostsOutput:
    """
    Attributes:
        costs (list[CostItem]):
        total_expected (str):
        cost_count (int):
        work_item_id (str):
        work_item_name (str):
        project_id (str):
        project_currency_symbol (str):
    """

    costs: list[CostItem]
    total_expected: str
    cost_count: int
    work_item_id: str
    work_item_name: str
    project_id: str
    project_currency_symbol: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        costs = []
        for costs_item_data in self.costs:
            costs_item = costs_item_data.to_dict()
            costs.append(costs_item)

        total_expected = self.total_expected

        cost_count = self.cost_count

        work_item_id = self.work_item_id

        work_item_name = self.work_item_name

        project_id = self.project_id

        project_currency_symbol = self.project_currency_symbol

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "costs": costs,
                "total_expected": total_expected,
                "cost_count": cost_count,
                "work_item_id": work_item_id,
                "work_item_name": work_item_name,
                "project_id": project_id,
                "project_currency_symbol": project_currency_symbol,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cost_item import CostItem

        d = dict(src_dict)
        costs = []
        _costs = d.pop("costs")
        for costs_item_data in _costs:
            costs_item = CostItem.from_dict(costs_item_data)

            costs.append(costs_item)

        total_expected = d.pop("total_expected")

        cost_count = d.pop("cost_count")

        work_item_id = d.pop("work_item_id")

        work_item_name = d.pop("work_item_name")

        project_id = d.pop("project_id")

        project_currency_symbol = d.pop("project_currency_symbol")

        work_item_costs_output = cls(
            costs=costs,
            total_expected=total_expected,
            cost_count=cost_count,
            work_item_id=work_item_id,
            work_item_name=work_item_name,
            project_id=project_id,
            project_currency_symbol=project_currency_symbol,
        )

        work_item_costs_output.additional_properties = d
        return work_item_costs_output

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
