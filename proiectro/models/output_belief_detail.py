from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.belief_split_row import BeliefSplitRow
    from ..models.output_belief import OutputBelief
    from ..models.output_belief_detail_items_item import OutputBeliefDetailItemsItem


T = TypeVar("T", bound="OutputBeliefDetail")


@_attrs_define
class OutputBeliefDetail:
    """
    Attributes:
        summary (OutputBelief):
        split (list[BeliefSplitRow] | Unset):
        items (list[OutputBeliefDetailItemsItem] | Unset):
    """

    summary: OutputBelief
    split: list[BeliefSplitRow] | Unset = UNSET
    items: list[OutputBeliefDetailItemsItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        summary = self.summary.to_dict()

        split: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.split, Unset):
            split = []
            for split_item_data in self.split:
                split_item = split_item_data.to_dict()
                split.append(split_item)

        items: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.items, Unset):
            items = []
            for items_item_data in self.items:
                items_item = items_item_data.to_dict()
                items.append(items_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "summary": summary,
            }
        )
        if split is not UNSET:
            field_dict["split"] = split
        if items is not UNSET:
            field_dict["items"] = items

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.belief_split_row import BeliefSplitRow
        from ..models.output_belief import OutputBelief
        from ..models.output_belief_detail_items_item import OutputBeliefDetailItemsItem

        d = dict(src_dict)
        summary = OutputBelief.from_dict(d.pop("summary"))

        _split = d.pop("split", UNSET)
        split: list[BeliefSplitRow] | Unset = UNSET
        if _split is not UNSET:
            split = []
            for split_item_data in _split:
                split_item = BeliefSplitRow.from_dict(split_item_data)

                split.append(split_item)

        _items = d.pop("items", UNSET)
        items: list[OutputBeliefDetailItemsItem] | Unset = UNSET
        if _items is not UNSET:
            items = []
            for items_item_data in _items:
                items_item = OutputBeliefDetailItemsItem.from_dict(items_item_data)

                items.append(items_item)

        output_belief_detail = cls(
            summary=summary,
            split=split,
            items=items,
        )

        output_belief_detail.additional_properties = d
        return output_belief_detail

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
