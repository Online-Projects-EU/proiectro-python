from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.notification_item import NotificationItem


T = TypeVar("T", bound="OutputUserNotifications")


@_attrs_define
class OutputUserNotifications:
    """
    Attributes:
        notifications (list[NotificationItem]):
        page (int):
        per_page (int):
        total_count (int):
        has_next (bool):
        next_page (int):
        unread_count (int):
        user_tenant_count (int):
    """

    notifications: list[NotificationItem]
    page: int
    per_page: int
    total_count: int
    has_next: bool
    next_page: int
    unread_count: int
    user_tenant_count: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        notifications = []
        for notifications_item_data in self.notifications:
            notifications_item = notifications_item_data.to_dict()
            notifications.append(notifications_item)

        page = self.page

        per_page = self.per_page

        total_count = self.total_count

        has_next = self.has_next

        next_page = self.next_page

        unread_count = self.unread_count

        user_tenant_count = self.user_tenant_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "notifications": notifications,
                "page": page,
                "per_page": per_page,
                "total_count": total_count,
                "has_next": has_next,
                "next_page": next_page,
                "unread_count": unread_count,
                "user_tenant_count": user_tenant_count,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.notification_item import NotificationItem

        d = dict(src_dict)
        notifications = []
        _notifications = d.pop("notifications")
        for notifications_item_data in _notifications:
            notifications_item = NotificationItem.from_dict(notifications_item_data)

            notifications.append(notifications_item)

        page = d.pop("page")

        per_page = d.pop("per_page")

        total_count = d.pop("total_count")

        has_next = d.pop("has_next")

        next_page = d.pop("next_page")

        unread_count = d.pop("unread_count")

        user_tenant_count = d.pop("user_tenant_count")

        output_user_notifications = cls(
            notifications=notifications,
            page=page,
            per_page=per_page,
            total_count=total_count,
            has_next=has_next,
            next_page=next_page,
            unread_count=unread_count,
            user_tenant_count=user_tenant_count,
        )

        output_user_notifications.additional_properties = d
        return output_user_notifications

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
