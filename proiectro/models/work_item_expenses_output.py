from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.expense_item import ExpenseItem
    from ..models.work_item_expenses_output_total_by_currency import (
        WorkItemExpensesOutputTotalByCurrency,
    )


T = TypeVar("T", bound="WorkItemExpensesOutput")


@_attrs_define
class WorkItemExpensesOutput:
    """
    Attributes:
        expenses (list[ExpenseItem]):
        expense_count (int):
        work_item_id (str):
        work_item_name (str):
        project_id (str):
        project_currency_symbol (str):
        total_actual (None | str | Unset):
        total_by_currency (WorkItemExpensesOutputTotalByCurrency | Unset):
        uncovered_currencies (list[str] | Unset):
        total_in_workspace_currency (None | str | Unset):
        workspace_currency (str | Unset):  Default: ''.
        project_currency (str | Unset):  Default: ''.
    """

    expenses: list[ExpenseItem]
    expense_count: int
    work_item_id: str
    work_item_name: str
    project_id: str
    project_currency_symbol: str
    total_actual: None | str | Unset = UNSET
    total_by_currency: WorkItemExpensesOutputTotalByCurrency | Unset = UNSET
    uncovered_currencies: list[str] | Unset = UNSET
    total_in_workspace_currency: None | str | Unset = UNSET
    workspace_currency: str | Unset = ""
    project_currency: str | Unset = ""
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        expenses = []
        for expenses_item_data in self.expenses:
            expenses_item = expenses_item_data.to_dict()
            expenses.append(expenses_item)

        expense_count = self.expense_count

        work_item_id = self.work_item_id

        work_item_name = self.work_item_name

        project_id = self.project_id

        project_currency_symbol = self.project_currency_symbol

        total_actual: None | str | Unset
        if isinstance(self.total_actual, Unset):
            total_actual = UNSET
        else:
            total_actual = self.total_actual

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
                "expenses": expenses,
                "expense_count": expense_count,
                "work_item_id": work_item_id,
                "work_item_name": work_item_name,
                "project_id": project_id,
                "project_currency_symbol": project_currency_symbol,
            }
        )
        if total_actual is not UNSET:
            field_dict["total_actual"] = total_actual
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
        from ..models.expense_item import ExpenseItem
        from ..models.work_item_expenses_output_total_by_currency import (
            WorkItemExpensesOutputTotalByCurrency,
        )

        d = dict(src_dict)
        expenses = []
        _expenses = d.pop("expenses")
        for expenses_item_data in _expenses:
            expenses_item = ExpenseItem.from_dict(expenses_item_data)

            expenses.append(expenses_item)

        expense_count = d.pop("expense_count")

        work_item_id = d.pop("work_item_id")

        work_item_name = d.pop("work_item_name")

        project_id = d.pop("project_id")

        project_currency_symbol = d.pop("project_currency_symbol")

        def _parse_total_actual(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        total_actual = _parse_total_actual(d.pop("total_actual", UNSET))

        _total_by_currency = d.pop("total_by_currency", UNSET)
        total_by_currency: WorkItemExpensesOutputTotalByCurrency | Unset
        if isinstance(_total_by_currency, Unset):
            total_by_currency = UNSET
        else:
            total_by_currency = WorkItemExpensesOutputTotalByCurrency.from_dict(
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

        work_item_expenses_output = cls(
            expenses=expenses,
            expense_count=expense_count,
            work_item_id=work_item_id,
            work_item_name=work_item_name,
            project_id=project_id,
            project_currency_symbol=project_currency_symbol,
            total_actual=total_actual,
            total_by_currency=total_by_currency,
            uncovered_currencies=uncovered_currencies,
            total_in_workspace_currency=total_in_workspace_currency,
            workspace_currency=workspace_currency,
            project_currency=project_currency,
        )

        work_item_expenses_output.additional_properties = d
        return work_item_expenses_output

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
