from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="OutputLeadAtCompany")


@_attrs_define
class OutputLeadAtCompany:
    """Another open lead at the same company, one the caller may open.

    Attributes:
        id (str):
        name (str):
        status_label (str):
        company_name (str | Unset):  Default: ''.
        owner_name (None | str | Unset):
    """

    id: str
    name: str
    status_label: str
    company_name: str | Unset = ""
    owner_name: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        status_label = self.status_label

        company_name = self.company_name

        owner_name: None | str | Unset
        if isinstance(self.owner_name, Unset):
            owner_name = UNSET
        else:
            owner_name = self.owner_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "status_label": status_label,
            }
        )
        if company_name is not UNSET:
            field_dict["company_name"] = company_name
        if owner_name is not UNSET:
            field_dict["owner_name"] = owner_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        status_label = d.pop("status_label")

        company_name = d.pop("company_name", UNSET)

        def _parse_owner_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        owner_name = _parse_owner_name(d.pop("owner_name", UNSET))

        output_lead_at_company = cls(
            id=id,
            name=name,
            status_label=status_label,
            company_name=company_name,
            owner_name=owner_name,
        )

        output_lead_at_company.additional_properties = d
        return output_lead_at_company

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
