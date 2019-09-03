# Copyright (c) 2018 iXsystems, Inc.
# All rights reserved.
# This file is a part of TrueNAS
# and may not be copied and/or distributed
# without the express permission of iXsystems.
from middlewared.alert.base import AlertClass, AlertCategory, AlertLevel, Alert, AlertSource


class DisksAreNotPresentOnBackupNodeAlertClass(AlertClass):
    category = AlertCategory.HA
    level = AlertLevel.CRITICAL
    title = "Disks Missing on Passive Storage Controller"
    text = "Disks %(disks)s present on active storage controller but missing on passive storage controller."


class DisksAreNotPresentOnMasterNodeAlertClass(AlertClass):
    category = AlertCategory.HA
    level = AlertLevel.CRITICAL
    title = "Disks Missing on Active Storage Controller"
    text = "Disks %(disks)s present on passive storage controller but missing on active storage controller."


class FailoverDisksAlertSource(AlertSource):
    failover_related = True
    run_on_backup_node = False

    async def check(self):
        alerts = []

        if not await self.middleware.call("failover.licensed"):
            return alerts

        mismatch_disks = await self.middleware.call("failover.mismatch_disks")

        if mismatch_disks["missing_remote"]:
            alerts.append(Alert(DisksAreNotPresentOnBackupNodeAlertClass,
                                {"disks": ", ".join(mismatch_disks["missing_remote"])}))

        if mismatch_disks["missing_local"]:
            alerts.append(Alert(DisksAreNotPresentOnMasterNodeAlertClass,
                                {"disks": ", ".join(mismatch_disks["missing_local"])}))

        return alerts