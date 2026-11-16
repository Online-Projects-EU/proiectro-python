from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.belief_estimate import BeliefEstimate


T = TypeVar("T", bound="ChainNextStep")


@_attrs_define
class ChainNextStep:
    """
    Attributes:
        key (str):
        name (str):
        estimate (BeliefEstimate): A figure with what it rests on. A share carries `rate` and `successes`; an average
            carries `average`
            and `middle`. `low` and `high` are the two ends of the likely range. Everything is empty while `needed`
            cases are still missing.
    """

    key: str
    name: str
    estimate: BeliefEstimate
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        key = self.key

        name = self.name

        estimate = self.estimate.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "key": key,
                "name": name,
                "estimate": estimate,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.belief_estimate import BeliefEstimate

        d = dict(src_dict)
        key = d.pop("key")

        name = d.pop("name")

        estimate = BeliefEstimate.from_dict(d.pop("estimate"))

        chain_next_step = cls(
            key=key,
            name=name,
            estimate=estimate,
        )

        chain_next_step.additional_properties = d
        return chain_next_step

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
