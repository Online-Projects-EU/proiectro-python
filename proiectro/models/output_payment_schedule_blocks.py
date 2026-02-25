from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.payment_schedule_block_detail import PaymentScheduleBlockDetail
    from ..models.payment_schedule_summary import PaymentScheduleSummary


T = TypeVar("T", bound="OutputPaymentScheduleBlocks")


@_attrs_define
class OutputPaymentScheduleBlocks:
    """
    Attributes:
        blocks (list[PaymentScheduleBlockDetail]):
        summary (PaymentScheduleSummary):
        proposal_id (str):
        proposal_sent (bool):
        can_edit (bool):
        is_locked (bool):
    """

    blocks: list[PaymentScheduleBlockDetail]
    summary: PaymentScheduleSummary
    proposal_id: str
    proposal_sent: bool
    can_edit: bool
    is_locked: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        blocks = []
        for blocks_item_data in self.blocks:
            blocks_item = blocks_item_data.to_dict()
            blocks.append(blocks_item)

        summary = self.summary.to_dict()

        proposal_id = self.proposal_id

        proposal_sent = self.proposal_sent

        can_edit = self.can_edit

        is_locked = self.is_locked

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "blocks": blocks,
                "summary": summary,
                "proposal_id": proposal_id,
                "proposal_sent": proposal_sent,
                "can_edit": can_edit,
                "is_locked": is_locked,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.payment_schedule_block_detail import PaymentScheduleBlockDetail
        from ..models.payment_schedule_summary import PaymentScheduleSummary

        d = dict(src_dict)
        blocks = []
        _blocks = d.pop("blocks")
        for blocks_item_data in _blocks:
            blocks_item = PaymentScheduleBlockDetail.from_dict(blocks_item_data)

            blocks.append(blocks_item)

        summary = PaymentScheduleSummary.from_dict(d.pop("summary"))

        proposal_id = d.pop("proposal_id")

        proposal_sent = d.pop("proposal_sent")

        can_edit = d.pop("can_edit")

        is_locked = d.pop("is_locked")

        output_payment_schedule_blocks = cls(
            blocks=blocks,
            summary=summary,
            proposal_id=proposal_id,
            proposal_sent=proposal_sent,
            can_edit=can_edit,
            is_locked=is_locked,
        )

        output_payment_schedule_blocks.additional_properties = d
        return output_payment_schedule_blocks

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
