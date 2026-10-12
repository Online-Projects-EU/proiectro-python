from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.output_document_template import OutputDocumentTemplate


T = TypeVar("T", bound="OutputDocumentTemplates")


@_attrs_define
class OutputDocumentTemplates:
    """
    Attributes:
        document_templates (list[OutputDocumentTemplate]):
        total_count (int | Unset):  Default: 0.
    """

    document_templates: list[OutputDocumentTemplate]
    total_count: int | Unset = 0
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        document_templates = []
        for document_templates_item_data in self.document_templates:
            document_templates_item = document_templates_item_data.to_dict()
            document_templates.append(document_templates_item)

        total_count = self.total_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "document_templates": document_templates,
            }
        )
        if total_count is not UNSET:
            field_dict["total_count"] = total_count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.output_document_template import OutputDocumentTemplate

        d = dict(src_dict)
        document_templates = []
        _document_templates = d.pop("document_templates")
        for document_templates_item_data in _document_templates:
            document_templates_item = OutputDocumentTemplate.from_dict(
                document_templates_item_data
            )

            document_templates.append(document_templates_item)

        total_count = d.pop("total_count", UNSET)

        output_document_templates = cls(
            document_templates=document_templates,
            total_count=total_count,
        )

        output_document_templates.additional_properties = d
        return output_document_templates

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
