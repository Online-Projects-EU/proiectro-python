from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.add_belief_evidence import AddBeliefEvidence
from ..models.add_belief_split_by_type_0 import AddBeliefSplitByType0
from ..models.add_belief_threshold_side_type_0 import AddBeliefThresholdSideType0
from ..types import UNSET, Unset

T = TypeVar("T", bound="AddBelief")


@_attrs_define
class AddBelief:
    """A belief names what is counted as evidence and, optionally, your own starting guess. For evidence
    `form`, name the form and one of its questions: a yes/no question is counted as it is, a choice question
    by one `option`, and a number either against a `threshold` or, with none, as an average. `guess` and
    `bar` are a percentage from 0 to 100 for a share and a plain number for an average.

        Attributes:
            statement (str):
            evidence (AddBeliefEvidence):
            split_by (AddBeliefSplitByType0 | None | Unset):
            form (None | str | Unset):
            field_name (None | str | Unset):
            option (None | str | Unset):
            threshold (float | None | str | Unset):
            threshold_side (AddBeliefThresholdSideType0 | None | Unset):
            guess (float | None | str | Unset):
            guess_weight (int | None | Unset):
            bar (float | None | str | Unset):
            count_from (None | str | Unset):
    """

    statement: str
    evidence: AddBeliefEvidence
    split_by: AddBeliefSplitByType0 | None | Unset = UNSET
    form: None | str | Unset = UNSET
    field_name: None | str | Unset = UNSET
    option: None | str | Unset = UNSET
    threshold: float | None | str | Unset = UNSET
    threshold_side: AddBeliefThresholdSideType0 | None | Unset = UNSET
    guess: float | None | str | Unset = UNSET
    guess_weight: int | None | Unset = UNSET
    bar: float | None | str | Unset = UNSET
    count_from: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        statement = self.statement

        evidence = self.evidence.value

        split_by: None | str | Unset
        if isinstance(self.split_by, Unset):
            split_by = UNSET
        elif isinstance(self.split_by, AddBeliefSplitByType0):
            split_by = self.split_by.value
        else:
            split_by = self.split_by

        form: None | str | Unset
        if isinstance(self.form, Unset):
            form = UNSET
        else:
            form = self.form

        field_name: None | str | Unset
        if isinstance(self.field_name, Unset):
            field_name = UNSET
        else:
            field_name = self.field_name

        option: None | str | Unset
        if isinstance(self.option, Unset):
            option = UNSET
        else:
            option = self.option

        threshold: float | None | str | Unset
        if isinstance(self.threshold, Unset):
            threshold = UNSET
        else:
            threshold = self.threshold

        threshold_side: None | str | Unset
        if isinstance(self.threshold_side, Unset):
            threshold_side = UNSET
        elif isinstance(self.threshold_side, AddBeliefThresholdSideType0):
            threshold_side = self.threshold_side.value
        else:
            threshold_side = self.threshold_side

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
        field_dict.update(
            {
                "statement": statement,
                "evidence": evidence,
            }
        )
        if split_by is not UNSET:
            field_dict["split_by"] = split_by
        if form is not UNSET:
            field_dict["form"] = form
        if field_name is not UNSET:
            field_dict["field_name"] = field_name
        if option is not UNSET:
            field_dict["option"] = option
        if threshold is not UNSET:
            field_dict["threshold"] = threshold
        if threshold_side is not UNSET:
            field_dict["threshold_side"] = threshold_side
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
        statement = d.pop("statement")

        evidence = AddBeliefEvidence(d.pop("evidence"))

        def _parse_split_by(data: object) -> AddBeliefSplitByType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                split_by_type_0 = AddBeliefSplitByType0(data)

                return split_by_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(AddBeliefSplitByType0 | None | Unset, data)

        split_by = _parse_split_by(d.pop("split_by", UNSET))

        def _parse_form(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        form = _parse_form(d.pop("form", UNSET))

        def _parse_field_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        field_name = _parse_field_name(d.pop("field_name", UNSET))

        def _parse_option(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        option = _parse_option(d.pop("option", UNSET))

        def _parse_threshold(data: object) -> float | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | str | Unset, data)

        threshold = _parse_threshold(d.pop("threshold", UNSET))

        def _parse_threshold_side(
            data: object,
        ) -> AddBeliefThresholdSideType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                threshold_side_type_0 = AddBeliefThresholdSideType0(data)

                return threshold_side_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(AddBeliefThresholdSideType0 | None | Unset, data)

        threshold_side = _parse_threshold_side(d.pop("threshold_side", UNSET))

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

        add_belief = cls(
            statement=statement,
            evidence=evidence,
            split_by=split_by,
            form=form,
            field_name=field_name,
            option=option,
            threshold=threshold,
            threshold_side=threshold_side,
            guess=guess,
            guess_weight=guess_weight,
            bar=bar,
            count_from=count_from,
        )

        add_belief.additional_properties = d
        return add_belief

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
