from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AddOperationalWorkItemComment")


@_attrs_define
class AddOperationalWorkItemComment:
    """Input schema for adding a comment to an operational work item

    Attributes:
        operational_work_item_id (str):
        content (str):
        parent_id (None | str | Unset):
    """

    operational_work_item_id: str
    content: str
    parent_id: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        operational_work_item_id = self.operational_work_item_id

        content = self.content

        parent_id: None | str | Unset
        if isinstance(self.parent_id, Unset):
            parent_id = UNSET
        else:
            parent_id = self.parent_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "operational_work_item_id": operational_work_item_id,
                "content": content,
            }
        )
        if parent_id is not UNSET:
            field_dict["parent_id"] = parent_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        operational_work_item_id = d.pop("operational_work_item_id")

        content = d.pop("content")

        def _parse_parent_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        parent_id = _parse_parent_id(d.pop("parent_id", UNSET))

        add_operational_work_item_comment = cls(
            operational_work_item_id=operational_work_item_id,
            content=content,
            parent_id=parent_id,
        )

        add_operational_work_item_comment.additional_properties = d
        return add_operational_work_item_comment

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
