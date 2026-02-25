from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.project_cash_balance_chart_data_cash_balance_data_item import (
        ProjectCashBalanceChartDataCashBalanceDataItem,
    )


T = TypeVar("T", bound="ProjectCashBalanceChartData")


@_attrs_define
class ProjectCashBalanceChartData:
    """Cash balance chart data for S-curve visualization.
    Shows cumulative cash balance over project duration by week.

        Attributes:
            cash_balance_data (list[ProjectCashBalanceChartDataCashBalanceDataItem]):
            currency_symbol (str):
            currency_code (None | str | Unset):
            project_start (None | str | Unset):
            project_end (None | str | Unset):
    """

    cash_balance_data: list[ProjectCashBalanceChartDataCashBalanceDataItem]
    currency_symbol: str
    currency_code: None | str | Unset = UNSET
    project_start: None | str | Unset = UNSET
    project_end: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cash_balance_data = []
        for cash_balance_data_item_data in self.cash_balance_data:
            cash_balance_data_item = cash_balance_data_item_data.to_dict()
            cash_balance_data.append(cash_balance_data_item)

        currency_symbol = self.currency_symbol

        currency_code: None | str | Unset
        if isinstance(self.currency_code, Unset):
            currency_code = UNSET
        else:
            currency_code = self.currency_code

        project_start: None | str | Unset
        if isinstance(self.project_start, Unset):
            project_start = UNSET
        else:
            project_start = self.project_start

        project_end: None | str | Unset
        if isinstance(self.project_end, Unset):
            project_end = UNSET
        else:
            project_end = self.project_end

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "cash_balance_data": cash_balance_data,
                "currency_symbol": currency_symbol,
            }
        )
        if currency_code is not UNSET:
            field_dict["currency_code"] = currency_code
        if project_start is not UNSET:
            field_dict["project_start"] = project_start
        if project_end is not UNSET:
            field_dict["project_end"] = project_end

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.project_cash_balance_chart_data_cash_balance_data_item import (
            ProjectCashBalanceChartDataCashBalanceDataItem,
        )

        d = dict(src_dict)
        cash_balance_data = []
        _cash_balance_data = d.pop("cash_balance_data")
        for cash_balance_data_item_data in _cash_balance_data:
            cash_balance_data_item = (
                ProjectCashBalanceChartDataCashBalanceDataItem.from_dict(
                    cash_balance_data_item_data
                )
            )

            cash_balance_data.append(cash_balance_data_item)

        currency_symbol = d.pop("currency_symbol")

        def _parse_currency_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        currency_code = _parse_currency_code(d.pop("currency_code", UNSET))

        def _parse_project_start(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        project_start = _parse_project_start(d.pop("project_start", UNSET))

        def _parse_project_end(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        project_end = _parse_project_end(d.pop("project_end", UNSET))

        project_cash_balance_chart_data = cls(
            cash_balance_data=cash_balance_data,
            currency_symbol=currency_symbol,
            currency_code=currency_code,
            project_start=project_start,
            project_end=project_end,
        )

        project_cash_balance_chart_data.additional_properties = d
        return project_cash_balance_chart_data

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
