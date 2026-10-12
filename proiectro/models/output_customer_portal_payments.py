from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.output_customer_portal_payments_org import (
        OutputCustomerPortalPaymentsOrg,
    )
    from ..models.output_customer_portal_payments_payments_item import (
        OutputCustomerPortalPaymentsPaymentsItem,
    )


T = TypeVar("T", bound="OutputCustomerPortalPayments")


@_attrs_define
class OutputCustomerPortalPayments:
    """Customer portal payments view - unified list sorted by due date

    Attributes:
        payments (list[OutputCustomerPortalPaymentsPaymentsItem]):
        org (OutputCustomerPortalPaymentsOrg):
    """

    payments: list[OutputCustomerPortalPaymentsPaymentsItem]
    org: OutputCustomerPortalPaymentsOrg
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        payments = []
        for payments_item_data in self.payments:
            payments_item = payments_item_data.to_dict()
            payments.append(payments_item)

        org = self.org.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "payments": payments,
                "org": org,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.output_customer_portal_payments_org import (
            OutputCustomerPortalPaymentsOrg,
        )
        from ..models.output_customer_portal_payments_payments_item import (
            OutputCustomerPortalPaymentsPaymentsItem,
        )

        d = dict(src_dict)
        payments = []
        _payments = d.pop("payments")
        for payments_item_data in _payments:
            payments_item = OutputCustomerPortalPaymentsPaymentsItem.from_dict(
                payments_item_data
            )

            payments.append(payments_item)

        org = OutputCustomerPortalPaymentsOrg.from_dict(d.pop("org"))

        output_customer_portal_payments = cls(
            payments=payments,
            org=org,
        )

        output_customer_portal_payments.additional_properties = d
        return output_customer_portal_payments

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
