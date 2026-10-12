from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.output_tag import OutputTag


T = TypeVar("T", bound="ProposalListItem")


@_attrs_define
class ProposalListItem:
    """
    Attributes:
        id (str):
        name (str):
        funnel (str):
        stage (str):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        internal_costs (float | str):
        external_value (float | str):
        currency (str):
        currency_symbol (str):
        tenant_path (str):
        tags (list[OutputTag] | Unset):
    """

    id: str
    name: str
    funnel: str
    stage: str
    created_at: datetime.datetime
    updated_at: datetime.datetime
    internal_costs: float | str
    external_value: float | str
    currency: str
    currency_symbol: str
    tenant_path: str
    tags: list[OutputTag] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        funnel = self.funnel

        stage = self.stage

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        internal_costs: float | str
        internal_costs = self.internal_costs

        external_value: float | str
        external_value = self.external_value

        currency = self.currency

        currency_symbol = self.currency_symbol

        tenant_path = self.tenant_path

        tags: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.tags, Unset):
            tags = []
            for tags_item_data in self.tags:
                tags_item = tags_item_data.to_dict()
                tags.append(tags_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "funnel": funnel,
                "stage": stage,
                "created_at": created_at,
                "updated_at": updated_at,
                "internal_costs": internal_costs,
                "external_value": external_value,
                "currency": currency,
                "currency_symbol": currency_symbol,
                "tenant_path": tenant_path,
            }
        )
        if tags is not UNSET:
            field_dict["tags"] = tags

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.output_tag import OutputTag

        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        funnel = d.pop("funnel")

        stage = d.pop("stage")

        created_at = isoparse(d.pop("created_at"))

        updated_at = isoparse(d.pop("updated_at"))

        def _parse_internal_costs(data: object) -> float | str:
            return cast(float | str, data)

        internal_costs = _parse_internal_costs(d.pop("internal_costs"))

        def _parse_external_value(data: object) -> float | str:
            return cast(float | str, data)

        external_value = _parse_external_value(d.pop("external_value"))

        currency = d.pop("currency")

        currency_symbol = d.pop("currency_symbol")

        tenant_path = d.pop("tenant_path")

        _tags = d.pop("tags", UNSET)
        tags: list[OutputTag] | Unset = UNSET
        if _tags is not UNSET:
            tags = []
            for tags_item_data in _tags:
                tags_item = OutputTag.from_dict(tags_item_data)

                tags.append(tags_item)

        proposal_list_item = cls(
            id=id,
            name=name,
            funnel=funnel,
            stage=stage,
            created_at=created_at,
            updated_at=updated_at,
            internal_costs=internal_costs,
            external_value=external_value,
            currency=currency,
            currency_symbol=currency_symbol,
            tenant_path=tenant_path,
            tags=tags,
        )

        proposal_list_item.additional_properties = d
        return proposal_list_item

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
