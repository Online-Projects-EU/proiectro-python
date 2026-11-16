from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.belief_estimate import BeliefEstimate


T = TypeVar("T", bound="BeliefSplitRow")


@_attrs_define
class BeliefSplitRow:
    """
    Attributes:
        key (str):
        name (str):
        estimate (BeliefEstimate): A figure with what it rests on. A share carries `rate` and `successes`; an average
            carries `average`
            and `middle`. `low` and `high` are the two ends of the likely range. Everything is empty while `needed`
            cases are still missing.
        verdict (str | Unset):  Default: 'cannot_tell'.
    """

    key: str
    name: str
    estimate: BeliefEstimate
    verdict: str | Unset = "cannot_tell"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        key = self.key

        name = self.name

        estimate = self.estimate.to_dict()

        verdict = self.verdict

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "key": key,
                "name": name,
                "estimate": estimate,
            }
        )
        if verdict is not UNSET:
            field_dict["verdict"] = verdict

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.belief_estimate import BeliefEstimate

        d = dict(src_dict)
        key = d.pop("key")

        name = d.pop("name")

        estimate = BeliefEstimate.from_dict(d.pop("estimate"))

        verdict = d.pop("verdict", UNSET)

        belief_split_row = cls(
            key=key,
            name=name,
            estimate=estimate,
            verdict=verdict,
        )

        belief_split_row.additional_properties = d
        return belief_split_row

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
