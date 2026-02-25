from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="OutputProcessStageLink")


@_attrs_define
class OutputProcessStageLink:
    """A cross-process link attached to this stage

    Attributes:
        link_id (str):
        direction (str):
        remote_stage_id (str):
        remote_stage_name (str):
        remote_process_id (str):
        remote_process_name (str):
    """

    link_id: str
    direction: str
    remote_stage_id: str
    remote_stage_name: str
    remote_process_id: str
    remote_process_name: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        link_id = self.link_id

        direction = self.direction

        remote_stage_id = self.remote_stage_id

        remote_stage_name = self.remote_stage_name

        remote_process_id = self.remote_process_id

        remote_process_name = self.remote_process_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "link_id": link_id,
                "direction": direction,
                "remote_stage_id": remote_stage_id,
                "remote_stage_name": remote_stage_name,
                "remote_process_id": remote_process_id,
                "remote_process_name": remote_process_name,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        link_id = d.pop("link_id")

        direction = d.pop("direction")

        remote_stage_id = d.pop("remote_stage_id")

        remote_stage_name = d.pop("remote_stage_name")

        remote_process_id = d.pop("remote_process_id")

        remote_process_name = d.pop("remote_process_name")

        output_process_stage_link = cls(
            link_id=link_id,
            direction=direction,
            remote_stage_id=remote_stage_id,
            remote_stage_name=remote_stage_name,
            remote_process_id=remote_process_id,
            remote_process_name=remote_process_name,
        )

        output_process_stage_link.additional_properties = d
        return output_process_stage_link

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
