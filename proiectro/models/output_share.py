from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.output_share_state import OutputShareState
from ..types import UNSET, Unset

T = TypeVar("T", bound="OutputShare")


@_attrs_define
class OutputShare:
    """
    Attributes:
        id (str):
        org_id (str):
        title (str):
        message (str):
        language (str):
        state (OutputShareState):
        created_at (datetime.datetime):
        expires_at (datetime.datetime | None | Unset):
        published_at (datetime.datetime | None | Unset):
        first_published_at (datetime.datetime | None | Unset):
        has_link (bool | Unset):  Default: False.
        last_opened_at (datetime.datetime | None | Unset):
        created_by (None | str | Unset):
        proposal_count (int | Unset):  Default: 0.
        document_count (int | Unset):  Default: 0.
        file_count (int | Unset):  Default: 0.
        pending_count (int | Unset):  Default: 0.
    """

    id: str
    org_id: str
    title: str
    message: str
    language: str
    state: OutputShareState
    created_at: datetime.datetime
    expires_at: datetime.datetime | None | Unset = UNSET
    published_at: datetime.datetime | None | Unset = UNSET
    first_published_at: datetime.datetime | None | Unset = UNSET
    has_link: bool | Unset = False
    last_opened_at: datetime.datetime | None | Unset = UNSET
    created_by: None | str | Unset = UNSET
    proposal_count: int | Unset = 0
    document_count: int | Unset = 0
    file_count: int | Unset = 0
    pending_count: int | Unset = 0
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        org_id = self.org_id

        title = self.title

        message = self.message

        language = self.language

        state = self.state.value

        created_at = self.created_at.isoformat()

        expires_at: None | str | Unset
        if isinstance(self.expires_at, Unset):
            expires_at = UNSET
        elif isinstance(self.expires_at, datetime.datetime):
            expires_at = self.expires_at.isoformat()
        else:
            expires_at = self.expires_at

        published_at: None | str | Unset
        if isinstance(self.published_at, Unset):
            published_at = UNSET
        elif isinstance(self.published_at, datetime.datetime):
            published_at = self.published_at.isoformat()
        else:
            published_at = self.published_at

        first_published_at: None | str | Unset
        if isinstance(self.first_published_at, Unset):
            first_published_at = UNSET
        elif isinstance(self.first_published_at, datetime.datetime):
            first_published_at = self.first_published_at.isoformat()
        else:
            first_published_at = self.first_published_at

        has_link = self.has_link

        last_opened_at: None | str | Unset
        if isinstance(self.last_opened_at, Unset):
            last_opened_at = UNSET
        elif isinstance(self.last_opened_at, datetime.datetime):
            last_opened_at = self.last_opened_at.isoformat()
        else:
            last_opened_at = self.last_opened_at

        created_by: None | str | Unset
        if isinstance(self.created_by, Unset):
            created_by = UNSET
        else:
            created_by = self.created_by

        proposal_count = self.proposal_count

        document_count = self.document_count

        file_count = self.file_count

        pending_count = self.pending_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "org_id": org_id,
                "title": title,
                "message": message,
                "language": language,
                "state": state,
                "created_at": created_at,
            }
        )
        if expires_at is not UNSET:
            field_dict["expires_at"] = expires_at
        if published_at is not UNSET:
            field_dict["published_at"] = published_at
        if first_published_at is not UNSET:
            field_dict["first_published_at"] = first_published_at
        if has_link is not UNSET:
            field_dict["has_link"] = has_link
        if last_opened_at is not UNSET:
            field_dict["last_opened_at"] = last_opened_at
        if created_by is not UNSET:
            field_dict["created_by"] = created_by
        if proposal_count is not UNSET:
            field_dict["proposal_count"] = proposal_count
        if document_count is not UNSET:
            field_dict["document_count"] = document_count
        if file_count is not UNSET:
            field_dict["file_count"] = file_count
        if pending_count is not UNSET:
            field_dict["pending_count"] = pending_count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        org_id = d.pop("org_id")

        title = d.pop("title")

        message = d.pop("message")

        language = d.pop("language")

        state = OutputShareState(d.pop("state"))

        created_at = isoparse(d.pop("created_at"))

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

        def _parse_published_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                published_at_type_0 = isoparse(data)

                return published_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        published_at = _parse_published_at(d.pop("published_at", UNSET))

        def _parse_first_published_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                first_published_at_type_0 = isoparse(data)

                return first_published_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        first_published_at = _parse_first_published_at(
            d.pop("first_published_at", UNSET)
        )

        has_link = d.pop("has_link", UNSET)

        def _parse_last_opened_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_opened_at_type_0 = isoparse(data)

                return last_opened_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        last_opened_at = _parse_last_opened_at(d.pop("last_opened_at", UNSET))

        def _parse_created_by(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        created_by = _parse_created_by(d.pop("created_by", UNSET))

        proposal_count = d.pop("proposal_count", UNSET)

        document_count = d.pop("document_count", UNSET)

        file_count = d.pop("file_count", UNSET)

        pending_count = d.pop("pending_count", UNSET)

        output_share = cls(
            id=id,
            org_id=org_id,
            title=title,
            message=message,
            language=language,
            state=state,
            created_at=created_at,
            expires_at=expires_at,
            published_at=published_at,
            first_published_at=first_published_at,
            has_link=has_link,
            last_opened_at=last_opened_at,
            created_by=created_by,
            proposal_count=proposal_count,
            document_count=document_count,
            file_count=file_count,
            pending_count=pending_count,
        )

        output_share.additional_properties = d
        return output_share

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
