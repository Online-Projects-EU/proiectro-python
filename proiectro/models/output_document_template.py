from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="OutputDocumentTemplate")


@_attrs_define
class OutputDocumentTemplate:
    """
    Attributes:
        id (str):
        name (str):
        entity_type (str):
        entity_type_display (str):
        data_classification (str):
        is_active (bool):
        default_series (None | str | Unset):
        default_series_code (None | str | Unset):
        retention_days (int | None | Unset):
    """

    id: str
    name: str
    entity_type: str
    entity_type_display: str
    data_classification: str
    is_active: bool
    default_series: None | str | Unset = UNSET
    default_series_code: None | str | Unset = UNSET
    retention_days: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        entity_type = self.entity_type

        entity_type_display = self.entity_type_display

        data_classification = self.data_classification

        is_active = self.is_active

        default_series: None | str | Unset
        if isinstance(self.default_series, Unset):
            default_series = UNSET
        else:
            default_series = self.default_series

        default_series_code: None | str | Unset
        if isinstance(self.default_series_code, Unset):
            default_series_code = UNSET
        else:
            default_series_code = self.default_series_code

        retention_days: int | None | Unset
        if isinstance(self.retention_days, Unset):
            retention_days = UNSET
        else:
            retention_days = self.retention_days

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "entity_type": entity_type,
                "entity_type_display": entity_type_display,
                "data_classification": data_classification,
                "is_active": is_active,
            }
        )
        if default_series is not UNSET:
            field_dict["default_series"] = default_series
        if default_series_code is not UNSET:
            field_dict["default_series_code"] = default_series_code
        if retention_days is not UNSET:
            field_dict["retention_days"] = retention_days

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        entity_type = d.pop("entity_type")

        entity_type_display = d.pop("entity_type_display")

        data_classification = d.pop("data_classification")

        is_active = d.pop("is_active")

        def _parse_default_series(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        default_series = _parse_default_series(d.pop("default_series", UNSET))

        def _parse_default_series_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        default_series_code = _parse_default_series_code(
            d.pop("default_series_code", UNSET)
        )

        def _parse_retention_days(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        retention_days = _parse_retention_days(d.pop("retention_days", UNSET))

        output_document_template = cls(
            id=id,
            name=name,
            entity_type=entity_type,
            entity_type_display=entity_type_display,
            data_classification=data_classification,
            is_active=is_active,
            default_series=default_series,
            default_series_code=default_series_code,
            retention_days=retention_days,
        )

        output_document_template.additional_properties = d
        return output_document_template

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
