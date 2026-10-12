from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.top_entity_by_storage import TopEntityByStorage


T = TypeVar("T", bound="OutputTopEntitiesByStorage")


@_attrs_define
class OutputTopEntitiesByStorage:
    """Top entities by storage usage

    Attributes:
        entities (list[TopEntityByStorage]):
        entity_type (str):
    """

    entities: list[TopEntityByStorage]
    entity_type: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        entities = []
        for entities_item_data in self.entities:
            entities_item = entities_item_data.to_dict()
            entities.append(entities_item)

        entity_type = self.entity_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "entities": entities,
                "entity_type": entity_type,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.top_entity_by_storage import TopEntityByStorage

        d = dict(src_dict)
        entities = []
        _entities = d.pop("entities")
        for entities_item_data in _entities:
            entities_item = TopEntityByStorage.from_dict(entities_item_data)

            entities.append(entities_item)

        entity_type = d.pop("entity_type")

        output_top_entities_by_storage = cls(
            entities=entities,
            entity_type=entity_type,
        )

        output_top_entities_by_storage.additional_properties = d
        return output_top_entities_by_storage

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
