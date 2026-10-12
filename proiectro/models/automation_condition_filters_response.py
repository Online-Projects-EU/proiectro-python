from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.automation_condition_filters_response_filters import (
        AutomationConditionFiltersResponseFilters,
    )
    from ..models.automation_condition_filters_response_operators import (
        AutomationConditionFiltersResponseOperators,
    )


T = TypeVar("T", bound="AutomationConditionFiltersResponse")


@_attrs_define
class AutomationConditionFiltersResponse:
    """Output: available condition fields and operators for an action.

    Attributes:
        filters (AutomationConditionFiltersResponseFilters):
        operators (AutomationConditionFiltersResponseOperators):
        prefix (str | Unset):  Default: ''.
        action_idx (int | Unset):  Default: 0.
    """

    filters: AutomationConditionFiltersResponseFilters
    operators: AutomationConditionFiltersResponseOperators
    prefix: str | Unset = ""
    action_idx: int | Unset = 0
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        filters = self.filters.to_dict()

        operators = self.operators.to_dict()

        prefix = self.prefix

        action_idx = self.action_idx

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "filters": filters,
                "operators": operators,
            }
        )
        if prefix is not UNSET:
            field_dict["prefix"] = prefix
        if action_idx is not UNSET:
            field_dict["action_idx"] = action_idx

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.automation_condition_filters_response_filters import (
            AutomationConditionFiltersResponseFilters,
        )
        from ..models.automation_condition_filters_response_operators import (
            AutomationConditionFiltersResponseOperators,
        )

        d = dict(src_dict)
        filters = AutomationConditionFiltersResponseFilters.from_dict(d.pop("filters"))

        operators = AutomationConditionFiltersResponseOperators.from_dict(
            d.pop("operators")
        )

        prefix = d.pop("prefix", UNSET)

        action_idx = d.pop("action_idx", UNSET)

        automation_condition_filters_response = cls(
            filters=filters,
            operators=operators,
            prefix=prefix,
            action_idx=action_idx,
        )

        automation_condition_filters_response.additional_properties = d
        return automation_condition_filters_response

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
