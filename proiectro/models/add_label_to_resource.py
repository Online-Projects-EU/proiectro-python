from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AddLabelToResource")


@_attrs_define
class AddLabelToResource:
    """
    Attributes:
        resource (str):
        label (str):
        value_text (None | str | Unset):
        value_integer (int | None | Unset):
        value_decimal (float | None | str | Unset):
        value_date (None | str | Unset):
    """

    resource: str
    label: str
    value_text: None | str | Unset = UNSET
    value_integer: int | None | Unset = UNSET
    value_decimal: float | None | str | Unset = UNSET
    value_date: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        resource = self.resource

        label = self.label

        value_text: None | str | Unset
        if isinstance(self.value_text, Unset):
            value_text = UNSET
        else:
            value_text = self.value_text

        value_integer: int | None | Unset
        if isinstance(self.value_integer, Unset):
            value_integer = UNSET
        else:
            value_integer = self.value_integer

        value_decimal: float | None | str | Unset
        if isinstance(self.value_decimal, Unset):
            value_decimal = UNSET
        else:
            value_decimal = self.value_decimal

        value_date: None | str | Unset
        if isinstance(self.value_date, Unset):
            value_date = UNSET
        else:
            value_date = self.value_date

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "resource": resource,
                "label": label,
            }
        )
        if value_text is not UNSET:
            field_dict["value_text"] = value_text
        if value_integer is not UNSET:
            field_dict["value_integer"] = value_integer
        if value_decimal is not UNSET:
            field_dict["value_decimal"] = value_decimal
        if value_date is not UNSET:
            field_dict["value_date"] = value_date

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        resource = d.pop("resource")

        label = d.pop("label")

        def _parse_value_text(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        value_text = _parse_value_text(d.pop("value_text", UNSET))

        def _parse_value_integer(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        value_integer = _parse_value_integer(d.pop("value_integer", UNSET))

        def _parse_value_decimal(data: object) -> float | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | str | Unset, data)

        value_decimal = _parse_value_decimal(d.pop("value_decimal", UNSET))

        def _parse_value_date(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        value_date = _parse_value_date(d.pop("value_date", UNSET))

        add_label_to_resource = cls(
            resource=resource,
            label=label,
            value_text=value_text,
            value_integer=value_integer,
            value_decimal=value_decimal,
            value_date=value_date,
        )

        add_label_to_resource.additional_properties = d
        return add_label_to_resource

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
