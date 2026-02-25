from __future__ import annotations

from collections.abc import Mapping
from typing import (
    Any,
    Literal,
    TypeVar,
    cast,
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AnalyticsPerformanceEntry")


@_attrs_define
class AnalyticsPerformanceEntry:
    """Single performer entry (salesperson, customer, or product)

    Attributes:
        id (str):
        name (str):
        deals_won (int):
        deals_lost (int):
        total_revenue (float | str):
        win_rate (float | str):
        avg_deal_size (float | str):
        avatar_url (None | str | Unset):
        prev_revenue (float | None | str | Unset):
        revenue_change_pct (float | Literal['new'] | None | str | Unset):
    """

    id: str
    name: str
    deals_won: int
    deals_lost: int
    total_revenue: float | str
    win_rate: float | str
    avg_deal_size: float | str
    avatar_url: None | str | Unset = UNSET
    prev_revenue: float | None | str | Unset = UNSET
    revenue_change_pct: float | Literal["new"] | None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        deals_won = self.deals_won

        deals_lost = self.deals_lost

        total_revenue: float | str
        total_revenue = self.total_revenue

        win_rate: float | str
        win_rate = self.win_rate

        avg_deal_size: float | str
        avg_deal_size = self.avg_deal_size

        avatar_url: None | str | Unset
        if isinstance(self.avatar_url, Unset):
            avatar_url = UNSET
        else:
            avatar_url = self.avatar_url

        prev_revenue: float | None | str | Unset
        if isinstance(self.prev_revenue, Unset):
            prev_revenue = UNSET
        else:
            prev_revenue = self.prev_revenue

        revenue_change_pct: float | Literal["new"] | None | str | Unset
        if isinstance(self.revenue_change_pct, Unset):
            revenue_change_pct = UNSET
        else:
            revenue_change_pct = self.revenue_change_pct

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "deals_won": deals_won,
                "deals_lost": deals_lost,
                "total_revenue": total_revenue,
                "win_rate": win_rate,
                "avg_deal_size": avg_deal_size,
            }
        )
        if avatar_url is not UNSET:
            field_dict["avatar_url"] = avatar_url
        if prev_revenue is not UNSET:
            field_dict["prev_revenue"] = prev_revenue
        if revenue_change_pct is not UNSET:
            field_dict["revenue_change_pct"] = revenue_change_pct

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        deals_won = d.pop("deals_won")

        deals_lost = d.pop("deals_lost")

        def _parse_total_revenue(data: object) -> float | str:
            return cast(float | str, data)

        total_revenue = _parse_total_revenue(d.pop("total_revenue"))

        def _parse_win_rate(data: object) -> float | str:
            return cast(float | str, data)

        win_rate = _parse_win_rate(d.pop("win_rate"))

        def _parse_avg_deal_size(data: object) -> float | str:
            return cast(float | str, data)

        avg_deal_size = _parse_avg_deal_size(d.pop("avg_deal_size"))

        def _parse_avatar_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        avatar_url = _parse_avatar_url(d.pop("avatar_url", UNSET))

        def _parse_prev_revenue(data: object) -> float | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | str | Unset, data)

        prev_revenue = _parse_prev_revenue(d.pop("prev_revenue", UNSET))

        def _parse_revenue_change_pct(
            data: object,
        ) -> float | Literal["new"] | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            revenue_change_pct_type_2 = cast(Literal["new"], data)
            if revenue_change_pct_type_2 != "new":
                raise ValueError(
                    f"revenue_change_pct_type_2 must match const 'new', got '{revenue_change_pct_type_2}'"
                )
            return revenue_change_pct_type_2
            return cast(float | Literal["new"] | None | str | Unset, data)

        revenue_change_pct = _parse_revenue_change_pct(
            d.pop("revenue_change_pct", UNSET)
        )

        analytics_performance_entry = cls(
            id=id,
            name=name,
            deals_won=deals_won,
            deals_lost=deals_lost,
            total_revenue=total_revenue,
            win_rate=win_rate,
            avg_deal_size=avg_deal_size,
            avatar_url=avatar_url,
            prev_revenue=prev_revenue,
            revenue_change_pct=revenue_change_pct,
        )

        analytics_performance_entry.additional_properties = d
        return analytics_performance_entry

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
