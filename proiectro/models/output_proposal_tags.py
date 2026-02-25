from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.output_tag import OutputTag


T = TypeVar("T", bound="OutputProposalTags")


@_attrs_define
class OutputProposalTags:
    """
    Attributes:
        proposal (str):
        tags (list[OutputTag]):
        unassigned_tags (list[OutputTag]):
    """

    proposal: str
    tags: list[OutputTag]
    unassigned_tags: list[OutputTag]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        proposal = self.proposal

        tags = []
        for tags_item_data in self.tags:
            tags_item = tags_item_data.to_dict()
            tags.append(tags_item)

        unassigned_tags = []
        for unassigned_tags_item_data in self.unassigned_tags:
            unassigned_tags_item = unassigned_tags_item_data.to_dict()
            unassigned_tags.append(unassigned_tags_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "proposal": proposal,
                "tags": tags,
                "unassigned_tags": unassigned_tags,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.output_tag import OutputTag

        d = dict(src_dict)
        proposal = d.pop("proposal")

        tags = []
        _tags = d.pop("tags")
        for tags_item_data in _tags:
            tags_item = OutputTag.from_dict(tags_item_data)

            tags.append(tags_item)

        unassigned_tags = []
        _unassigned_tags = d.pop("unassigned_tags")
        for unassigned_tags_item_data in _unassigned_tags:
            unassigned_tags_item = OutputTag.from_dict(unassigned_tags_item_data)

            unassigned_tags.append(unassigned_tags_item)

        output_proposal_tags = cls(
            proposal=proposal,
            tags=tags,
            unassigned_tags=unassigned_tags,
        )

        output_proposal_tags.additional_properties = d
        return output_proposal_tags

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
