from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.payment_flow_chart_data_cumulative_expected_item import (
        PaymentFlowChartDataCumulativeExpectedItem,
    )
    from ..models.payment_flow_chart_data_cumulative_paid_item import (
        PaymentFlowChartDataCumulativePaidItem,
    )
    from ..models.payment_flow_chart_data_paid_payments_item import (
        PaymentFlowChartDataPaidPaymentsItem,
    )
    from ..models.payment_flow_chart_data_payments_item import (
        PaymentFlowChartDataPaymentsItem,
    )
    from ..models.payment_flow_chart_data_summary import PaymentFlowChartDataSummary
    from ..models.payment_flow_chart_data_unpaid_payments_item import (
        PaymentFlowChartDataUnpaidPaymentsItem,
    )


T = TypeVar("T", bound="PaymentFlowChartData")


@_attrs_define
class PaymentFlowChartData:
    """Data for payment flow visualization

    Attributes:
        payments (list[PaymentFlowChartDataPaymentsItem]):
        dates (list[str]):
        paid_payments (list[PaymentFlowChartDataPaidPaymentsItem]):
        unpaid_payments (list[PaymentFlowChartDataUnpaidPaymentsItem]):
        cumulative_expected (list[PaymentFlowChartDataCumulativeExpectedItem]):
        cumulative_paid (list[PaymentFlowChartDataCumulativePaidItem]):
        summary (PaymentFlowChartDataSummary):
        currency_symbol (str):
    """

    payments: list[PaymentFlowChartDataPaymentsItem]
    dates: list[str]
    paid_payments: list[PaymentFlowChartDataPaidPaymentsItem]
    unpaid_payments: list[PaymentFlowChartDataUnpaidPaymentsItem]
    cumulative_expected: list[PaymentFlowChartDataCumulativeExpectedItem]
    cumulative_paid: list[PaymentFlowChartDataCumulativePaidItem]
    summary: PaymentFlowChartDataSummary
    currency_symbol: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        payments = []
        for payments_item_data in self.payments:
            payments_item = payments_item_data.to_dict()
            payments.append(payments_item)

        dates = self.dates

        paid_payments = []
        for paid_payments_item_data in self.paid_payments:
            paid_payments_item = paid_payments_item_data.to_dict()
            paid_payments.append(paid_payments_item)

        unpaid_payments = []
        for unpaid_payments_item_data in self.unpaid_payments:
            unpaid_payments_item = unpaid_payments_item_data.to_dict()
            unpaid_payments.append(unpaid_payments_item)

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
                "payments": payments,
                "dates": dates,
                "paid_payments": paid_payments,
                "unpaid_payments": unpaid_payments,
                "cumulative_expected": cumulative_expected,
                "cumulative_paid": cumulative_paid,
                "summary": summary,
                "currency_symbol": currency_symbol,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.payment_flow_chart_data_cumulative_expected_item import (
            PaymentFlowChartDataCumulativeExpectedItem,
        )
        from ..models.payment_flow_chart_data_cumulative_paid_item import (
            PaymentFlowChartDataCumulativePaidItem,
        )
        from ..models.payment_flow_chart_data_paid_payments_item import (
            PaymentFlowChartDataPaidPaymentsItem,
        )
        from ..models.payment_flow_chart_data_payments_item import (
            PaymentFlowChartDataPaymentsItem,
        )
        from ..models.payment_flow_chart_data_summary import PaymentFlowChartDataSummary
        from ..models.payment_flow_chart_data_unpaid_payments_item import (
            PaymentFlowChartDataUnpaidPaymentsItem,
        )

        d = dict(src_dict)
        payments = []
        _payments = d.pop("payments")
        for payments_item_data in _payments:
            payments_item = PaymentFlowChartDataPaymentsItem.from_dict(
                payments_item_data
            )

            payments.append(payments_item)

        dates = cast(list[str], d.pop("dates"))

        paid_payments = []
        _paid_payments = d.pop("paid_payments")
        for paid_payments_item_data in _paid_payments:
            paid_payments_item = PaymentFlowChartDataPaidPaymentsItem.from_dict(
                paid_payments_item_data
            )

            paid_payments.append(paid_payments_item)

        unpaid_payments = []
        _unpaid_payments = d.pop("unpaid_payments")
        for unpaid_payments_item_data in _unpaid_payments:
            unpaid_payments_item = PaymentFlowChartDataUnpaidPaymentsItem.from_dict(
                unpaid_payments_item_data
            )

            unpaid_payments.append(unpaid_payments_item)

        cumulative_expected = []
        _cumulative_expected = d.pop("cumulative_expected")
        for cumulative_expected_item_data in _cumulative_expected:
            cumulative_expected_item = (
                PaymentFlowChartDataCumulativeExpectedItem.from_dict(
                    cumulative_expected_item_data
                )
            )

            cumulative_expected.append(cumulative_expected_item)

        cumulative_paid = []
        _cumulative_paid = d.pop("cumulative_paid")
        for cumulative_paid_item_data in _cumulative_paid:
            cumulative_paid_item = PaymentFlowChartDataCumulativePaidItem.from_dict(
                cumulative_paid_item_data
            )

            cumulative_paid.append(cumulative_paid_item)

        summary = PaymentFlowChartDataSummary.from_dict(d.pop("summary"))

        currency_symbol = d.pop("currency_symbol")

        payment_flow_chart_data = cls(
            payments=payments,
            dates=dates,
            paid_payments=paid_payments,
            unpaid_payments=unpaid_payments,
            cumulative_expected=cumulative_expected,
            cumulative_paid=cumulative_paid,
            summary=summary,
            currency_symbol=currency_symbol,
        )

        payment_flow_chart_data.additional_properties = d
        return payment_flow_chart_data

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
