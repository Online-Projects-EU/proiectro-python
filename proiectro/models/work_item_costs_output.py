from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cost_item import CostItem
    from ..models.work_item_costs_output_total_by_currency import (
        WorkItemCostsOutputTotalByCurrency,
    )


T = TypeVar("T", bound="WorkItemCostsOutput")


@_attrs_define
class WorkItemCostsOutput:
    """
    Attributes:
        costs (list[CostItem]):
        cost_count (int):
        work_item_id (str):
        work_item_name (str):
        project_id (str):
        project_currency_symbol (str):
        total_expected (None | str | Unset):
        total_by_currency (WorkItemCostsOutputTotalByCurrency | Unset):
        uncovered_currencies (list[str] | Unset):
        total_in_workspace_currency (None | str | Unset):
        workspace_currency (str | Unset):  Default: ''.
        project_currency (str | Unset):  Default: ''.
    """

    costs: list[CostItem]
    cost_count: int
    work_item_id: str
    work_item_name: str
    project_id: str
    project_currency_symbol: str
    total_expected: None | str | Unset = UNSET
    total_by_currency: WorkItemCostsOutputTotalByCurrency | Unset = UNSET
    uncovered_currencies: list[str] | Unset = UNSET
    total_in_workspace_currency: None | str | Unset = UNSET
    workspace_currency: str | Unset = ""
    project_currency: str | Unset = ""
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        costs = []
        for costs_item_data in self.costs:
            costs_item = costs_item_data.to_dict()
            costs.append(costs_item)

        cost_count = self.cost_count

        work_item_id = self.work_item_id

        work_item_name = self.work_item_name

        project_id = self.project_id

        project_currency_symbol = self.project_currency_symbol

        total_expected: None | str | Unset
        if isinstance(self.total_expected, Unset):
            total_expected = UNSET
        else:
            total_expected = self.total_expected

        total_by_currency: dict[str, Any] | Unset = UNSET
        if not isinstance(self.total_by_currency, Unset):
            total_by_currency = self.total_by_currency.to_dict()

        uncovered_currencies: list[str] | Unset = UNSET
        if not isinstance(self.uncovered_currencies, Unset):
            uncovered_currencies = self.uncovered_currencies

        total_in_workspace_currency: None | str | Unset
        if isinstance(self.total_in_workspace_currency, Unset):
            total_in_workspace_currency = UNSET
        else:
            total_in_workspace_currency = self.total_in_workspace_currency

        workspace_currency = self.workspace_currency

        project_currency = self.project_currency

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "costs": costs,
                "cost_count": cost_count,
                "work_item_id": work_item_id,
                "work_item_name": work_item_name,
                "project_id": project_id,
                "project_currency_symbol": project_currency_symbol,
            }
        )
        if total_expected is not UNSET:
            field_dict["total_expected"] = total_expected
        if total_by_currency is not UNSET:
            field_dict["total_by_currency"] = total_by_currency
        if uncovered_currencies is not UNSET:
            field_dict["uncovered_currencies"] = uncovered_currencies
        if total_in_workspace_currency is not UNSET:
            field_dict["total_in_workspace_currency"] = total_in_workspace_currency
        if workspace_currency is not UNSET:
            field_dict["workspace_currency"] = workspace_currency
        if project_currency is not UNSET:
            field_dict["project_currency"] = project_currency

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cost_item import CostItem
        from ..models.work_item_costs_output_total_by_currency import (
            WorkItemCostsOutputTotalByCurrency,
        )

        d = dict(src_dict)
        costs = []
        _costs = d.pop("costs")
        for costs_item_data in _costs:
            costs_item = CostItem.from_dict(costs_item_data)

            costs.append(costs_item)

        cost_count = d.pop("cost_count")

        work_item_id = d.pop("work_item_id")

        work_item_name = d.pop("work_item_name")

        project_id = d.pop("project_id")

        project_currency_symbol = d.pop("project_currency_symbol")

        def _parse_total_expected(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        total_expected = _parse_total_expected(d.pop("total_expected", UNSET))

        _total_by_currency = d.pop("total_by_currency", UNSET)
        total_by_currency: WorkItemCostsOutputTotalByCurrency | Unset
        if isinstance(_total_by_currency, Unset):
            total_by_currency = UNSET
        else:
            total_by_currency = WorkItemCostsOutputTotalByCurrency.from_dict(
                _total_by_currency
            )

        uncovered_currencies = cast(list[str], d.pop("uncovered_currencies", UNSET))

        def _parse_total_in_workspace_currency(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        total_in_workspace_currency = _parse_total_in_workspace_currency(
            d.pop("total_in_workspace_currency", UNSET)
        )

        workspace_currency = d.pop("workspace_currency", UNSET)

        project_currency = d.pop("project_currency", UNSET)

        work_item_costs_output = cls(
            costs=costs,
            cost_count=cost_count,
            work_item_id=work_item_id,
            work_item_name=work_item_name,
            project_id=project_id,
            project_currency_symbol=project_currency_symbol,
            total_expected=total_expected,
            total_by_currency=total_by_currency,
            uncovered_currencies=uncovered_currencies,
            total_in_workspace_currency=total_in_workspace_currency,
            workspace_currency=workspace_currency,
            project_currency=project_currency,
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
