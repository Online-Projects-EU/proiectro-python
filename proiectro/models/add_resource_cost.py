from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AddResourceCost")


@_attrs_define
class AddResourceCost:
    """
    Attributes:
        resource (str):
        cost_type (str):
        name (str):
        value (float | str):
        currency (str):
        uom (str):
        description (None | str | Unset):
    """

    resource: str
    cost_type: str
    name: str
    value: float | str
    currency: str
    uom: str
    description: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        resource = self.resource

        cost_type = self.cost_type

        name = self.name

        value: float | str
        value = self.value

        currency = self.currency

        uom = self.uom

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "resource": resource,
                "cost_type": cost_type,
                "name": name,
                "value": value,
                "currency": currency,
                "uom": uom,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        resource = d.pop("resource")

        cost_type = d.pop("cost_type")

        name = d.pop("name")

        def _parse_value(data: object) -> float | str:
            return cast(float | str, data)

        value = _parse_value(d.pop("value"))

        currency = d.pop("currency")

        uom = d.pop("uom")

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        add_resource_cost = cls(
            resource=resource,
            cost_type=cost_type,
            name=name,
            value=value,
            currency=currency,
            uom=uom,
            description=description,
        )

        add_resource_cost.additional_properties = d
        return add_resource_cost

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
