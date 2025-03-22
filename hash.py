from passlib.hash import sha512_crypt

password = "contraseña1"  # Cambia esto por tu contraseña real
hashed_password = sha512_crypt.hash(password)

print("Hash compatible con aMQTT:")
print(hashed_password)
