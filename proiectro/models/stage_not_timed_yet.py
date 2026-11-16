from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="StageNotTimedYet")


@_attrs_define
class StageNotTimedYet:
    """A stage whose deals cannot be given an estimated close date yet, and what it still needs.

    Attributes:
        stage_id (str):
        stage_name (str):
        won_known (int):
        won_needed (int):
    """

    stage_id: str
    stage_name: str
    won_known: int
    won_needed: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        stage_id = self.stage_id

        stage_name = self.stage_name

        won_known = self.won_known

        won_needed = self.won_needed

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "stage_id": stage_id,
                "stage_name": stage_name,
                "won_known": won_known,
                "won_needed": won_needed,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        stage_id = d.pop("stage_id")

        stage_name = d.pop("stage_name")

        won_known = d.pop("won_known")

        won_needed = d.pop("won_needed")

        stage_not_timed_yet = cls(
            stage_id=stage_id,
            stage_name=stage_name,
            won_known=won_known,
            won_needed=won_needed,
        )

        stage_not_timed_yet.additional_properties = d
        return stage_not_timed_yet

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
