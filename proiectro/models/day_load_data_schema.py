from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.booking_info_schema import BookingInfoSchema


T = TypeVar("T", bound="DayLoadDataSchema")


@_attrs_define
class DayLoadDataSchema:
    """Load data for a single day

    Attributes:
        booked (float):
        available (float):
        display (str):
        is_holiday (bool):
        is_today (bool):
        holiday_name (None | str | Unset):
        bookings (list[BookingInfoSchema] | None | Unset):
    """

    booked: float
    available: float
    display: str
    is_holiday: bool
    is_today: bool
    holiday_name: None | str | Unset = UNSET
    bookings: list[BookingInfoSchema] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        booked = self.booked

        available = self.available

        display = self.display

        is_holiday = self.is_holiday

        is_today = self.is_today

        holiday_name: None | str | Unset
        if isinstance(self.holiday_name, Unset):
            holiday_name = UNSET
        else:
            holiday_name = self.holiday_name

        bookings: list[dict[str, Any]] | None | Unset
        if isinstance(self.bookings, Unset):
            bookings = UNSET
        elif isinstance(self.bookings, list):
            bookings = []
            for bookings_type_0_item_data in self.bookings:
                bookings_type_0_item = bookings_type_0_item_data.to_dict()
                bookings.append(bookings_type_0_item)

        else:
            bookings = self.bookings

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "booked": booked,
                "available": available,
                "display": display,
                "is_holiday": is_holiday,
                "is_today": is_today,
            }
        )
        if holiday_name is not UNSET:
            field_dict["holiday_name"] = holiday_name
        if bookings is not UNSET:
            field_dict["bookings"] = bookings

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.booking_info_schema import BookingInfoSchema

        d = dict(src_dict)
        booked = d.pop("booked")

        available = d.pop("available")

        display = d.pop("display")

        is_holiday = d.pop("is_holiday")

        is_today = d.pop("is_today")

        def _parse_holiday_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        holiday_name = _parse_holiday_name(d.pop("holiday_name", UNSET))

        def _parse_bookings(data: object) -> list[BookingInfoSchema] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                bookings_type_0 = []
                _bookings_type_0 = data
                for bookings_type_0_item_data in _bookings_type_0:
                    bookings_type_0_item = BookingInfoSchema.from_dict(
                        bookings_type_0_item_data
                    )

                    bookings_type_0.append(bookings_type_0_item)

                return bookings_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[BookingInfoSchema] | None | Unset, data)

        bookings = _parse_bookings(d.pop("bookings", UNSET))

        day_load_data_schema = cls(
            booked=booked,
            available=available,
            display=display,
            is_holiday=is_holiday,
            is_today=is_today,
            holiday_name=holiday_name,
            bookings=bookings,
        )

        day_load_data_schema.additional_properties = d
        return day_load_data_schema

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
