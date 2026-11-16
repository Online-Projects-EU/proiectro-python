from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.belief_estimate import BeliefEstimate


T = TypeVar("T", bound="OutputBelief")


@_attrs_define
class OutputBelief:
    """
    Attributes:
        id (str):
        statement (str):
        evidence (str):
        evidence_label (str):
        reading (str):
        count_from (datetime.datetime):
        created_at (datetime.datetime):
        estimate (BeliefEstimate): A figure with what it rests on. A share carries `rate` and `successes`; an average
            carries `average`
            and `middle`. `low` and `high` are the two ends of the likely range. Everything is empty while `needed`
            cases are still missing.
        counted_alone (BeliefEstimate): A figure with what it rests on. A share carries `rate` and `successes`; an
            average carries `average`
            and `middle`. `low` and `high` are the two ends of the likely range. Everything is empty while `needed`
            cases are still missing.
        split_by (str | Unset):  Default: ''.
        form (None | str | Unset):
        form_name (None | str | Unset):
        field_name (str | Unset):  Default: ''.
        field_label (str | Unset):  Default: ''.
        option (str | Unset):  Default: ''.
        threshold (float | None | str | Unset):
        threshold_side (str | Unset):  Default: ''.
        guess (float | None | str | Unset):
        guess_weight (int | None | Unset):
        guess_is_autonomous (bool | Unset):  Default: False.
        bar (float | None | str | Unset):
        includes_history (bool | Unset):  Default: False.
        updated_at (datetime.datetime | None | Unset):
        chance_above_bar (float | None | str | Unset):
        verdict (str | Unset):  Default: ''.
    """

    id: str
    statement: str
    evidence: str
    evidence_label: str
    reading: str
    count_from: datetime.datetime
    created_at: datetime.datetime
    estimate: BeliefEstimate
    counted_alone: BeliefEstimate
    split_by: str | Unset = ""
    form: None | str | Unset = UNSET
    form_name: None | str | Unset = UNSET
    field_name: str | Unset = ""
    field_label: str | Unset = ""
    option: str | Unset = ""
    threshold: float | None | str | Unset = UNSET
    threshold_side: str | Unset = ""
    guess: float | None | str | Unset = UNSET
    guess_weight: int | None | Unset = UNSET
    guess_is_autonomous: bool | Unset = False
    bar: float | None | str | Unset = UNSET
    includes_history: bool | Unset = False
    updated_at: datetime.datetime | None | Unset = UNSET
    chance_above_bar: float | None | str | Unset = UNSET
    verdict: str | Unset = ""
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        statement = self.statement

        evidence = self.evidence

        evidence_label = self.evidence_label

        reading = self.reading

        count_from = self.count_from.isoformat()

        created_at = self.created_at.isoformat()

        estimate = self.estimate.to_dict()

        counted_alone = self.counted_alone.to_dict()

        split_by = self.split_by

        form: None | str | Unset
        if isinstance(self.form, Unset):
            form = UNSET
        else:
            form = self.form

        form_name: None | str | Unset
        if isinstance(self.form_name, Unset):
            form_name = UNSET
        else:
            form_name = self.form_name

        field_name = self.field_name

        field_label = self.field_label

        option = self.option

        threshold: float | None | str | Unset
        if isinstance(self.threshold, Unset):
            threshold = UNSET
        else:
            threshold = self.threshold

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

        guess_is_autonomous = self.guess_is_autonomous

        bar: float | None | str | Unset
        if isinstance(self.bar, Unset):
            bar = UNSET
        else:
            bar = self.bar

        includes_history = self.includes_history

        updated_at: None | str | Unset
        if isinstance(self.updated_at, Unset):
            updated_at = UNSET
        elif isinstance(self.updated_at, datetime.datetime):
            updated_at = self.updated_at.isoformat()
        else:
            updated_at = self.updated_at

        chance_above_bar: float | None | str | Unset
        if isinstance(self.chance_above_bar, Unset):
            chance_above_bar = UNSET
        else:
            chance_above_bar = self.chance_above_bar

        verdict = self.verdict

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "statement": statement,
                "evidence": evidence,
                "evidence_label": evidence_label,
                "reading": reading,
                "count_from": count_from,
                "created_at": created_at,
                "estimate": estimate,
                "counted_alone": counted_alone,
            }
        )
        if split_by is not UNSET:
            field_dict["split_by"] = split_by
        if form is not UNSET:
            field_dict["form"] = form
        if form_name is not UNSET:
            field_dict["form_name"] = form_name
        if field_name is not UNSET:
            field_dict["field_name"] = field_name
        if field_label is not UNSET:
            field_dict["field_label"] = field_label
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
        if guess_is_autonomous is not UNSET:
            field_dict["guess_is_autonomous"] = guess_is_autonomous
        if bar is not UNSET:
            field_dict["bar"] = bar
        if includes_history is not UNSET:
            field_dict["includes_history"] = includes_history
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if chance_above_bar is not UNSET:
            field_dict["chance_above_bar"] = chance_above_bar
        if verdict is not UNSET:
            field_dict["verdict"] = verdict

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.belief_estimate import BeliefEstimate

        d = dict(src_dict)
        id = d.pop("id")

        statement = d.pop("statement")

        evidence = d.pop("evidence")

        evidence_label = d.pop("evidence_label")

        reading = d.pop("reading")

        count_from = isoparse(d.pop("count_from"))

        created_at = isoparse(d.pop("created_at"))

        estimate = BeliefEstimate.from_dict(d.pop("estimate"))

        counted_alone = BeliefEstimate.from_dict(d.pop("counted_alone"))

        split_by = d.pop("split_by", UNSET)

        def _parse_form(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        form = _parse_form(d.pop("form", UNSET))

        def _parse_form_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        form_name = _parse_form_name(d.pop("form_name", UNSET))

        field_name = d.pop("field_name", UNSET)

        field_label = d.pop("field_label", UNSET)

        option = d.pop("option", UNSET)

        def _parse_threshold(data: object) -> float | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | str | Unset, data)

        threshold = _parse_threshold(d.pop("threshold", UNSET))

        threshold_side = d.pop("threshold_side", UNSET)

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

        guess_is_autonomous = d.pop("guess_is_autonomous", UNSET)

        def _parse_bar(data: object) -> float | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | str | Unset, data)

        bar = _parse_bar(d.pop("bar", UNSET))

        includes_history = d.pop("includes_history", UNSET)

        def _parse_updated_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                updated_at_type_0 = isoparse(data)

                return updated_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        updated_at = _parse_updated_at(d.pop("updated_at", UNSET))

        def _parse_chance_above_bar(data: object) -> float | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | str | Unset, data)

        chance_above_bar = _parse_chance_above_bar(d.pop("chance_above_bar", UNSET))

        verdict = d.pop("verdict", UNSET)

        output_belief = cls(
            id=id,
            statement=statement,
            evidence=evidence,
            evidence_label=evidence_label,
            reading=reading,
            count_from=count_from,
            created_at=created_at,
            estimate=estimate,
            counted_alone=counted_alone,
            split_by=split_by,
            form=form,
            form_name=form_name,
            field_name=field_name,
            field_label=field_label,
            option=option,
            threshold=threshold,
            threshold_side=threshold_side,
            guess=guess,
            guess_weight=guess_weight,
            guess_is_autonomous=guess_is_autonomous,
            bar=bar,
            includes_history=includes_history,
            updated_at=updated_at,
            chance_above_bar=chance_above_bar,
            verdict=verdict,
        )

        output_belief.additional_properties = d
        return output_belief

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
