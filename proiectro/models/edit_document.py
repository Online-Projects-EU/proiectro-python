from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.edit_document_data_classification_type_0 import EditDocumentDataClassificationType0
from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="EditDocument")



@_attrs_define
class EditDocument:
    """ 
        Attributes:
            title (None | str | Unset):
            body (None | str | Unset):
            data_classification (EditDocumentDataClassificationType0 | None | Unset):
     """

    title: None | str | Unset = UNSET
    body: None | str | Unset = UNSET
    data_classification: EditDocumentDataClassificationType0 | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        title: None | str | Unset
        if isinstance(self.title, Unset):
            title = UNSET
        else:
            title = self.title

        body: None | str | Unset
        if isinstance(self.body, Unset):
            body = UNSET
        else:
            body = self.body

        data_classification: None | str | Unset
        if isinstance(self.data_classification, Unset):
            data_classification = UNSET
        elif isinstance(self.data_classification, EditDocumentDataClassificationType0):
            data_classification = self.data_classification.value
        else:
            data_classification = self.data_classification


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if title is not UNSET:
            field_dict["title"] = title
        if body is not UNSET:
            field_dict["body"] = body
        if data_classification is not UNSET:
            field_dict["data_classification"] = data_classification

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_title(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        title = _parse_title(d.pop("title", UNSET))


        def _parse_body(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        body = _parse_body(d.pop("body", UNSET))


        def _parse_data_classification(data: object) -> EditDocumentDataClassificationType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                data_classification_type_0 = EditDocumentDataClassificationType0(data)



                return data_classification_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(EditDocumentDataClassificationType0 | None | Unset, data)

        data_classification = _parse_data_classification(d.pop("data_classification", UNSET))


        edit_document = cls(
            title=title,
            body=body,
            data_classification=data_classification,
        )


        edit_document.additional_properties = d
        return edit_document

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
