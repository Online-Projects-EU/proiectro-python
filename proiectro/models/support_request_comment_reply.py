from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SupportRequestCommentReply")


@_attrs_define
class SupportRequestCommentReply:
    """Schema for a comment reply

    Attributes:
        comment_id (str):
        author_name (str):
        author_id (str):
        content (str):
        timestamp (str):
        edited (bool | Unset):  Default: False.
        show_to_requester (bool | Unset):  Default: False.
    """

    comment_id: str
    author_name: str
    author_id: str
    content: str
    timestamp: str
    edited: bool | Unset = False
    show_to_requester: bool | Unset = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        comment_id = self.comment_id

        author_name = self.author_name

        author_id = self.author_id

        content = self.content

        timestamp = self.timestamp

        edited = self.edited

        show_to_requester = self.show_to_requester

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "comment_id": comment_id,
                "author_name": author_name,
                "author_id": author_id,
                "content": content,
                "timestamp": timestamp,
            }
        )
        if edited is not UNSET:
            field_dict["edited"] = edited
        if show_to_requester is not UNSET:
            field_dict["show_to_requester"] = show_to_requester

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        comment_id = d.pop("comment_id")

        author_name = d.pop("author_name")

        author_id = d.pop("author_id")

        content = d.pop("content")

        timestamp = d.pop("timestamp")

        edited = d.pop("edited", UNSET)

        show_to_requester = d.pop("show_to_requester", UNSET)

        support_request_comment_reply = cls(
            comment_id=comment_id,
            author_name=author_name,
            author_id=author_id,
            content=content,
            timestamp=timestamp,
            edited=edited,
            show_to_requester=show_to_requester,
        )

        support_request_comment_reply.additional_properties = d
        return support_request_comment_reply

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
