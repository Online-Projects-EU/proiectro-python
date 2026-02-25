from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.notification_item_sender_type_0 import NotificationItemSenderType0
    from ..models.notification_item_tenant_type_0 import NotificationItemTenantType0


T = TypeVar("T", bound="NotificationItem")


@_attrs_define
class NotificationItem:
    """
    Attributes:
        id (str):
        external_id (str):
        external_id_str (str):
        title (str):
        message (str):
        notification_type (str):
        priority (str):
        icon (str):
        is_read (bool):
        created_at (datetime.datetime):
        read_at (datetime.datetime | None | Unset):
        tenant (None | NotificationItemTenantType0 | Unset):
        sender (None | NotificationItemSenderType0 | Unset):
        action_url (None | str | Unset):
    """

    id: str
    external_id: str
    external_id_str: str
    title: str
    message: str
    notification_type: str
    priority: str
    icon: str
    is_read: bool
    created_at: datetime.datetime
    read_at: datetime.datetime | None | Unset = UNSET
    tenant: None | NotificationItemTenantType0 | Unset = UNSET
    sender: None | NotificationItemSenderType0 | Unset = UNSET
    action_url: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.notification_item_sender_type_0 import NotificationItemSenderType0
        from ..models.notification_item_tenant_type_0 import NotificationItemTenantType0

        id = self.id

        external_id = self.external_id

        external_id_str = self.external_id_str

        title = self.title

        message = self.message

        notification_type = self.notification_type

        priority = self.priority

        icon = self.icon

        is_read = self.is_read

        created_at = self.created_at.isoformat()

        read_at: None | str | Unset
        if isinstance(self.read_at, Unset):
            read_at = UNSET
        elif isinstance(self.read_at, datetime.datetime):
            read_at = self.read_at.isoformat()
        else:
            read_at = self.read_at

        tenant: dict[str, Any] | None | Unset
        if isinstance(self.tenant, Unset):
            tenant = UNSET
        elif isinstance(self.tenant, NotificationItemTenantType0):
            tenant = self.tenant.to_dict()
        else:
            tenant = self.tenant

        sender: dict[str, Any] | None | Unset
        if isinstance(self.sender, Unset):
            sender = UNSET
        elif isinstance(self.sender, NotificationItemSenderType0):
            sender = self.sender.to_dict()
        else:
            sender = self.sender

        action_url: None | str | Unset
        if isinstance(self.action_url, Unset):
            action_url = UNSET
        else:
            action_url = self.action_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "external_id": external_id,
                "external_id_str": external_id_str,
                "title": title,
                "message": message,
                "notification_type": notification_type,
                "priority": priority,
                "icon": icon,
                "is_read": is_read,
                "created_at": created_at,
            }
        )
        if read_at is not UNSET:
            field_dict["read_at"] = read_at
        if tenant is not UNSET:
            field_dict["tenant"] = tenant
        if sender is not UNSET:
            field_dict["sender"] = sender
        if action_url is not UNSET:
            field_dict["action_url"] = action_url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.notification_item_sender_type_0 import NotificationItemSenderType0
        from ..models.notification_item_tenant_type_0 import NotificationItemTenantType0

        d = dict(src_dict)
        id = d.pop("id")

        external_id = d.pop("external_id")

        external_id_str = d.pop("external_id_str")

        title = d.pop("title")

        message = d.pop("message")

        notification_type = d.pop("notification_type")

        priority = d.pop("priority")

        icon = d.pop("icon")

        is_read = d.pop("is_read")

        created_at = isoparse(d.pop("created_at"))

        def _parse_read_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                read_at_type_0 = isoparse(data)

                return read_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        read_at = _parse_read_at(d.pop("read_at", UNSET))

        def _parse_tenant(data: object) -> None | NotificationItemTenantType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                tenant_type_0 = NotificationItemTenantType0.from_dict(data)

                return tenant_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | NotificationItemTenantType0 | Unset, data)

        tenant = _parse_tenant(d.pop("tenant", UNSET))

        def _parse_sender(data: object) -> None | NotificationItemSenderType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                sender_type_0 = NotificationItemSenderType0.from_dict(data)

                return sender_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | NotificationItemSenderType0 | Unset, data)

        sender = _parse_sender(d.pop("sender", UNSET))

        def _parse_action_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        action_url = _parse_action_url(d.pop("action_url", UNSET))

        notification_item = cls(
            id=id,
            external_id=external_id,
            external_id_str=external_id_str,
            title=title,
            message=message,
            notification_type=notification_type,
            priority=priority,
            icon=icon,
            is_read=is_read,
            created_at=created_at,
            read_at=read_at,
            tenant=tenant,
            sender=sender,
            action_url=action_url,
        )

        notification_item.additional_properties = d
        return notification_item

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
