from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.member_availability_days import MemberAvailabilityDays


T = TypeVar("T", bound="MemberAvailability")


@_attrs_define
class MemberAvailability:
    """
    Attributes:
        member (str):
        member_timezone (str):
        days (MemberAvailabilityDays):
    """

    member: str
    member_timezone: str
    days: MemberAvailabilityDays
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        member = self.member

        member_timezone = self.member_timezone

        days = self.days.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "member": member,
                "member_timezone": member_timezone,
                "days": days,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.member_availability_days import MemberAvailabilityDays

        d = dict(src_dict)
        member = d.pop("member")

        member_timezone = d.pop("member_timezone")

        days = MemberAvailabilityDays.from_dict(d.pop("days"))

        member_availability = cls(
            member=member,
            member_timezone=member_timezone,
            days=days,
        )

        member_availability.additional_properties = d
        return member_availability

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
