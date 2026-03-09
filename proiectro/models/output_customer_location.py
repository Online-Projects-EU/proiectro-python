from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="OutputCustomerLocation")


@_attrs_define
class OutputCustomerLocation:
    """
    Attributes:
        id (str):
        customer_id (str):
        customer_name (str):
        customer_first_letter (str):
        location_id (str):
        location_path (str):
        name (str):
        is_active (bool):
        description (None | str | Unset):
        internal_code (None | str | Unset):
        asset_count (int | Unset):  Default: 0.
    """

    id: str
    customer_id: str
    customer_name: str
    customer_first_letter: str
    location_id: str
    location_path: str
    name: str
    is_active: bool
    description: None | str | Unset = UNSET
    internal_code: None | str | Unset = UNSET
    asset_count: int | Unset = 0
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        customer_id = self.customer_id

        customer_name = self.customer_name

        customer_first_letter = self.customer_first_letter

        location_id = self.location_id

        location_path = self.location_path

        name = self.name

        is_active = self.is_active

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        internal_code: None | str | Unset
        if isinstance(self.internal_code, Unset):
            internal_code = UNSET
        else:
            internal_code = self.internal_code

        asset_count = self.asset_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "customer_id": customer_id,
                "customer_name": customer_name,
                "customer_first_letter": customer_first_letter,
                "location_id": location_id,
                "location_path": location_path,
                "name": name,
                "is_active": is_active,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if internal_code is not UNSET:
            field_dict["internal_code"] = internal_code
        if asset_count is not UNSET:
            field_dict["asset_count"] = asset_count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        customer_id = d.pop("customer_id")

        customer_name = d.pop("customer_name")

        customer_first_letter = d.pop("customer_first_letter")

        location_id = d.pop("location_id")

        location_path = d.pop("location_path")

        name = d.pop("name")

        is_active = d.pop("is_active")

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_internal_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        internal_code = _parse_internal_code(d.pop("internal_code", UNSET))

        asset_count = d.pop("asset_count", UNSET)

        output_customer_location = cls(
            id=id,
            customer_id=customer_id,
            customer_name=customer_name,
            customer_first_letter=customer_first_letter,
            location_id=location_id,
            location_path=location_path,
            name=name,
            is_active=is_active,
            description=description,
            internal_code=internal_code,
            asset_count=asset_count,
        )

        output_customer_location.additional_properties = d
        return output_customer_location

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
