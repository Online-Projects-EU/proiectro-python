from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.block_payments_summary import BlockPaymentsSummary
    from ..models.payment_detail import PaymentDetail


T = TypeVar("T", bound="OutputBlockPayments")


@_attrs_define
class OutputBlockPayments:
    """
    Attributes:
        payments (list[PaymentDetail]):
        summary (BlockPaymentsSummary):
        block_id (str):
        block_name (str):
        block_type (str):
        proposal_currency (str):
        can_edit (bool):
        is_closed_won (bool):
    """

    payments: list[PaymentDetail]
    summary: BlockPaymentsSummary
    block_id: str
    block_name: str
    block_type: str
    proposal_currency: str
    can_edit: bool
    is_closed_won: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        payments = []
        for payments_item_data in self.payments:
            payments_item = payments_item_data.to_dict()
            payments.append(payments_item)

        summary = self.summary.to_dict()

        block_id = self.block_id

        block_name = self.block_name

        block_type = self.block_type

        proposal_currency = self.proposal_currency

        can_edit = self.can_edit

        is_closed_won = self.is_closed_won

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "payments": payments,
                "summary": summary,
                "block_id": block_id,
                "block_name": block_name,
                "block_type": block_type,
                "proposal_currency": proposal_currency,
                "can_edit": can_edit,
                "is_closed_won": is_closed_won,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.block_payments_summary import BlockPaymentsSummary
        from ..models.payment_detail import PaymentDetail

        d = dict(src_dict)
        payments = []
        _payments = d.pop("payments")
        for payments_item_data in _payments:
            payments_item = PaymentDetail.from_dict(payments_item_data)

            payments.append(payments_item)

        summary = BlockPaymentsSummary.from_dict(d.pop("summary"))

        block_id = d.pop("block_id")

        block_name = d.pop("block_name")

        block_type = d.pop("block_type")

        proposal_currency = d.pop("proposal_currency")

        can_edit = d.pop("can_edit")

        is_closed_won = d.pop("is_closed_won")

        output_block_payments = cls(
            payments=payments,
            summary=summary,
            block_id=block_id,
            block_name=block_name,
            block_type=block_type,
            proposal_currency=proposal_currency,
            can_edit=can_edit,
            is_closed_won=is_closed_won,
        )

        output_block_payments.additional_properties = d
        return output_block_payments

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
