from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.generate_document_data_classification_type_0 import GenerateDocumentDataClassificationType0
from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="GenerateDocument")



@_attrs_define
class GenerateDocument:
    """ 
        Attributes:
            template_id (str):
            title (None | str | Unset):
            body (None | str | Unset):
            data_classification (GenerateDocumentDataClassificationType0 | None | Unset):
     """

    template_id: str
    title: None | str | Unset = UNSET
    body: None | str | Unset = UNSET
    data_classification: GenerateDocumentDataClassificationType0 | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        template_id = self.template_id

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
        elif isinstance(self.data_classification, GenerateDocumentDataClassificationType0):
            data_classification = self.data_classification.value
        else:
            data_classification = self.data_classification


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "template_id": template_id,
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
        template_id = d.pop("template_id")

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


        def _parse_data_classification(data: object) -> GenerateDocumentDataClassificationType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                data_classification_type_0 = GenerateDocumentDataClassificationType0(data)



                return data_classification_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GenerateDocumentDataClassificationType0 | None | Unset, data)

        data_classification = _parse_data_classification(d.pop("data_classification", UNSET))


        generate_document = cls(
            template_id=template_id,
            title=title,
            body=body,
            data_classification=data_classification,
        )


        generate_document.additional_properties = d
        return generate_document

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
