#!/usr/bin/env python
# -*- coding: utf-8 -*-
from enum import Enum, unique


@unique
class CardBrand(Enum):
    VISA = "VISA"
    MASTERCARD = "MASTERCARD"
    MAESTRO = "MAESTRO"
    AMEX = "AMEX"
    JCB = "JCB"
    DINERS = "DINERS"
    DISCOVER = "DISCOVER"
    CUP = "CUP"
    MIR = "MIR"
    ELO = "ELO"
    HIPERCARD = "HIPERCARD"
    TROY = "TROY"

    def to_ams_dict(self):
        return self.name

    @staticmethod
    def value_of(value):
        if not value:
            return None

        if CardBrand.VISA.value == value:
            return CardBrand.VISA
        elif CardBrand.MASTERCARD.value == value:
            return CardBrand.MASTERCARD
        elif CardBrand.MAESTRO.value == value:
            return CardBrand.MAESTRO
        elif CardBrand.AMEX.value == value:
            return CardBrand.AMEX
        elif CardBrand.JCB.value == value:
            return CardBrand.JCB
        elif CardBrand.DINERS.value == value:
            return CardBrand.DINERS
        elif CardBrand.DISCOVER.value == value:
            return CardBrand.DISCOVER
        elif CardBrand.CUP.value == value:
            return CardBrand.CUP
        elif CardBrand.MIR.value == value:
            return CardBrand.MIR
        elif CardBrand.ELO.value == value:
            return CardBrand.ELO
        elif CardBrand.HIPERCARD.value == value:
            return CardBrand.HIPERCARD
        elif CardBrand.TROY.value == value:
            return CardBrand.TROY
        else:
            return None
