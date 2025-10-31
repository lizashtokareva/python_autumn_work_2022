import json
import csv
from datetime import datetime
import xml.etree.ElementTree as ET
from xml.dom import minidom


class DataExporter:
    def export(self, data):
        pass

    def get_format_name(self):
        pass

    def validate_data(self, data):
        if not data:
            raise ValueError('Пустые данные')
        return 'Данные не пустые'


class JSONExporter(DataExporter):
    def export(self, data):
        self.validate_data(data)
        # Добавляем timestamp ко всем записям
        exported_data = []
        for item in data:
            item_with_timestamp = item.copy()
            item_with_timestamp['export_timestamp'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            exported_data.append(item_with_timestamp)
        return json.dumps(exported_data)

    def get_format_name(self):
        return "JSON"


class CSVExporter(DataExporter):
    def export(self, data):
        self.validate_data(data)
        # Проверяем, что все элементы — словари


        keys = data[0].keys()
        with open('data.csv', 'w') as output_file:
            dict_writer = csv.DictWriter(output_file, fieldnames=keys)
            dict_writer.writeheader()
            dict_writer.writerows(data)
        print(f"Данные сохранены в data.csv")

    def get_format_name(self):
        return "CSV"


class XMLExporter(DataExporter):
    def export(self, data):
        self.validate_data(data)

        # Начинаем XML
        xml = '<?xml version="1.0" encoding="utf-8"?>\n'
        xml += '<report>\n'

        # Для каждой записи создаём блок <record>
        for item in data:
            xml += '  <record>\n'
            # Для каждого поля создаём тег
            for key, value in item.items():
                xml += f'    <{key}>{value}</{key}>\n'
            xml += '  </record>\n'

        xml += '</report>'
        return xml

    def get_format_name(self):
        return "XML"


sales_data = [
    {"product": "Laptop", "price": 1000, "quantity": 2},
    {"product": "Mouse", "price": 50, "quantity": 10}
]

exporters = [
    JSONExporter(),
    CSVExporter(),
    XMLExporter()
]

for exporter in exporters:
    print(f"Формат: {exporter.get_format_name()}")
    exporter.export(sales_data)
    print("---")