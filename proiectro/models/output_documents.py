from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.output_document import OutputDocument


T = TypeVar("T", bound="OutputDocuments")


@_attrs_define
class OutputDocuments:
    """
    Attributes:
        documents (list[OutputDocument]):
        total_count (int | Unset):  Default: 0.
        is_filtered (bool | Unset):  Default: False.
        entity_id (None | str | Unset):
    """

    documents: list[OutputDocument]
    total_count: int | Unset = 0
    is_filtered: bool | Unset = False
    entity_id: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        documents = []
        for documents_item_data in self.documents:
            documents_item = documents_item_data.to_dict()
            documents.append(documents_item)

        total_count = self.total_count

        is_filtered = self.is_filtered

        entity_id: None | str | Unset
        if isinstance(self.entity_id, Unset):
            entity_id = UNSET
        else:
            entity_id = self.entity_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "documents": documents,
            }
        )
        if total_count is not UNSET:
            field_dict["total_count"] = total_count
        if is_filtered is not UNSET:
            field_dict["is_filtered"] = is_filtered
        if entity_id is not UNSET:
            field_dict["entity_id"] = entity_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.output_document import OutputDocument

        d = dict(src_dict)
        documents = []
        _documents = d.pop("documents")
        for documents_item_data in _documents:
            documents_item = OutputDocument.from_dict(documents_item_data)

            documents.append(documents_item)

        total_count = d.pop("total_count", UNSET)

        is_filtered = d.pop("is_filtered", UNSET)

        def _parse_entity_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        entity_id = _parse_entity_id(d.pop("entity_id", UNSET))

        output_documents = cls(
            documents=documents,
            total_count=total_count,
            is_filtered=is_filtered,
            entity_id=entity_id,
        )

        output_documents.additional_properties = d
        return output_documents

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
