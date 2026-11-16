from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.belief_over_time_point import BeliefOverTimePoint


T = TypeVar("T", bound="OutputBeliefOverTime")


@_attrs_define
class OutputBeliefOverTime:
    """How a belief's figure moved as its cases arrived, oldest first, with the likely range at each moment.

    Attributes:
        id (str):
        statement (str):
        reading (str):
        guess (float | None | str | Unset):
        bar (float | None | str | Unset):
        points (list[BeliefOverTimePoint] | Unset):
    """

    id: str
    statement: str
    reading: str
    guess: float | None | str | Unset = UNSET
    bar: float | None | str | Unset = UNSET
    points: list[BeliefOverTimePoint] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        statement = self.statement

        reading = self.reading

        guess: float | None | str | Unset
        if isinstance(self.guess, Unset):
            guess = UNSET
        else:
            guess = self.guess

        bar: float | None | str | Unset
        if isinstance(self.bar, Unset):
            bar = UNSET
        else:
            bar = self.bar

        points: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.points, Unset):
            points = []
            for points_item_data in self.points:
                points_item = points_item_data.to_dict()
                points.append(points_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "statement": statement,
                "reading": reading,
            }
        )
        if guess is not UNSET:
            field_dict["guess"] = guess
        if bar is not UNSET:
            field_dict["bar"] = bar
        if points is not UNSET:
            field_dict["points"] = points

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.belief_over_time_point import BeliefOverTimePoint

        d = dict(src_dict)
        id = d.pop("id")

        statement = d.pop("statement")

        reading = d.pop("reading")

        def _parse_guess(data: object) -> float | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | str | Unset, data)

        guess = _parse_guess(d.pop("guess", UNSET))

        def _parse_bar(data: object) -> float | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | str | Unset, data)

        bar = _parse_bar(d.pop("bar", UNSET))

        _points = d.pop("points", UNSET)
        points: list[BeliefOverTimePoint] | Unset = UNSET
        if _points is not UNSET:
            points = []
            for points_item_data in _points:
                points_item = BeliefOverTimePoint.from_dict(points_item_data)

                points.append(points_item)

        output_belief_over_time = cls(
            id=id,
            statement=statement,
            reading=reading,
            guess=guess,
            bar=bar,
            points=points,
        )

        output_belief_over_time.additional_properties = d
        return output_belief_over_time

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
