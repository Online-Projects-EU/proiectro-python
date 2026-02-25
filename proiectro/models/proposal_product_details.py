from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="ProposalProductDetails")


@_attrs_define
class ProposalProductDetails:
    """
    Attributes:
        id (str):
        name (str):
        description (str):
        pricing_type (str):
        pricing_value (float | str):
        pricing_currency (str):
        currency_symbol (str):
        is_finished (bool):
        is_accepted (bool):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        owner_id (str):
        owner_name (str):
        catalog_id (None | str | Unset):
        catalog_name (None | str | Unset):
    """

    id: str
    name: str
    description: str
    pricing_type: str
    pricing_value: float | str
    pricing_currency: str
    currency_symbol: str
    is_finished: bool
    is_accepted: bool
    created_at: datetime.datetime
    updated_at: datetime.datetime
    owner_id: str
    owner_name: str
    catalog_id: None | str | Unset = UNSET
    catalog_name: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        description = self.description

        pricing_type = self.pricing_type

        pricing_value: float | str
        pricing_value = self.pricing_value

        pricing_currency = self.pricing_currency

        currency_symbol = self.currency_symbol

        is_finished = self.is_finished

        is_accepted = self.is_accepted

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        owner_id = self.owner_id

        owner_name = self.owner_name

        catalog_id: None | str | Unset
        if isinstance(self.catalog_id, Unset):
            catalog_id = UNSET
        else:
            catalog_id = self.catalog_id

        catalog_name: None | str | Unset
        if isinstance(self.catalog_name, Unset):
            catalog_name = UNSET
        else:
            catalog_name = self.catalog_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "description": description,
                "pricing_type": pricing_type,
                "pricing_value": pricing_value,
                "pricing_currency": pricing_currency,
                "currency_symbol": currency_symbol,
                "is_finished": is_finished,
                "is_accepted": is_accepted,
                "created_at": created_at,
                "updated_at": updated_at,
                "owner_id": owner_id,
                "owner_name": owner_name,
            }
        )
        if catalog_id is not UNSET:
            field_dict["catalog_id"] = catalog_id
        if catalog_name is not UNSET:
            field_dict["catalog_name"] = catalog_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        description = d.pop("description")

        pricing_type = d.pop("pricing_type")

        def _parse_pricing_value(data: object) -> float | str:
            return cast(float | str, data)

        pricing_value = _parse_pricing_value(d.pop("pricing_value"))

        pricing_currency = d.pop("pricing_currency")

        currency_symbol = d.pop("currency_symbol")

        is_finished = d.pop("is_finished")

        is_accepted = d.pop("is_accepted")

        created_at = isoparse(d.pop("created_at"))

        updated_at = isoparse(d.pop("updated_at"))

        owner_id = d.pop("owner_id")

        owner_name = d.pop("owner_name")

        def _parse_catalog_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        catalog_id = _parse_catalog_id(d.pop("catalog_id", UNSET))

        def _parse_catalog_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        catalog_name = _parse_catalog_name(d.pop("catalog_name", UNSET))

        proposal_product_details = cls(
            id=id,
            name=name,
            description=description,
            pricing_type=pricing_type,
            pricing_value=pricing_value,
            pricing_currency=pricing_currency,
            currency_symbol=currency_symbol,
            is_finished=is_finished,
            is_accepted=is_accepted,
            created_at=created_at,
            updated_at=updated_at,
            owner_id=owner_id,
            owner_name=owner_name,
            catalog_id=catalog_id,
            catalog_name=catalog_name,
        )

        proposal_product_details.additional_properties = d
        return proposal_product_details

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
