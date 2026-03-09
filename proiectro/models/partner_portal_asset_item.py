from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PartnerPortalAssetItem")


@_attrs_define
class PartnerPortalAssetItem:
    """Single asset in partner portal

    Attributes:
        id (str):
        name (str):
        category_name (str):
        status (str):
        status_display (str):
        description (None | str | Unset):
        internal_code (None | str | Unset):
        installation_date (None | str | Unset):
        warranty_expiration (None | str | Unset):
    """

    id: str
    name: str
    category_name: str
    status: str
    status_display: str
    description: None | str | Unset = UNSET
    internal_code: None | str | Unset = UNSET
    installation_date: None | str | Unset = UNSET
    warranty_expiration: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        category_name = self.category_name

        status = self.status

        status_display = self.status_display

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

        installation_date: None | str | Unset
        if isinstance(self.installation_date, Unset):
            installation_date = UNSET
        else:
            installation_date = self.installation_date

        warranty_expiration: None | str | Unset
        if isinstance(self.warranty_expiration, Unset):
            warranty_expiration = UNSET
        else:
            warranty_expiration = self.warranty_expiration

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "category_name": category_name,
                "status": status,
                "status_display": status_display,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if internal_code is not UNSET:
            field_dict["internal_code"] = internal_code
        if installation_date is not UNSET:
            field_dict["installation_date"] = installation_date
        if warranty_expiration is not UNSET:
            field_dict["warranty_expiration"] = warranty_expiration

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        category_name = d.pop("category_name")

        status = d.pop("status")

        status_display = d.pop("status_display")

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

        def _parse_installation_date(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        installation_date = _parse_installation_date(d.pop("installation_date", UNSET))

        def _parse_warranty_expiration(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        warranty_expiration = _parse_warranty_expiration(
            d.pop("warranty_expiration", UNSET)
        )

        partner_portal_asset_item = cls(
            id=id,
            name=name,
            category_name=category_name,
            status=status,
            status_display=status_display,
            description=description,
            internal_code=internal_code,
            installation_date=installation_date,
            warranty_expiration=warranty_expiration,
        )

        partner_portal_asset_item.additional_properties = d
        return partner_portal_asset_item

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
