import json
import os
import re
import time

import logger

import requests

log = logger.get(__name__)

headers = {
    'Authorization': f'Bearer {os.getenv("HOME_ASSISTANT_KEY")}'
}

ha_server = os.getenv("HOME_ASSISTANT_URL")
node_red_server = os.getenv("HOME_ASSISTANT_NODE_RED_URL")


def call_service_immediately(data):
    domain = data.pop('domain')
    service = data.pop('service')
    # just in case remove delay from payload
    entity = data['entity_id'].split('.')
    if domain != entity[0]:
        domain = entity[0]
    log.info(f'Call service now, payload: {data}')
    url = f'{ha_server}/api/services/{domain}/{service}'
    response = requests.post(url, json=data, headers=headers)
    log.info(response.json())


def call_service_with_delay(data):
    log.info(f'Schedule service call, payload: {data}')
    url = f'{node_red_server}/endpoint/delay'
    response = requests.post(url, json=data)
    log.info(response.json())


def call_service(data):
    if not len(data):
        pass

    start = time.time()
    data = prepare_json(data)
    if not data or not data.get('domain') or not data.get('service') or not data.get('entity_id'):
        return
    if data.get('delay') or data.get('time'):
        call_service_with_delay(data)
    else:
        call_service_immediately(data)
    end = time.time()
    log.info(f'Home Assistant call processed in {end - start} seconds')


def set_ai_input_state(request):
    data = {
        "state": request
    }
    log.info(f'Set state, payload: {data}')
    url = f'{ha_server}/api/states/input_text.ai_assistant_input'
    response = requests.post(url, json=data, headers=headers)
    log.info(response.json())


def get_states():
    response = requests.get(f'{ha_server}/api/states', headers=headers)
    states = response.json()
    result = ''
    for state in states:
        entity_id = state['entity_id']
        if skip_entity(entity_id):
            continue
        value = state['state']
        friendly_name = state['attributes'].get(
            'friendly_name')  # if bool(state['attributes']['friendly_name']) else ''
        if entity_id.startswith('weather'):
            value = value + ', weather parameters: ' + json.dumps(state['attributes'])
        result = result + f' Entity: {entity_id}, friendly name: {friendly_name}, state: {value};'
    return result


def skip_entity(entity: str):
    return (entity.startswith('update')
            or entity.startswith('number')
            or entity.startswith('tts')
            or entity.startswith('automation')
            or '.0x' in entity)


def get_states_from_template():
    data = {
        "template": "{% set temperature = state_attr('weather.forecast_home', 'temperature') %}{% set humidity = state_attr('weather.forecast_home', 'humidity') %}{% set wind_speed = state_attr('weather.forecast_home', 'wind_speed') %}{% set data = namespace(entities_with_area=[])  %} Список усіх пристроїв, їх сенсори(entity) якими можна керувати та кімнати до яких вони належать(room, device, entity name(entity ID): значення або стан):{% for area in areas() %} Room: {{area_name(area)}}{% for device in area_devices(area_name(area)) %}{% if device_entities(device) %}, device: {{device_attr(device, 'name')}}, entities: {% for entity in device_entities(device)  | sort%}{{state_attr(entity, 'friendly_name')+'('+entity+')'}}: {{ state_translated(entity) }};{% set data.entities_with_area = data.entities_with_area + [entity] %}{% endfor %}{% endif %}{% endfor %}{% endfor %}. Пристрої які не належать до жодної кімнтаи: {% for state in states |  rejectattr ('entity_id', 'in',data.entities_with_area) | map(attribute='entity_id')  | reject('match', '^update.') | reject('match', '^automation.') | sort %}{{state_attr(state, 'friendly_name')+'('+state+')'}} is {{ state_translated(state) }};{% endfor %}. Інформація про погоду: {{state_translated('weather.forecast_home')}}, температура: {{ temperature }} °C, вологість: {{humidity}} %, швидкість вітру: {{wind_speed}} km/h"
    }
    response = requests.post(f'{ha_server}/api/template', json=data, headers=headers)
    decode = response.content.decode('utf-8')
    return decode.replace('"', '\\"')


def get_prompt():
    response = requests.get(f'{node_red_server}/endpoint/prompt', headers=headers)
    response = response.content.decode('utf-8')
    return response.replace('\n', '')


def prepare_json(text):
    # Use regular expression to match text inside curved brackets
    match = re.search(r'{.*?}', text)

    if match:
        # Return the matched text inside curved brackets
        group = match.group()
        return json.loads(group)
    else:
        return None


if __name__ == "__main__":
    call_service({
        "domain": "switch",
        "service": "turn_off",
        "entity_id": "light.workshop_led_switch"
    })
    log.info(get_states())
