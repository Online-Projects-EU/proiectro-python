from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.partner_portal_file_names_node_type import PartnerPortalFileNamesNodeType

if TYPE_CHECKING:
    from ..models.output_file_name import OutputFileName
    from ..models.output_file_name_trash import OutputFileNameTrash


T = TypeVar("T", bound="PartnerPortalFileNames")


@_attrs_define
class PartnerPortalFileNames:
    """Partner portal files with bridge_id for file operations

    Attributes:
        node_type (PartnerPortalFileNamesNodeType):
        node_id (str):
        successfully_retrieved_files (bool):
        successfully_retrieved_trash (bool):
        files (list[OutputFileName]):
        trash_can (list[OutputFileNameTrash]):
        bridge_id (str):
    """

    node_type: PartnerPortalFileNamesNodeType
    node_id: str
    successfully_retrieved_files: bool
    successfully_retrieved_trash: bool
    files: list[OutputFileName]
    trash_can: list[OutputFileNameTrash]
    bridge_id: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        node_type = self.node_type.value

        node_id = self.node_id

        successfully_retrieved_files = self.successfully_retrieved_files

        successfully_retrieved_trash = self.successfully_retrieved_trash

        files = []
        for files_item_data in self.files:
            files_item = files_item_data.to_dict()
            files.append(files_item)

        trash_can = []
        for trash_can_item_data in self.trash_can:
            trash_can_item = trash_can_item_data.to_dict()
            trash_can.append(trash_can_item)

        bridge_id = self.bridge_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "node_type": node_type,
                "node_id": node_id,
                "successfully_retrieved_files": successfully_retrieved_files,
                "successfully_retrieved_trash": successfully_retrieved_trash,
                "files": files,
                "trash_can": trash_can,
                "bridge_id": bridge_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.output_file_name import OutputFileName
        from ..models.output_file_name_trash import OutputFileNameTrash

        d = dict(src_dict)
        node_type = PartnerPortalFileNamesNodeType(d.pop("node_type"))

        node_id = d.pop("node_id")

        successfully_retrieved_files = d.pop("successfully_retrieved_files")

        successfully_retrieved_trash = d.pop("successfully_retrieved_trash")

        files = []
        _files = d.pop("files")
        for files_item_data in _files:
            files_item = OutputFileName.from_dict(files_item_data)

            files.append(files_item)

        trash_can = []
        _trash_can = d.pop("trash_can")
        for trash_can_item_data in _trash_can:
            trash_can_item = OutputFileNameTrash.from_dict(trash_can_item_data)

            trash_can.append(trash_can_item)

        bridge_id = d.pop("bridge_id")

        partner_portal_file_names = cls(
            node_type=node_type,
            node_id=node_id,
            successfully_retrieved_files=successfully_retrieved_files,
            successfully_retrieved_trash=successfully_retrieved_trash,
            files=files,
            trash_can=trash_can,
            bridge_id=bridge_id,
        )

        partner_portal_file_names.additional_properties = d
        return partner_portal_file_names

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
