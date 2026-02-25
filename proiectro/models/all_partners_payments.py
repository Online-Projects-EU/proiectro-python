from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.all_partners_payment_item import AllPartnersPaymentItem


T = TypeVar("T", bound="AllPartnersPayments")


@_attrs_define
class AllPartnersPayments:
    """Aggregated payments from all active partnerships

    Attributes:
        payments (list[AllPartnersPaymentItem]):
        total (int):
    """

    payments: list[AllPartnersPaymentItem]
    total: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        payments = []
        for payments_item_data in self.payments:
            payments_item = payments_item_data.to_dict()
            payments.append(payments_item)

        total = self.total

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "payments": payments,
                "total": total,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.all_partners_payment_item import AllPartnersPaymentItem

        d = dict(src_dict)
        payments = []
        _payments = d.pop("payments")
        for payments_item_data in _payments:
            payments_item = AllPartnersPaymentItem.from_dict(payments_item_data)

            payments.append(payments_item)

        total = d.pop("total")

        all_partners_payments = cls(
            payments=payments,
            total=total,
        )

        all_partners_payments.additional_properties = d
        return all_partners_payments

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
