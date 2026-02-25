from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.payment_status_chart_data_paid_payments_item import (
        PaymentStatusChartDataPaidPaymentsItem,
    )
    from ..models.payment_status_chart_data_unpaid_payments_item import (
        PaymentStatusChartDataUnpaidPaymentsItem,
    )


T = TypeVar("T", bound="PaymentStatusChartData")


@_attrs_define
class PaymentStatusChartData:
    """Data for payment status breakdown chart

    Attributes:
        paid_payments (list[PaymentStatusChartDataPaidPaymentsItem]):
        unpaid_payments (list[PaymentStatusChartDataUnpaidPaymentsItem]):
        currency_symbol (str):
    """

    paid_payments: list[PaymentStatusChartDataPaidPaymentsItem]
    unpaid_payments: list[PaymentStatusChartDataUnpaidPaymentsItem]
    currency_symbol: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        paid_payments = []
        for paid_payments_item_data in self.paid_payments:
            paid_payments_item = paid_payments_item_data.to_dict()
            paid_payments.append(paid_payments_item)

        unpaid_payments = []
        for unpaid_payments_item_data in self.unpaid_payments:
            unpaid_payments_item = unpaid_payments_item_data.to_dict()
            unpaid_payments.append(unpaid_payments_item)

        currency_symbol = self.currency_symbol

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "paid_payments": paid_payments,
                "unpaid_payments": unpaid_payments,
                "currency_symbol": currency_symbol,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.payment_status_chart_data_paid_payments_item import (
            PaymentStatusChartDataPaidPaymentsItem,
        )
        from ..models.payment_status_chart_data_unpaid_payments_item import (
            PaymentStatusChartDataUnpaidPaymentsItem,
        )

        d = dict(src_dict)
        paid_payments = []
        _paid_payments = d.pop("paid_payments")
        for paid_payments_item_data in _paid_payments:
            paid_payments_item = PaymentStatusChartDataPaidPaymentsItem.from_dict(
                paid_payments_item_data
            )

            paid_payments.append(paid_payments_item)

        unpaid_payments = []
        _unpaid_payments = d.pop("unpaid_payments")
        for unpaid_payments_item_data in _unpaid_payments:
            unpaid_payments_item = PaymentStatusChartDataUnpaidPaymentsItem.from_dict(
                unpaid_payments_item_data
            )

            unpaid_payments.append(unpaid_payments_item)

        currency_symbol = d.pop("currency_symbol")

        payment_status_chart_data = cls(
            paid_payments=paid_payments,
            unpaid_payments=unpaid_payments,
            currency_symbol=currency_symbol,
        )

        payment_status_chart_data.additional_properties = d
        return payment_status_chart_data

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
