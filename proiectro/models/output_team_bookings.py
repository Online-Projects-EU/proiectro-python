from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.output_team_booking import OutputTeamBooking


T = TypeVar("T", bound="OutputTeamBookings")


@_attrs_define
class OutputTeamBookings:
    """Output schema for listing team bookings

    Attributes:
        bookings (list[OutputTeamBooking]):
        total (int):
    """

    bookings: list[OutputTeamBooking]
    total: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bookings = []
        for bookings_item_data in self.bookings:
            bookings_item = bookings_item_data.to_dict()
            bookings.append(bookings_item)

        total = self.total

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "bookings": bookings,
                "total": total,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.output_team_booking import OutputTeamBooking

        d = dict(src_dict)
        bookings = []
        _bookings = d.pop("bookings")
        for bookings_item_data in _bookings:
            bookings_item = OutputTeamBooking.from_dict(bookings_item_data)

            bookings.append(bookings_item)

        total = d.pop("total")

        output_team_bookings = cls(
            bookings=bookings,
            total=total,
        )

        output_team_bookings.additional_properties = d
        return output_team_bookings

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
