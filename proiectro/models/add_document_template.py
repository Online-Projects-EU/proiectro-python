from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.add_document_template_data_classification import (
    AddDocumentTemplateDataClassification,
)
from ..models.add_document_template_kind import AddDocumentTemplateKind
from ..types import UNSET, Unset

T = TypeVar("T", bound="AddDocumentTemplate")


@_attrs_define
class AddDocumentTemplate:
    """
    Attributes:
        name (str):
        description (None | str | Unset):  Default: ''.
        entity_type (str | Unset):  Default: 'general'.
        kind (AddDocumentTemplateKind | Unset):  Default: AddDocumentTemplateKind.DOCUMENT.
        subject (None | str | Unset):  Default: ''.
        body (None | str | Unset):  Default: ''.
        default_series_id (None | str | Unset):
        retention_days (int | None | Unset):
        data_classification (AddDocumentTemplateDataClassification | Unset):  Default:
            AddDocumentTemplateDataClassification.INTERNAL.
        is_active (bool | Unset):  Default: True.
    """

    name: str
    description: None | str | Unset = ""
    entity_type: str | Unset = "general"
    kind: AddDocumentTemplateKind | Unset = AddDocumentTemplateKind.DOCUMENT
    subject: None | str | Unset = ""
    body: None | str | Unset = ""
    default_series_id: None | str | Unset = UNSET
    retention_days: int | None | Unset = UNSET
    data_classification: AddDocumentTemplateDataClassification | Unset = (
        AddDocumentTemplateDataClassification.INTERNAL
    )
    is_active: bool | Unset = True
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        entity_type = self.entity_type

        kind: str | Unset = UNSET
        if not isinstance(self.kind, Unset):
            kind = self.kind.value

        subject: None | str | Unset
        if isinstance(self.subject, Unset):
            subject = UNSET
        else:
            subject = self.subject

        body: None | str | Unset
        if isinstance(self.body, Unset):
            body = UNSET
        else:
            body = self.body

        default_series_id: None | str | Unset
        if isinstance(self.default_series_id, Unset):
            default_series_id = UNSET
        else:
            default_series_id = self.default_series_id

        retention_days: int | None | Unset
        if isinstance(self.retention_days, Unset):
            retention_days = UNSET
        else:
            retention_days = self.retention_days

        data_classification: str | Unset = UNSET
        if not isinstance(self.data_classification, Unset):
            data_classification = self.data_classification.value

        is_active = self.is_active

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if entity_type is not UNSET:
            field_dict["entity_type"] = entity_type
        if kind is not UNSET:
            field_dict["kind"] = kind
        if subject is not UNSET:
            field_dict["subject"] = subject
        if body is not UNSET:
            field_dict["body"] = body
        if default_series_id is not UNSET:
            field_dict["default_series_id"] = default_series_id
        if retention_days is not UNSET:
            field_dict["retention_days"] = retention_days
        if data_classification is not UNSET:
            field_dict["data_classification"] = data_classification
        if is_active is not UNSET:
            field_dict["is_active"] = is_active

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        entity_type = d.pop("entity_type", UNSET)

        _kind = d.pop("kind", UNSET)
        kind: AddDocumentTemplateKind | Unset
        if isinstance(_kind, Unset):
            kind = UNSET
        else:
            kind = AddDocumentTemplateKind(_kind)

        def _parse_subject(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        subject = _parse_subject(d.pop("subject", UNSET))

        def _parse_body(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        body = _parse_body(d.pop("body", UNSET))

        def _parse_default_series_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        default_series_id = _parse_default_series_id(d.pop("default_series_id", UNSET))

        def _parse_retention_days(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        retention_days = _parse_retention_days(d.pop("retention_days", UNSET))

        _data_classification = d.pop("data_classification", UNSET)
        data_classification: AddDocumentTemplateDataClassification | Unset
        if isinstance(_data_classification, Unset):
            data_classification = UNSET
        else:
            data_classification = AddDocumentTemplateDataClassification(
                _data_classification
            )

        is_active = d.pop("is_active", UNSET)

        add_document_template = cls(
            name=name,
            description=description,
            entity_type=entity_type,
            kind=kind,
            subject=subject,
            body=body,
            default_series_id=default_series_id,
            retention_days=retention_days,
            data_classification=data_classification,
            is_active=is_active,
        )

        add_document_template.additional_properties = d
        return add_document_template

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
