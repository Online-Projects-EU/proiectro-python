from __future__ import annotations

from collections.abc import Mapping
from io import BytesIO
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .. import types
from ..models.import_leads_multi_part_body_params_default_next_action import (
    ImportLeadsMultiPartBodyParamsDefaultNextAction,
)
from ..types import UNSET, File, FileTypes, Unset

T = TypeVar("T", bound="ImportLeadsMultiPartBodyParams")


@_attrs_define
class ImportLeadsMultiPartBodyParams:
    """
    Attributes:
        assign_to_list_id (None | str | Unset):
        default_next_action (ImportLeadsMultiPartBodyParamsDefaultNextAction | Unset):  Default:
            ImportLeadsMultiPartBodyParamsDefaultNextAction.TRIAGE_LATER.
        upload_token (None | str | Unset):
        file (File | Unset):
    """

    assign_to_list_id: None | str | Unset = UNSET
    default_next_action: ImportLeadsMultiPartBodyParamsDefaultNextAction | Unset = (
        ImportLeadsMultiPartBodyParamsDefaultNextAction.TRIAGE_LATER
    )
    upload_token: None | str | Unset = UNSET
    file: File | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        assign_to_list_id: None | str | Unset
        if isinstance(self.assign_to_list_id, Unset):
            assign_to_list_id = UNSET
        else:
            assign_to_list_id = self.assign_to_list_id

        default_next_action: str | Unset = UNSET
        if not isinstance(self.default_next_action, Unset):
            default_next_action = self.default_next_action.value

        upload_token: None | str | Unset
        if isinstance(self.upload_token, Unset):
            upload_token = UNSET
        else:
            upload_token = self.upload_token

        file: FileTypes | Unset = UNSET
        if not isinstance(self.file, Unset):
            file = self.file.to_tuple()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if assign_to_list_id is not UNSET:
            field_dict["assign_to_list_id"] = assign_to_list_id
        if default_next_action is not UNSET:
            field_dict["default_next_action"] = default_next_action
        if upload_token is not UNSET:
            field_dict["upload_token"] = upload_token
        if file is not UNSET:
            field_dict["file"] = file

        return field_dict

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        if not isinstance(self.assign_to_list_id, Unset):
            if isinstance(self.assign_to_list_id, str):
                files.append(
                    (
                        "assign_to_list_id",
                        (None, str(self.assign_to_list_id).encode(), "text/plain"),
                    )
                )
            else:
                files.append(
                    (
                        "assign_to_list_id",
                        (None, str(self.assign_to_list_id).encode(), "text/plain"),
                    )
                )

        if not isinstance(self.default_next_action, Unset):
            files.append(
                (
                    "default_next_action",
                    (None, str(self.default_next_action.value).encode(), "text/plain"),
                )
            )

        if not isinstance(self.upload_token, Unset):
            if isinstance(self.upload_token, str):
                files.append(
                    (
                        "upload_token",
                        (None, str(self.upload_token).encode(), "text/plain"),
                    )
                )
            else:
                files.append(
                    (
                        "upload_token",
                        (None, str(self.upload_token).encode(), "text/plain"),
                    )
                )

        if not isinstance(self.file, Unset):
            files.append(("file", self.file.to_tuple()))

        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))

        return files

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_assign_to_list_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        assign_to_list_id = _parse_assign_to_list_id(d.pop("assign_to_list_id", UNSET))

        _default_next_action = d.pop("default_next_action", UNSET)
        default_next_action: ImportLeadsMultiPartBodyParamsDefaultNextAction | Unset
        if isinstance(_default_next_action, Unset):
            default_next_action = UNSET
        else:
            default_next_action = ImportLeadsMultiPartBodyParamsDefaultNextAction(
                _default_next_action
            )

        def _parse_upload_token(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        upload_token = _parse_upload_token(d.pop("upload_token", UNSET))

        _file = d.pop("file", UNSET)
        file: File | Unset
        if isinstance(_file, Unset):
            file = UNSET
        else:
            file = File(payload=BytesIO(_file))

        import_leads_multi_part_body_params = cls(
            assign_to_list_id=assign_to_list_id,
            default_next_action=default_next_action,
            upload_token=upload_token,
            file=file,
        )

        import_leads_multi_part_body_params.additional_properties = d
        return import_leads_multi_part_body_params

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
