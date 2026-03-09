from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AddExternalSupportRequestForProject")


@_attrs_define
class AddExternalSupportRequestForProject:
    """Input schema for creating external support request for a specific project from customer portal

    Attributes:
        request_type (str):
        request_severity (str):
        title (str):
        description (str):
        project_id (str):
        reported_asset (None | str | Unset):
    """

    request_type: str
    request_severity: str
    title: str
    description: str
    project_id: str
    reported_asset: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        request_type = self.request_type

        request_severity = self.request_severity

        title = self.title

        description = self.description

        project_id = self.project_id

        reported_asset: None | str | Unset
        if isinstance(self.reported_asset, Unset):
            reported_asset = UNSET
        else:
            reported_asset = self.reported_asset

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "request_type": request_type,
                "request_severity": request_severity,
                "title": title,
                "description": description,
                "project_id": project_id,
            }
        )
        if reported_asset is not UNSET:
            field_dict["reported_asset"] = reported_asset

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        request_type = d.pop("request_type")

        request_severity = d.pop("request_severity")

        title = d.pop("title")

        description = d.pop("description")

        project_id = d.pop("project_id")

        def _parse_reported_asset(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        reported_asset = _parse_reported_asset(d.pop("reported_asset", UNSET))

        add_external_support_request_for_project = cls(
            request_type=request_type,
            request_severity=request_severity,
            title=title,
            description=description,
            project_id=project_id,
            reported_asset=reported_asset,
        )

        add_external_support_request_for_project.additional_properties = d
        return add_external_support_request_for_project

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
