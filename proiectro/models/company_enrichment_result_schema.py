from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CompanyEnrichmentResultSchema")


@_attrs_define
class CompanyEnrichmentResultSchema:
    """
    Attributes:
        cui (str):
        name (str):
        is_active (bool):
        is_vat_registered (bool):
        address (None | str | Unset):
        registration_number (None | str | Unset):
        caen_code (None | str | Unset):
        region (None | str | Unset):
        city (None | str | Unset):
        postal_code (None | str | Unset):
        address_detail (None | str | Unset):
        error_message (None | str | Unset):
    """

    cui: str
    name: str
    is_active: bool
    is_vat_registered: bool
    address: None | str | Unset = UNSET
    registration_number: None | str | Unset = UNSET
    caen_code: None | str | Unset = UNSET
    region: None | str | Unset = UNSET
    city: None | str | Unset = UNSET
    postal_code: None | str | Unset = UNSET
    address_detail: None | str | Unset = UNSET
    error_message: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cui = self.cui

        name = self.name

        is_active = self.is_active

        is_vat_registered = self.is_vat_registered

        address: None | str | Unset
        if isinstance(self.address, Unset):
            address = UNSET
        else:
            address = self.address

        registration_number: None | str | Unset
        if isinstance(self.registration_number, Unset):
            registration_number = UNSET
        else:
            registration_number = self.registration_number

        caen_code: None | str | Unset
        if isinstance(self.caen_code, Unset):
            caen_code = UNSET
        else:
            caen_code = self.caen_code

        region: None | str | Unset
        if isinstance(self.region, Unset):
            region = UNSET
        else:
            region = self.region

        city: None | str | Unset
        if isinstance(self.city, Unset):
            city = UNSET
        else:
            city = self.city

        postal_code: None | str | Unset
        if isinstance(self.postal_code, Unset):
            postal_code = UNSET
        else:
            postal_code = self.postal_code

        address_detail: None | str | Unset
        if isinstance(self.address_detail, Unset):
            address_detail = UNSET
        else:
            address_detail = self.address_detail

        error_message: None | str | Unset
        if isinstance(self.error_message, Unset):
            error_message = UNSET
        else:
            error_message = self.error_message

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "cui": cui,
                "name": name,
                "is_active": is_active,
                "is_vat_registered": is_vat_registered,
            }
        )
        if address is not UNSET:
            field_dict["address"] = address
        if registration_number is not UNSET:
            field_dict["registration_number"] = registration_number
        if caen_code is not UNSET:
            field_dict["caen_code"] = caen_code
        if region is not UNSET:
            field_dict["region"] = region
        if city is not UNSET:
            field_dict["city"] = city
        if postal_code is not UNSET:
            field_dict["postal_code"] = postal_code
        if address_detail is not UNSET:
            field_dict["address_detail"] = address_detail
        if error_message is not UNSET:
            field_dict["error_message"] = error_message

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        cui = d.pop("cui")

        name = d.pop("name")

        is_active = d.pop("is_active")

        is_vat_registered = d.pop("is_vat_registered")

        def _parse_address(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        address = _parse_address(d.pop("address", UNSET))

        def _parse_registration_number(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        registration_number = _parse_registration_number(
            d.pop("registration_number", UNSET)
        )

        def _parse_caen_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        caen_code = _parse_caen_code(d.pop("caen_code", UNSET))

        def _parse_region(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        region = _parse_region(d.pop("region", UNSET))

        def _parse_city(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        city = _parse_city(d.pop("city", UNSET))

        def _parse_postal_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        postal_code = _parse_postal_code(d.pop("postal_code", UNSET))

        def _parse_address_detail(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        address_detail = _parse_address_detail(d.pop("address_detail", UNSET))

        def _parse_error_message(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        error_message = _parse_error_message(d.pop("error_message", UNSET))

        company_enrichment_result_schema = cls(
            cui=cui,
            name=name,
            is_active=is_active,
            is_vat_registered=is_vat_registered,
            address=address,
            registration_number=registration_number,
            caen_code=caen_code,
            region=region,
            city=city,
            postal_code=postal_code,
            address_detail=address_detail,
            error_message=error_message,
        )

        company_enrichment_result_schema.additional_properties = d
        return company_enrichment_result_schema

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
