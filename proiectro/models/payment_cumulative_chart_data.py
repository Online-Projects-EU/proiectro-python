from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.payment_cumulative_chart_data_cumulative_expected_item import (
        PaymentCumulativeChartDataCumulativeExpectedItem,
    )
    from ..models.payment_cumulative_chart_data_cumulative_paid_item import (
        PaymentCumulativeChartDataCumulativePaidItem,
    )
    from ..models.payment_cumulative_chart_data_summary import (
        PaymentCumulativeChartDataSummary,
    )


T = TypeVar("T", bound="PaymentCumulativeChartData")


@_attrs_define
class PaymentCumulativeChartData:
    """Data for cumulative payment flow chart

    Attributes:
        cumulative_expected (list[PaymentCumulativeChartDataCumulativeExpectedItem]):
        cumulative_paid (list[PaymentCumulativeChartDataCumulativePaidItem]):
        summary (PaymentCumulativeChartDataSummary):
        currency_symbol (str):
    """

    cumulative_expected: list[PaymentCumulativeChartDataCumulativeExpectedItem]
    cumulative_paid: list[PaymentCumulativeChartDataCumulativePaidItem]
    summary: PaymentCumulativeChartDataSummary
    currency_symbol: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cumulative_expected = []
        for cumulative_expected_item_data in self.cumulative_expected:
            cumulative_expected_item = cumulative_expected_item_data.to_dict()
            cumulative_expected.append(cumulative_expected_item)

        cumulative_paid = []
        for cumulative_paid_item_data in self.cumulative_paid:
            cumulative_paid_item = cumulative_paid_item_data.to_dict()
            cumulative_paid.append(cumulative_paid_item)

        summary = self.summary.to_dict()

        currency_symbol = self.currency_symbol

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "cumulative_expected": cumulative_expected,
                "cumulative_paid": cumulative_paid,
                "summary": summary,
                "currency_symbol": currency_symbol,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.payment_cumulative_chart_data_cumulative_expected_item import (
            PaymentCumulativeChartDataCumulativeExpectedItem,
        )
        from ..models.payment_cumulative_chart_data_cumulative_paid_item import (
            PaymentCumulativeChartDataCumulativePaidItem,
        )
        from ..models.payment_cumulative_chart_data_summary import (
            PaymentCumulativeChartDataSummary,
        )

        d = dict(src_dict)
        cumulative_expected = []
        _cumulative_expected = d.pop("cumulative_expected")
        for cumulative_expected_item_data in _cumulative_expected:
            cumulative_expected_item = (
                PaymentCumulativeChartDataCumulativeExpectedItem.from_dict(
                    cumulative_expected_item_data
                )
            )

            cumulative_expected.append(cumulative_expected_item)

        cumulative_paid = []
        _cumulative_paid = d.pop("cumulative_paid")
        for cumulative_paid_item_data in _cumulative_paid:
            cumulative_paid_item = (
                PaymentCumulativeChartDataCumulativePaidItem.from_dict(
                    cumulative_paid_item_data
                )
            )

            cumulative_paid.append(cumulative_paid_item)

        summary = PaymentCumulativeChartDataSummary.from_dict(d.pop("summary"))

        currency_symbol = d.pop("currency_symbol")

        payment_cumulative_chart_data = cls(
            cumulative_expected=cumulative_expected,
            cumulative_paid=cumulative_paid,
            summary=summary,
            currency_symbol=currency_symbol,
        )

        payment_cumulative_chart_data.additional_properties = d
        return payment_cumulative_chart_data

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
