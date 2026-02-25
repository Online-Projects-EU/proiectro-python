from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="ResourceCostRecord")


@_attrs_define
class ResourceCostRecord:
    """
    Attributes:
        id (str):
        name (str):
        status (str):
        value (str):
        currency (str):
        cost_type (str):
        effective_start_datetime (datetime.datetime):
        created_at (datetime.datetime):
        created_by (str):
        description (None | str | Unset):
        effective_end_datetime (datetime.datetime | None | Unset):
        updated_at (datetime.datetime | None | Unset):
        updated_by (None | str | Unset):
    """

    id: str
    name: str
    status: str
    value: str
    currency: str
    cost_type: str
    effective_start_datetime: datetime.datetime
    created_at: datetime.datetime
    created_by: str
    description: None | str | Unset = UNSET
    effective_end_datetime: datetime.datetime | None | Unset = UNSET
    updated_at: datetime.datetime | None | Unset = UNSET
    updated_by: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        status = self.status

        value = self.value

        currency = self.currency

        cost_type = self.cost_type

        effective_start_datetime = self.effective_start_datetime.isoformat()

        created_at = self.created_at.isoformat()

        created_by = self.created_by

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        effective_end_datetime: None | str | Unset
        if isinstance(self.effective_end_datetime, Unset):
            effective_end_datetime = UNSET
        elif isinstance(self.effective_end_datetime, datetime.datetime):
            effective_end_datetime = self.effective_end_datetime.isoformat()
        else:
            effective_end_datetime = self.effective_end_datetime

        updated_at: None | str | Unset
        if isinstance(self.updated_at, Unset):
            updated_at = UNSET
        elif isinstance(self.updated_at, datetime.datetime):
            updated_at = self.updated_at.isoformat()
        else:
            updated_at = self.updated_at

        updated_by: None | str | Unset
        if isinstance(self.updated_by, Unset):
            updated_by = UNSET
        else:
            updated_by = self.updated_by

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "status": status,
                "value": value,
                "currency": currency,
                "cost_type": cost_type,
                "effective_start_datetime": effective_start_datetime,
                "created_at": created_at,
                "created_by": created_by,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if effective_end_datetime is not UNSET:
            field_dict["effective_end_datetime"] = effective_end_datetime
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if updated_by is not UNSET:
            field_dict["updated_by"] = updated_by

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        status = d.pop("status")

        value = d.pop("value")

        currency = d.pop("currency")

        cost_type = d.pop("cost_type")

        effective_start_datetime = isoparse(d.pop("effective_start_datetime"))

        created_at = isoparse(d.pop("created_at"))

        created_by = d.pop("created_by")

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_effective_end_datetime(
            data: object,
        ) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                effective_end_datetime_type_0 = isoparse(data)

                return effective_end_datetime_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        effective_end_datetime = _parse_effective_end_datetime(
            d.pop("effective_end_datetime", UNSET)
        )

        def _parse_updated_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                updated_at_type_0 = isoparse(data)

                return updated_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        updated_at = _parse_updated_at(d.pop("updated_at", UNSET))

        def _parse_updated_by(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        updated_by = _parse_updated_by(d.pop("updated_by", UNSET))

        resource_cost_record = cls(
            id=id,
            name=name,
            status=status,
            value=value,
            currency=currency,
            cost_type=cost_type,
            effective_start_datetime=effective_start_datetime,
            created_at=created_at,
            created_by=created_by,
            description=description,
            effective_end_datetime=effective_end_datetime,
            updated_at=updated_at,
            updated_by=updated_by,
        )

        resource_cost_record.additional_properties = d
        return resource_cost_record

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
