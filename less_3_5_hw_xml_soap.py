"""lesson_3_5_homework «API, xml/soap»

"""

import chardet
import os
from urllib.parse import urlencode
import osa
import re
import requests
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


def convert_temperature(value, from_unit, to_unit):
    client = osa.Client('http://www.webservicex.net/ConvertTemperature.asmx?WSDL')
    result = client.service.ConvertTemp(
        Temperature=value,
        FromUnit=from_unit,
        ToUnit=to_unit
    )
    return result


def average_temperature(full_file_name):
    with open(full_file_name, 'rb') as f:
        text = f.read()  # чтение байтовое
        result = chardet.detect(text)
        si = text.decode(result['encoding'])
    from_unit = ''
    to_unit = ''
    temp_data = [x.upper() for x in si.split() if x.isalpha()]
    if temp_data[0] == 'F':
        from_unit = 'degreeFahrenheit'
        to_unit = 'degreeCelsius'
    elif temp_data[0] == 'C':
        from_unit = 'degreeCelsius'
        to_unit = 'degreeFahrenheit'
    else:
        print('Error source data by temperature')
        exit(0)
    temp_data = [int(x) for x in si.split() if x.isdigit()]
    result_data = list(map(lambda x: round(convert_temperature(x, from_unit, to_unit), 2), temp_data))
    return round(sum(result_data) / len(result_data), 2)


def convert_currency(value, from_unit, to_unit):
    client = osa.Client('http://fx.currencysystem.com/webservices/CurrencyServer4.asmx?WSDL')
    result = client.service.ConvertToNum(
        fromCurrency=from_unit,
        toCurrency=to_unit,
        amount=value,
        rounding=True
    )
    return result


def cost_of_travel(full_file_name):
    with open(full_file_name, 'rb') as f:
        text = f.read()  # чтение байтовое
        result = chardet.detect(text)
        data = text.decode(result['encoding'])
    # print(data)
    pattern = re.compile(r'\d+ \w\w\w')
    cost_list = pattern.findall(data)
    total_cost = 0
    for cost in cost_list:
        price = int(cost.split()[0])
        currency_type = cost.split()[1]
        # print('price =', price, 'currency_type =', currency_type)
        total_cost += convert_currency(price, currency_type, 'RUB')
    return total_cost


def convert_len(value, from_unit, to_unit):
    client = osa.Client('http://www.webservicex.net/length.asmx?WSDL')
    result = client.service.ChangeLengthUnit(
        fromLengthUnit=from_unit,
        toLengthUnit=to_unit,
        LengthValue=value
    )
    return result


def len_of_travel(full_file_name):
    total_len = 0
    with open(full_file_name, 'rb') as f:
        text = f.read()  # чтение байтовое
        result = chardet.detect(text)
        data = text.decode(result['encoding'])
    pattern = re.compile(r': \S*\d\d+\.\d\d.\w\w')
    len_list = pattern.findall(data)
    # print(len_list)
    for stage in len_list:
        stage = stage[2:]
        # print(stage)
        len_type = stage.split()[1].upper()
        if len_type == 'MI':
            len_type = 'Miles'
        len_of_stage = float(stage.split()[0].replace(',', ''))
        # print('len_of_stage =', len_of_stage, 'len_type =', len_type)
        total_len += convert_len(len_of_stage, len_type, 'Kilometers')
    return total_len


def main():
    source_file_path = 'D:\Python_my\Python_Netology_homework\PY3_Lesson_3.4\Homework'
    source_file_temp_name = 'temps.txt'
    source_file_currency_name = 'currencies.txt'
    source_file_travel_name = 'travel.txt'
    print('Average temperature = {} C'.format(
        average_temperature(os.path.normpath(os.path.join(source_file_path, source_file_temp_name)))))
    travel_cost = cost_of_travel(os.path.normpath(os.path.join(source_file_path, source_file_currency_name)))
    print('Travel cost = {}'.format(round(travel_cost, 0)))
    travel_len = len_of_travel(os.path.normpath(os.path.join(source_file_path, source_file_travel_name)))
    print('Total travel len = {} Kilometers'.format(round(travel_len, 2)))


if __name__ == '__main__':
    main()
