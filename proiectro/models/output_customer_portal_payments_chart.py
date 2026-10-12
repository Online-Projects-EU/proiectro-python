from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.output_customer_portal_payments_chart_series_by_currency import (
        OutputCustomerPortalPaymentsChartSeriesByCurrency,
    )


T = TypeVar("T", bound="OutputCustomerPortalPaymentsChart")


@_attrs_define
class OutputCustomerPortalPaymentsChart:
    """Customer portal payments chart data

    Attributes:
        series_by_currency (OutputCustomerPortalPaymentsChartSeriesByCurrency):
        currencies (list[str]):
        months (list[str]):
    """

    series_by_currency: OutputCustomerPortalPaymentsChartSeriesByCurrency
    currencies: list[str]
    months: list[str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        series_by_currency = self.series_by_currency.to_dict()

        currencies = self.currencies

        months = self.months

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "series_by_currency": series_by_currency,
                "currencies": currencies,
                "months": months,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.output_customer_portal_payments_chart_series_by_currency import (
            OutputCustomerPortalPaymentsChartSeriesByCurrency,
        )

        d = dict(src_dict)
        series_by_currency = (
            OutputCustomerPortalPaymentsChartSeriesByCurrency.from_dict(
                d.pop("series_by_currency")
            )
        )

        currencies = cast(list[str], d.pop("currencies"))

        months = cast(list[str], d.pop("months"))

        output_customer_portal_payments_chart = cls(
            series_by_currency=series_by_currency,
            currencies=currencies,
            months=months,
        )

        output_customer_portal_payments_chart.additional_properties = d
        return output_customer_portal_payments_chart

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
