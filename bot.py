from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import requests

# Telegram config
TOKEN = '8047337853:AAGizHiBxQSrrUl8IQw-TX9Zjz86PcJGhlU'
CHAT_ID = '6821521589'

# Chrome headless
options = Options()
options.add_argument("--headless")
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
driver = webdriver.Chrome(options=options)

def send_telegram_message(message):
    url = f'https://api.telegram.org/bot{TOKEN}/sendMessage'
    payload = {'chat_id': CHAT_ID, 'text': message}
    requests.post(url, data=payload)

def get_last_colors():
    driver.get("https://blaze.bet.br/pt/games/double")
    time.sleep(6)
    elements = driver.find_elements(By.CLASS_NAME, "entry")
    colors = []
    for el in elements[:7]:
        color = el.get_attribute("class")
        if "white" in color:
            colors.append("white")
        elif "red" in color:
            colors.append("red")
        elif "black" in color:
            colors.append("black")
    return colors

def predict_next_color(colors):
    reds = colors.count("red")
    blacks = colors.count("black")
    if reds > blacks:
        return "Provável: 🔴 RED"
    elif blacks > reds:
        return "Provável: ⚫ BLACK"
    else:
        return "⚪ Atenção ao possível BRANCO!"

def main_loop():
    while True:
        try:
            colors = get_last_colors()
            prediction = predict_next_color(colors)
            send_telegram_message(f"🧠 Sinal da Blaze:\nÚltimos: {colors}\n🎯 Próxima aposta: {prediction}")
            time.sleep(60)
        except Exception as e:
            send_telegram_message(f"Erro: {e}")
            time.sleep(60)

if __name__ == "__main__":
    send_telegram_message("🤖 Bot iniciado e funcionando!")
    main_loop()
