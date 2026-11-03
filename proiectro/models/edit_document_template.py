from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.edit_document_template_data_classification_type_0 import (
    EditDocumentTemplateDataClassificationType0,
)
from ..models.edit_document_template_kind_type_0 import EditDocumentTemplateKindType0
from ..types import UNSET, Unset

T = TypeVar("T", bound="EditDocumentTemplate")


@_attrs_define
class EditDocumentTemplate:
    """
    Attributes:
        name (None | str | Unset):
        description (None | str | Unset):
        entity_type (None | str | Unset):
        kind (EditDocumentTemplateKindType0 | None | Unset):
        subject (None | str | Unset):
        body (None | str | Unset):
        default_series_id (None | str | Unset):
        retention_days (int | None | Unset):
        data_classification (EditDocumentTemplateDataClassificationType0 | None | Unset):
        is_active (bool | None | Unset):
    """

    name: None | str | Unset = UNSET
    description: None | str | Unset = UNSET
    entity_type: None | str | Unset = UNSET
    kind: EditDocumentTemplateKindType0 | None | Unset = UNSET
    subject: None | str | Unset = UNSET
    body: None | str | Unset = UNSET
    default_series_id: None | str | Unset = UNSET
    retention_days: int | None | Unset = UNSET
    data_classification: EditDocumentTemplateDataClassificationType0 | None | Unset = (
        UNSET
    )
    is_active: bool | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        entity_type: None | str | Unset
        if isinstance(self.entity_type, Unset):
            entity_type = UNSET
        else:
            entity_type = self.entity_type

        kind: None | str | Unset
        if isinstance(self.kind, Unset):
            kind = UNSET
        elif isinstance(self.kind, EditDocumentTemplateKindType0):
            kind = self.kind.value
        else:
            kind = self.kind

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

        data_classification: None | str | Unset
        if isinstance(self.data_classification, Unset):
            data_classification = UNSET
        elif isinstance(
            self.data_classification, EditDocumentTemplateDataClassificationType0
        ):
            data_classification = self.data_classification.value
        else:
            data_classification = self.data_classification

        is_active: bool | None | Unset
        if isinstance(self.is_active, Unset):
            is_active = UNSET
        else:
            is_active = self.is_active

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
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

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_entity_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        entity_type = _parse_entity_type(d.pop("entity_type", UNSET))

        def _parse_kind(data: object) -> EditDocumentTemplateKindType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                kind_type_0 = EditDocumentTemplateKindType0(data)

                return kind_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(EditDocumentTemplateKindType0 | None | Unset, data)

        kind = _parse_kind(d.pop("kind", UNSET))

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

        def _parse_data_classification(
            data: object,
        ) -> EditDocumentTemplateDataClassificationType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                data_classification_type_0 = (
                    EditDocumentTemplateDataClassificationType0(data)
                )

                return data_classification_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                EditDocumentTemplateDataClassificationType0 | None | Unset, data
            )

        data_classification = _parse_data_classification(
            d.pop("data_classification", UNSET)
        )

        def _parse_is_active(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_active = _parse_is_active(d.pop("is_active", UNSET))

        edit_document_template = cls(
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

        edit_document_template.additional_properties = d
        return edit_document_template

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
