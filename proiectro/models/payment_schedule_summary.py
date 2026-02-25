from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PaymentScheduleSummary")


@_attrs_define
class PaymentScheduleSummary:
    """
    Attributes:
        total_blocks (int):
        upfront_payments (int):
        milestone_payments (int):
        progress_payments (int):
        completion_payments (int):
    """

    total_blocks: int
    upfront_payments: int
    milestone_payments: int
    progress_payments: int
    completion_payments: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        total_blocks = self.total_blocks

        upfront_payments = self.upfront_payments

        milestone_payments = self.milestone_payments

        progress_payments = self.progress_payments

        completion_payments = self.completion_payments

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "total_blocks": total_blocks,
                "upfront_payments": upfront_payments,
                "milestone_payments": milestone_payments,
                "progress_payments": progress_payments,
                "completion_payments": completion_payments,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        total_blocks = d.pop("total_blocks")

        upfront_payments = d.pop("upfront_payments")

        milestone_payments = d.pop("milestone_payments")

        progress_payments = d.pop("progress_payments")

        completion_payments = d.pop("completion_payments")

        payment_schedule_summary = cls(
            total_blocks=total_blocks,
            upfront_payments=upfront_payments,
            milestone_payments=milestone_payments,
            progress_payments=progress_payments,
            completion_payments=completion_payments,
        )

        payment_schedule_summary.additional_properties = d
        return payment_schedule_summary

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
