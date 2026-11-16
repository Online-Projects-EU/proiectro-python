from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SendProposalByEmailAndMove")


@_attrs_define
class SendProposalByEmailAndMove:
    """
    Attributes:
        template_id (str):
        to (str):
        subject (str):
        body (str):
        idempotency_key (str):
        connection_id (None | str | Unset):
        record_activity (bool | Unset):  Default: False.
        attach_pdf (bool | Unset):  Default: False.
        move_stage (bool | Unset):  Default: False.
        i_have_followed_the_instructions (bool | Unset):  Default: False.
    """

    template_id: str
    to: str
    subject: str
    body: str
    idempotency_key: str
    connection_id: None | str | Unset = UNSET
    record_activity: bool | Unset = False
    attach_pdf: bool | Unset = False
    move_stage: bool | Unset = False
    i_have_followed_the_instructions: bool | Unset = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        template_id = self.template_id

        to = self.to

        subject = self.subject

        body = self.body

        idempotency_key = self.idempotency_key

        connection_id: None | str | Unset
        if isinstance(self.connection_id, Unset):
            connection_id = UNSET
        else:
            connection_id = self.connection_id

        record_activity = self.record_activity

        attach_pdf = self.attach_pdf

        move_stage = self.move_stage

        i_have_followed_the_instructions = self.i_have_followed_the_instructions

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "template_id": template_id,
                "to": to,
                "subject": subject,
                "body": body,
                "idempotency_key": idempotency_key,
            }
        )
        if connection_id is not UNSET:
            field_dict["connection_id"] = connection_id
        if record_activity is not UNSET:
            field_dict["record_activity"] = record_activity
        if attach_pdf is not UNSET:
            field_dict["attach_pdf"] = attach_pdf
        if move_stage is not UNSET:
            field_dict["move_stage"] = move_stage
        if i_have_followed_the_instructions is not UNSET:
            field_dict["i_have_followed_the_instructions"] = (
                i_have_followed_the_instructions
            )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        template_id = d.pop("template_id")

        to = d.pop("to")

        subject = d.pop("subject")

        body = d.pop("body")

        idempotency_key = d.pop("idempotency_key")

        def _parse_connection_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        connection_id = _parse_connection_id(d.pop("connection_id", UNSET))

        record_activity = d.pop("record_activity", UNSET)

        attach_pdf = d.pop("attach_pdf", UNSET)

        move_stage = d.pop("move_stage", UNSET)

        i_have_followed_the_instructions = d.pop(
            "i_have_followed_the_instructions", UNSET
        )

        send_proposal_by_email_and_move = cls(
            template_id=template_id,
            to=to,
            subject=subject,
            body=body,
            idempotency_key=idempotency_key,
            connection_id=connection_id,
            record_activity=record_activity,
            attach_pdf=attach_pdf,
            move_stage=move_stage,
            i_have_followed_the_instructions=i_have_followed_the_instructions,
        )

        send_proposal_by_email_and_move.additional_properties = d
        return send_proposal_by_email_and_move

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
