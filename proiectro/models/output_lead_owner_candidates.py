from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.output_lead_owner_candidate import OutputLeadOwnerCandidate


T = TypeVar("T", bound="OutputLeadOwnerCandidates")


@_attrs_define
class OutputLeadOwnerCandidates:
    """
    Attributes:
        candidates (list[OutputLeadOwnerCandidate] | Unset):
    """

    candidates: list[OutputLeadOwnerCandidate] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        candidates: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.candidates, Unset):
            candidates = []
            for candidates_item_data in self.candidates:
                candidates_item = candidates_item_data.to_dict()
                candidates.append(candidates_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if candidates is not UNSET:
            field_dict["candidates"] = candidates

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.output_lead_owner_candidate import OutputLeadOwnerCandidate

        d = dict(src_dict)
        _candidates = d.pop("candidates", UNSET)
        candidates: list[OutputLeadOwnerCandidate] | Unset = UNSET
        if _candidates is not UNSET:
            candidates = []
            for candidates_item_data in _candidates:
                candidates_item = OutputLeadOwnerCandidate.from_dict(
                    candidates_item_data
                )

                candidates.append(candidates_item)

        output_lead_owner_candidates = cls(
            candidates=candidates,
        )

        output_lead_owner_candidates.additional_properties = d
        return output_lead_owner_candidates

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
