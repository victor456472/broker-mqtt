import paho.mqtt.client as mqtt
import time

def on_publish(client, userdata, mid):
    print(f"📤 Mensaje publicado correctamente con ID: {mid}")

print("🔄 Creando cliente MQTT con WebSockets...")
client = mqtt.Client(client_id="publicador_1", transport="websockets")  # Se agrega un ID único

print("🔑 Configurando credenciales...")
client.username_pw_set("sensor1", "prueba1234")

client.on_publish = on_publish  # ✅ Callback que confirma la publicación

print("🔄 Conectando al broker WebSockets...")
client.connect("localhost", 9001)

print("📡 Publicando mensaje en 'sensores/gas'...")
client.loop_start()  # 🔄 Inicia el loop para manejar eventos MQTT

(client_publish_result, mid) = client.publish("sensores/gas", "10ppm", qos=1)
print(f"🔍 Publicación resultado: {client_publish_result}, Mensaje ID: {mid}")

time.sleep(1)  # ⏳ Espera un poco para que `on_publish()` tenga tiempo de ejecutarse

client.loop_stop()  # 🚫 Detiene el loop
client.disconnect()

print("✅ Mensaje publicado con éxito.")
