from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.chain_finish import ChainFinish
    from ..models.chain_next_step import ChainNextStep


T = TypeVar("T", bound="ChainState")


@_attrs_define
class ChainState:
    """
    Attributes:
        key (str):
        name (str):
        exits (int | Unset):  Default: 0.
        next_steps (list[ChainNextStep] | Unset):
        finishes (list[ChainFinish] | Unset):
        stays_ended (int | Unset):  Default: 0.
        usual_stay_days (int | None | Unset):
        middle_stay_days (int | None | Unset):
    """

    key: str
    name: str
    exits: int | Unset = 0
    next_steps: list[ChainNextStep] | Unset = UNSET
    finishes: list[ChainFinish] | Unset = UNSET
    stays_ended: int | Unset = 0
    usual_stay_days: int | None | Unset = UNSET
    middle_stay_days: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        key = self.key

        name = self.name

        exits = self.exits

        next_steps: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.next_steps, Unset):
            next_steps = []
            for next_steps_item_data in self.next_steps:
                next_steps_item = next_steps_item_data.to_dict()
                next_steps.append(next_steps_item)

        finishes: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.finishes, Unset):
            finishes = []
            for finishes_item_data in self.finishes:
                finishes_item = finishes_item_data.to_dict()
                finishes.append(finishes_item)

        stays_ended = self.stays_ended

        usual_stay_days: int | None | Unset
        if isinstance(self.usual_stay_days, Unset):
            usual_stay_days = UNSET
        else:
            usual_stay_days = self.usual_stay_days

        middle_stay_days: int | None | Unset
        if isinstance(self.middle_stay_days, Unset):
            middle_stay_days = UNSET
        else:
            middle_stay_days = self.middle_stay_days

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "key": key,
                "name": name,
            }
        )
        if exits is not UNSET:
            field_dict["exits"] = exits
        if next_steps is not UNSET:
            field_dict["next_steps"] = next_steps
        if finishes is not UNSET:
            field_dict["finishes"] = finishes
        if stays_ended is not UNSET:
            field_dict["stays_ended"] = stays_ended
        if usual_stay_days is not UNSET:
            field_dict["usual_stay_days"] = usual_stay_days
        if middle_stay_days is not UNSET:
            field_dict["middle_stay_days"] = middle_stay_days

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.chain_finish import ChainFinish
        from ..models.chain_next_step import ChainNextStep

        d = dict(src_dict)
        key = d.pop("key")

        name = d.pop("name")

        exits = d.pop("exits", UNSET)

        _next_steps = d.pop("next_steps", UNSET)
        next_steps: list[ChainNextStep] | Unset = UNSET
        if _next_steps is not UNSET:
            next_steps = []
            for next_steps_item_data in _next_steps:
                next_steps_item = ChainNextStep.from_dict(next_steps_item_data)

                next_steps.append(next_steps_item)

        _finishes = d.pop("finishes", UNSET)
        finishes: list[ChainFinish] | Unset = UNSET
        if _finishes is not UNSET:
            finishes = []
            for finishes_item_data in _finishes:
                finishes_item = ChainFinish.from_dict(finishes_item_data)

                finishes.append(finishes_item)

        stays_ended = d.pop("stays_ended", UNSET)

        def _parse_usual_stay_days(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        usual_stay_days = _parse_usual_stay_days(d.pop("usual_stay_days", UNSET))

        def _parse_middle_stay_days(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        middle_stay_days = _parse_middle_stay_days(d.pop("middle_stay_days", UNSET))

        chain_state = cls(
            key=key,
            name=name,
            exits=exits,
            next_steps=next_steps,
            finishes=finishes,
            stays_ended=stays_ended,
            usual_stay_days=usual_stay_days,
            middle_stay_days=middle_stay_days,
        )

        chain_state.additional_properties = d
        return chain_state

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
