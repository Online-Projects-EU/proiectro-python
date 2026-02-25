from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="OutputTeamBooking")


@_attrs_define
class OutputTeamBooking:
    """Output schema for a single team booking

    Attributes:
        id (str):
        member_id (str):
        member_name (str):
        project_id (str):
        project_name (str):
        start_date (str):
        end_date (str):
        hours_per_day (int):
        name (str):
        member_avatar_url (None | str | Unset):
        product_id (None | str | Unset):
        product_name (None | str | Unset):
    """

    id: str
    member_id: str
    member_name: str
    project_id: str
    project_name: str
    start_date: str
    end_date: str
    hours_per_day: int
    name: str
    member_avatar_url: None | str | Unset = UNSET
    product_id: None | str | Unset = UNSET
    product_name: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        member_id = self.member_id

        member_name = self.member_name

        project_id = self.project_id

        project_name = self.project_name

        start_date = self.start_date

        end_date = self.end_date

        hours_per_day = self.hours_per_day

        name = self.name

        member_avatar_url: None | str | Unset
        if isinstance(self.member_avatar_url, Unset):
            member_avatar_url = UNSET
        else:
            member_avatar_url = self.member_avatar_url

        product_id: None | str | Unset
        if isinstance(self.product_id, Unset):
            product_id = UNSET
        else:
            product_id = self.product_id

        product_name: None | str | Unset
        if isinstance(self.product_name, Unset):
            product_name = UNSET
        else:
            product_name = self.product_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "member_id": member_id,
                "member_name": member_name,
                "project_id": project_id,
                "project_name": project_name,
                "start_date": start_date,
                "end_date": end_date,
                "hours_per_day": hours_per_day,
                "name": name,
            }
        )
        if member_avatar_url is not UNSET:
            field_dict["member_avatar_url"] = member_avatar_url
        if product_id is not UNSET:
            field_dict["product_id"] = product_id
        if product_name is not UNSET:
            field_dict["product_name"] = product_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        member_id = d.pop("member_id")

        member_name = d.pop("member_name")

        project_id = d.pop("project_id")

        project_name = d.pop("project_name")

        start_date = d.pop("start_date")

        end_date = d.pop("end_date")

        hours_per_day = d.pop("hours_per_day")

        name = d.pop("name")

        def _parse_member_avatar_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        member_avatar_url = _parse_member_avatar_url(d.pop("member_avatar_url", UNSET))

        def _parse_product_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        product_id = _parse_product_id(d.pop("product_id", UNSET))

        def _parse_product_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        product_name = _parse_product_name(d.pop("product_name", UNSET))

        output_team_booking = cls(
            id=id,
            member_id=member_id,
            member_name=member_name,
            project_id=project_id,
            project_name=project_name,
            start_date=start_date,
            end_date=end_date,
            hours_per_day=hours_per_day,
            name=name,
            member_avatar_url=member_avatar_url,
            product_id=product_id,
            product_name=product_name,
        )

        output_team_booking.additional_properties = d
        return output_team_booking

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
