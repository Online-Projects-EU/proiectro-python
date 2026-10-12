from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.my_booking_item import MyBookingItem


T = TypeVar("T", bound="OutputMyBookings")


@_attrs_define
class OutputMyBookings:
    """Cross-tenant bookings for the current user

    Attributes:
        bookings (list[MyBookingItem]):
        total_count (int):
        current_count (int):
        upcoming_count (int):
    """

    bookings: list[MyBookingItem]
    total_count: int
    current_count: int
    upcoming_count: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bookings = []
        for bookings_item_data in self.bookings:
            bookings_item = bookings_item_data.to_dict()
            bookings.append(bookings_item)

        total_count = self.total_count

        current_count = self.current_count

        upcoming_count = self.upcoming_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "bookings": bookings,
                "total_count": total_count,
                "current_count": current_count,
                "upcoming_count": upcoming_count,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.my_booking_item import MyBookingItem

        d = dict(src_dict)
        bookings = []
        _bookings = d.pop("bookings")
        for bookings_item_data in _bookings:
            bookings_item = MyBookingItem.from_dict(bookings_item_data)

            bookings.append(bookings_item)

        total_count = d.pop("total_count")

        current_count = d.pop("current_count")

        upcoming_count = d.pop("upcoming_count")

        output_my_bookings = cls(
            bookings=bookings,
            total_count=total_count,
            current_count=current_count,
            upcoming_count=upcoming_count,
        )

        output_my_bookings.additional_properties = d
        return output_my_bookings

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
