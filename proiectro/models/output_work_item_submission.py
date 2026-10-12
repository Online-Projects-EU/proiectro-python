from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.output_work_item_submission_fields_item import (
        OutputWorkItemSubmissionFieldsItem,
    )
    from ..models.output_work_item_submission_values import (
        OutputWorkItemSubmissionValues,
    )


T = TypeVar("T", bound="OutputWorkItemSubmission")


@_attrs_define
class OutputWorkItemSubmission:
    """One submission captured for a work item, rendered against its OWN version's fields
    (historical accuracy) for the persistent 'Form data' section on the work item card.

        Attributes:
            id (str):
            form_name (str):
            form_version (int):
            submitted_at (datetime.datetime):
            status (str):
            fields (list[OutputWorkItemSubmissionFieldsItem]):
            values (OutputWorkItemSubmissionValues):
            submitter_name (str | Unset):  Default: ''.
            status_color (str | Unset):  Default: 'primary'.
            status_label (str | Unset):  Default: ''.
    """

    id: str
    form_name: str
    form_version: int
    submitted_at: datetime.datetime
    status: str
    fields: list[OutputWorkItemSubmissionFieldsItem]
    values: OutputWorkItemSubmissionValues
    submitter_name: str | Unset = ""
    status_color: str | Unset = "primary"
    status_label: str | Unset = ""
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        form_name = self.form_name

        form_version = self.form_version

        submitted_at = self.submitted_at.isoformat()

        status = self.status

        fields = []
        for fields_item_data in self.fields:
            fields_item = fields_item_data.to_dict()
            fields.append(fields_item)

        values = self.values.to_dict()

        submitter_name = self.submitter_name

        status_color = self.status_color

        status_label = self.status_label

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "form_name": form_name,
                "form_version": form_version,
                "submitted_at": submitted_at,
                "status": status,
                "fields": fields,
                "values": values,
            }
        )
        if submitter_name is not UNSET:
            field_dict["submitter_name"] = submitter_name
        if status_color is not UNSET:
            field_dict["status_color"] = status_color
        if status_label is not UNSET:
            field_dict["status_label"] = status_label

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.output_work_item_submission_fields_item import (
            OutputWorkItemSubmissionFieldsItem,
        )
        from ..models.output_work_item_submission_values import (
            OutputWorkItemSubmissionValues,
        )

        d = dict(src_dict)
        id = d.pop("id")

        form_name = d.pop("form_name")

        form_version = d.pop("form_version")

        submitted_at = isoparse(d.pop("submitted_at"))

        status = d.pop("status")

        fields = []
        _fields = d.pop("fields")
        for fields_item_data in _fields:
            fields_item = OutputWorkItemSubmissionFieldsItem.from_dict(fields_item_data)

            fields.append(fields_item)

        values = OutputWorkItemSubmissionValues.from_dict(d.pop("values"))

        submitter_name = d.pop("submitter_name", UNSET)

        status_color = d.pop("status_color", UNSET)

        status_label = d.pop("status_label", UNSET)

        output_work_item_submission = cls(
            id=id,
            form_name=form_name,
            form_version=form_version,
            submitted_at=submitted_at,
            status=status,
            fields=fields,
            values=values,
            submitter_name=submitter_name,
            status_color=status_color,
            status_label=status_label,
        )

        output_work_item_submission.additional_properties = d
        return output_work_item_submission

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
