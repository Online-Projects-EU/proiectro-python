from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.portal_quote_line import PortalQuoteLine


T = TypeVar("T", bound="PortalRequestQuote")


@_attrs_define
class PortalRequestQuote:
    """Input schema for a customer asking for a quote in the portal

    Attributes:
        lines (list[PortalQuoteLine]):
        description (str | Unset):  Default: ''.
        customer_location (None | str | Unset):
        customer_asset (None | str | Unset):
        customer_reference (None | str | Unset):
        wanted_by (None | str | Unset):
    """

    lines: list[PortalQuoteLine]
    description: str | Unset = ""
    customer_location: None | str | Unset = UNSET
    customer_asset: None | str | Unset = UNSET
    customer_reference: None | str | Unset = UNSET
    wanted_by: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        lines = []
        for lines_item_data in self.lines:
            lines_item = lines_item_data.to_dict()
            lines.append(lines_item)

        description = self.description

        customer_location: None | str | Unset
        if isinstance(self.customer_location, Unset):
            customer_location = UNSET
        else:
            customer_location = self.customer_location

        customer_asset: None | str | Unset
        if isinstance(self.customer_asset, Unset):
            customer_asset = UNSET
        else:
            customer_asset = self.customer_asset

        customer_reference: None | str | Unset
        if isinstance(self.customer_reference, Unset):
            customer_reference = UNSET
        else:
            customer_reference = self.customer_reference

        wanted_by: None | str | Unset
        if isinstance(self.wanted_by, Unset):
            wanted_by = UNSET
        else:
            wanted_by = self.wanted_by

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "lines": lines,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if customer_location is not UNSET:
            field_dict["customer_location"] = customer_location
        if customer_asset is not UNSET:
            field_dict["customer_asset"] = customer_asset
        if customer_reference is not UNSET:
            field_dict["customer_reference"] = customer_reference
        if wanted_by is not UNSET:
            field_dict["wanted_by"] = wanted_by

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.portal_quote_line import PortalQuoteLine

        d = dict(src_dict)
        lines = []
        _lines = d.pop("lines")
        for lines_item_data in _lines:
            lines_item = PortalQuoteLine.from_dict(lines_item_data)

            lines.append(lines_item)

        description = d.pop("description", UNSET)

        def _parse_customer_location(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        customer_location = _parse_customer_location(d.pop("customer_location", UNSET))

        def _parse_customer_asset(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        customer_asset = _parse_customer_asset(d.pop("customer_asset", UNSET))

        def _parse_customer_reference(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        customer_reference = _parse_customer_reference(
            d.pop("customer_reference", UNSET)
        )

        def _parse_wanted_by(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        wanted_by = _parse_wanted_by(d.pop("wanted_by", UNSET))

        portal_request_quote = cls(
            lines=lines,
            description=description,
            customer_location=customer_location,
            customer_asset=customer_asset,
            customer_reference=customer_reference,
            wanted_by=wanted_by,
        )

        portal_request_quote.additional_properties = d
        return portal_request_quote

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
