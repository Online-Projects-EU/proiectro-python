from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PortalQuoteRequestLine")


@_attrs_define
class PortalQuoteRequestLine:
    """
    Attributes:
        name (str):
        quantity (int):
        unit_of_measure (str | Unset):  Default: ''.
        image_url (None | str | Unset):
    """

    name: str
    quantity: int
    unit_of_measure: str | Unset = ""
    image_url: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        quantity = self.quantity

        unit_of_measure = self.unit_of_measure

        image_url: None | str | Unset
        if isinstance(self.image_url, Unset):
            image_url = UNSET
        else:
            image_url = self.image_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "quantity": quantity,
            }
        )
        if unit_of_measure is not UNSET:
            field_dict["unit_of_measure"] = unit_of_measure
        if image_url is not UNSET:
            field_dict["image_url"] = image_url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        quantity = d.pop("quantity")

        unit_of_measure = d.pop("unit_of_measure", UNSET)

        def _parse_image_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        image_url = _parse_image_url(d.pop("image_url", UNSET))

        portal_quote_request_line = cls(
            name=name,
            quantity=quantity,
            unit_of_measure=unit_of_measure,
            image_url=image_url,
        )

        portal_quote_request_line.additional_properties = d
        return portal_quote_request_line

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
