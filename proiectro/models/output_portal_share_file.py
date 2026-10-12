from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.output_portal_share_file_state import OutputPortalShareFileState

T = TypeVar("T", bound="OutputPortalShareFile")


@_attrs_define
class OutputPortalShareFile:
    """
    Attributes:
        id (str):
        name (str):
        size (int):
        state (OutputPortalShareFileState):
    """

    id: str
    name: str
    size: int
    state: OutputPortalShareFileState
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        size = self.size

        state = self.state.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "size": size,
                "state": state,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        size = d.pop("size")

        state = OutputPortalShareFileState(d.pop("state"))

        output_portal_share_file = cls(
            id=id,
            name=name,
            size=size,
            state=state,
        )

        output_portal_share_file.additional_properties = d
        return output_portal_share_file

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
