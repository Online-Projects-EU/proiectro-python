from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PartnerPortalProjectItem")


@_attrs_define
class PartnerPortalProjectItem:
    """Single project in partner portal

    Attributes:
        id (str):
        name (str):
        description (None | str):
        status (str):
        start_date (None | str):
        target_date (None | str):
        progress_percentage (int | None):
    """

    id: str
    name: str
    description: None | str
    status: str
    start_date: None | str
    target_date: None | str
    progress_percentage: int | None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        description: None | str
        description = self.description

        status = self.status

        start_date: None | str
        start_date = self.start_date

        target_date: None | str
        target_date = self.target_date

        progress_percentage: int | None
        progress_percentage = self.progress_percentage

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "description": description,
                "status": status,
                "start_date": start_date,
                "target_date": target_date,
                "progress_percentage": progress_percentage,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        def _parse_description(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        description = _parse_description(d.pop("description"))

        status = d.pop("status")

        def _parse_start_date(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        start_date = _parse_start_date(d.pop("start_date"))

        def _parse_target_date(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        target_date = _parse_target_date(d.pop("target_date"))

        def _parse_progress_percentage(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        progress_percentage = _parse_progress_percentage(d.pop("progress_percentage"))

        partner_portal_project_item = cls(
            id=id,
            name=name,
            description=description,
            status=status,
            start_date=start_date,
            target_date=target_date,
            progress_percentage=progress_percentage,
        )

        partner_portal_project_item.additional_properties = d
        return partner_portal_project_item

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
