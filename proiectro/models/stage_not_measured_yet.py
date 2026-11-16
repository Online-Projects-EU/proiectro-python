from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="StageNotMeasuredYet")


@_attrs_define
class StageNotMeasuredYet:
    """A stage whose win probability is not shown yet, and what it still needs.

    Attributes:
        stage_id (str):
        stage_name (str):
        outcomes_known (int):
        outcomes_needed (int):
    """

    stage_id: str
    stage_name: str
    outcomes_known: int
    outcomes_needed: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        stage_id = self.stage_id

        stage_name = self.stage_name

        outcomes_known = self.outcomes_known

        outcomes_needed = self.outcomes_needed

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "stage_id": stage_id,
                "stage_name": stage_name,
                "outcomes_known": outcomes_known,
                "outcomes_needed": outcomes_needed,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        stage_id = d.pop("stage_id")

        stage_name = d.pop("stage_name")

        outcomes_known = d.pop("outcomes_known")

        outcomes_needed = d.pop("outcomes_needed")

        stage_not_measured_yet = cls(
            stage_id=stage_id,
            stage_name=stage_name,
            outcomes_known=outcomes_known,
            outcomes_needed=outcomes_needed,
        )

        stage_not_measured_yet.additional_properties = d
        return stage_not_measured_yet

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
