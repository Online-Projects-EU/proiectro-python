from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.reorder_payment_schedule_blocks_block_sequences_item import (
        ReorderPaymentScheduleBlocksBlockSequencesItem,
    )


T = TypeVar("T", bound="ReorderPaymentScheduleBlocks")


@_attrs_define
class ReorderPaymentScheduleBlocks:
    """
    Attributes:
        block_sequences (list[ReorderPaymentScheduleBlocksBlockSequencesItem]):
    """

    block_sequences: list[ReorderPaymentScheduleBlocksBlockSequencesItem]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        block_sequences = []
        for block_sequences_item_data in self.block_sequences:
            block_sequences_item = block_sequences_item_data.to_dict()
            block_sequences.append(block_sequences_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "block_sequences": block_sequences,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.reorder_payment_schedule_blocks_block_sequences_item import (
            ReorderPaymentScheduleBlocksBlockSequencesItem,
        )

        d = dict(src_dict)
        block_sequences = []
        _block_sequences = d.pop("block_sequences")
        for block_sequences_item_data in _block_sequences:
            block_sequences_item = (
                ReorderPaymentScheduleBlocksBlockSequencesItem.from_dict(
                    block_sequences_item_data
                )
            )

            block_sequences.append(block_sequences_item)

        reorder_payment_schedule_blocks = cls(
            block_sequences=block_sequences,
        )

        reorder_payment_schedule_blocks.additional_properties = d
        return reorder_payment_schedule_blocks

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
