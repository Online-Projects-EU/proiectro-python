from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="OutputRFPItem")


@_attrs_define
class OutputRFPItem:
    """Single RFP in tenant's list

    Attributes:
        id (str):
        name (str):
        internal_code (None | str):
        category (str):
        category_display (str):
        currency_code (str):
        budget_min (float | None | str):
        budget_max (float | None | str):
        submission_deadline (str):
        status (str):
        status_display (str):
    """

    id: str
    name: str
    internal_code: None | str
    category: str
    category_display: str
    currency_code: str
    budget_min: float | None | str
    budget_max: float | None | str
    submission_deadline: str
    status: str
    status_display: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        internal_code: None | str
        internal_code = self.internal_code

        category = self.category

        category_display = self.category_display

        currency_code = self.currency_code

        budget_min: float | None | str
        budget_min = self.budget_min

        budget_max: float | None | str
        budget_max = self.budget_max

        submission_deadline = self.submission_deadline

        status = self.status

        status_display = self.status_display

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "internal_code": internal_code,
                "category": category,
                "category_display": category_display,
                "currency_code": currency_code,
                "budget_min": budget_min,
                "budget_max": budget_max,
                "submission_deadline": submission_deadline,
                "status": status,
                "status_display": status_display,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        def _parse_internal_code(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        internal_code = _parse_internal_code(d.pop("internal_code"))

        category = d.pop("category")

        category_display = d.pop("category_display")

        currency_code = d.pop("currency_code")

        def _parse_budget_min(data: object) -> float | None | str:
            if data is None:
                return data
            return cast(float | None | str, data)

        budget_min = _parse_budget_min(d.pop("budget_min"))

        def _parse_budget_max(data: object) -> float | None | str:
            if data is None:
                return data
            return cast(float | None | str, data)

        budget_max = _parse_budget_max(d.pop("budget_max"))

        submission_deadline = d.pop("submission_deadline")

        status = d.pop("status")

        status_display = d.pop("status_display")

        output_rfp_item = cls(
            id=id,
            name=name,
            internal_code=internal_code,
            category=category,
            category_display=category_display,
            currency_code=currency_code,
            budget_min=budget_min,
            budget_max=budget_max,
            submission_deadline=submission_deadline,
            status=status,
            status_display=status_display,
        )

        output_rfp_item.additional_properties = d
        return output_rfp_item

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
