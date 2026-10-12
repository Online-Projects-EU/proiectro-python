from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AddRFP")


@_attrs_define
class AddRFP:
    """Input schema for creating a new RFP

    Attributes:
        name (str):
        category (str):
        currency (str):
        submission_deadline (str):
        internal_code (None | str | Unset):
        description (None | str | Unset):
        budget_min (float | None | str | Unset):
        budget_max (float | None | str | Unset):
    """

    name: str
    category: str
    currency: str
    submission_deadline: str
    internal_code: None | str | Unset = UNSET
    description: None | str | Unset = UNSET
    budget_min: float | None | str | Unset = UNSET
    budget_max: float | None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        category = self.category

        currency = self.currency

        submission_deadline = self.submission_deadline

        internal_code: None | str | Unset
        if isinstance(self.internal_code, Unset):
            internal_code = UNSET
        else:
            internal_code = self.internal_code

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        budget_min: float | None | str | Unset
        if isinstance(self.budget_min, Unset):
            budget_min = UNSET
        else:
            budget_min = self.budget_min

        budget_max: float | None | str | Unset
        if isinstance(self.budget_max, Unset):
            budget_max = UNSET
        else:
            budget_max = self.budget_max

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "category": category,
                "currency": currency,
                "submission_deadline": submission_deadline,
            }
        )
        if internal_code is not UNSET:
            field_dict["internal_code"] = internal_code
        if description is not UNSET:
            field_dict["description"] = description
        if budget_min is not UNSET:
            field_dict["budget_min"] = budget_min
        if budget_max is not UNSET:
            field_dict["budget_max"] = budget_max

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        category = d.pop("category")

        currency = d.pop("currency")

        submission_deadline = d.pop("submission_deadline")

        def _parse_internal_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        internal_code = _parse_internal_code(d.pop("internal_code", UNSET))

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_budget_min(data: object) -> float | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | str | Unset, data)

        budget_min = _parse_budget_min(d.pop("budget_min", UNSET))

        def _parse_budget_max(data: object) -> float | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | str | Unset, data)

        budget_max = _parse_budget_max(d.pop("budget_max", UNSET))

        add_rfp = cls(
            name=name,
            category=category,
            currency=currency,
            submission_deadline=submission_deadline,
            internal_code=internal_code,
            description=description,
            budget_min=budget_min,
            budget_max=budget_max,
        )

        add_rfp.additional_properties = d
        return add_rfp

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
