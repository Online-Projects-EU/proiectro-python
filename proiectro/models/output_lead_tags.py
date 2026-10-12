from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.output_tag import OutputTag


T = TypeVar("T", bound="OutputLeadTags")


@_attrs_define
class OutputLeadTags:
    """
    Attributes:
        lead (str):
        tags (list[OutputTag] | Unset):
        unassigned_tags (list[OutputTag] | Unset):
    """

    lead: str
    tags: list[OutputTag] | Unset = UNSET
    unassigned_tags: list[OutputTag] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        lead = self.lead

        tags: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.tags, Unset):
            tags = []
            for tags_item_data in self.tags:
                tags_item = tags_item_data.to_dict()
                tags.append(tags_item)

        unassigned_tags: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.unassigned_tags, Unset):
            unassigned_tags = []
            for unassigned_tags_item_data in self.unassigned_tags:
                unassigned_tags_item = unassigned_tags_item_data.to_dict()
                unassigned_tags.append(unassigned_tags_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "lead": lead,
            }
        )
        if tags is not UNSET:
            field_dict["tags"] = tags
        if unassigned_tags is not UNSET:
            field_dict["unassigned_tags"] = unassigned_tags

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.output_tag import OutputTag

        d = dict(src_dict)
        lead = d.pop("lead")

        _tags = d.pop("tags", UNSET)
        tags: list[OutputTag] | Unset = UNSET
        if _tags is not UNSET:
            tags = []
            for tags_item_data in _tags:
                tags_item = OutputTag.from_dict(tags_item_data)

                tags.append(tags_item)

        _unassigned_tags = d.pop("unassigned_tags", UNSET)
        unassigned_tags: list[OutputTag] | Unset = UNSET
        if _unassigned_tags is not UNSET:
            unassigned_tags = []
            for unassigned_tags_item_data in _unassigned_tags:
                unassigned_tags_item = OutputTag.from_dict(unassigned_tags_item_data)

                unassigned_tags.append(unassigned_tags_item)

        output_lead_tags = cls(
            lead=lead,
            tags=tags,
            unassigned_tags=unassigned_tags,
        )

        output_lead_tags.additional_properties = d
        return output_lead_tags

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
