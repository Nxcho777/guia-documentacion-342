# Proyecto de ejemplo - Guia 3.4.2

Este proyecto de Python/Flask es un ejemplo para practicar **Git, Jenkins, Doxygen y CI/CD**.

## Endpoints

- `GET /hello?name=Gabriela` devuelve `Hello, Gabriela!`.
- `GET /hello` devuelve `Hello, mundo!`.
- `GET /health` devuelve `{"status": "ok"}`.

## Ejecutar localmente (Windows / PowerShell)

```powershell
py -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe -m pytest -q
.\.venv\Scripts\python.exe app.py
```

En el navegador, usar `http://127.0.0.1:5000/hello?name=Gabriela`.

## Generar la documentacion

```powershell
doxygen Doxyfile
```

Abrir `docs/html/index.html` en el navegador.

## Crear Jenkins con Docker Desktop (PowerShell)

Asegurate de que Docker Desktop esta abierto. Desde la raiz del proyecto:

```powershell
docker version
docker build -f infra/Jenkins.Dockerfile -t jenkins-docs-342 .
docker run -d --name jenkins-342 -p 8080:8080 -p 50000:50000 -v jenkins_342_home:/var/jenkins_home jenkins-docs-342
docker exec jenkins-342 cat /var/jenkins_home/secrets/initialAdminPassword
```

Abre `http://localhost:8080`, introduce la contrasena inicial y completa el asistente.

**Importante:** Este contenedor trae Python, Git, Doxygen y curl. La imagen oficial
simple de Jenkins puede NO tenerlos instalados. El puerto 8080 debe estar libre.

## Subirlo a GitHub (repositorio vacio)

Crea un repositorio llamado `guia-documentacion-342` (sin README inicial). Después,
desde la carpeta del proyecto:

```powershell
git init -b main
git add .
git commit -m "feat: proyecto inicial y pipeline"
git remote add origin https://github.com/TU_USUARIO/guia-documentacion-342.git
git push -u origin main
```

Sustituye `TU_USUARIO`. Si Git te pide autenticarte, usa Git Credential Manager,
no escribas tokens en archivos del proyecto. Para repositorios privados, configura
credenciales de lectura en Jenkins.

## Crear la tarea Pipeline en Jenkins

1. **New Item** > nombre `guia-documentacion-342` > **Pipeline**.
2. **Pipeline > Definition**: `Pipeline script from SCM`.
3. **SCM**: `Git`.
4. **Repository URL**: URL HTTPS de tu repo GitHub.
5. **Branches to build**: `*/main`.
6. **Script Path**: `Jenkinsfile`.
7. **Save** y **Build Now**.
8. **Console Output** para revisar Build, Test, Generate Documentation,
   Version Control y Deploy.

### Push de documentacion a GitHub (completar requisito de versionamiento)

La primera ejecucion deja `PUSH_DOCS = 'false'` para evitar un fallo por credenciales.
En esa modalidad se registran cambios en el repositorio Git **local de Jenkins**,
pero **no se actualiza GitHub**.

Para subir efectivamente la documentacion generada:

1. En Jenkins > **Manage Jenkins > Credentials**, crea una credencial de tipo
   **Username with password**. Usuario = tu usuario GitHub;
   password = un token personal con permisos **Contents: Read and write**
   para *este repositorio*; ID = `github-docs-token`.
2. Confirma que el repositorio del pipeline usa URL HTTPS y que la herramienta
   Git en Jenkins se llama `Default` (o ajusta `gitToolName` en Jenkinsfile).
3. Cambia `PUSH_DOCS = 'false'` a `PUSH_DOCS = 'true'`, guarda, commit y push.
4. Vuelve a pulsar **Build Now** en Jenkins y verifica que el stage Version Control
   ejecuta `git push origin HEAD:main` correctamente.
5. Comprueba en GitHub que aparece la carpeta `docs/html`.

Nunca incluyas tokens en el repositorio, el informe o las capturas.
No programes un webhook automatico sin antes configurar una estrategia para evitar
la ejecucion en bucle por commits de documentacion; para la guia basta **Build Now**.

## Alertas y notificaciones del paso 5

- El archivo `Jenkinsfile` ya muestra un aviso de **ALERTA** en el log cuando falla
  una ejecucion (`post { failure { ... } }`).
- Para enviar correos reales, configura **Manage Jenkins > System > E-mail Notification**
  con un servidor SMTP valido y comprueba que el complemento **Mailer** este instalado.
- Despues escribe tu correo en `NOTIFY_EMAIL = 'TU_CORREO'` en `Jenkinsfile`,
  haz commit y push, y vuelve a ejecutar el pipeline. Solo entonces se enviara
  notificacion por correo en caso de fallo. No se enviaran correos en la
  configuracion inicial.
- Como evidencia sin correo, captura el estado del job y el registro de consola.

## Que significa el stage Deploy

En este ejemplo el Deploy copia los artefactos a `staging/` y ejecuta una prueba
funcional (smoke test) con Flask. Es un **despliegue de ensayo temporal**, no una
aplicacion publicada en Internet ni un servicio persistente. Si el docente requiere
un servidor de pruebas real y accesible, hay que adaptar esta etapa.

## Evidencias a guardar

- `git --version` y `docker version`.
- Captura del pipeline con sus 5 etapas verdes.
- `Console Output` de la ejecucion.
- Test Report: 3 pruebas correctas.
- `docs/html/index.html` generado por Doxygen.
- Commit de documentacion en GitHub (cuando se habilita PUSH_DOCS).
- Archivos `Jenkinsfile`, `Doxyfile` y `infra/Jenkins.Dockerfile`.

Completa `INFORME_PLANTILLA.md` con TUS resultados reales y capturas.
