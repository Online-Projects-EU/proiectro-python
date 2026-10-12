from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="OutputFormVersion")


@_attrs_define
class OutputFormVersion:
    """
    Attributes:
        id (str):
        form_id (str):
        version (int):
        is_active (bool):
        is_locked (bool):
        created_at (datetime.datetime):
        step_count (int | Unset):  Default: 0.
        field_count (int | Unset):  Default: 0.
        submission_count (int | Unset):  Default: 0.
    """

    id: str
    form_id: str
    version: int
    is_active: bool
    is_locked: bool
    created_at: datetime.datetime
    step_count: int | Unset = 0
    field_count: int | Unset = 0
    submission_count: int | Unset = 0
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        form_id = self.form_id

        version = self.version

        is_active = self.is_active

        is_locked = self.is_locked

        created_at = self.created_at.isoformat()

        step_count = self.step_count

        field_count = self.field_count

        submission_count = self.submission_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "form_id": form_id,
                "version": version,
                "is_active": is_active,
                "is_locked": is_locked,
                "created_at": created_at,
            }
        )
        if step_count is not UNSET:
            field_dict["step_count"] = step_count
        if field_count is not UNSET:
            field_dict["field_count"] = field_count
        if submission_count is not UNSET:
            field_dict["submission_count"] = submission_count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        form_id = d.pop("form_id")

        version = d.pop("version")

        is_active = d.pop("is_active")

        is_locked = d.pop("is_locked")

        created_at = isoparse(d.pop("created_at"))

        step_count = d.pop("step_count", UNSET)

        field_count = d.pop("field_count", UNSET)

        submission_count = d.pop("submission_count", UNSET)

        output_form_version = cls(
            id=id,
            form_id=form_id,
            version=version,
            is_active=is_active,
            is_locked=is_locked,
            created_at=created_at,
            step_count=step_count,
            field_count=field_count,
            submission_count=submission_count,
        )

        output_form_version.additional_properties = d
        return output_form_version

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
