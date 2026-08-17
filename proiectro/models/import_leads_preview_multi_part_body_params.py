from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field
import json
from .. import types

from ..types import UNSET, Unset

from ..models.import_leads_preview_multi_part_body_params_default_next_action import ImportLeadsPreviewMultiPartBodyParamsDefaultNextAction
from ..types import File, FileTypes
from ..types import UNSET, Unset
from io import BytesIO
from typing import cast






T = TypeVar("T", bound="ImportLeadsPreviewMultiPartBodyParams")



@_attrs_define
class ImportLeadsPreviewMultiPartBodyParams:
    """ 
        Attributes:
            file (File):
            assign_to_list_id (None | str | Unset):
            default_next_action (ImportLeadsPreviewMultiPartBodyParamsDefaultNextAction | Unset):  Default:
                ImportLeadsPreviewMultiPartBodyParamsDefaultNextAction.TRIAGE_LATER.
            upload_token (None | str | Unset):
     """

    file: File
    assign_to_list_id: None | str | Unset = UNSET
    default_next_action: ImportLeadsPreviewMultiPartBodyParamsDefaultNextAction | Unset = ImportLeadsPreviewMultiPartBodyParamsDefaultNextAction.TRIAGE_LATER
    upload_token: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        file = self.file.to_tuple()


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


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "file": file,
        })
        if assign_to_list_id is not UNSET:
            field_dict["assign_to_list_id"] = assign_to_list_id
        if default_next_action is not UNSET:
            field_dict["default_next_action"] = default_next_action
        if upload_token is not UNSET:
            field_dict["upload_token"] = upload_token

        return field_dict


    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        files.append(("file", self.file.to_tuple()))



        if not isinstance(self.assign_to_list_id, Unset):
            if isinstance(self.assign_to_list_id, str):

                files.append(("assign_to_list_id", (None, str(self.assign_to_list_id).encode(), "text/plain")))
            else:
                files.append(("assign_to_list_id", (None, str(self.assign_to_list_id).encode(), "text/plain")))


        if not isinstance(self.default_next_action, Unset):
            files.append(("default_next_action",  (None, str(self.default_next_action.value).encode(), "text/plain")))



        if not isinstance(self.upload_token, Unset):
            if isinstance(self.upload_token, str):

                files.append(("upload_token", (None, str(self.upload_token).encode(), "text/plain")))
            else:
                files.append(("upload_token", (None, str(self.upload_token).encode(), "text/plain")))



        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))



        return files


    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        file = File(
             payload = BytesIO(d.pop("file"))
        )




        def _parse_assign_to_list_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        assign_to_list_id = _parse_assign_to_list_id(d.pop("assign_to_list_id", UNSET))


        _default_next_action = d.pop("default_next_action", UNSET)
        default_next_action: ImportLeadsPreviewMultiPartBodyParamsDefaultNextAction | Unset
        if isinstance(_default_next_action,  Unset):
            default_next_action = UNSET
        else:
            default_next_action = ImportLeadsPreviewMultiPartBodyParamsDefaultNextAction(_default_next_action)




        def _parse_upload_token(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        upload_token = _parse_upload_token(d.pop("upload_token", UNSET))


        import_leads_preview_multi_part_body_params = cls(
            file=file,
            assign_to_list_id=assign_to_list_id,
            default_next_action=default_next_action,
            upload_token=upload_token,
        )


        import_leads_preview_multi_part_body_params.additional_properties = d
        return import_leads_preview_multi_part_body_params

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
