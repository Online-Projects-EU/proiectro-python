from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.portal_action_status import PortalActionStatus
    from ..models.product_status_detail import ProductStatusDetail


T = TypeVar("T", bound="PartnerPortalProjectProductItem")


@_attrs_define
class PartnerPortalProjectProductItem:
    """Individual project product item for partner portal

    Attributes:
        external_id (str):
        name (str):
        product_count (int):
        is_active (bool):
        is_asap (bool):
        current_status (ProductStatusDetail): Product status for lifecycle display.
            Used in status dropdowns to show current status and all available lifecycle stages.
            Use lifecycle_type with templatetags for styling (status_bg, status_text, status_icon, etc.)
        lifecycle_statuses (list[ProductStatusDetail]):
        planned_start (None | str | Unset):
        planned_end (None | str | Unset):
        duration_days (int | None | Unset):
        is_partner_actionable (bool | Unset):  Default: False.
        accept_status (None | PortalActionStatus | Unset):
        reject_statuses (list[PortalActionStatus] | Unset):
    """

    external_id: str
    name: str
    product_count: int
    is_active: bool
    is_asap: bool
    current_status: ProductStatusDetail
    lifecycle_statuses: list[ProductStatusDetail]
    planned_start: None | str | Unset = UNSET
    planned_end: None | str | Unset = UNSET
    duration_days: int | None | Unset = UNSET
    is_partner_actionable: bool | Unset = False
    accept_status: None | PortalActionStatus | Unset = UNSET
    reject_statuses: list[PortalActionStatus] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.portal_action_status import PortalActionStatus

        external_id = self.external_id

        name = self.name

        product_count = self.product_count

        is_active = self.is_active

        is_asap = self.is_asap

        current_status = self.current_status.to_dict()

        lifecycle_statuses = []
        for lifecycle_statuses_item_data in self.lifecycle_statuses:
            lifecycle_statuses_item = lifecycle_statuses_item_data.to_dict()
            lifecycle_statuses.append(lifecycle_statuses_item)

        planned_start: None | str | Unset
        if isinstance(self.planned_start, Unset):
            planned_start = UNSET
        else:
            planned_start = self.planned_start

        planned_end: None | str | Unset
        if isinstance(self.planned_end, Unset):
            planned_end = UNSET
        else:
            planned_end = self.planned_end

        duration_days: int | None | Unset
        if isinstance(self.duration_days, Unset):
            duration_days = UNSET
        else:
            duration_days = self.duration_days

        is_partner_actionable = self.is_partner_actionable

        accept_status: dict[str, Any] | None | Unset
        if isinstance(self.accept_status, Unset):
            accept_status = UNSET
        elif isinstance(self.accept_status, PortalActionStatus):
            accept_status = self.accept_status.to_dict()
        else:
            accept_status = self.accept_status

        reject_statuses: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.reject_statuses, Unset):
            reject_statuses = []
            for reject_statuses_item_data in self.reject_statuses:
                reject_statuses_item = reject_statuses_item_data.to_dict()
                reject_statuses.append(reject_statuses_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "external_id": external_id,
                "name": name,
                "product_count": product_count,
                "is_active": is_active,
                "is_asap": is_asap,
                "current_status": current_status,
                "lifecycle_statuses": lifecycle_statuses,
            }
        )
        if planned_start is not UNSET:
            field_dict["planned_start"] = planned_start
        if planned_end is not UNSET:
            field_dict["planned_end"] = planned_end
        if duration_days is not UNSET:
            field_dict["duration_days"] = duration_days
        if is_partner_actionable is not UNSET:
            field_dict["is_partner_actionable"] = is_partner_actionable
        if accept_status is not UNSET:
            field_dict["accept_status"] = accept_status
        if reject_statuses is not UNSET:
            field_dict["reject_statuses"] = reject_statuses

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.portal_action_status import PortalActionStatus
        from ..models.product_status_detail import ProductStatusDetail

        d = dict(src_dict)
        external_id = d.pop("external_id")

        name = d.pop("name")

        product_count = d.pop("product_count")

        is_active = d.pop("is_active")

        is_asap = d.pop("is_asap")

        current_status = ProductStatusDetail.from_dict(d.pop("current_status"))

        lifecycle_statuses = []
        _lifecycle_statuses = d.pop("lifecycle_statuses")
        for lifecycle_statuses_item_data in _lifecycle_statuses:
            lifecycle_statuses_item = ProductStatusDetail.from_dict(
                lifecycle_statuses_item_data
            )

            lifecycle_statuses.append(lifecycle_statuses_item)

        def _parse_planned_start(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        planned_start = _parse_planned_start(d.pop("planned_start", UNSET))

        def _parse_planned_end(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        planned_end = _parse_planned_end(d.pop("planned_end", UNSET))

        def _parse_duration_days(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        duration_days = _parse_duration_days(d.pop("duration_days", UNSET))

        is_partner_actionable = d.pop("is_partner_actionable", UNSET)

        def _parse_accept_status(data: object) -> None | PortalActionStatus | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                accept_status_type_0 = PortalActionStatus.from_dict(data)

                return accept_status_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | PortalActionStatus | Unset, data)

        accept_status = _parse_accept_status(d.pop("accept_status", UNSET))

        _reject_statuses = d.pop("reject_statuses", UNSET)
        reject_statuses: list[PortalActionStatus] | Unset = UNSET
        if _reject_statuses is not UNSET:
            reject_statuses = []
            for reject_statuses_item_data in _reject_statuses:
                reject_statuses_item = PortalActionStatus.from_dict(
                    reject_statuses_item_data
                )

                reject_statuses.append(reject_statuses_item)

        partner_portal_project_product_item = cls(
            external_id=external_id,
            name=name,
            product_count=product_count,
            is_active=is_active,
            is_asap=is_asap,
            current_status=current_status,
            lifecycle_statuses=lifecycle_statuses,
            planned_start=planned_start,
            planned_end=planned_end,
            duration_days=duration_days,
            is_partner_actionable=is_partner_actionable,
            accept_status=accept_status,
            reject_statuses=reject_statuses,
        )

        partner_portal_project_product_item.additional_properties = d
        return partner_portal_project_product_item

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
