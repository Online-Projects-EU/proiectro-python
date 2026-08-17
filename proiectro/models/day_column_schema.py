from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from dateutil.parser import isoparse
from typing import cast
import datetime






T = TypeVar("T", bound="DayColumnSchema")



@_attrs_define
class DayColumnSchema:
    """ Column header for a day in the week.

    Carries the day itself. The template renders the weekday with |date:"D" (which Django
    translates) and the day/month with |date:"SHORT_DATE_FORMAT" (which is day-first in Romanian).

        Attributes:
            date (datetime.date):
            is_today (bool):
     """

    date: datetime.date
    is_today: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        date = self.date.isoformat()

        is_today = self.is_today


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "date": date,
            "is_today": is_today,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        date = isoparse(d.pop("date")).date()




        is_today = d.pop("is_today")

        day_column_schema = cls(
            date=date,
            is_today=is_today,
        )


        day_column_schema.additional_properties = d
        return day_column_schema

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
