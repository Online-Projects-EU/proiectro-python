from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.output_sent_message_attachment import OutputSentMessageAttachment


T = TypeVar("T", bound="OutputSentMessage")


@_attrs_define
class OutputSentMessage:
    """An email or chat message as it went out: never numbered, never edited.

    Attributes:
        id (str):
        kind (str):
        title (str):
        sent_at (datetime.datetime | None | Unset):
        sent_through (str | Unset):  Default: ''.
        sent_by (str | Unset):  Default: ''.
        sent_by_rule (str | Unset):  Default: ''.
        delivery_state (str | Unset):  Default: ''.
        delivery_error (str | Unset):  Default: ''.
        delivery_reason (str | Unset):  Default: ''.
        attachments (list[OutputSentMessageAttachment] | Unset):
        recipients (list[str] | Unset):
        context_type (None | str | Unset):
        context_label (str | Unset):  Default: ''.
        org_label (str | Unset):  Default: ''.
        render_route (None | str | Unset):
    """

    id: str
    kind: str
    title: str
    sent_at: datetime.datetime | None | Unset = UNSET
    sent_through: str | Unset = ""
    sent_by: str | Unset = ""
    sent_by_rule: str | Unset = ""
    delivery_state: str | Unset = ""
    delivery_error: str | Unset = ""
    delivery_reason: str | Unset = ""
    attachments: list[OutputSentMessageAttachment] | Unset = UNSET
    recipients: list[str] | Unset = UNSET
    context_type: None | str | Unset = UNSET
    context_label: str | Unset = ""
    org_label: str | Unset = ""
    render_route: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        kind = self.kind

        title = self.title

        sent_at: None | str | Unset
        if isinstance(self.sent_at, Unset):
            sent_at = UNSET
        elif isinstance(self.sent_at, datetime.datetime):
            sent_at = self.sent_at.isoformat()
        else:
            sent_at = self.sent_at

        sent_through = self.sent_through

        sent_by = self.sent_by

        sent_by_rule = self.sent_by_rule

        delivery_state = self.delivery_state

        delivery_error = self.delivery_error

        delivery_reason = self.delivery_reason

        attachments: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.attachments, Unset):
            attachments = []
            for attachments_item_data in self.attachments:
                attachments_item = attachments_item_data.to_dict()
                attachments.append(attachments_item)

        recipients: list[str] | Unset = UNSET
        if not isinstance(self.recipients, Unset):
            recipients = self.recipients

        context_type: None | str | Unset
        if isinstance(self.context_type, Unset):
            context_type = UNSET
        else:
            context_type = self.context_type

        context_label = self.context_label

        org_label = self.org_label

        render_route: None | str | Unset
        if isinstance(self.render_route, Unset):
            render_route = UNSET
        else:
            render_route = self.render_route

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "kind": kind,
                "title": title,
            }
        )
        if sent_at is not UNSET:
            field_dict["sent_at"] = sent_at
        if sent_through is not UNSET:
            field_dict["sent_through"] = sent_through
        if sent_by is not UNSET:
            field_dict["sent_by"] = sent_by
        if sent_by_rule is not UNSET:
            field_dict["sent_by_rule"] = sent_by_rule
        if delivery_state is not UNSET:
            field_dict["delivery_state"] = delivery_state
        if delivery_error is not UNSET:
            field_dict["delivery_error"] = delivery_error
        if delivery_reason is not UNSET:
            field_dict["delivery_reason"] = delivery_reason
        if attachments is not UNSET:
            field_dict["attachments"] = attachments
        if recipients is not UNSET:
            field_dict["recipients"] = recipients
        if context_type is not UNSET:
            field_dict["context_type"] = context_type
        if context_label is not UNSET:
            field_dict["context_label"] = context_label
        if org_label is not UNSET:
            field_dict["org_label"] = org_label
        if render_route is not UNSET:
            field_dict["render_route"] = render_route

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.output_sent_message_attachment import OutputSentMessageAttachment

        d = dict(src_dict)
        id = d.pop("id")

        kind = d.pop("kind")

        title = d.pop("title")

        def _parse_sent_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                sent_at_type_0 = isoparse(data)

                return sent_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        sent_at = _parse_sent_at(d.pop("sent_at", UNSET))

        sent_through = d.pop("sent_through", UNSET)

        sent_by = d.pop("sent_by", UNSET)

        sent_by_rule = d.pop("sent_by_rule", UNSET)

        delivery_state = d.pop("delivery_state", UNSET)

        delivery_error = d.pop("delivery_error", UNSET)

        delivery_reason = d.pop("delivery_reason", UNSET)

        _attachments = d.pop("attachments", UNSET)
        attachments: list[OutputSentMessageAttachment] | Unset = UNSET
        if _attachments is not UNSET:
            attachments = []
            for attachments_item_data in _attachments:
                attachments_item = OutputSentMessageAttachment.from_dict(
                    attachments_item_data
                )

                attachments.append(attachments_item)

        recipients = cast(list[str], d.pop("recipients", UNSET))

        def _parse_context_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        context_type = _parse_context_type(d.pop("context_type", UNSET))

        context_label = d.pop("context_label", UNSET)

        org_label = d.pop("org_label", UNSET)

        def _parse_render_route(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        render_route = _parse_render_route(d.pop("render_route", UNSET))

        output_sent_message = cls(
            id=id,
            kind=kind,
            title=title,
            sent_at=sent_at,
            sent_through=sent_through,
            sent_by=sent_by,
            sent_by_rule=sent_by_rule,
            delivery_state=delivery_state,
            delivery_error=delivery_error,
            delivery_reason=delivery_reason,
            attachments=attachments,
            recipients=recipients,
            context_type=context_type,
            context_label=context_label,
            org_label=org_label,
            render_route=render_route,
        )

        output_sent_message.additional_properties = d
        return output_sent_message

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
