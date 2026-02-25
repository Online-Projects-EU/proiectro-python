from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bridge_history_entry_details_type_0 import (
        BridgeHistoryEntryDetailsType0,
    )


T = TypeVar("T", bound="BridgeHistoryEntry")


@_attrs_define
class BridgeHistoryEntry:
    """Single audit entry for a bridge

    Attributes:
        action (str):
        timestamp (str):
        previous_status (None | str):
        new_status (str):
        performed_by_name (str):
        performed_by_email (str):
        performed_by_tenant_name (str):
        grants (list[str] | None | Unset):
        details (BridgeHistoryEntryDetailsType0 | None | Unset):
        ip_address (None | str | Unset):
    """

    action: str
    timestamp: str
    previous_status: None | str
    new_status: str
    performed_by_name: str
    performed_by_email: str
    performed_by_tenant_name: str
    grants: list[str] | None | Unset = UNSET
    details: BridgeHistoryEntryDetailsType0 | None | Unset = UNSET
    ip_address: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.bridge_history_entry_details_type_0 import (
            BridgeHistoryEntryDetailsType0,
        )

        action = self.action

        timestamp = self.timestamp

        previous_status: None | str
        previous_status = self.previous_status

        new_status = self.new_status

        performed_by_name = self.performed_by_name

        performed_by_email = self.performed_by_email

        performed_by_tenant_name = self.performed_by_tenant_name

        grants: list[str] | None | Unset
        if isinstance(self.grants, Unset):
            grants = UNSET
        elif isinstance(self.grants, list):
            grants = self.grants

        else:
            grants = self.grants

        details: dict[str, Any] | None | Unset
        if isinstance(self.details, Unset):
            details = UNSET
        elif isinstance(self.details, BridgeHistoryEntryDetailsType0):
            details = self.details.to_dict()
        else:
            details = self.details

        ip_address: None | str | Unset
        if isinstance(self.ip_address, Unset):
            ip_address = UNSET
        else:
            ip_address = self.ip_address

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "action": action,
                "timestamp": timestamp,
                "previous_status": previous_status,
                "new_status": new_status,
                "performed_by_name": performed_by_name,
                "performed_by_email": performed_by_email,
                "performed_by_tenant_name": performed_by_tenant_name,
            }
        )
        if grants is not UNSET:
            field_dict["grants"] = grants
        if details is not UNSET:
            field_dict["details"] = details
        if ip_address is not UNSET:
            field_dict["ip_address"] = ip_address

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bridge_history_entry_details_type_0 import (
            BridgeHistoryEntryDetailsType0,
        )

        d = dict(src_dict)
        action = d.pop("action")

        timestamp = d.pop("timestamp")

        def _parse_previous_status(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        previous_status = _parse_previous_status(d.pop("previous_status"))

        new_status = d.pop("new_status")

        performed_by_name = d.pop("performed_by_name")

        performed_by_email = d.pop("performed_by_email")

        performed_by_tenant_name = d.pop("performed_by_tenant_name")

        def _parse_grants(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                grants_type_0 = cast(list[str], data)

                return grants_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        grants = _parse_grants(d.pop("grants", UNSET))

        def _parse_details(
            data: object,
        ) -> BridgeHistoryEntryDetailsType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                details_type_0 = BridgeHistoryEntryDetailsType0.from_dict(data)

                return details_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(BridgeHistoryEntryDetailsType0 | None | Unset, data)

        details = _parse_details(d.pop("details", UNSET))

        def _parse_ip_address(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        ip_address = _parse_ip_address(d.pop("ip_address", UNSET))

        bridge_history_entry = cls(
            action=action,
            timestamp=timestamp,
            previous_status=previous_status,
            new_status=new_status,
            performed_by_name=performed_by_name,
            performed_by_email=performed_by_email,
            performed_by_tenant_name=performed_by_tenant_name,
            grants=grants,
            details=details,
            ip_address=ip_address,
        )

        bridge_history_entry.additional_properties = d
        return bridge_history_entry

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
