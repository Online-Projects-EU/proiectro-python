from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="OutputCustomForm")


@_attrs_define
class OutputCustomForm:
    """
    Attributes:
        id (str):
        name (str):
        slug (str):
        is_active (bool):
        data_classification (str):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        description (str | Unset):  Default: ''.
        retention_days (int | None | Unset):
        active_version (int | None | Unset):
        version_count (int | Unset):  Default: 0.
        submission_count (int | Unset):  Default: 0.
    """

    id: str
    name: str
    slug: str
    is_active: bool
    data_classification: str
    created_at: datetime.datetime
    updated_at: datetime.datetime
    description: str | Unset = ""
    retention_days: int | None | Unset = UNSET
    active_version: int | None | Unset = UNSET
    version_count: int | Unset = 0
    submission_count: int | Unset = 0
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        slug = self.slug

        is_active = self.is_active

        data_classification = self.data_classification

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        description = self.description

        retention_days: int | None | Unset
        if isinstance(self.retention_days, Unset):
            retention_days = UNSET
        else:
            retention_days = self.retention_days

        active_version: int | None | Unset
        if isinstance(self.active_version, Unset):
            active_version = UNSET
        else:
            active_version = self.active_version

        version_count = self.version_count

        submission_count = self.submission_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "slug": slug,
                "is_active": is_active,
                "data_classification": data_classification,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if retention_days is not UNSET:
            field_dict["retention_days"] = retention_days
        if active_version is not UNSET:
            field_dict["active_version"] = active_version
        if version_count is not UNSET:
            field_dict["version_count"] = version_count
        if submission_count is not UNSET:
            field_dict["submission_count"] = submission_count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        slug = d.pop("slug")

        is_active = d.pop("is_active")

        data_classification = d.pop("data_classification")

        created_at = isoparse(d.pop("created_at"))

        updated_at = isoparse(d.pop("updated_at"))

        description = d.pop("description", UNSET)

        def _parse_retention_days(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        retention_days = _parse_retention_days(d.pop("retention_days", UNSET))

        def _parse_active_version(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        active_version = _parse_active_version(d.pop("active_version", UNSET))

        version_count = d.pop("version_count", UNSET)

        submission_count = d.pop("submission_count", UNSET)

        output_custom_form = cls(
            id=id,
            name=name,
            slug=slug,
            is_active=is_active,
            data_classification=data_classification,
            created_at=created_at,
            updated_at=updated_at,
            description=description,
            retention_days=retention_days,
            active_version=active_version,
            version_count=version_count,
            submission_count=submission_count,
        )

        output_custom_form.additional_properties = d
        return output_custom_form

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
