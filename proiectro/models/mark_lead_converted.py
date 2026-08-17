from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
import datetime






T = TypeVar("T", bound="MarkLeadConverted")



@_attrs_define
class MarkLeadConverted:
    """ Convert a lead to an Opportunity.

    Two branches:
      1. Existing-org branch: caller supplies `org` (a 32-hex external_id of
         an active subtenant) and leaves the new_org_* fields empty/absent.
      2. New-org branch: caller leaves `org` empty/absent and supplies the
         full new_org_* set; the API creates the subtenant, then converts.

    Cross-field validation rejects "neither" and "both", and requires the
    full new_org_* set when the new-org branch is taken (single-field gaps
    return a clear error rather than a downstream IntegrityError).

        Attributes:
            updated_at (datetime.datetime):
            org (None | str | Unset):
            new_org_name (None | str | Unset):
            new_org_currency (None | str | Unset):
            new_org_country (None | str | Unset):
            new_org_timezone (None | str | Unset):
            new_org_manager (None | str | Unset):
     """

    updated_at: datetime.datetime
    org: None | str | Unset = UNSET
    new_org_name: None | str | Unset = UNSET
    new_org_currency: None | str | Unset = UNSET
    new_org_country: None | str | Unset = UNSET
    new_org_timezone: None | str | Unset = UNSET
    new_org_manager: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        updated_at = self.updated_at.isoformat()

        org: None | str | Unset
        if isinstance(self.org, Unset):
            org = UNSET
        else:
            org = self.org

        new_org_name: None | str | Unset
        if isinstance(self.new_org_name, Unset):
            new_org_name = UNSET
        else:
            new_org_name = self.new_org_name

        new_org_currency: None | str | Unset
        if isinstance(self.new_org_currency, Unset):
            new_org_currency = UNSET
        else:
            new_org_currency = self.new_org_currency

        new_org_country: None | str | Unset
        if isinstance(self.new_org_country, Unset):
            new_org_country = UNSET
        else:
            new_org_country = self.new_org_country

        new_org_timezone: None | str | Unset
        if isinstance(self.new_org_timezone, Unset):
            new_org_timezone = UNSET
        else:
            new_org_timezone = self.new_org_timezone

        new_org_manager: None | str | Unset
        if isinstance(self.new_org_manager, Unset):
            new_org_manager = UNSET
        else:
            new_org_manager = self.new_org_manager


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "updated_at": updated_at,
        })
        if org is not UNSET:
            field_dict["org"] = org
        if new_org_name is not UNSET:
            field_dict["new_org_name"] = new_org_name
        if new_org_currency is not UNSET:
            field_dict["new_org_currency"] = new_org_currency
        if new_org_country is not UNSET:
            field_dict["new_org_country"] = new_org_country
        if new_org_timezone is not UNSET:
            field_dict["new_org_timezone"] = new_org_timezone
        if new_org_manager is not UNSET:
            field_dict["new_org_manager"] = new_org_manager

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        updated_at = isoparse(d.pop("updated_at"))




        def _parse_org(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        org = _parse_org(d.pop("org", UNSET))


        def _parse_new_org_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        new_org_name = _parse_new_org_name(d.pop("new_org_name", UNSET))


        def _parse_new_org_currency(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        new_org_currency = _parse_new_org_currency(d.pop("new_org_currency", UNSET))


        def _parse_new_org_country(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        new_org_country = _parse_new_org_country(d.pop("new_org_country", UNSET))


        def _parse_new_org_timezone(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        new_org_timezone = _parse_new_org_timezone(d.pop("new_org_timezone", UNSET))


        def _parse_new_org_manager(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        new_org_manager = _parse_new_org_manager(d.pop("new_org_manager", UNSET))


        mark_lead_converted = cls(
            updated_at=updated_at,
            org=org,
            new_org_name=new_org_name,
            new_org_currency=new_org_currency,
            new_org_country=new_org_country,
            new_org_timezone=new_org_timezone,
            new_org_manager=new_org_manager,
        )


        mark_lead_converted.additional_properties = d
        return mark_lead_converted

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
