from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.target_attainment_entry import TargetAttainmentEntry


T = TypeVar("T", bound="AnalyticsPerformanceEntry")


@_attrs_define
class AnalyticsPerformanceEntry:
    """Single performer entry (salesperson, customer, or product)

    Attributes:
        id (str):
        name (str):
        deals_won (int):
        deals_lost (int):
        currency (str):
        avatar_url (None | str | Unset):
        total_revenue (float | None | str | Unset):
        win_rate (float | None | str | Unset):
        avg_deal_size (float | None | str | Unset):
        prev_revenue (float | None | str | Unset):
        revenue_change_pct (float | None | str | Unset): A percentage, or "new" when the prior period had nothing to
            compare against.
        uncovered_currencies (list[str] | Unset):
        attainment (list[TargetAttainmentEntry] | Unset):
    """

    id: str
    name: str
    deals_won: int
    deals_lost: int
    currency: str
    avatar_url: None | str | Unset = UNSET
    total_revenue: float | None | str | Unset = UNSET
    win_rate: float | None | str | Unset = UNSET
    avg_deal_size: float | None | str | Unset = UNSET
    prev_revenue: float | None | str | Unset = UNSET
    revenue_change_pct: float | None | str | Unset = UNSET
    uncovered_currencies: list[str] | Unset = UNSET
    attainment: list[TargetAttainmentEntry] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        deals_won = self.deals_won

        deals_lost = self.deals_lost

        currency = self.currency

        avatar_url: None | str | Unset
        if isinstance(self.avatar_url, Unset):
            avatar_url = UNSET
        else:
            avatar_url = self.avatar_url

        total_revenue: float | None | str | Unset
        if isinstance(self.total_revenue, Unset):
            total_revenue = UNSET
        else:
            total_revenue = self.total_revenue

        win_rate: float | None | str | Unset
        if isinstance(self.win_rate, Unset):
            win_rate = UNSET
        else:
            win_rate = self.win_rate

        avg_deal_size: float | None | str | Unset
        if isinstance(self.avg_deal_size, Unset):
            avg_deal_size = UNSET
        else:
            avg_deal_size = self.avg_deal_size

        prev_revenue: float | None | str | Unset
        if isinstance(self.prev_revenue, Unset):
            prev_revenue = UNSET
        else:
            prev_revenue = self.prev_revenue

        revenue_change_pct: float | None | str | Unset
        if isinstance(self.revenue_change_pct, Unset):
            revenue_change_pct = UNSET
        else:
            revenue_change_pct = self.revenue_change_pct

        uncovered_currencies: list[str] | Unset = UNSET
        if not isinstance(self.uncovered_currencies, Unset):
            uncovered_currencies = self.uncovered_currencies

        attainment: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.attainment, Unset):
            attainment = []
            for attainment_item_data in self.attainment:
                attainment_item = attainment_item_data.to_dict()
                attainment.append(attainment_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "deals_won": deals_won,
                "deals_lost": deals_lost,
                "currency": currency,
            }
        )
        if avatar_url is not UNSET:
            field_dict["avatar_url"] = avatar_url
        if total_revenue is not UNSET:
            field_dict["total_revenue"] = total_revenue
        if win_rate is not UNSET:
            field_dict["win_rate"] = win_rate
        if avg_deal_size is not UNSET:
            field_dict["avg_deal_size"] = avg_deal_size
        if prev_revenue is not UNSET:
            field_dict["prev_revenue"] = prev_revenue
        if revenue_change_pct is not UNSET:
            field_dict["revenue_change_pct"] = revenue_change_pct
        if uncovered_currencies is not UNSET:
            field_dict["uncovered_currencies"] = uncovered_currencies
        if attainment is not UNSET:
            field_dict["attainment"] = attainment

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.target_attainment_entry import TargetAttainmentEntry

        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        deals_won = d.pop("deals_won")

        deals_lost = d.pop("deals_lost")

        currency = d.pop("currency")

        def _parse_avatar_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        avatar_url = _parse_avatar_url(d.pop("avatar_url", UNSET))

        def _parse_total_revenue(data: object) -> float | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | str | Unset, data)

        total_revenue = _parse_total_revenue(d.pop("total_revenue", UNSET))

        def _parse_win_rate(data: object) -> float | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | str | Unset, data)

        win_rate = _parse_win_rate(d.pop("win_rate", UNSET))

        def _parse_avg_deal_size(data: object) -> float | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | str | Unset, data)

        avg_deal_size = _parse_avg_deal_size(d.pop("avg_deal_size", UNSET))

        def _parse_prev_revenue(data: object) -> float | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | str | Unset, data)

        prev_revenue = _parse_prev_revenue(d.pop("prev_revenue", UNSET))

        def _parse_revenue_change_pct(data: object) -> float | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | str | Unset, data)

        revenue_change_pct = _parse_revenue_change_pct(
            d.pop("revenue_change_pct", UNSET)
        )

        uncovered_currencies = cast(list[str], d.pop("uncovered_currencies", UNSET))

        _attainment = d.pop("attainment", UNSET)
        attainment: list[TargetAttainmentEntry] | Unset = UNSET
        if _attainment is not UNSET:
            attainment = []
            for attainment_item_data in _attainment:
                attainment_item = TargetAttainmentEntry.from_dict(attainment_item_data)

                attainment.append(attainment_item)

        analytics_performance_entry = cls(
            id=id,
            name=name,
            deals_won=deals_won,
            deals_lost=deals_lost,
            currency=currency,
            avatar_url=avatar_url,
            total_revenue=total_revenue,
            win_rate=win_rate,
            avg_deal_size=avg_deal_size,
            prev_revenue=prev_revenue,
            revenue_change_pct=revenue_change_pct,
            uncovered_currencies=uncovered_currencies,
            attainment=attainment,
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
