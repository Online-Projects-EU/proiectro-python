from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.comment_output import CommentOutput


T = TypeVar("T", bound="OutputCommentsFeed")


@_attrs_define
class OutputCommentsFeed:
    """Output schema for paginated comment feed

    Attributes:
        comments (list[CommentOutput]):
        per_page (int):
        next_page (int):
        entity_type (str):
        entity_id (str):
    """

    comments: list[CommentOutput]
    per_page: int
    next_page: int
    entity_type: str
    entity_id: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        comments = []
        for comments_item_data in self.comments:
            comments_item = comments_item_data.to_dict()
            comments.append(comments_item)

        per_page = self.per_page

        next_page = self.next_page

        entity_type = self.entity_type

        entity_id = self.entity_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "comments": comments,
                "per_page": per_page,
                "next_page": next_page,
                "entity_type": entity_type,
                "entity_id": entity_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.comment_output import CommentOutput

        d = dict(src_dict)
        comments = []
        _comments = d.pop("comments")
        for comments_item_data in _comments:
            comments_item = CommentOutput.from_dict(comments_item_data)

            comments.append(comments_item)

        per_page = d.pop("per_page")

        next_page = d.pop("next_page")

        entity_type = d.pop("entity_type")

        entity_id = d.pop("entity_id")

        output_comments_feed = cls(
            comments=comments,
            per_page=per_page,
            next_page=next_page,
            entity_type=entity_type,
            entity_id=entity_id,
        )

        output_comments_feed.additional_properties = d
        return output_comments_feed

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
