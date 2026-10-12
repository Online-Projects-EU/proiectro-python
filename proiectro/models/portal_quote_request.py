from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.portal_quote_request_line import PortalQuoteRequestLine


T = TypeVar("T", bound="PortalQuoteRequest")


@_attrs_define
class PortalQuoteRequest:
    """A quote request as its customer sees it while it waits for an offer: what was asked, never
    the supplier's prices while the offer is being prepared.

        Attributes:
            id (str):
            name (str):
            created_at (datetime.datetime):
            can_withdraw (bool):
            reference (None | str | Unset):
            description (str | Unset):  Default: ''.
            wanted_by (datetime.date | None | Unset):
            customer_reference (str | Unset):  Default: ''.
            location_name (None | str | Unset):
            asset_name (None | str | Unset):
            requested_by_name (None | str | Unset):
            lines (list[PortalQuoteRequestLine] | Unset):
    """

    id: str
    name: str
    created_at: datetime.datetime
    can_withdraw: bool
    reference: None | str | Unset = UNSET
    description: str | Unset = ""
    wanted_by: datetime.date | None | Unset = UNSET
    customer_reference: str | Unset = ""
    location_name: None | str | Unset = UNSET
    asset_name: None | str | Unset = UNSET
    requested_by_name: None | str | Unset = UNSET
    lines: list[PortalQuoteRequestLine] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        created_at = self.created_at.isoformat()

        can_withdraw = self.can_withdraw

        reference: None | str | Unset
        if isinstance(self.reference, Unset):
            reference = UNSET
        else:
            reference = self.reference

        description = self.description

        wanted_by: None | str | Unset
        if isinstance(self.wanted_by, Unset):
            wanted_by = UNSET
        elif isinstance(self.wanted_by, datetime.date):
            wanted_by = self.wanted_by.isoformat()
        else:
            wanted_by = self.wanted_by

        customer_reference = self.customer_reference

        location_name: None | str | Unset
        if isinstance(self.location_name, Unset):
            location_name = UNSET
        else:
            location_name = self.location_name

        asset_name: None | str | Unset
        if isinstance(self.asset_name, Unset):
            asset_name = UNSET
        else:
            asset_name = self.asset_name

        requested_by_name: None | str | Unset
        if isinstance(self.requested_by_name, Unset):
            requested_by_name = UNSET
        else:
            requested_by_name = self.requested_by_name

        lines: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.lines, Unset):
            lines = []
            for lines_item_data in self.lines:
                lines_item = lines_item_data.to_dict()
                lines.append(lines_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "created_at": created_at,
                "can_withdraw": can_withdraw,
            }
        )
        if reference is not UNSET:
            field_dict["reference"] = reference
        if description is not UNSET:
            field_dict["description"] = description
        if wanted_by is not UNSET:
            field_dict["wanted_by"] = wanted_by
        if customer_reference is not UNSET:
            field_dict["customer_reference"] = customer_reference
        if location_name is not UNSET:
            field_dict["location_name"] = location_name
        if asset_name is not UNSET:
            field_dict["asset_name"] = asset_name
        if requested_by_name is not UNSET:
            field_dict["requested_by_name"] = requested_by_name
        if lines is not UNSET:
            field_dict["lines"] = lines

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.portal_quote_request_line import PortalQuoteRequestLine

        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        created_at = isoparse(d.pop("created_at"))

        can_withdraw = d.pop("can_withdraw")

        def _parse_reference(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        reference = _parse_reference(d.pop("reference", UNSET))

        description = d.pop("description", UNSET)

        def _parse_wanted_by(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                wanted_by_type_0 = isoparse(data).date()

                return wanted_by_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None | Unset, data)

        wanted_by = _parse_wanted_by(d.pop("wanted_by", UNSET))

        customer_reference = d.pop("customer_reference", UNSET)

        def _parse_location_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        location_name = _parse_location_name(d.pop("location_name", UNSET))

        def _parse_asset_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        asset_name = _parse_asset_name(d.pop("asset_name", UNSET))

        def _parse_requested_by_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        requested_by_name = _parse_requested_by_name(d.pop("requested_by_name", UNSET))

        _lines = d.pop("lines", UNSET)
        lines: list[PortalQuoteRequestLine] | Unset = UNSET
        if _lines is not UNSET:
            lines = []
            for lines_item_data in _lines:
                lines_item = PortalQuoteRequestLine.from_dict(lines_item_data)

                lines.append(lines_item)

        portal_quote_request = cls(
            id=id,
            name=name,
            created_at=created_at,
            can_withdraw=can_withdraw,
            reference=reference,
            description=description,
            wanted_by=wanted_by,
            customer_reference=customer_reference,
            location_name=location_name,
            asset_name=asset_name,
            requested_by_name=requested_by_name,
            lines=lines,
        )

        portal_quote_request.additional_properties = d
        return portal_quote_request

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
