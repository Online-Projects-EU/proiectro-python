from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.edit_submission_status_status import EditSubmissionStatusStatus






T = TypeVar("T", bound="EditSubmissionStatus")



@_attrs_define
class EditSubmissionStatus:
    """ 
        Attributes:
            submission_id (str):
            status (EditSubmissionStatusStatus):
     """

    submission_id: str
    status: EditSubmissionStatusStatus
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        submission_id = self.submission_id

        status = self.status.value


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "submission_id": submission_id,
            "status": status,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        submission_id = d.pop("submission_id")

        status = EditSubmissionStatusStatus(d.pop("status"))




        edit_submission_status = cls(
            submission_id=submission_id,
            status=status,
        )


        edit_submission_status.additional_properties = d
        return edit_submission_status

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
