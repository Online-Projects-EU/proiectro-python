from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bridge_details_initiator_grants import BridgeDetailsInitiatorGrants
    from ..models.bridge_details_responder_grants import BridgeDetailsResponderGrants
    from ..models.bridge_tenant_info import BridgeTenantInfo


T = TypeVar("T", bound="BridgeDetails")


@_attrs_define
class BridgeDetails:
    """Details of a single bridge for subtenant display

    Attributes:
        bridge_id (str):
        status (str):
        role (str):
        initiator_tenant (BridgeTenantInfo): Tenant information in a bridge context
        initiator_grants (BridgeDetailsInitiatorGrants):
        responder_grants (BridgeDetailsResponderGrants):
        responder_tenant (BridgeTenantInfo | None | Unset):
        invitation_message (None | str | Unset):
        created_at (None | str | Unset):
        last_timestamp_name (None | str | Unset):
        last_timestamp (None | str | Unset):
        suspended_by_tenant_id (None | str | Unset):
        can_unsuspend (bool | Unset):  Default: False.
    """

    bridge_id: str
    status: str
    role: str
    initiator_tenant: BridgeTenantInfo
    initiator_grants: BridgeDetailsInitiatorGrants
    responder_grants: BridgeDetailsResponderGrants
    responder_tenant: BridgeTenantInfo | None | Unset = UNSET
    invitation_message: None | str | Unset = UNSET
    created_at: None | str | Unset = UNSET
    last_timestamp_name: None | str | Unset = UNSET
    last_timestamp: None | str | Unset = UNSET
    suspended_by_tenant_id: None | str | Unset = UNSET
    can_unsuspend: bool | Unset = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.bridge_tenant_info import BridgeTenantInfo

        bridge_id = self.bridge_id

        status = self.status

        role = self.role

        initiator_tenant = self.initiator_tenant.to_dict()

        initiator_grants = self.initiator_grants.to_dict()

        responder_grants = self.responder_grants.to_dict()

        responder_tenant: dict[str, Any] | None | Unset
        if isinstance(self.responder_tenant, Unset):
            responder_tenant = UNSET
        elif isinstance(self.responder_tenant, BridgeTenantInfo):
            responder_tenant = self.responder_tenant.to_dict()
        else:
            responder_tenant = self.responder_tenant

        invitation_message: None | str | Unset
        if isinstance(self.invitation_message, Unset):
            invitation_message = UNSET
        else:
            invitation_message = self.invitation_message

        created_at: None | str | Unset
        if isinstance(self.created_at, Unset):
            created_at = UNSET
        else:
            created_at = self.created_at

        last_timestamp_name: None | str | Unset
        if isinstance(self.last_timestamp_name, Unset):
            last_timestamp_name = UNSET
        else:
            last_timestamp_name = self.last_timestamp_name

        last_timestamp: None | str | Unset
        if isinstance(self.last_timestamp, Unset):
            last_timestamp = UNSET
        else:
            last_timestamp = self.last_timestamp

        suspended_by_tenant_id: None | str | Unset
        if isinstance(self.suspended_by_tenant_id, Unset):
            suspended_by_tenant_id = UNSET
        else:
            suspended_by_tenant_id = self.suspended_by_tenant_id

        can_unsuspend = self.can_unsuspend

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "bridge_id": bridge_id,
                "status": status,
                "role": role,
                "initiator_tenant": initiator_tenant,
                "initiator_grants": initiator_grants,
                "responder_grants": responder_grants,
            }
        )
        if responder_tenant is not UNSET:
            field_dict["responder_tenant"] = responder_tenant
        if invitation_message is not UNSET:
            field_dict["invitation_message"] = invitation_message
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if last_timestamp_name is not UNSET:
            field_dict["last_timestamp_name"] = last_timestamp_name
        if last_timestamp is not UNSET:
            field_dict["last_timestamp"] = last_timestamp
        if suspended_by_tenant_id is not UNSET:
            field_dict["suspended_by_tenant_id"] = suspended_by_tenant_id
        if can_unsuspend is not UNSET:
            field_dict["can_unsuspend"] = can_unsuspend

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bridge_details_initiator_grants import (
            BridgeDetailsInitiatorGrants,
        )
        from ..models.bridge_details_responder_grants import (
            BridgeDetailsResponderGrants,
        )
        from ..models.bridge_tenant_info import BridgeTenantInfo

        d = dict(src_dict)
        bridge_id = d.pop("bridge_id")

        status = d.pop("status")

        role = d.pop("role")

        initiator_tenant = BridgeTenantInfo.from_dict(d.pop("initiator_tenant"))

        initiator_grants = BridgeDetailsInitiatorGrants.from_dict(
            d.pop("initiator_grants")
        )

        responder_grants = BridgeDetailsResponderGrants.from_dict(
            d.pop("responder_grants")
        )

        def _parse_responder_tenant(data: object) -> BridgeTenantInfo | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                responder_tenant_type_0 = BridgeTenantInfo.from_dict(data)

                return responder_tenant_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(BridgeTenantInfo | None | Unset, data)

        responder_tenant = _parse_responder_tenant(d.pop("responder_tenant", UNSET))

        def _parse_invitation_message(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        invitation_message = _parse_invitation_message(
            d.pop("invitation_message", UNSET)
        )

        def _parse_created_at(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        created_at = _parse_created_at(d.pop("created_at", UNSET))

        def _parse_last_timestamp_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        last_timestamp_name = _parse_last_timestamp_name(
            d.pop("last_timestamp_name", UNSET)
        )

        def _parse_last_timestamp(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        last_timestamp = _parse_last_timestamp(d.pop("last_timestamp", UNSET))

        def _parse_suspended_by_tenant_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        suspended_by_tenant_id = _parse_suspended_by_tenant_id(
            d.pop("suspended_by_tenant_id", UNSET)
        )

        can_unsuspend = d.pop("can_unsuspend", UNSET)

        bridge_details = cls(
            bridge_id=bridge_id,
            status=status,
            role=role,
            initiator_tenant=initiator_tenant,
            initiator_grants=initiator_grants,
            responder_grants=responder_grants,
            responder_tenant=responder_tenant,
            invitation_message=invitation_message,
            created_at=created_at,
            last_timestamp_name=last_timestamp_name,
            last_timestamp=last_timestamp,
            suspended_by_tenant_id=suspended_by_tenant_id,
            can_unsuspend=can_unsuspend,
        )

        bridge_details.additional_properties = d
        return bridge_details

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
