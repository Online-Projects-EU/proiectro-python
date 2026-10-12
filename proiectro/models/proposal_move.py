from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ProposalMove")


@_attrs_define
class ProposalMove:
    """A stage a proposal may move to next, per FunnelStage.MOVES. `instructions` is what the stage asks
    the mover to confirm having done, empty when it asks nothing. `sequence_no` is the stage's place in its
    funnel, so a client can tell a step forward from a step back.

        Attributes:
            id (str):
            name (str):
            stage_type (str):
            instructions (str | Unset):  Default: ''.
            sequence_no (int | Unset):  Default: 0.
    """

    id: str
    name: str
    stage_type: str
    instructions: str | Unset = ""
    sequence_no: int | Unset = 0
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        stage_type = self.stage_type

        instructions = self.instructions

        sequence_no = self.sequence_no

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "stage_type": stage_type,
            }
        )
        if instructions is not UNSET:
            field_dict["instructions"] = instructions
        if sequence_no is not UNSET:
            field_dict["sequence_no"] = sequence_no

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        stage_type = d.pop("stage_type")

        instructions = d.pop("instructions", UNSET)

        sequence_no = d.pop("sequence_no", UNSET)

        proposal_move = cls(
            id=id,
            name=name,
            stage_type=stage_type,
            instructions=instructions,
            sequence_no=sequence_no,
        )

        proposal_move.additional_properties = d
        return proposal_move

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
