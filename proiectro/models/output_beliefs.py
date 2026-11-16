from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.output_belief import OutputBelief
    from ..models.output_beliefs_summary import OutputBeliefsSummary


T = TypeVar("T", bound="OutputBeliefs")


@_attrs_define
class OutputBeliefs:
    """
    Attributes:
        summary (OutputBeliefsSummary):
        beliefs (list[OutputBelief] | Unset):
    """

    summary: OutputBeliefsSummary
    beliefs: list[OutputBelief] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        summary = self.summary.to_dict()

        beliefs: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.beliefs, Unset):
            beliefs = []
            for beliefs_item_data in self.beliefs:
                beliefs_item = beliefs_item_data.to_dict()
                beliefs.append(beliefs_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "summary": summary,
            }
        )
        if beliefs is not UNSET:
            field_dict["beliefs"] = beliefs

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.output_belief import OutputBelief
        from ..models.output_beliefs_summary import OutputBeliefsSummary

        d = dict(src_dict)
        summary = OutputBeliefsSummary.from_dict(d.pop("summary"))

        _beliefs = d.pop("beliefs", UNSET)
        beliefs: list[OutputBelief] | Unset = UNSET
        if _beliefs is not UNSET:
            beliefs = []
            for beliefs_item_data in _beliefs:
                beliefs_item = OutputBelief.from_dict(beliefs_item_data)

                beliefs.append(beliefs_item)

        output_beliefs = cls(
            summary=summary,
            beliefs=beliefs,
        )

        output_beliefs.additional_properties = d
        return output_beliefs

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
