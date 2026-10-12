from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.output_project_work_item_detail_scheduling_behaviour import (
    OutputProjectWorkItemDetailSchedulingBehaviour,
)
from ..models.output_project_work_item_detail_timeline_source import (
    OutputProjectWorkItemDetailTimelineSource,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.output_project_work_item_detail_project_settings import (
        OutputProjectWorkItemDetailProjectSettings,
    )
    from ..models.product_status_option import ProductStatusOption


T = TypeVar("T", bound="OutputProjectWorkItemDetail")


@_attrs_define
class OutputProjectWorkItemDetail:
    """Detail output for a single project work item

    Attributes:
        external_id (str):
        name (str):
        hierarchy_id (str):
        work_item_type_id (str):
        work_item_type_name (str):
        scheduling_behaviour (OutputProjectWorkItemDetailSchedulingBehaviour):
        project_id (str):
        project_name (str):
        timeline_source (OutputProjectWorkItemDetailTimelineSource):
        is_finished (bool):
        is_accepted (bool):
        visible_to_customer (bool):
        is_parent (bool):
        can_have_dependencies (bool):
        description (None | str | Unset):
        project_settings (OutputProjectWorkItemDetailProjectSettings | Unset):
        parent_id (None | str | Unset):
        parent_name (None | str | Unset):
        parent_is_not_root (bool | Unset):  Default: False.
        owner_id (None | str | Unset):
        owner_name (None | str | Unset):
        owner_avatar_url (None | str | Unset):
        estimated_work_hours (int | None | Unset):
        percent_complete (int | None | Unset):
        planned_start (datetime.datetime | None | Unset):
        planned_end (datetime.datetime | None | Unset):
        actual_start (datetime.datetime | None | Unset):
        actual_end (datetime.datetime | None | Unset):
        schedule_not_calculated (bool | Unset):  Default: False.
        finished_at (datetime.datetime | None | Unset):
        can_have_children (bool | Unset):  Default: False.
        product_id (None | str | Unset):
        product_name (None | str | Unset):
        product_status (None | str | Unset):
        product_status_lifecycle_type (None | str | Unset):
        product_status_options (list[ProductStatusOption] | Unset):
        can_deliver (bool | Unset):  Default: False.
        deliver_blocked_reason (None | str | Unset):
        reopen_grace_days (int | Unset):  Default: 0.
    """

    external_id: str
    name: str
    hierarchy_id: str
    work_item_type_id: str
    work_item_type_name: str
    scheduling_behaviour: OutputProjectWorkItemDetailSchedulingBehaviour
    project_id: str
    project_name: str
    timeline_source: OutputProjectWorkItemDetailTimelineSource
    is_finished: bool
    is_accepted: bool
    visible_to_customer: bool
    is_parent: bool
    can_have_dependencies: bool
    description: None | str | Unset = UNSET
    project_settings: OutputProjectWorkItemDetailProjectSettings | Unset = UNSET
    parent_id: None | str | Unset = UNSET
    parent_name: None | str | Unset = UNSET
    parent_is_not_root: bool | Unset = False
    owner_id: None | str | Unset = UNSET
    owner_name: None | str | Unset = UNSET
    owner_avatar_url: None | str | Unset = UNSET
    estimated_work_hours: int | None | Unset = UNSET
    percent_complete: int | None | Unset = UNSET
    planned_start: datetime.datetime | None | Unset = UNSET
    planned_end: datetime.datetime | None | Unset = UNSET
    actual_start: datetime.datetime | None | Unset = UNSET
    actual_end: datetime.datetime | None | Unset = UNSET
    schedule_not_calculated: bool | Unset = False
    finished_at: datetime.datetime | None | Unset = UNSET
    can_have_children: bool | Unset = False
    product_id: None | str | Unset = UNSET
    product_name: None | str | Unset = UNSET
    product_status: None | str | Unset = UNSET
    product_status_lifecycle_type: None | str | Unset = UNSET
    product_status_options: list[ProductStatusOption] | Unset = UNSET
    can_deliver: bool | Unset = False
    deliver_blocked_reason: None | str | Unset = UNSET
    reopen_grace_days: int | Unset = 0
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        external_id = self.external_id

        name = self.name

        hierarchy_id = self.hierarchy_id

        work_item_type_id = self.work_item_type_id

        work_item_type_name = self.work_item_type_name

        scheduling_behaviour = self.scheduling_behaviour.value

        project_id = self.project_id

        project_name = self.project_name

        timeline_source = self.timeline_source.value

        is_finished = self.is_finished

        is_accepted = self.is_accepted

        visible_to_customer = self.visible_to_customer

        is_parent = self.is_parent

        can_have_dependencies = self.can_have_dependencies

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        project_settings: dict[str, Any] | Unset = UNSET
        if not isinstance(self.project_settings, Unset):
            project_settings = self.project_settings.to_dict()

        parent_id: None | str | Unset
        if isinstance(self.parent_id, Unset):
            parent_id = UNSET
        else:
            parent_id = self.parent_id

        parent_name: None | str | Unset
        if isinstance(self.parent_name, Unset):
            parent_name = UNSET
        else:
            parent_name = self.parent_name

        parent_is_not_root = self.parent_is_not_root

        owner_id: None | str | Unset
        if isinstance(self.owner_id, Unset):
            owner_id = UNSET
        else:
            owner_id = self.owner_id

        owner_name: None | str | Unset
        if isinstance(self.owner_name, Unset):
            owner_name = UNSET
        else:
            owner_name = self.owner_name

        owner_avatar_url: None | str | Unset
        if isinstance(self.owner_avatar_url, Unset):
            owner_avatar_url = UNSET
        else:
            owner_avatar_url = self.owner_avatar_url

        estimated_work_hours: int | None | Unset
        if isinstance(self.estimated_work_hours, Unset):
            estimated_work_hours = UNSET
        else:
            estimated_work_hours = self.estimated_work_hours

        percent_complete: int | None | Unset
        if isinstance(self.percent_complete, Unset):
            percent_complete = UNSET
        else:
            percent_complete = self.percent_complete

        planned_start: None | str | Unset
        if isinstance(self.planned_start, Unset):
            planned_start = UNSET
        elif isinstance(self.planned_start, datetime.datetime):
            planned_start = self.planned_start.isoformat()
        else:
            planned_start = self.planned_start

        planned_end: None | str | Unset
        if isinstance(self.planned_end, Unset):
            planned_end = UNSET
        elif isinstance(self.planned_end, datetime.datetime):
            planned_end = self.planned_end.isoformat()
        else:
            planned_end = self.planned_end

        actual_start: None | str | Unset
        if isinstance(self.actual_start, Unset):
            actual_start = UNSET
        elif isinstance(self.actual_start, datetime.datetime):
            actual_start = self.actual_start.isoformat()
        else:
            actual_start = self.actual_start

        actual_end: None | str | Unset
        if isinstance(self.actual_end, Unset):
            actual_end = UNSET
        elif isinstance(self.actual_end, datetime.datetime):
            actual_end = self.actual_end.isoformat()
        else:
            actual_end = self.actual_end

        schedule_not_calculated = self.schedule_not_calculated

        finished_at: None | str | Unset
        if isinstance(self.finished_at, Unset):
            finished_at = UNSET
        elif isinstance(self.finished_at, datetime.datetime):
            finished_at = self.finished_at.isoformat()
        else:
            finished_at = self.finished_at

        can_have_children = self.can_have_children

        product_id: None | str | Unset
        if isinstance(self.product_id, Unset):
            product_id = UNSET
        else:
            product_id = self.product_id

        product_name: None | str | Unset
        if isinstance(self.product_name, Unset):
            product_name = UNSET
        else:
            product_name = self.product_name

        product_status: None | str | Unset
        if isinstance(self.product_status, Unset):
            product_status = UNSET
        else:
            product_status = self.product_status

        product_status_lifecycle_type: None | str | Unset
        if isinstance(self.product_status_lifecycle_type, Unset):
            product_status_lifecycle_type = UNSET
        else:
            product_status_lifecycle_type = self.product_status_lifecycle_type

        product_status_options: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.product_status_options, Unset):
            product_status_options = []
            for product_status_options_item_data in self.product_status_options:
                product_status_options_item = product_status_options_item_data.to_dict()
                product_status_options.append(product_status_options_item)

        can_deliver = self.can_deliver

        deliver_blocked_reason: None | str | Unset
        if isinstance(self.deliver_blocked_reason, Unset):
            deliver_blocked_reason = UNSET
        else:
            deliver_blocked_reason = self.deliver_blocked_reason

        reopen_grace_days = self.reopen_grace_days

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "external_id": external_id,
                "name": name,
                "hierarchy_id": hierarchy_id,
                "work_item_type_id": work_item_type_id,
                "work_item_type_name": work_item_type_name,
                "scheduling_behaviour": scheduling_behaviour,
                "project_id": project_id,
                "project_name": project_name,
                "timeline_source": timeline_source,
                "is_finished": is_finished,
                "is_accepted": is_accepted,
                "visible_to_customer": visible_to_customer,
                "is_parent": is_parent,
                "can_have_dependencies": can_have_dependencies,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if project_settings is not UNSET:
            field_dict["project_settings"] = project_settings
        if parent_id is not UNSET:
            field_dict["parent_id"] = parent_id
        if parent_name is not UNSET:
            field_dict["parent_name"] = parent_name
        if parent_is_not_root is not UNSET:
            field_dict["parent_is_not_root"] = parent_is_not_root
        if owner_id is not UNSET:
            field_dict["owner_id"] = owner_id
        if owner_name is not UNSET:
            field_dict["owner_name"] = owner_name
        if owner_avatar_url is not UNSET:
            field_dict["owner_avatar_url"] = owner_avatar_url
        if estimated_work_hours is not UNSET:
            field_dict["estimated_work_hours"] = estimated_work_hours
        if percent_complete is not UNSET:
            field_dict["percent_complete"] = percent_complete
        if planned_start is not UNSET:
            field_dict["planned_start"] = planned_start
        if planned_end is not UNSET:
            field_dict["planned_end"] = planned_end
        if actual_start is not UNSET:
            field_dict["actual_start"] = actual_start
        if actual_end is not UNSET:
            field_dict["actual_end"] = actual_end
        if schedule_not_calculated is not UNSET:
            field_dict["schedule_not_calculated"] = schedule_not_calculated
        if finished_at is not UNSET:
            field_dict["finished_at"] = finished_at
        if can_have_children is not UNSET:
            field_dict["can_have_children"] = can_have_children
        if product_id is not UNSET:
            field_dict["product_id"] = product_id
        if product_name is not UNSET:
            field_dict["product_name"] = product_name
        if product_status is not UNSET:
            field_dict["product_status"] = product_status
        if product_status_lifecycle_type is not UNSET:
            field_dict["product_status_lifecycle_type"] = product_status_lifecycle_type
        if product_status_options is not UNSET:
            field_dict["product_status_options"] = product_status_options
        if can_deliver is not UNSET:
            field_dict["can_deliver"] = can_deliver
        if deliver_blocked_reason is not UNSET:
            field_dict["deliver_blocked_reason"] = deliver_blocked_reason
        if reopen_grace_days is not UNSET:
            field_dict["reopen_grace_days"] = reopen_grace_days

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.output_project_work_item_detail_project_settings import (
            OutputProjectWorkItemDetailProjectSettings,
        )
        from ..models.product_status_option import ProductStatusOption

        d = dict(src_dict)
        external_id = d.pop("external_id")

        name = d.pop("name")

        hierarchy_id = d.pop("hierarchy_id")

        work_item_type_id = d.pop("work_item_type_id")

        work_item_type_name = d.pop("work_item_type_name")

        scheduling_behaviour = OutputProjectWorkItemDetailSchedulingBehaviour(
            d.pop("scheduling_behaviour")
        )

        project_id = d.pop("project_id")

        project_name = d.pop("project_name")

        timeline_source = OutputProjectWorkItemDetailTimelineSource(
            d.pop("timeline_source")
        )

        is_finished = d.pop("is_finished")

        is_accepted = d.pop("is_accepted")

        visible_to_customer = d.pop("visible_to_customer")

        is_parent = d.pop("is_parent")

        can_have_dependencies = d.pop("can_have_dependencies")

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        _project_settings = d.pop("project_settings", UNSET)
        project_settings: OutputProjectWorkItemDetailProjectSettings | Unset
        if isinstance(_project_settings, Unset):
            project_settings = UNSET
        else:
            project_settings = OutputProjectWorkItemDetailProjectSettings.from_dict(
                _project_settings
            )

        def _parse_parent_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        parent_id = _parse_parent_id(d.pop("parent_id", UNSET))

        def _parse_parent_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        parent_name = _parse_parent_name(d.pop("parent_name", UNSET))

        parent_is_not_root = d.pop("parent_is_not_root", UNSET)

        def _parse_owner_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        owner_id = _parse_owner_id(d.pop("owner_id", UNSET))

        def _parse_owner_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        owner_name = _parse_owner_name(d.pop("owner_name", UNSET))

        def _parse_owner_avatar_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        owner_avatar_url = _parse_owner_avatar_url(d.pop("owner_avatar_url", UNSET))

        def _parse_estimated_work_hours(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        estimated_work_hours = _parse_estimated_work_hours(
            d.pop("estimated_work_hours", UNSET)
        )

        def _parse_percent_complete(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        percent_complete = _parse_percent_complete(d.pop("percent_complete", UNSET))

        def _parse_planned_start(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                planned_start_type_0 = isoparse(data)

                return planned_start_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        planned_start = _parse_planned_start(d.pop("planned_start", UNSET))

        def _parse_planned_end(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                planned_end_type_0 = isoparse(data)

                return planned_end_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        planned_end = _parse_planned_end(d.pop("planned_end", UNSET))

        def _parse_actual_start(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                actual_start_type_0 = isoparse(data)

                return actual_start_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        actual_start = _parse_actual_start(d.pop("actual_start", UNSET))

        def _parse_actual_end(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                actual_end_type_0 = isoparse(data)

                return actual_end_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        actual_end = _parse_actual_end(d.pop("actual_end", UNSET))

        schedule_not_calculated = d.pop("schedule_not_calculated", UNSET)

        def _parse_finished_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                finished_at_type_0 = isoparse(data)

                return finished_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        finished_at = _parse_finished_at(d.pop("finished_at", UNSET))

        can_have_children = d.pop("can_have_children", UNSET)

        def _parse_product_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        product_id = _parse_product_id(d.pop("product_id", UNSET))

        def _parse_product_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        product_name = _parse_product_name(d.pop("product_name", UNSET))

        def _parse_product_status(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        product_status = _parse_product_status(d.pop("product_status", UNSET))

        def _parse_product_status_lifecycle_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        product_status_lifecycle_type = _parse_product_status_lifecycle_type(
            d.pop("product_status_lifecycle_type", UNSET)
        )

        _product_status_options = d.pop("product_status_options", UNSET)
        product_status_options: list[ProductStatusOption] | Unset = UNSET
        if _product_status_options is not UNSET:
            product_status_options = []
            for product_status_options_item_data in _product_status_options:
                product_status_options_item = ProductStatusOption.from_dict(
                    product_status_options_item_data
                )

                product_status_options.append(product_status_options_item)

        can_deliver = d.pop("can_deliver", UNSET)

        def _parse_deliver_blocked_reason(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        deliver_blocked_reason = _parse_deliver_blocked_reason(
            d.pop("deliver_blocked_reason", UNSET)
        )

        reopen_grace_days = d.pop("reopen_grace_days", UNSET)

        output_project_work_item_detail = cls(
            external_id=external_id,
            name=name,
            hierarchy_id=hierarchy_id,
            work_item_type_id=work_item_type_id,
            work_item_type_name=work_item_type_name,
            scheduling_behaviour=scheduling_behaviour,
            project_id=project_id,
            project_name=project_name,
            timeline_source=timeline_source,
            is_finished=is_finished,
            is_accepted=is_accepted,
            visible_to_customer=visible_to_customer,
            is_parent=is_parent,
            can_have_dependencies=can_have_dependencies,
            description=description,
            project_settings=project_settings,
            parent_id=parent_id,
            parent_name=parent_name,
            parent_is_not_root=parent_is_not_root,
            owner_id=owner_id,
            owner_name=owner_name,
            owner_avatar_url=owner_avatar_url,
            estimated_work_hours=estimated_work_hours,
            percent_complete=percent_complete,
            planned_start=planned_start,
            planned_end=planned_end,
            actual_start=actual_start,
            actual_end=actual_end,
            schedule_not_calculated=schedule_not_calculated,
            finished_at=finished_at,
            can_have_children=can_have_children,
            product_id=product_id,
            product_name=product_name,
            product_status=product_status,
            product_status_lifecycle_type=product_status_lifecycle_type,
            product_status_options=product_status_options,
            can_deliver=can_deliver,
            deliver_blocked_reason=deliver_blocked_reason,
            reopen_grace_days=reopen_grace_days,
        )

        output_project_work_item_detail.additional_properties = d
        return output_project_work_item_detail

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
