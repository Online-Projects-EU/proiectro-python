from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.output_share_document_state import OutputShareDocumentState
from ..types import UNSET, Unset

T = TypeVar("T", bound="OutputShareDocument")


@_attrs_define
class OutputShareDocument:
    """
    Attributes:
        id (str):
        document_id (str):
        title (str):
        state (OutputShareDocumentState):
        added_at (datetime.datetime):
        page_route (None | str | Unset):
        updated_at (datetime.datetime | None | Unset):
        full_number (None | str | Unset):
        published (bool | Unset):  Default: False.
        added_by (None | str | Unset):
    """

    id: str
    document_id: str
    title: str
    state: OutputShareDocumentState
    added_at: datetime.datetime
    page_route: None | str | Unset = UNSET
    updated_at: datetime.datetime | None | Unset = UNSET
    full_number: None | str | Unset = UNSET
    published: bool | Unset = False
    added_by: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        document_id = self.document_id

        title = self.title

        state = self.state.value

        added_at = self.added_at.isoformat()

        page_route: None | str | Unset
        if isinstance(self.page_route, Unset):
            page_route = UNSET
        else:
            page_route = self.page_route

        updated_at: None | str | Unset
        if isinstance(self.updated_at, Unset):
            updated_at = UNSET
        elif isinstance(self.updated_at, datetime.datetime):
            updated_at = self.updated_at.isoformat()
        else:
            updated_at = self.updated_at

        full_number: None | str | Unset
        if isinstance(self.full_number, Unset):
            full_number = UNSET
        else:
            full_number = self.full_number

        published = self.published

        added_by: None | str | Unset
        if isinstance(self.added_by, Unset):
            added_by = UNSET
        else:
            added_by = self.added_by

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "document_id": document_id,
                "title": title,
                "state": state,
                "added_at": added_at,
            }
        )
        if page_route is not UNSET:
            field_dict["page_route"] = page_route
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if full_number is not UNSET:
            field_dict["full_number"] = full_number
        if published is not UNSET:
            field_dict["published"] = published
        if added_by is not UNSET:
            field_dict["added_by"] = added_by

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        document_id = d.pop("document_id")

        title = d.pop("title")

        state = OutputShareDocumentState(d.pop("state"))

        added_at = isoparse(d.pop("added_at"))

        def _parse_page_route(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        page_route = _parse_page_route(d.pop("page_route", UNSET))

        def _parse_updated_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                updated_at_type_0 = isoparse(data)

                return updated_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        updated_at = _parse_updated_at(d.pop("updated_at", UNSET))

        def _parse_full_number(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        full_number = _parse_full_number(d.pop("full_number", UNSET))

        published = d.pop("published", UNSET)

        def _parse_added_by(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        added_by = _parse_added_by(d.pop("added_by", UNSET))

        output_share_document = cls(
            id=id,
            document_id=document_id,
            title=title,
            state=state,
            added_at=added_at,
            page_route=page_route,
            updated_at=updated_at,
            full_number=full_number,
            published=published,
            added_by=added_by,
        )

        output_share_document.additional_properties = d
        return output_share_document

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
