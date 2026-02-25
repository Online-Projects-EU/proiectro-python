from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AddExternalSupportRequestComment")


@_attrs_define
class AddExternalSupportRequestComment:
    """
    Attributes:
        support_request_id (str):
        content (str):
        parent_id (None | str | Unset):
        show_to_requester (bool | Unset):  Default: False.
    """

    support_request_id: str
    content: str
    parent_id: None | str | Unset = UNSET
    show_to_requester: bool | Unset = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        support_request_id = self.support_request_id

        content = self.content

        parent_id: None | str | Unset
        if isinstance(self.parent_id, Unset):
            parent_id = UNSET
        else:
            parent_id = self.parent_id

        show_to_requester = self.show_to_requester

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "support_request_id": support_request_id,
                "content": content,
            }
        )
        if parent_id is not UNSET:
            field_dict["parent_id"] = parent_id
        if show_to_requester is not UNSET:
            field_dict["show_to_requester"] = show_to_requester

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        support_request_id = d.pop("support_request_id")

        content = d.pop("content")

        def _parse_parent_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        parent_id = _parse_parent_id(d.pop("parent_id", UNSET))

        show_to_requester = d.pop("show_to_requester", UNSET)

        add_external_support_request_comment = cls(
            support_request_id=support_request_id,
            content=content,
            parent_id=parent_id,
            show_to_requester=show_to_requester,
        )

        add_external_support_request_comment.additional_properties = d
        return add_external_support_request_comment

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
