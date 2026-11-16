from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.edit_belief_split_by_type_0 import EditBeliefSplitByType0
from ..types import UNSET, Unset

T = TypeVar("T", bound="EditBelief")


@_attrs_define
class EditBelief:
    """Only what you send changes. What a belief counts as evidence is fixed when it is added: a different
    question is a different belief. Send `guess`, `bar` or `split_by` empty to remove it.

        Attributes:
            statement (None | str | Unset):
            split_by (EditBeliefSplitByType0 | None | Unset):
            guess (float | None | str | Unset):
            guess_weight (int | None | Unset):
            bar (float | None | str | Unset):
            count_from (None | str | Unset):
    """

    statement: None | str | Unset = UNSET
    split_by: EditBeliefSplitByType0 | None | Unset = UNSET
    guess: float | None | str | Unset = UNSET
    guess_weight: int | None | Unset = UNSET
    bar: float | None | str | Unset = UNSET
    count_from: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        statement: None | str | Unset
        if isinstance(self.statement, Unset):
            statement = UNSET
        else:
            statement = self.statement

        split_by: None | str | Unset
        if isinstance(self.split_by, Unset):
            split_by = UNSET
        elif isinstance(self.split_by, EditBeliefSplitByType0):
            split_by = self.split_by.value
        else:
            split_by = self.split_by

        guess: float | None | str | Unset
        if isinstance(self.guess, Unset):
            guess = UNSET
        else:
            guess = self.guess

        guess_weight: int | None | Unset
        if isinstance(self.guess_weight, Unset):
            guess_weight = UNSET
        else:
            guess_weight = self.guess_weight

        bar: float | None | str | Unset
        if isinstance(self.bar, Unset):
            bar = UNSET
        else:
            bar = self.bar

        count_from: None | str | Unset
        if isinstance(self.count_from, Unset):
            count_from = UNSET
        else:
            count_from = self.count_from

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if statement is not UNSET:
            field_dict["statement"] = statement
        if split_by is not UNSET:
            field_dict["split_by"] = split_by
        if guess is not UNSET:
            field_dict["guess"] = guess
        if guess_weight is not UNSET:
            field_dict["guess_weight"] = guess_weight
        if bar is not UNSET:
            field_dict["bar"] = bar
        if count_from is not UNSET:
            field_dict["count_from"] = count_from

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_statement(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        statement = _parse_statement(d.pop("statement", UNSET))

        def _parse_split_by(data: object) -> EditBeliefSplitByType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                split_by_type_0 = EditBeliefSplitByType0(data)

                return split_by_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(EditBeliefSplitByType0 | None | Unset, data)

        split_by = _parse_split_by(d.pop("split_by", UNSET))

        def _parse_guess(data: object) -> float | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | str | Unset, data)

        guess = _parse_guess(d.pop("guess", UNSET))

        def _parse_guess_weight(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        guess_weight = _parse_guess_weight(d.pop("guess_weight", UNSET))

        def _parse_bar(data: object) -> float | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | str | Unset, data)

        bar = _parse_bar(d.pop("bar", UNSET))

        def _parse_count_from(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        count_from = _parse_count_from(d.pop("count_from", UNSET))

        edit_belief = cls(
            statement=statement,
            split_by=split_by,
            guess=guess,
            guess_weight=guess_weight,
            bar=bar,
            count_from=count_from,
        )

        edit_belief.additional_properties = d
        return edit_belief

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
