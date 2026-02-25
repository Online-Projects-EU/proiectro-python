from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="CommentOutput")


@_attrs_define
class CommentOutput:
    """Output schema for a single comment

    Attributes:
        id (str):
        author_name (str):
        content (str):
        internal (bool):
        created (datetime.datetime):
        updated (datetime.datetime):
        edited (bool):
        attachments (bool):
        author_avatar (None | str | Unset):
        replies (list[CommentOutput] | Unset):
    """

    id: str
    author_name: str
    content: str
    internal: bool
    created: datetime.datetime
    updated: datetime.datetime
    edited: bool
    attachments: bool
    author_avatar: None | str | Unset = UNSET
    replies: list[CommentOutput] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        author_name = self.author_name

        content = self.content

        internal = self.internal

        created = self.created.isoformat()

        updated = self.updated.isoformat()

        edited = self.edited

        attachments = self.attachments

        author_avatar: None | str | Unset
        if isinstance(self.author_avatar, Unset):
            author_avatar = UNSET
        else:
            author_avatar = self.author_avatar

        replies: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.replies, Unset):
            replies = []
            for replies_item_data in self.replies:
                replies_item = replies_item_data.to_dict()
                replies.append(replies_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "author_name": author_name,
                "content": content,
                "internal": internal,
                "created": created,
                "updated": updated,
                "edited": edited,
                "attachments": attachments,
            }
        )
        if author_avatar is not UNSET:
            field_dict["author_avatar"] = author_avatar
        if replies is not UNSET:
            field_dict["replies"] = replies

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        author_name = d.pop("author_name")

        content = d.pop("content")

        internal = d.pop("internal")

        created = isoparse(d.pop("created"))

        updated = isoparse(d.pop("updated"))

        edited = d.pop("edited")

        attachments = d.pop("attachments")

        def _parse_author_avatar(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        author_avatar = _parse_author_avatar(d.pop("author_avatar", UNSET))

        _replies = d.pop("replies", UNSET)
        replies: list[CommentOutput] | Unset = UNSET
        if _replies is not UNSET:
            replies = []
            for replies_item_data in _replies:
                replies_item = CommentOutput.from_dict(replies_item_data)

                replies.append(replies_item)

        comment_output = cls(
            id=id,
            author_name=author_name,
            content=content,
            internal=internal,
            created=created,
            updated=updated,
            edited=edited,
            attachments=attachments,
            author_avatar=author_avatar,
            replies=replies,
        )

        comment_output.additional_properties = d
        return comment_output

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
