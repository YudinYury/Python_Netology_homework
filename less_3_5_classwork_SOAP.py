"""lesson_3_5_classwork «API, xml/soap»

"""

import chardet
import json
import os
import pprint
import requests
from urllib.parse import urlencode
import osa
from xml.etree.ElementTree import fromstring, ElementTree


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
    # print(round(mgramm_to_kgramm(1_234_567), 2))

    response = requests.post('http://www.webservicex.net/convertMetricWeight.asmx?WSDL',
                             headers={'Content-Type': 'text/xml; charset=utf-8'},
                             data='''<?xml version="1.0" encoding="utf-8"?>
                                    <soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
                                      <soap:Body>
                                        <ChangeMetricWeightUnit xmlns="http://www.webserviceX.NET/">
                                          <MetricWeightValue>1234567</MetricWeightValue>
                                          <fromMetricWeightUnit>milligram</fromMetricWeightUnit>
                                          <toMetricWeightUnit>kilogram</toMetricWeightUnit>
                                        </ChangeMetricWeightUnit>
                                      </soap:Body>
                                    </soap:Envelope>
                             '''
    )
    # tree = ElementTree(fromstring(response.text))
    # tree = fromstring(response.text)
    # el = list(list(list(tree)[0])[0])
    # print(el.text)

    # print(response.text)

    print(convert_weight(1234567, 'milligram', 'kilogram'))


if __name__ == '__main__':
    main()
