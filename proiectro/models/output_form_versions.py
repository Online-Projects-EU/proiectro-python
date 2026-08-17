from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.output_form_version import OutputFormVersion





T = TypeVar("T", bound="OutputFormVersions")



@_attrs_define
class OutputFormVersions:
    """ 
        Attributes:
            form_id (str):
            versions (list[OutputFormVersion]):
     """

    form_id: str
    versions: list[OutputFormVersion]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.output_form_version import OutputFormVersion
        form_id = self.form_id

        versions = []
        for versions_item_data in self.versions:
            versions_item = versions_item_data.to_dict()
            versions.append(versions_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "form_id": form_id,
            "versions": versions,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.output_form_version import OutputFormVersion
        d = dict(src_dict)
        form_id = d.pop("form_id")

        versions = []
        _versions = d.pop("versions")
        for versions_item_data in (_versions):
            versions_item = OutputFormVersion.from_dict(versions_item_data)



            versions.append(versions_item)


        output_form_versions = cls(
            form_id=form_id,
            versions=versions,
        )


        output_form_versions.additional_properties = d
        return output_form_versions

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
