import json

with open('tests.json', 'r', encoding='utf-8') as tests_file:
    tests_data = json.load(tests_file)

with open('values.json', 'r', encoding='utf-8') as values_file:
    values_data = json.load(values_file)

value_map = {item['id']: item['value'] for item in values_data['values']}


def fill_values(tests):
    for test in tests:
        if 'value' in test:
            test['value'] = value_map.get(test['id'], "")

        if 'values' in test:
            fill_values(test['values'])


fill_values(tests_data['tests'])


with open('report.json', 'w', encoding='utf-8') as output_file:
    json.dump(tests_data, output_file, indent=2, ensure_ascii=False)
