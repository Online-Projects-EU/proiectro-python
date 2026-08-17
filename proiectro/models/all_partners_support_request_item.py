from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from dateutil.parser import isoparse
from typing import cast
import datetime






T = TypeVar("T", bound="AllPartnersSupportRequestItem")



@_attrs_define
class AllPartnersSupportRequestItem:
    """ Support request item with partner context for aggregated view

        Attributes:
            id (str):
            public_reference (str):
            title (str):
            description (None | str):
            status (str):
            priority (str):
            created_at (datetime.datetime):
            updated_at (datetime.datetime):
            requester_name (None | str):
            partner_tenant_name (str):
            bridge_id (str):
            proxy_subtenant_id (str):
     """

    id: str
    public_reference: str
    title: str
    description: None | str
    status: str
    priority: str
    created_at: datetime.datetime
    updated_at: datetime.datetime
    requester_name: None | str
    partner_tenant_name: str
    bridge_id: str
    proxy_subtenant_id: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        id = self.id

        public_reference = self.public_reference

        title = self.title

        description: None | str
        description = self.description

        status = self.status

        priority = self.priority

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        requester_name: None | str
        requester_name = self.requester_name

        partner_tenant_name = self.partner_tenant_name

        bridge_id = self.bridge_id

        proxy_subtenant_id = self.proxy_subtenant_id


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "id": id,
            "public_reference": public_reference,
            "title": title,
            "description": description,
            "status": status,
            "priority": priority,
            "created_at": created_at,
            "updated_at": updated_at,
            "requester_name": requester_name,
            "partner_tenant_name": partner_tenant_name,
            "bridge_id": bridge_id,
            "proxy_subtenant_id": proxy_subtenant_id,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        public_reference = d.pop("public_reference")

        title = d.pop("title")

        def _parse_description(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        description = _parse_description(d.pop("description"))


        status = d.pop("status")

        priority = d.pop("priority")

        created_at = isoparse(d.pop("created_at"))




        updated_at = isoparse(d.pop("updated_at"))




        def _parse_requester_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        requester_name = _parse_requester_name(d.pop("requester_name"))


        partner_tenant_name = d.pop("partner_tenant_name")

        bridge_id = d.pop("bridge_id")

        proxy_subtenant_id = d.pop("proxy_subtenant_id")

        all_partners_support_request_item = cls(
            id=id,
            public_reference=public_reference,
            title=title,
            description=description,
            status=status,
            priority=priority,
            created_at=created_at,
            updated_at=updated_at,
            requester_name=requester_name,
            partner_tenant_name=partner_tenant_name,
            bridge_id=bridge_id,
            proxy_subtenant_id=proxy_subtenant_id,
        )


        all_partners_support_request_item.additional_properties = d
        return all_partners_support_request_item

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
