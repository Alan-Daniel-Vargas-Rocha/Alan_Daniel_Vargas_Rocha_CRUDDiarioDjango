## Instalación paso a paso
# Clonar el repositorio
bash
git clone https://github.com/TU_USUARIO/diario-miki.git
cd diario-miki
Reemplaza TU_USUARIO y diario-miki por los datos reales de tu repo.

#  Crear el entorno virtual
Windows (CMD):

bash
python -m venv .venv
.venv\Scripts\activate
Windows (Git Bash):

bash
python -m venv .venv
source .venv/Scripts/activate
Linux / Mac:

bash
python3 -m venv .venv
source .venv/bin/activate
Sabrás que el venv está activo cuando veas (.venv) al inicio de la línea de comandos.

# Instalar las dependencias
Con el entorno virtual activado:

bash
pip install -r requirements.txt
Esto instala automáticamente:

Paquete	Versión	Uso
Django	6.1.1	Framework web
asgiref	3.12.1	Dependencia interna de Django
sqlparse	0.6.0	Parser SQL (usado por Django)
tzdata	2026.4	Zonas horarias
python-dotenv	última	Leer variables desde .env


bash
pip install python-dotenv
# Configurar variables de entorno
Crea un archivo llamado .env en la raíz del proyecto (donde está manage.py):

env
SECRET_KEY=django-insecure-cambia-esto-por-una-clave-propia
DEBUG=True

💡 Puedes copiar el archivo .env.example como base:

bash
cp .env.example .env
Luego edita .env y coloca tu propia SECRET_KEY.

#  Aplicar migraciones
bash
python manage.py makemigrations
python manage.py migrate
Esto crea la base de datos db.sqlite3 con todas las tablas necesarias.

# Crear superusuario (opcional)
Para acceder al panel de administración de Django:

bash
python manage.py createsuperuser
Te pedirá usuario, correo y contraseña.

# Levantar el servidor
bash
python manage.py runserver
Abre tu navegador en: http://127.0.0.1:8000/

# Enlaces y rutas principales
Rutas de la aplicación
Acción	URL	Nombre en Django
Crear perfil	http://127.0.0.1:8000/create_profile/	profile_createuser
Crear entrada	http://127.0.0.1:8000/diario/crear/	diario_create
Listar entradas	http://127.0.0.1:8000/diario/lista/	diario_list
Ver detalle	http://127.0.0.1:8000/diario/detalle/<pk>/	diario_detail
Editar entrada	http://127.0.0.1:8000/diario/editar/<pk>/	diario_update
Eliminar entrada	http://127.0.0.1:8000/diario/eliminar/<pk>/	diario_delete
Admin de Django	http://127.0.0.1:8000/admin/	admin
Reemplaza <pk> por el ID numérico de la entrada (ej: 1, 2, 3...).
