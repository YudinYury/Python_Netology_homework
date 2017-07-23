"""lesson_3_4_homework «API VK, Oauth protocol»

"""

import chardet
import json
import os
import pprint
import requests
from urllib.parse import urlencode
import osa


def mgramm_to_kgramm(mgramm):
    kgramm = mgramm / 1_000_000
    return kgramm


def convert_weight(value, from_unit, to_unit):
    client = osa.Client('http://www.webservicex.net/convertMetricWeight.asmx?WSDL')
    result = client.service.ChangeMetricWeightUnit(
        MetricWeightValue=value,
        fromMetricWeightUnit=from_unit,
        toMetricWeightUnit=to_unit
    )

    return result


def main():
    print(
        round(mgramm_to_kgramm(12_345_678), 2)
    )


if __name__ == '__main__':
    main()
