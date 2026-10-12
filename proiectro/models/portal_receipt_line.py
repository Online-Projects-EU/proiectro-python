from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.portal_receipt_line_outcome import PortalReceiptLineOutcome

T = TypeVar("T", bound="PortalReceiptLine")


@_attrs_define
class PortalReceiptLine:
    """
    Attributes:
        line_id (str):
        outcome (PortalReceiptLineOutcome):
    """

    line_id: str
    outcome: PortalReceiptLineOutcome
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        line_id = self.line_id

        outcome = self.outcome.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "line_id": line_id,
                "outcome": outcome,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        line_id = d.pop("line_id")

        outcome = PortalReceiptLineOutcome(d.pop("outcome"))

        portal_receipt_line = cls(
            line_id=line_id,
            outcome=outcome,
        )

        portal_receipt_line.additional_properties = d
        return portal_receipt_line

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
