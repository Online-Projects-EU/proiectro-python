from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.output_share_file_entity_type import OutputShareFileEntityType
from ..models.output_share_file_state import OutputShareFileState
from ..types import UNSET, Unset

T = TypeVar("T", bound="OutputShareFile")


@_attrs_define
class OutputShareFile:
    """
    Attributes:
        id (str):
        entity_type (OutputShareFileEntityType):
        entity_id (str):
        name (str):
        size (int):
        state (OutputShareFileState):
        added_at (datetime.datetime):
        content_type (str | Unset):  Default: ''.
        published (bool | Unset):  Default: False.
        added_by (None | str | Unset):
    """

    id: str
    entity_type: OutputShareFileEntityType
    entity_id: str
    name: str
    size: int
    state: OutputShareFileState
    added_at: datetime.datetime
    content_type: str | Unset = ""
    published: bool | Unset = False
    added_by: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        entity_type = self.entity_type.value

        entity_id = self.entity_id

        name = self.name

        size = self.size

        state = self.state.value

        added_at = self.added_at.isoformat()

        content_type = self.content_type

        published = self.published

        added_by: None | str | Unset
        if isinstance(self.added_by, Unset):
            added_by = UNSET
        else:
            added_by = self.added_by

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "entity_type": entity_type,
                "entity_id": entity_id,
                "name": name,
                "size": size,
                "state": state,
                "added_at": added_at,
            }
        )
        if content_type is not UNSET:
            field_dict["content_type"] = content_type
        if published is not UNSET:
            field_dict["published"] = published
        if added_by is not UNSET:
            field_dict["added_by"] = added_by

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        entity_type = OutputShareFileEntityType(d.pop("entity_type"))

        entity_id = d.pop("entity_id")

        name = d.pop("name")

        size = d.pop("size")

        state = OutputShareFileState(d.pop("state"))

        added_at = isoparse(d.pop("added_at"))

        content_type = d.pop("content_type", UNSET)

        published = d.pop("published", UNSET)

        def _parse_added_by(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        added_by = _parse_added_by(d.pop("added_by", UNSET))

        output_share_file = cls(
            id=id,
            entity_type=entity_type,
            entity_id=entity_id,
            name=name,
            size=size,
            state=state,
            added_at=added_at,
            content_type=content_type,
            published=published,
            added_by=added_by,
        )

        output_share_file.additional_properties = d
        return output_share_file

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
