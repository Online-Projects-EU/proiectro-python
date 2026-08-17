from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
import datetime






T = TypeVar("T", bound="ProjectTeamMember")



@_attrs_define
class ProjectTeamMember:
    """ Team member booked for a project

        Attributes:
            id (str):
            member_name (str):
            member_email (str):
            start_date (datetime.date):
            hours_per_day (int):
            name (str):
            is_active (bool):
            member_avatar_url (None | str | Unset):
            end_date (datetime.date | None | Unset):
     """

    id: str
    member_name: str
    member_email: str
    start_date: datetime.date
    hours_per_day: int
    name: str
    is_active: bool
    member_avatar_url: None | str | Unset = UNSET
    end_date: datetime.date | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        id = self.id

        member_name = self.member_name

        member_email = self.member_email

        start_date = self.start_date.isoformat()

        hours_per_day = self.hours_per_day

        name = self.name

        is_active = self.is_active

        member_avatar_url: None | str | Unset
        if isinstance(self.member_avatar_url, Unset):
            member_avatar_url = UNSET
        else:
            member_avatar_url = self.member_avatar_url

        end_date: None | str | Unset
        if isinstance(self.end_date, Unset):
            end_date = UNSET
        elif isinstance(self.end_date, datetime.date):
            end_date = self.end_date.isoformat()
        else:
            end_date = self.end_date


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "id": id,
            "member_name": member_name,
            "member_email": member_email,
            "start_date": start_date,
            "hours_per_day": hours_per_day,
            "name": name,
            "is_active": is_active,
        })
        if member_avatar_url is not UNSET:
            field_dict["member_avatar_url"] = member_avatar_url
        if end_date is not UNSET:
            field_dict["end_date"] = end_date

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        member_name = d.pop("member_name")

        member_email = d.pop("member_email")

        start_date = isoparse(d.pop("start_date")).date()




        hours_per_day = d.pop("hours_per_day")

        name = d.pop("name")

        is_active = d.pop("is_active")

        def _parse_member_avatar_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        member_avatar_url = _parse_member_avatar_url(d.pop("member_avatar_url", UNSET))


        def _parse_end_date(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                end_date_type_0 = isoparse(data).date()



                return end_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None | Unset, data)

        end_date = _parse_end_date(d.pop("end_date", UNSET))


        project_team_member = cls(
            id=id,
            member_name=member_name,
            member_email=member_email,
            start_date=start_date,
            hours_per_day=hours_per_day,
            name=name,
            is_active=is_active,
            member_avatar_url=member_avatar_url,
            end_date=end_date,
        )


        project_team_member.additional_properties = d
        return project_team_member

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
