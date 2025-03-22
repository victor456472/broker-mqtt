import paho.mqtt.client as mqtt
import time

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("✅ Conectado al broker MQTT por TCP (1883)")
    else:
        print(f"❌ Error de conexión (código {rc})")

def on_publish(client, userdata, mid):
    print(f"📤 Mensaje publicado correctamente con ID: {mid}")

# 🔄 Crear cliente MQTT con protocolo TCP (por defecto)
client = mqtt.Client(client_id="publicador_tcp")

# 🔑 Configurar credenciales
client.username_pw_set("sensor1", "prueba1234")

# 🔗 Configurar callbacks
client.on_connect = on_connect
client.on_publish = on_publish

# 🔌 Conectar al broker por TCP (puerto 1883)
client.connect("localhost", 1883)

# 🚀 Iniciar el loop para permitir que se ejecute on_publish
client.loop_start()

# 📨 Publicar mensaje
topic = "sensores/gas"
mensaje = "15ppm"
(client_publish_result, mid) = client.publish(topic, mensaje, qos=1)
print(f"🔍 Publicando en '{topic}' -> {mensaje} (result: {client_publish_result})")

# ⏳ Esperar un momento para recibir confirmación
#time.sleep(1)

# 🔌 Finalizar
client.loop_stop()
client.disconnect()
print("✅ Desconectado")
