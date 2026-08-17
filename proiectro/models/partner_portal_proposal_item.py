from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from dateutil.parser import isoparse
from typing import cast
import datetime






T = TypeVar("T", bound="PartnerPortalProposalItem")



@_attrs_define
class PartnerPortalProposalItem:
    """ Single proposal in partner portal

        Attributes:
            id (str):
            title (str):
            description (None | str):
            status (str):
            created_at (datetime.datetime):
            estimated_value (None | str):
            currency (None | str):
     """

    id: str
    title: str
    description: None | str
    status: str
    created_at: datetime.datetime
    estimated_value: None | str
    currency: None | str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        id = self.id

        title = self.title

        description: None | str
        description = self.description

        status = self.status

        created_at = self.created_at.isoformat()

        estimated_value: None | str
        estimated_value = self.estimated_value

        currency: None | str
        currency = self.currency


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "id": id,
            "title": title,
            "description": description,
            "status": status,
            "created_at": created_at,
            "estimated_value": estimated_value,
            "currency": currency,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        title = d.pop("title")

        def _parse_description(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        description = _parse_description(d.pop("description"))


        status = d.pop("status")

        created_at = isoparse(d.pop("created_at"))




        def _parse_estimated_value(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        estimated_value = _parse_estimated_value(d.pop("estimated_value"))


        def _parse_currency(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        currency = _parse_currency(d.pop("currency"))


        partner_portal_proposal_item = cls(
            id=id,
            title=title,
            description=description,
            status=status,
            created_at=created_at,
            estimated_value=estimated_value,
            currency=currency,
        )


        partner_portal_proposal_item.additional_properties = d
        return partner_portal_proposal_item

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
