from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.automation_filters_response_filters import (
        AutomationFiltersResponseFilters,
    )
    from ..models.automation_filters_response_operators import (
        AutomationFiltersResponseOperators,
    )


T = TypeVar("T", bound="AutomationFiltersResponse")


@_attrs_define
class AutomationFiltersResponse:
    """Output: available filters and operators for a trigger.

    Attributes:
        filters (AutomationFiltersResponseFilters):
        operators (AutomationFiltersResponseOperators):
    """

    filters: AutomationFiltersResponseFilters
    operators: AutomationFiltersResponseOperators
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        filters = self.filters.to_dict()

        operators = self.operators.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "filters": filters,
                "operators": operators,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.automation_filters_response_filters import (
            AutomationFiltersResponseFilters,
        )
        from ..models.automation_filters_response_operators import (
            AutomationFiltersResponseOperators,
        )

        d = dict(src_dict)
        filters = AutomationFiltersResponseFilters.from_dict(d.pop("filters"))

        operators = AutomationFiltersResponseOperators.from_dict(d.pop("operators"))

        automation_filters_response = cls(
            filters=filters,
            operators=operators,
        )

        automation_filters_response.additional_properties = d
        return automation_filters_response

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
