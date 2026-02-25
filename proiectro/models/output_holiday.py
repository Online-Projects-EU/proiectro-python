from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

T = TypeVar("T", bound="OutputHoliday")


@_attrs_define
class OutputHoliday:
    """Output schema for a single holiday

    Attributes:
        id (str):
        date (datetime.date):
        date_display (str):
        name (str):
        territory (str):
    """

    id: str
    date: datetime.date
    date_display: str
    name: str
    territory: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        date = self.date.isoformat()

        date_display = self.date_display

        name = self.name

        territory = self.territory

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "date": date,
                "date_display": date_display,
                "name": name,
                "territory": territory,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        date = isoparse(d.pop("date")).date()

        date_display = d.pop("date_display")

        name = d.pop("name")

        territory = d.pop("territory")

        output_holiday = cls(
            id=id,
            date=date,
            date_display=date_display,
            name=name,
            territory=territory,
        )

        output_holiday.additional_properties = d
        return output_holiday

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
