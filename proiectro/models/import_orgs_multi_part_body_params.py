from __future__ import annotations

from collections.abc import Mapping
from io import BytesIO
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .. import types
from ..types import UNSET, File, FileTypes, Unset

T = TypeVar("T", bound="ImportOrgsMultiPartBodyParams")


@_attrs_define
class ImportOrgsMultiPartBodyParams:
    """
    Attributes:
        upload_token (None | str | Unset):
        file (File | Unset):
    """

    upload_token: None | str | Unset = UNSET
    file: File | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
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
        if upload_token is not UNSET:
            field_dict["upload_token"] = upload_token
        if file is not UNSET:
            field_dict["file"] = file

        return field_dict

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

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

        import_orgs_multi_part_body_params = cls(
            upload_token=upload_token,
            file=file,
        )

        import_orgs_multi_part_body_params.additional_properties = d
        return import_orgs_multi_part_body_params

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
