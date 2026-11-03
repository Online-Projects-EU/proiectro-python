from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.output_sent_message import OutputSentMessage


T = TypeVar("T", bound="OutputSentMessages")


@_attrs_define
class OutputSentMessages:
    """
    Attributes:
        messages (list[OutputSentMessage]):
        total_count (int | Unset):  Default: 0.
        page (int | Unset):  Default: 1.
        has_next (bool | Unset):  Default: False.
        kind (None | str | Unset):
        entity_id (None | str | Unset):
        query (str | Unset):  Default: ''.
    """

    messages: list[OutputSentMessage]
    total_count: int | Unset = 0
    page: int | Unset = 1
    has_next: bool | Unset = False
    kind: None | str | Unset = UNSET
    entity_id: None | str | Unset = UNSET
    query: str | Unset = ""
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        messages = []
        for messages_item_data in self.messages:
            messages_item = messages_item_data.to_dict()
            messages.append(messages_item)

        total_count = self.total_count

        page = self.page

        has_next = self.has_next

        kind: None | str | Unset
        if isinstance(self.kind, Unset):
            kind = UNSET
        else:
            kind = self.kind

        entity_id: None | str | Unset
        if isinstance(self.entity_id, Unset):
            entity_id = UNSET
        else:
            entity_id = self.entity_id

        query = self.query

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "messages": messages,
            }
        )
        if total_count is not UNSET:
            field_dict["total_count"] = total_count
        if page is not UNSET:
            field_dict["page"] = page
        if has_next is not UNSET:
            field_dict["has_next"] = has_next
        if kind is not UNSET:
            field_dict["kind"] = kind
        if entity_id is not UNSET:
            field_dict["entity_id"] = entity_id
        if query is not UNSET:
            field_dict["query"] = query

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.output_sent_message import OutputSentMessage

        d = dict(src_dict)
        messages = []
        _messages = d.pop("messages")
        for messages_item_data in _messages:
            messages_item = OutputSentMessage.from_dict(messages_item_data)

            messages.append(messages_item)

        total_count = d.pop("total_count", UNSET)

        page = d.pop("page", UNSET)

        has_next = d.pop("has_next", UNSET)

        def _parse_kind(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        kind = _parse_kind(d.pop("kind", UNSET))

        def _parse_entity_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        entity_id = _parse_entity_id(d.pop("entity_id", UNSET))

        query = d.pop("query", UNSET)

        output_sent_messages = cls(
            messages=messages,
            total_count=total_count,
            page=page,
            has_next=has_next,
            kind=kind,
            entity_id=entity_id,
            query=query,
        )

        output_sent_messages.additional_properties = d
        return output_sent_messages

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
