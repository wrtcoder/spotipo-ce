# -*- coding: utf-8 -*-
from spotipo_plugins import connect_event

from unifispot.modules import SpotipoPlugin,create_method_field

from .main import module

__version__ = "0.1"
__plugin__ = "VoucherLoginPlugin"


def create_voucher_settings_button():
    return create_method_field('Voucher Login','auth_voucher','voucher')


class VoucherLoginPlugin(SpotipoPlugin):

    name = "Voucher Login Plugin"

    description = ("This Plugin provides Voucher Login for Spotipo.")

    author = "rakeshmukundan"

    license = "AGPL"

    version = __version__


    def setup(self):
        self.register_blueprint(module, url_prefix="")
        connect_event("print-login-method-settings", 
                       create_voucher_settings_button)



