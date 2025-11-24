# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Inventory(models.Model):

    #__Inventory_FIELDS__
    hostname = models.CharField(max_length=255, null=True, blank=True)
    mgmt_ip_address = models.CharField(max_length=255, null=True, blank=True)
    serial_number = models.CharField(max_length=255, null=True, blank=True)
    device_type = models.CharField(max_length=255, null=True, blank=True)
    device_group = models.CharField(max_length=255, null=True, blank=True)
    model = models.CharField(max_length=255, null=True, blank=True)
    source = models.CharField(max_length=255, null=True, blank=True)
    software_version = models.CharField(max_length=255, null=True, blank=True)
    location = models.CharField(max_length=255, null=True, blank=True)
    contacts = models.CharField(max_length=255, null=True, blank=True)
    do_ping = models.BooleanField()
    reachable_pct = models.IntegerField(null=True, blank=True)
    avg_latency = models.IntegerField(null=True, blank=True)
    min_latency = models.IntegerField(null=True, blank=True)
    max_latency = models.IntegerField(null=True, blank=True)
    datetime_lastup = models.DateTimeField(blank=True, null=True, default=timezone.now)
    down_count = models.IntegerField(null=True, blank=True)
    deployment_status = models.CharField(max_length=255, null=True, blank=True)
    deployment_location = models.CharField(max_length=255, null=True, blank=True)

    #__Inventory_FIELDS__END

    class Meta:
        verbose_name        = _("Inventory")
        verbose_name_plural = _("Inventory")


class Wirelessaps(models.Model):

    #__Wirelessaps_FIELDS__
    serial_number = models.CharField(max_length=255, null=True, blank=True)
    radio_mac_address = models.CharField(max_length=255, null=True, blank=True)
    model = models.CharField(max_length=255, null=True, blank=True)
    controller = models.CharField(max_length=255, null=True, blank=True)
    datetime_firstseen = models.DateTimeField(blank=True, null=True, default=timezone.now)
    datetime_lastseen = models.DateTimeField(blank=True, null=True, default=timezone.now)

    #__Wirelessaps_FIELDS__END

    class Meta:
        verbose_name        = _("Wirelessaps")
        verbose_name_plural = _("Wirelessaps")


class Wirelessclients(models.Model):

    #__Wirelessclients_FIELDS__
    channel = models.IntegerField(null=True, blank=True)
    ssid = models.CharField(max_length=255, null=True, blank=True)
    radio_type = models.CharField(max_length=255, null=True, blank=True)
    radio_phy_type = models.CharField(max_length=255, null=True, blank=True)
    wpa_version = models.CharField(max_length=255, null=True, blank=True)
    cipher_suite = models.CharField(max_length=255, null=True, blank=True)
    six_ghz_capable = models.BooleanField()
    ap_slot_id = models.IntegerField(null=True, blank=True)
    seen_count = models.IntegerField(null=True, blank=True)
    datetime_lastseen = models.DateTimeField(blank=True, null=True, default=timezone.now)
    seen_last_poll = models.BooleanField()
    controller = models.CharField(max_length=255, null=True, blank=True)

    #__Wirelessclients_FIELDS__END

    class Meta:
        verbose_name        = _("Wirelessclients")
        verbose_name_plural = _("Wirelessclients")



#__MODELS__END
