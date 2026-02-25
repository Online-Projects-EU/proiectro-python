from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="EditTeamBooking")


@_attrs_define
class EditTeamBooking:
    """Input schema for editing a team booking

    Attributes:
        member (str):
        start_date (str):
        end_date (str):
        name (str):
        product (None | str | Unset):
        hours_per_day (int | None | Unset):  Default: 0.
        only_working_days (bool | None | Unset):  Default: False.
    """

    member: str
    start_date: str
    end_date: str
    name: str
    product: None | str | Unset = UNSET
    hours_per_day: int | None | Unset = 0
    only_working_days: bool | None | Unset = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        member = self.member

        start_date = self.start_date

        end_date = self.end_date

        name = self.name

        product: None | str | Unset
        if isinstance(self.product, Unset):
            product = UNSET
        else:
            product = self.product

        hours_per_day: int | None | Unset
        if isinstance(self.hours_per_day, Unset):
            hours_per_day = UNSET
        else:
            hours_per_day = self.hours_per_day

        only_working_days: bool | None | Unset
        if isinstance(self.only_working_days, Unset):
            only_working_days = UNSET
        else:
            only_working_days = self.only_working_days

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "member": member,
                "start_date": start_date,
                "end_date": end_date,
                "name": name,
            }
        )
        if product is not UNSET:
            field_dict["product"] = product
        if hours_per_day is not UNSET:
            field_dict["hours_per_day"] = hours_per_day
        if only_working_days is not UNSET:
            field_dict["only_working_days"] = only_working_days

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        member = d.pop("member")

        start_date = d.pop("start_date")

        end_date = d.pop("end_date")

        name = d.pop("name")

        def _parse_product(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        product = _parse_product(d.pop("product", UNSET))

        def _parse_hours_per_day(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        hours_per_day = _parse_hours_per_day(d.pop("hours_per_day", UNSET))

        def _parse_only_working_days(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        only_working_days = _parse_only_working_days(d.pop("only_working_days", UNSET))

        edit_team_booking = cls(
            member=member,
            start_date=start_date,
            end_date=end_date,
            name=name,
            product=product,
            hours_per_day=hours_per_day,
            only_working_days=only_working_days,
        )

        edit_team_booking.additional_properties = d
        return edit_team_booking

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
