from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.output_portal_share_document import OutputPortalShareDocument
    from ..models.output_portal_share_file import OutputPortalShareFile
    from ..models.output_portal_share_proposal import OutputPortalShareProposal


T = TypeVar("T", bound="OutputPortalShare")


@_attrs_define
class OutputPortalShare:
    """
    Attributes:
        org_id (str):
        id (str):
        title (str):
        published_at (datetime.datetime):
        proposals (list[OutputPortalShareProposal]):
        documents (list[OutputPortalShareDocument]):
        files (list[OutputPortalShareFile]):
        message (str | Unset):  Default: ''.
        expires_at (datetime.datetime | None | Unset):
    """

    org_id: str
    id: str
    title: str
    published_at: datetime.datetime
    proposals: list[OutputPortalShareProposal]
    documents: list[OutputPortalShareDocument]
    files: list[OutputPortalShareFile]
    message: str | Unset = ""
    expires_at: datetime.datetime | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        org_id = self.org_id

        id = self.id

        title = self.title

        published_at = self.published_at.isoformat()

        proposals = []
        for proposals_item_data in self.proposals:
            proposals_item = proposals_item_data.to_dict()
            proposals.append(proposals_item)

        documents = []
        for documents_item_data in self.documents:
            documents_item = documents_item_data.to_dict()
            documents.append(documents_item)

        files = []
        for files_item_data in self.files:
            files_item = files_item_data.to_dict()
            files.append(files_item)

        message = self.message

        expires_at: None | str | Unset
        if isinstance(self.expires_at, Unset):
            expires_at = UNSET
        elif isinstance(self.expires_at, datetime.datetime):
            expires_at = self.expires_at.isoformat()
        else:
            expires_at = self.expires_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "org_id": org_id,
                "id": id,
                "title": title,
                "published_at": published_at,
                "proposals": proposals,
                "documents": documents,
                "files": files,
            }
        )
        if message is not UNSET:
            field_dict["message"] = message
        if expires_at is not UNSET:
            field_dict["expires_at"] = expires_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.output_portal_share_document import OutputPortalShareDocument
        from ..models.output_portal_share_file import OutputPortalShareFile
        from ..models.output_portal_share_proposal import OutputPortalShareProposal

        d = dict(src_dict)
        org_id = d.pop("org_id")

        id = d.pop("id")

        title = d.pop("title")

        published_at = isoparse(d.pop("published_at"))

        proposals = []
        _proposals = d.pop("proposals")
        for proposals_item_data in _proposals:
            proposals_item = OutputPortalShareProposal.from_dict(proposals_item_data)

            proposals.append(proposals_item)

        documents = []
        _documents = d.pop("documents")
        for documents_item_data in _documents:
            documents_item = OutputPortalShareDocument.from_dict(documents_item_data)

            documents.append(documents_item)

        files = []
        _files = d.pop("files")
        for files_item_data in _files:
            files_item = OutputPortalShareFile.from_dict(files_item_data)

            files.append(files_item)

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

        output_portal_share = cls(
            org_id=org_id,
            id=id,
            title=title,
            published_at=published_at,
            proposals=proposals,
            documents=documents,
            files=files,
            message=message,
            expires_at=expires_at,
        )

        output_portal_share.additional_properties = d
        return output_portal_share

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
