from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="AddBillableSourceEntry")



@_attrs_define
class AddBillableSourceEntry:
    """ 
        Attributes:
            source_external_id (str):
            amount (float | str):
            notes (None | str | Unset):
     """

    source_external_id: str
    amount: float | str
    notes: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        source_external_id = self.source_external_id

        amount: float | str
        amount = self.amount

        notes: None | str | Unset
        if isinstance(self.notes, Unset):
            notes = UNSET
        else:
            notes = self.notes


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "source_external_id": source_external_id,
            "amount": amount,
        })
        if notes is not UNSET:
            field_dict["notes"] = notes

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        source_external_id = d.pop("source_external_id")

        def _parse_amount(data: object) -> float | str:
            return cast(float | str, data)

        amount = _parse_amount(d.pop("amount"))


        def _parse_notes(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        notes = _parse_notes(d.pop("notes", UNSET))


        add_billable_source_entry = cls(
            source_external_id=source_external_id,
            amount=amount,
            notes=notes,
        )


        add_billable_source_entry.additional_properties = d
        return add_billable_source_entry

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
