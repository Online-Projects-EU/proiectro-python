from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="OutputPartnerPortalFormLink")


@_attrs_define
class OutputPartnerPortalFormLink:
    """One form published to a partner bridge (management view).

    Attributes:
        id (str):
        form_id (str):
        form_name (str):
        display_order (int | Unset):  Default: 0.
        has_active_version (bool | Unset):  Default: False.
        active_version (int | None | Unset):
        submission_count (int | Unset):  Default: 0.
    """

    id: str
    form_id: str
    form_name: str
    display_order: int | Unset = 0
    has_active_version: bool | Unset = False
    active_version: int | None | Unset = UNSET
    submission_count: int | Unset = 0
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        form_id = self.form_id

        form_name = self.form_name

        display_order = self.display_order

        has_active_version = self.has_active_version

        active_version: int | None | Unset
        if isinstance(self.active_version, Unset):
            active_version = UNSET
        else:
            active_version = self.active_version

        submission_count = self.submission_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "form_id": form_id,
                "form_name": form_name,
            }
        )
        if display_order is not UNSET:
            field_dict["display_order"] = display_order
        if has_active_version is not UNSET:
            field_dict["has_active_version"] = has_active_version
        if active_version is not UNSET:
            field_dict["active_version"] = active_version
        if submission_count is not UNSET:
            field_dict["submission_count"] = submission_count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        form_id = d.pop("form_id")

        form_name = d.pop("form_name")

        display_order = d.pop("display_order", UNSET)

        has_active_version = d.pop("has_active_version", UNSET)

        def _parse_active_version(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        active_version = _parse_active_version(d.pop("active_version", UNSET))

        submission_count = d.pop("submission_count", UNSET)

        output_partner_portal_form_link = cls(
            id=id,
            form_id=form_id,
            form_name=form_name,
            display_order=display_order,
            has_active_version=has_active_version,
            active_version=active_version,
            submission_count=submission_count,
        )

        output_partner_portal_form_link.additional_properties = d
        return output_partner_portal_form_link

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
