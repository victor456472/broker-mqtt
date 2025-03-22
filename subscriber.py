import paho.mqtt.client as mqtt
import logging

logging.basicConfig(level=logging.DEBUG)

def on_connect(client, userdata, flags, rc):
    print(f"🔗 Conexión con código: {rc}")
    if rc == 0:
        print("✅ Conectado al broker WebSocket correctamente")
        (result, mid) = client.subscribe("sensores/gas", qos=1)
        print(f"📡 Intentando suscribirse al tópico 'sensores/gas'... Resultado: {result}")
    else:
        print(f"⚠️ Error en la conexión: {rc}")

def on_subscribe(client, userdata, mid, granted_qos):
    print(f"✅ Suscripción exitosa (QoS: {granted_qos})")

def on_message(client, userdata, msg):
    print("🛑 Callback on_message() ejecutado")
    print(f"📩 Mensaje recibido -> {msg.topic}: {msg.payload.decode()}")

print("🔄 Creando cliente MQTT con WebSockets...")
client_id = "subscriptor_1"  # ✅ Se define un ID único
client = mqtt.Client(client_id=client_id, transport="websockets", clean_session=False)

print("🔑 Configurando credenciales...")
client.username_pw_set("sensor1", "prueba1234")

client.on_connect = on_connect
client.on_subscribe = on_subscribe
client.on_message = on_message

print("🔄 Intentando conectar al broker WebSockets...")
client.connect("localhost", 9001)

print("♻️ Iniciando loop...")
client.loop_forever()
