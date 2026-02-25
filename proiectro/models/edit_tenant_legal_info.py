from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="EditTenantLegalInfo")


@_attrs_define
class EditTenantLegalInfo:
    """Schema for editing tenant (workspace) legal info

    Attributes:
        legal_name (None | str | Unset):
        legal_country (None | str | Unset):
        legal_country_registration_id_name (None | str | Unset):
        legal_country_registration_id (None | str | Unset):
        legal_country_tax_id_1_name (None | str | Unset):
        legal_country_tax_id_1 (None | str | Unset):
        legal_country_tax_id_2_name (None | str | Unset):
        legal_country_tax_id_2 (None | str | Unset):
        legal_country_tax_id_3_name (None | str | Unset):
        legal_country_tax_id_3 (None | str | Unset):
        legal_world_tax_id_1_name (None | str | Unset):
        legal_world_tax_id_1 (None | str | Unset):
        legal_world_tax_id_2_name (None | str | Unset):
        legal_world_tax_id_2 (None | str | Unset):
        legal_world_tax_id_3_name (None | str | Unset):
        legal_world_tax_id_3 (None | str | Unset):
        legal_other_identifier_1_name (None | str | Unset):
        legal_other_identifier_1 (None | str | Unset):
        legal_other_identifier_2_name (None | str | Unset):
        legal_other_identifier_2 (None | str | Unset):
        legal_other_identifier_3_name (None | str | Unset):
        legal_other_identifier_3 (None | str | Unset):
        legal_region (None | str | Unset):
        legal_city (None | str | Unset):
        legal_address_line_1 (None | str | Unset):
        legal_address_line_2 (None | str | Unset):
        legal_postal_code (None | str | Unset):
    """

    legal_name: None | str | Unset = UNSET
    legal_country: None | str | Unset = UNSET
    legal_country_registration_id_name: None | str | Unset = UNSET
    legal_country_registration_id: None | str | Unset = UNSET
    legal_country_tax_id_1_name: None | str | Unset = UNSET
    legal_country_tax_id_1: None | str | Unset = UNSET
    legal_country_tax_id_2_name: None | str | Unset = UNSET
    legal_country_tax_id_2: None | str | Unset = UNSET
    legal_country_tax_id_3_name: None | str | Unset = UNSET
    legal_country_tax_id_3: None | str | Unset = UNSET
    legal_world_tax_id_1_name: None | str | Unset = UNSET
    legal_world_tax_id_1: None | str | Unset = UNSET
    legal_world_tax_id_2_name: None | str | Unset = UNSET
    legal_world_tax_id_2: None | str | Unset = UNSET
    legal_world_tax_id_3_name: None | str | Unset = UNSET
    legal_world_tax_id_3: None | str | Unset = UNSET
    legal_other_identifier_1_name: None | str | Unset = UNSET
    legal_other_identifier_1: None | str | Unset = UNSET
    legal_other_identifier_2_name: None | str | Unset = UNSET
    legal_other_identifier_2: None | str | Unset = UNSET
    legal_other_identifier_3_name: None | str | Unset = UNSET
    legal_other_identifier_3: None | str | Unset = UNSET
    legal_region: None | str | Unset = UNSET
    legal_city: None | str | Unset = UNSET
    legal_address_line_1: None | str | Unset = UNSET
    legal_address_line_2: None | str | Unset = UNSET
    legal_postal_code: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        legal_name: None | str | Unset
        if isinstance(self.legal_name, Unset):
            legal_name = UNSET
        else:
            legal_name = self.legal_name

        legal_country: None | str | Unset
        if isinstance(self.legal_country, Unset):
            legal_country = UNSET
        else:
            legal_country = self.legal_country

        legal_country_registration_id_name: None | str | Unset
        if isinstance(self.legal_country_registration_id_name, Unset):
            legal_country_registration_id_name = UNSET
        else:
            legal_country_registration_id_name = self.legal_country_registration_id_name

        legal_country_registration_id: None | str | Unset
        if isinstance(self.legal_country_registration_id, Unset):
            legal_country_registration_id = UNSET
        else:
            legal_country_registration_id = self.legal_country_registration_id

        legal_country_tax_id_1_name: None | str | Unset
        if isinstance(self.legal_country_tax_id_1_name, Unset):
            legal_country_tax_id_1_name = UNSET
        else:
            legal_country_tax_id_1_name = self.legal_country_tax_id_1_name

        legal_country_tax_id_1: None | str | Unset
        if isinstance(self.legal_country_tax_id_1, Unset):
            legal_country_tax_id_1 = UNSET
        else:
            legal_country_tax_id_1 = self.legal_country_tax_id_1

        legal_country_tax_id_2_name: None | str | Unset
        if isinstance(self.legal_country_tax_id_2_name, Unset):
            legal_country_tax_id_2_name = UNSET
        else:
            legal_country_tax_id_2_name = self.legal_country_tax_id_2_name

        legal_country_tax_id_2: None | str | Unset
        if isinstance(self.legal_country_tax_id_2, Unset):
            legal_country_tax_id_2 = UNSET
        else:
            legal_country_tax_id_2 = self.legal_country_tax_id_2

        legal_country_tax_id_3_name: None | str | Unset
        if isinstance(self.legal_country_tax_id_3_name, Unset):
            legal_country_tax_id_3_name = UNSET
        else:
            legal_country_tax_id_3_name = self.legal_country_tax_id_3_name

        legal_country_tax_id_3: None | str | Unset
        if isinstance(self.legal_country_tax_id_3, Unset):
            legal_country_tax_id_3 = UNSET
        else:
            legal_country_tax_id_3 = self.legal_country_tax_id_3

        legal_world_tax_id_1_name: None | str | Unset
        if isinstance(self.legal_world_tax_id_1_name, Unset):
            legal_world_tax_id_1_name = UNSET
        else:
            legal_world_tax_id_1_name = self.legal_world_tax_id_1_name

        legal_world_tax_id_1: None | str | Unset
        if isinstance(self.legal_world_tax_id_1, Unset):
            legal_world_tax_id_1 = UNSET
        else:
            legal_world_tax_id_1 = self.legal_world_tax_id_1

        legal_world_tax_id_2_name: None | str | Unset
        if isinstance(self.legal_world_tax_id_2_name, Unset):
            legal_world_tax_id_2_name = UNSET
        else:
            legal_world_tax_id_2_name = self.legal_world_tax_id_2_name

        legal_world_tax_id_2: None | str | Unset
        if isinstance(self.legal_world_tax_id_2, Unset):
            legal_world_tax_id_2 = UNSET
        else:
            legal_world_tax_id_2 = self.legal_world_tax_id_2

        legal_world_tax_id_3_name: None | str | Unset
        if isinstance(self.legal_world_tax_id_3_name, Unset):
            legal_world_tax_id_3_name = UNSET
        else:
            legal_world_tax_id_3_name = self.legal_world_tax_id_3_name

        legal_world_tax_id_3: None | str | Unset
        if isinstance(self.legal_world_tax_id_3, Unset):
            legal_world_tax_id_3 = UNSET
        else:
            legal_world_tax_id_3 = self.legal_world_tax_id_3

        legal_other_identifier_1_name: None | str | Unset
        if isinstance(self.legal_other_identifier_1_name, Unset):
            legal_other_identifier_1_name = UNSET
        else:
            legal_other_identifier_1_name = self.legal_other_identifier_1_name

        legal_other_identifier_1: None | str | Unset
        if isinstance(self.legal_other_identifier_1, Unset):
            legal_other_identifier_1 = UNSET
        else:
            legal_other_identifier_1 = self.legal_other_identifier_1

        legal_other_identifier_2_name: None | str | Unset
        if isinstance(self.legal_other_identifier_2_name, Unset):
            legal_other_identifier_2_name = UNSET
        else:
            legal_other_identifier_2_name = self.legal_other_identifier_2_name

        legal_other_identifier_2: None | str | Unset
        if isinstance(self.legal_other_identifier_2, Unset):
            legal_other_identifier_2 = UNSET
        else:
            legal_other_identifier_2 = self.legal_other_identifier_2

        legal_other_identifier_3_name: None | str | Unset
        if isinstance(self.legal_other_identifier_3_name, Unset):
            legal_other_identifier_3_name = UNSET
        else:
            legal_other_identifier_3_name = self.legal_other_identifier_3_name

        legal_other_identifier_3: None | str | Unset
        if isinstance(self.legal_other_identifier_3, Unset):
            legal_other_identifier_3 = UNSET
        else:
            legal_other_identifier_3 = self.legal_other_identifier_3

        legal_region: None | str | Unset
        if isinstance(self.legal_region, Unset):
            legal_region = UNSET
        else:
            legal_region = self.legal_region

        legal_city: None | str | Unset
        if isinstance(self.legal_city, Unset):
            legal_city = UNSET
        else:
            legal_city = self.legal_city

        legal_address_line_1: None | str | Unset
        if isinstance(self.legal_address_line_1, Unset):
            legal_address_line_1 = UNSET
        else:
            legal_address_line_1 = self.legal_address_line_1

        legal_address_line_2: None | str | Unset
        if isinstance(self.legal_address_line_2, Unset):
            legal_address_line_2 = UNSET
        else:
            legal_address_line_2 = self.legal_address_line_2

        legal_postal_code: None | str | Unset
        if isinstance(self.legal_postal_code, Unset):
            legal_postal_code = UNSET
        else:
            legal_postal_code = self.legal_postal_code

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if legal_name is not UNSET:
            field_dict["legal_name"] = legal_name
        if legal_country is not UNSET:
            field_dict["legal_country"] = legal_country
        if legal_country_registration_id_name is not UNSET:
            field_dict["legal_country_registration_id_name"] = (
                legal_country_registration_id_name
            )
        if legal_country_registration_id is not UNSET:
            field_dict["legal_country_registration_id"] = legal_country_registration_id
        if legal_country_tax_id_1_name is not UNSET:
            field_dict["legal_country_tax_id_1_name"] = legal_country_tax_id_1_name
        if legal_country_tax_id_1 is not UNSET:
            field_dict["legal_country_tax_id_1"] = legal_country_tax_id_1
        if legal_country_tax_id_2_name is not UNSET:
            field_dict["legal_country_tax_id_2_name"] = legal_country_tax_id_2_name
        if legal_country_tax_id_2 is not UNSET:
            field_dict["legal_country_tax_id_2"] = legal_country_tax_id_2
        if legal_country_tax_id_3_name is not UNSET:
            field_dict["legal_country_tax_id_3_name"] = legal_country_tax_id_3_name
        if legal_country_tax_id_3 is not UNSET:
            field_dict["legal_country_tax_id_3"] = legal_country_tax_id_3
        if legal_world_tax_id_1_name is not UNSET:
            field_dict["legal_world_tax_id_1_name"] = legal_world_tax_id_1_name
        if legal_world_tax_id_1 is not UNSET:
            field_dict["legal_world_tax_id_1"] = legal_world_tax_id_1
        if legal_world_tax_id_2_name is not UNSET:
            field_dict["legal_world_tax_id_2_name"] = legal_world_tax_id_2_name
        if legal_world_tax_id_2 is not UNSET:
            field_dict["legal_world_tax_id_2"] = legal_world_tax_id_2
        if legal_world_tax_id_3_name is not UNSET:
            field_dict["legal_world_tax_id_3_name"] = legal_world_tax_id_3_name
        if legal_world_tax_id_3 is not UNSET:
            field_dict["legal_world_tax_id_3"] = legal_world_tax_id_3
        if legal_other_identifier_1_name is not UNSET:
            field_dict["legal_other_identifier_1_name"] = legal_other_identifier_1_name
        if legal_other_identifier_1 is not UNSET:
            field_dict["legal_other_identifier_1"] = legal_other_identifier_1
        if legal_other_identifier_2_name is not UNSET:
            field_dict["legal_other_identifier_2_name"] = legal_other_identifier_2_name
        if legal_other_identifier_2 is not UNSET:
            field_dict["legal_other_identifier_2"] = legal_other_identifier_2
        if legal_other_identifier_3_name is not UNSET:
            field_dict["legal_other_identifier_3_name"] = legal_other_identifier_3_name
        if legal_other_identifier_3 is not UNSET:
            field_dict["legal_other_identifier_3"] = legal_other_identifier_3
        if legal_region is not UNSET:
            field_dict["legal_region"] = legal_region
        if legal_city is not UNSET:
            field_dict["legal_city"] = legal_city
        if legal_address_line_1 is not UNSET:
            field_dict["legal_address_line_1"] = legal_address_line_1
        if legal_address_line_2 is not UNSET:
            field_dict["legal_address_line_2"] = legal_address_line_2
        if legal_postal_code is not UNSET:
            field_dict["legal_postal_code"] = legal_postal_code

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_legal_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        legal_name = _parse_legal_name(d.pop("legal_name", UNSET))

        def _parse_legal_country(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        legal_country = _parse_legal_country(d.pop("legal_country", UNSET))

        def _parse_legal_country_registration_id_name(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        legal_country_registration_id_name = _parse_legal_country_registration_id_name(
            d.pop("legal_country_registration_id_name", UNSET)
        )

        def _parse_legal_country_registration_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        legal_country_registration_id = _parse_legal_country_registration_id(
            d.pop("legal_country_registration_id", UNSET)
        )

        def _parse_legal_country_tax_id_1_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        legal_country_tax_id_1_name = _parse_legal_country_tax_id_1_name(
            d.pop("legal_country_tax_id_1_name", UNSET)
        )

        def _parse_legal_country_tax_id_1(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        legal_country_tax_id_1 = _parse_legal_country_tax_id_1(
            d.pop("legal_country_tax_id_1", UNSET)
        )

        def _parse_legal_country_tax_id_2_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        legal_country_tax_id_2_name = _parse_legal_country_tax_id_2_name(
            d.pop("legal_country_tax_id_2_name", UNSET)
        )

        def _parse_legal_country_tax_id_2(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        legal_country_tax_id_2 = _parse_legal_country_tax_id_2(
            d.pop("legal_country_tax_id_2", UNSET)
        )

        def _parse_legal_country_tax_id_3_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        legal_country_tax_id_3_name = _parse_legal_country_tax_id_3_name(
            d.pop("legal_country_tax_id_3_name", UNSET)
        )

        def _parse_legal_country_tax_id_3(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        legal_country_tax_id_3 = _parse_legal_country_tax_id_3(
            d.pop("legal_country_tax_id_3", UNSET)
        )

        def _parse_legal_world_tax_id_1_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        legal_world_tax_id_1_name = _parse_legal_world_tax_id_1_name(
            d.pop("legal_world_tax_id_1_name", UNSET)
        )

        def _parse_legal_world_tax_id_1(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        legal_world_tax_id_1 = _parse_legal_world_tax_id_1(
            d.pop("legal_world_tax_id_1", UNSET)
        )

        def _parse_legal_world_tax_id_2_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        legal_world_tax_id_2_name = _parse_legal_world_tax_id_2_name(
            d.pop("legal_world_tax_id_2_name", UNSET)
        )

        def _parse_legal_world_tax_id_2(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        legal_world_tax_id_2 = _parse_legal_world_tax_id_2(
            d.pop("legal_world_tax_id_2", UNSET)
        )

        def _parse_legal_world_tax_id_3_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        legal_world_tax_id_3_name = _parse_legal_world_tax_id_3_name(
            d.pop("legal_world_tax_id_3_name", UNSET)
        )

        def _parse_legal_world_tax_id_3(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        legal_world_tax_id_3 = _parse_legal_world_tax_id_3(
            d.pop("legal_world_tax_id_3", UNSET)
        )

        def _parse_legal_other_identifier_1_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        legal_other_identifier_1_name = _parse_legal_other_identifier_1_name(
            d.pop("legal_other_identifier_1_name", UNSET)
        )

        def _parse_legal_other_identifier_1(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        legal_other_identifier_1 = _parse_legal_other_identifier_1(
            d.pop("legal_other_identifier_1", UNSET)
        )

        def _parse_legal_other_identifier_2_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        legal_other_identifier_2_name = _parse_legal_other_identifier_2_name(
            d.pop("legal_other_identifier_2_name", UNSET)
        )

        def _parse_legal_other_identifier_2(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        legal_other_identifier_2 = _parse_legal_other_identifier_2(
            d.pop("legal_other_identifier_2", UNSET)
        )

        def _parse_legal_other_identifier_3_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        legal_other_identifier_3_name = _parse_legal_other_identifier_3_name(
            d.pop("legal_other_identifier_3_name", UNSET)
        )

        def _parse_legal_other_identifier_3(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        legal_other_identifier_3 = _parse_legal_other_identifier_3(
            d.pop("legal_other_identifier_3", UNSET)
        )

        def _parse_legal_region(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        legal_region = _parse_legal_region(d.pop("legal_region", UNSET))

        def _parse_legal_city(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        legal_city = _parse_legal_city(d.pop("legal_city", UNSET))

        def _parse_legal_address_line_1(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        legal_address_line_1 = _parse_legal_address_line_1(
            d.pop("legal_address_line_1", UNSET)
        )

        def _parse_legal_address_line_2(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        legal_address_line_2 = _parse_legal_address_line_2(
            d.pop("legal_address_line_2", UNSET)
        )

        def _parse_legal_postal_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        legal_postal_code = _parse_legal_postal_code(d.pop("legal_postal_code", UNSET))

        edit_tenant_legal_info = cls(
            legal_name=legal_name,
            legal_country=legal_country,
            legal_country_registration_id_name=legal_country_registration_id_name,
            legal_country_registration_id=legal_country_registration_id,
            legal_country_tax_id_1_name=legal_country_tax_id_1_name,
            legal_country_tax_id_1=legal_country_tax_id_1,
            legal_country_tax_id_2_name=legal_country_tax_id_2_name,
            legal_country_tax_id_2=legal_country_tax_id_2,
            legal_country_tax_id_3_name=legal_country_tax_id_3_name,
            legal_country_tax_id_3=legal_country_tax_id_3,
            legal_world_tax_id_1_name=legal_world_tax_id_1_name,
            legal_world_tax_id_1=legal_world_tax_id_1,
            legal_world_tax_id_2_name=legal_world_tax_id_2_name,
            legal_world_tax_id_2=legal_world_tax_id_2,
            legal_world_tax_id_3_name=legal_world_tax_id_3_name,
            legal_world_tax_id_3=legal_world_tax_id_3,
            legal_other_identifier_1_name=legal_other_identifier_1_name,
            legal_other_identifier_1=legal_other_identifier_1,
            legal_other_identifier_2_name=legal_other_identifier_2_name,
            legal_other_identifier_2=legal_other_identifier_2,
            legal_other_identifier_3_name=legal_other_identifier_3_name,
            legal_other_identifier_3=legal_other_identifier_3,
            legal_region=legal_region,
            legal_city=legal_city,
            legal_address_line_1=legal_address_line_1,
            legal_address_line_2=legal_address_line_2,
            legal_postal_code=legal_postal_code,
        )

        edit_tenant_legal_info.additional_properties = d
        return edit_tenant_legal_info

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
