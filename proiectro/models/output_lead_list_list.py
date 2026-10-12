from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.output_lead_list_summary import OutputLeadListSummary


T = TypeVar("T", bound="OutputLeadListList")


@_attrs_define
class OutputLeadListList:
    """Lists tab payload — owned, peer-owned and pool lists, plus the unclaimed leads in no list.

    Attributes:
        mine (list[OutputLeadListSummary] | Unset):
        others (list[OutputLeadListSummary] | Unset):
        pools (list[OutputLeadListSummary] | Unset):
        unclaimed (None | OutputLeadListSummary | Unset):
        list_required (bool | Unset):  Default: False.
        empty_message (str | Unset):  Default: ''.
    """

    mine: list[OutputLeadListSummary] | Unset = UNSET
    others: list[OutputLeadListSummary] | Unset = UNSET
    pools: list[OutputLeadListSummary] | Unset = UNSET
    unclaimed: None | OutputLeadListSummary | Unset = UNSET
    list_required: bool | Unset = False
    empty_message: str | Unset = ""
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.output_lead_list_summary import OutputLeadListSummary

        mine: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.mine, Unset):
            mine = []
            for mine_item_data in self.mine:
                mine_item = mine_item_data.to_dict()
                mine.append(mine_item)

        others: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.others, Unset):
            others = []
            for others_item_data in self.others:
                others_item = others_item_data.to_dict()
                others.append(others_item)

        pools: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.pools, Unset):
            pools = []
            for pools_item_data in self.pools:
                pools_item = pools_item_data.to_dict()
                pools.append(pools_item)

        unclaimed: dict[str, Any] | None | Unset
        if isinstance(self.unclaimed, Unset):
            unclaimed = UNSET
        elif isinstance(self.unclaimed, OutputLeadListSummary):
            unclaimed = self.unclaimed.to_dict()
        else:
            unclaimed = self.unclaimed

        list_required = self.list_required

        empty_message = self.empty_message

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if mine is not UNSET:
            field_dict["mine"] = mine
        if others is not UNSET:
            field_dict["others"] = others
        if pools is not UNSET:
            field_dict["pools"] = pools
        if unclaimed is not UNSET:
            field_dict["unclaimed"] = unclaimed
        if list_required is not UNSET:
            field_dict["list_required"] = list_required
        if empty_message is not UNSET:
            field_dict["empty_message"] = empty_message

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.output_lead_list_summary import OutputLeadListSummary

        d = dict(src_dict)
        _mine = d.pop("mine", UNSET)
        mine: list[OutputLeadListSummary] | Unset = UNSET
        if _mine is not UNSET:
            mine = []
            for mine_item_data in _mine:
                mine_item = OutputLeadListSummary.from_dict(mine_item_data)

                mine.append(mine_item)

        _others = d.pop("others", UNSET)
        others: list[OutputLeadListSummary] | Unset = UNSET
        if _others is not UNSET:
            others = []
            for others_item_data in _others:
                others_item = OutputLeadListSummary.from_dict(others_item_data)

                others.append(others_item)

        _pools = d.pop("pools", UNSET)
        pools: list[OutputLeadListSummary] | Unset = UNSET
        if _pools is not UNSET:
            pools = []
            for pools_item_data in _pools:
                pools_item = OutputLeadListSummary.from_dict(pools_item_data)

                pools.append(pools_item)

        def _parse_unclaimed(data: object) -> None | OutputLeadListSummary | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                unclaimed_type_0 = OutputLeadListSummary.from_dict(data)

                return unclaimed_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | OutputLeadListSummary | Unset, data)

        unclaimed = _parse_unclaimed(d.pop("unclaimed", UNSET))

        list_required = d.pop("list_required", UNSET)

        empty_message = d.pop("empty_message", UNSET)

        output_lead_list_list = cls(
            mine=mine,
            others=others,
            pools=pools,
            unclaimed=unclaimed,
            list_required=list_required,
            empty_message=empty_message,
        )

        output_lead_list_list.additional_properties = d
        return output_lead_list_list

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
