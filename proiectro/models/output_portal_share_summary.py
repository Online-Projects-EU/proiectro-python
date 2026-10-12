from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="OutputPortalShareSummary")


@_attrs_define
class OutputPortalShareSummary:
    """
    Attributes:
        id (str):
        title (str):
        published_at (datetime.datetime):
        message (str | Unset):  Default: ''.
        expires_at (datetime.datetime | None | Unset):
        proposal_count (int | Unset):  Default: 0.
        document_count (int | Unset):  Default: 0.
        file_count (int | Unset):  Default: 0.
    """

    id: str
    title: str
    published_at: datetime.datetime
    message: str | Unset = ""
    expires_at: datetime.datetime | None | Unset = UNSET
    proposal_count: int | Unset = 0
    document_count: int | Unset = 0
    file_count: int | Unset = 0
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        title = self.title

        published_at = self.published_at.isoformat()

        message = self.message

        expires_at: None | str | Unset
        if isinstance(self.expires_at, Unset):
            expires_at = UNSET
        elif isinstance(self.expires_at, datetime.datetime):
            expires_at = self.expires_at.isoformat()
        else:
            expires_at = self.expires_at

        proposal_count = self.proposal_count

        document_count = self.document_count

        file_count = self.file_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "title": title,
                "published_at": published_at,
            }
        )
        if message is not UNSET:
            field_dict["message"] = message
        if expires_at is not UNSET:
            field_dict["expires_at"] = expires_at
        if proposal_count is not UNSET:
            field_dict["proposal_count"] = proposal_count
        if document_count is not UNSET:
            field_dict["document_count"] = document_count
        if file_count is not UNSET:
            field_dict["file_count"] = file_count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        title = d.pop("title")

        published_at = isoparse(d.pop("published_at"))

        message = d.pop("message", UNSET)

        def _parse_expires_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                expires_at_type_0 = isoparse(data)

                return expires_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        expires_at = _parse_expires_at(d.pop("expires_at", UNSET))

        proposal_count = d.pop("proposal_count", UNSET)

        document_count = d.pop("document_count", UNSET)

        file_count = d.pop("file_count", UNSET)

        output_portal_share_summary = cls(
            id=id,
            title=title,
            published_at=published_at,
            message=message,
            expires_at=expires_at,
            proposal_count=proposal_count,
            document_count=document_count,
            file_count=file_count,
        )

        output_portal_share_summary.additional_properties = d
        return output_portal_share_summary

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
