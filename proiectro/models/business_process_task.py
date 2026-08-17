from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="BusinessProcessTask")



@_attrs_define
class BusinessProcessTask:
    """ Individual task within a business process

        Attributes:
            task_number (int):
            description (str):
            user_has_permission (bool):
            branch_type (None | str | Unset):
            permission_display (str | Unset):  Default: ''.
     """

    task_number: int
    description: str
    user_has_permission: bool
    branch_type: None | str | Unset = UNSET
    permission_display: str | Unset = ''
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        task_number = self.task_number

        description = self.description

        user_has_permission = self.user_has_permission

        branch_type: None | str | Unset
        if isinstance(self.branch_type, Unset):
            branch_type = UNSET
        else:
            branch_type = self.branch_type

        permission_display = self.permission_display


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "task_number": task_number,
            "description": description,
            "user_has_permission": user_has_permission,
        })
        if branch_type is not UNSET:
            field_dict["branch_type"] = branch_type
        if permission_display is not UNSET:
            field_dict["permission_display"] = permission_display

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        task_number = d.pop("task_number")

        description = d.pop("description")

        user_has_permission = d.pop("user_has_permission")

        def _parse_branch_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        branch_type = _parse_branch_type(d.pop("branch_type", UNSET))


        permission_display = d.pop("permission_display", UNSET)

        business_process_task = cls(
            task_number=task_number,
            description=description,
            user_has_permission=user_has_permission,
            branch_type=branch_type,
            permission_display=permission_display,
        )


        business_process_task.additional_properties = d
        return business_process_task

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
