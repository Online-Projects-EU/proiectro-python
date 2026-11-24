from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.business_process_link import BusinessProcessLink


T = TypeVar("T", bound="BusinessProcessArtifact")


@_attrs_define
class BusinessProcessArtifact:
    """Input or output artifact for a business process

    Attributes:
        model_name (str):
        business_friendly_name (str):
        external_description (str):
        source_process (None | str | Unset):
        sources (list[BusinessProcessLink] | Unset):
    """

    model_name: str
    business_friendly_name: str
    external_description: str
    source_process: None | str | Unset = UNSET
    sources: list[BusinessProcessLink] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        model_name = self.model_name

        business_friendly_name = self.business_friendly_name

        external_description = self.external_description

        source_process: None | str | Unset
        if isinstance(self.source_process, Unset):
            source_process = UNSET
        else:
            source_process = self.source_process

        sources: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.sources, Unset):
            sources = []
            for sources_item_data in self.sources:
                sources_item = sources_item_data.to_dict()
                sources.append(sources_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "model_name": model_name,
                "business_friendly_name": business_friendly_name,
                "external_description": external_description,
            }
        )
        if source_process is not UNSET:
            field_dict["source_process"] = source_process
        if sources is not UNSET:
            field_dict["sources"] = sources

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.business_process_link import BusinessProcessLink

        d = dict(src_dict)
        model_name = d.pop("model_name")

        business_friendly_name = d.pop("business_friendly_name")

        external_description = d.pop("external_description")

        def _parse_source_process(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        source_process = _parse_source_process(d.pop("source_process", UNSET))

        _sources = d.pop("sources", UNSET)
        sources: list[BusinessProcessLink] | Unset = UNSET
        if _sources is not UNSET:
            sources = []
            for sources_item_data in _sources:
                sources_item = BusinessProcessLink.from_dict(sources_item_data)

                sources.append(sources_item)

        business_process_artifact = cls(
            model_name=model_name,
            business_friendly_name=business_friendly_name,
            external_description=external_description,
            source_process=source_process,
            sources=sources,
        )

        business_process_artifact.additional_properties = d
        return business_process_artifact

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
