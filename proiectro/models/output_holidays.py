from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.output_holiday import OutputHoliday


T = TypeVar("T", bound="OutputHolidays")


@_attrs_define
class OutputHolidays:
    """Output schema for listing holidays

    Attributes:
        holidays (list[OutputHoliday]):
        total (int):
    """

    holidays: list[OutputHoliday]
    total: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        holidays = []
        for holidays_item_data in self.holidays:
            holidays_item = holidays_item_data.to_dict()
            holidays.append(holidays_item)

        total = self.total

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "holidays": holidays,
                "total": total,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.output_holiday import OutputHoliday

        d = dict(src_dict)
        holidays = []
        _holidays = d.pop("holidays")
        for holidays_item_data in _holidays:
            holidays_item = OutputHoliday.from_dict(holidays_item_data)

            holidays.append(holidays_item)

        total = d.pop("total")

        output_holidays = cls(
            holidays=holidays,
            total=total,
        )

        output_holidays.additional_properties = d
        return output_holidays

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
