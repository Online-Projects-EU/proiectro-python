from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="AssignedInternalSupportRequestFilterSchema")


@_attrs_define
class AssignedInternalSupportRequestFilterSchema:
    """Filter schema for 'Assigned To Me - Internal Support Requests' page.

    Allows users to filter internal support requests assigned to them.
    Note: assignee field is excluded since it's implicit (assigned_to_me=True).

        Attributes:
            exclude_mode (bool | None | Unset): Invert filter logic to exclude matching results
            search (None | str | Unset): Search in title, description, or ticket ID
            type_ (None | str | Unset): Filter by request type
            severity (None | str | Unset): Filter by severity level
            status (None | str | Unset): Filter by status
            queue (None | str | Unset): Filter by queue
            customer (None | str | Unset): Filter by customer organization
            project (None | str | Unset): Filter by project
            resource (None | str | Unset): Filter by resource
            requester (None | str | Unset): Filter by requester
            has_assignee (bool | None | Unset): Filter by assignment status
            created_from (datetime.date | None | Unset): Filter by creation date (from)
            created_to (datetime.date | None | Unset): Filter by creation date (to)
            updated_from (datetime.date | None | Unset): Filter by last update date (from)
            updated_to (datetime.date | None | Unset): Filter by last update date (to)
    """

    exclude_mode: bool | None | Unset = UNSET
    search: None | str | Unset = UNSET
    type_: None | str | Unset = UNSET
    severity: None | str | Unset = UNSET
    status: None | str | Unset = UNSET
    queue: None | str | Unset = UNSET
    customer: None | str | Unset = UNSET
    project: None | str | Unset = UNSET
    resource: None | str | Unset = UNSET
    requester: None | str | Unset = UNSET
    has_assignee: bool | None | Unset = UNSET
    created_from: datetime.date | None | Unset = UNSET
    created_to: datetime.date | None | Unset = UNSET
    updated_from: datetime.date | None | Unset = UNSET
    updated_to: datetime.date | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        exclude_mode: bool | None | Unset
        if isinstance(self.exclude_mode, Unset):
            exclude_mode = UNSET
        else:
            exclude_mode = self.exclude_mode

        search: None | str | Unset
        if isinstance(self.search, Unset):
            search = UNSET
        else:
            search = self.search

        type_: None | str | Unset
        if isinstance(self.type_, Unset):
            type_ = UNSET
        else:
            type_ = self.type_

        severity: None | str | Unset
        if isinstance(self.severity, Unset):
            severity = UNSET
        else:
            severity = self.severity

        status: None | str | Unset
        if isinstance(self.status, Unset):
            status = UNSET
        else:
            status = self.status

        queue: None | str | Unset
        if isinstance(self.queue, Unset):
            queue = UNSET
        else:
            queue = self.queue

        customer: None | str | Unset
        if isinstance(self.customer, Unset):
            customer = UNSET
        else:
            customer = self.customer

        project: None | str | Unset
        if isinstance(self.project, Unset):
            project = UNSET
        else:
            project = self.project

        resource: None | str | Unset
        if isinstance(self.resource, Unset):
            resource = UNSET
        else:
            resource = self.resource

        requester: None | str | Unset
        if isinstance(self.requester, Unset):
            requester = UNSET
        else:
            requester = self.requester

        has_assignee: bool | None | Unset
        if isinstance(self.has_assignee, Unset):
            has_assignee = UNSET
        else:
            has_assignee = self.has_assignee

        created_from: None | str | Unset
        if isinstance(self.created_from, Unset):
            created_from = UNSET
        elif isinstance(self.created_from, datetime.date):
            created_from = self.created_from.isoformat()
        else:
            created_from = self.created_from

        created_to: None | str | Unset
        if isinstance(self.created_to, Unset):
            created_to = UNSET
        elif isinstance(self.created_to, datetime.date):
            created_to = self.created_to.isoformat()
        else:
            created_to = self.created_to

        updated_from: None | str | Unset
        if isinstance(self.updated_from, Unset):
            updated_from = UNSET
        elif isinstance(self.updated_from, datetime.date):
            updated_from = self.updated_from.isoformat()
        else:
            updated_from = self.updated_from

        updated_to: None | str | Unset
        if isinstance(self.updated_to, Unset):
            updated_to = UNSET
        elif isinstance(self.updated_to, datetime.date):
            updated_to = self.updated_to.isoformat()
        else:
            updated_to = self.updated_to

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if exclude_mode is not UNSET:
            field_dict["exclude_mode"] = exclude_mode
        if search is not UNSET:
            field_dict["search"] = search
        if type_ is not UNSET:
            field_dict["type"] = type_
        if severity is not UNSET:
            field_dict["severity"] = severity
        if status is not UNSET:
            field_dict["status"] = status
        if queue is not UNSET:
            field_dict["queue"] = queue
        if customer is not UNSET:
            field_dict["customer"] = customer
        if project is not UNSET:
            field_dict["project"] = project
        if resource is not UNSET:
            field_dict["resource"] = resource
        if requester is not UNSET:
            field_dict["requester"] = requester
        if has_assignee is not UNSET:
            field_dict["has_assignee"] = has_assignee
        if created_from is not UNSET:
            field_dict["created_from"] = created_from
        if created_to is not UNSET:
            field_dict["created_to"] = created_to
        if updated_from is not UNSET:
            field_dict["updated_from"] = updated_from
        if updated_to is not UNSET:
            field_dict["updated_to"] = updated_to

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_exclude_mode(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        exclude_mode = _parse_exclude_mode(d.pop("exclude_mode", UNSET))

        def _parse_search(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        search = _parse_search(d.pop("search", UNSET))

        def _parse_type_(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        type_ = _parse_type_(d.pop("type", UNSET))

        def _parse_severity(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        severity = _parse_severity(d.pop("severity", UNSET))

        def _parse_status(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        status = _parse_status(d.pop("status", UNSET))

        def _parse_queue(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        queue = _parse_queue(d.pop("queue", UNSET))

        def _parse_customer(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        customer = _parse_customer(d.pop("customer", UNSET))

        def _parse_project(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        project = _parse_project(d.pop("project", UNSET))

        def _parse_resource(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        resource = _parse_resource(d.pop("resource", UNSET))

        def _parse_requester(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        requester = _parse_requester(d.pop("requester", UNSET))

        def _parse_has_assignee(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        has_assignee = _parse_has_assignee(d.pop("has_assignee", UNSET))

        def _parse_created_from(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                created_from_type_0 = isoparse(data).date()

                return created_from_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None | Unset, data)

        created_from = _parse_created_from(d.pop("created_from", UNSET))

        def _parse_created_to(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                created_to_type_0 = isoparse(data).date()

                return created_to_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None | Unset, data)

        created_to = _parse_created_to(d.pop("created_to", UNSET))

        def _parse_updated_from(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                updated_from_type_0 = isoparse(data).date()

                return updated_from_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None | Unset, data)

        updated_from = _parse_updated_from(d.pop("updated_from", UNSET))

        def _parse_updated_to(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                updated_to_type_0 = isoparse(data).date()

                return updated_to_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None | Unset, data)

        updated_to = _parse_updated_to(d.pop("updated_to", UNSET))

        assigned_internal_support_request_filter_schema = cls(
            exclude_mode=exclude_mode,
            search=search,
            type_=type_,
            severity=severity,
            status=status,
            queue=queue,
            customer=customer,
            project=project,
            resource=resource,
            requester=requester,
            has_assignee=has_assignee,
            created_from=created_from,
            created_to=created_to,
            updated_from=updated_from,
            updated_to=updated_to,
        )

        assigned_internal_support_request_filter_schema.additional_properties = d
        return assigned_internal_support_request_filter_schema

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
