import sqlite3
from datetime import datetime

con = sqlite3.connect('conversation.db')

cur = con.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS conversation (date datetime, user text, assistant text)''')
#cur.execute('''DELETE FROM  conversation''')
#con.commit()

res = cur.execute('''SELECT * FROM  conversation''')
if not res.fetchall():
    print("No records")
    example_conversation = [
        (datetime.now(), 'вимкни світло у майстерні',
         'світло на кухні вимкнено, тепер ти залишися у цій пустій темряві. ##{\"domain\":\"light\",\"service\": \"turn_off\", \"entity_id\": \"light.workshop_led_switch\"}'),
        (datetime.now(), 'увімкни витяжку',
         'витяжка на кухні увімкнена. ##{\"domain\":\"switch\",\"service\": \"turn_on\", \"entity_id\": \"switch.kitchen_hood\"}'),
        (datetime.now(), 'виключи кондиціонер',
         'кондиціонер вимкнено, тепер ти будеш палати. ##{\"domain\":\"switch\",\"service\": \"turn_off\", \"entity_id\": \"switch.air_conditioner\"}'),
        (datetime.now(), 'призупини відтворення на телевізорі у спальні',
         'телевізор на паузі. ##{\"domain\":\"media_player\",\"service\": \"pause\", \"entity_id\": \"media_player.bedroom_kivi_tv_2\"}'),
        (datetime.now(), 'встанови колір світла у коридорі на зелений і яскравість пятдесят відсотків',
         'звісно, я це зроблю, але не думай що світло врятує тебе від порожнечі та темного майбутнього. ##{\"domain\":\"light\",\"service\": \"turn_on\", \"entity_id\": \"light.hallway_rgb\", \"rgb_color\":[0,255,0], \"brightness_pct\": 50}'),
        (datetime.now(), 'встанови таймер на дванадцять хвилин',
         'таймер встановлено, а поки можеш насолоджуватись думками про неминучу смерть. ##{\"domain\":\"timer\",\"service\": \"set\", \"entity_id\": \"timer.first\", \"value\":720}'),
    ]
    # cur.executemany("INSERT into conversation values (?, ?, ?)", example_conversation)
    # con.commit()


def save(request: str, response: str):
    cur.execute(f"INSERT INTO conversation VALUES (?, ?, ?)", (datetime.now(), request, response))
    con.commit()


def get_history(limit: int):
    history = []
    for row in cur.execute('SELECT * FROM conversation ORDER BY date ASC LIMIT ? OFFSET (SELECT COUNT(*) FROM conversation) - ?', (limit, limit)):
        history.append({
            "role": "user",
            "content": row[1]
        })
        history.append({
            "role": "assistant",
            "content": row[2]

        })
    return history


def populate_predefined_data():
    pass


if __name__ == "__main__":
    print(get_history(16))
