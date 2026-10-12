from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="OutputBillableSource")


@_attrs_define
class OutputBillableSource:
    """One eligible source row in the picker (a closed ExternalSupportRequest or
    a finished OperationalWorkItem in a final stage).

        Attributes:
            external_id (str):
            label (str):
            reference_date (datetime.datetime | None | Unset):
            suggested_amount (float | None | str | Unset):
    """

    external_id: str
    label: str
    reference_date: datetime.datetime | None | Unset = UNSET
    suggested_amount: float | None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        external_id = self.external_id

        label = self.label

        reference_date: None | str | Unset
        if isinstance(self.reference_date, Unset):
            reference_date = UNSET
        elif isinstance(self.reference_date, datetime.datetime):
            reference_date = self.reference_date.isoformat()
        else:
            reference_date = self.reference_date

        suggested_amount: float | None | str | Unset
        if isinstance(self.suggested_amount, Unset):
            suggested_amount = UNSET
        else:
            suggested_amount = self.suggested_amount

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "external_id": external_id,
                "label": label,
            }
        )
        if reference_date is not UNSET:
            field_dict["reference_date"] = reference_date
        if suggested_amount is not UNSET:
            field_dict["suggested_amount"] = suggested_amount

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        external_id = d.pop("external_id")

        label = d.pop("label")

        def _parse_reference_date(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                reference_date_type_0 = isoparse(data)

                return reference_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        reference_date = _parse_reference_date(d.pop("reference_date", UNSET))

        def _parse_suggested_amount(data: object) -> float | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | str | Unset, data)

        suggested_amount = _parse_suggested_amount(d.pop("suggested_amount", UNSET))

        output_billable_source = cls(
            external_id=external_id,
            label=label,
            reference_date=reference_date,
            suggested_amount=suggested_amount,
        )

        output_billable_source.additional_properties = d
        return output_billable_source

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
