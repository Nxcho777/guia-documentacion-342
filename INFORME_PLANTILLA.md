# Informe de actividad 3.4.2: Documentacion y trazabilidad

**Asignatura:** Ciberseguridad en desarrollo
**Estudiante:** [Nombre y apellido]
**Fecha:** [Fecha de ejecucion]
**Repositorio:** [URL de GitHub]

## 1. Objetivo
Configurar un flujo de integracion continua para generar documentacion del codigo,
registrar cambios y comprobar la calidad del software mediante Git, Jenkins y Doxygen.

## 2. Herramientas utilizadas
- Git: [Version: ejecutar `git --version`]
- Docker Desktop: [Version: ejecutar `docker version`]
- Jenkins: [Version visible en Jenkins]
- Doxygen: [Version: `docker exec jenkins-342 doxygen -v`]
- Python / Flask / pytest: [Versiones reales]

## 3. Procedimiento de configuracion
### 3.1 Instalacion de Git y Jenkins
[Explica como verificaste Git y Docker, construiste la imagen de Jenkins y
accediste a http://localhost:8080.]

**Evidencia 1:** [Insertar captura de Jenkins configurado]

### 3.2 Repositorio Git
[Incluye URL del repositorio y explica el primer commit.]

**Evidencia 2:** [Insertar captura del repositorio]

### 3.3 Doxygen
[Explica que comentarios hay en app.py y que hace el archivo Doxyfile.]

**Evidencia 3:** [Insertar captura de docs/html/index.html]

### 3.4 Pipeline CI/CD
| Etapa | Proposito | Resultado real |
|---|---|---|
| Build | Preparar entorno y validar sintaxis | [Pendiente] |
| Test | Ejecutar pruebas automaticas | [Pendiente] |
| Generate Documentation | Crear HTML con Doxygen | [Pendiente] |
| Version Control | Registrar y publicar cambios de docs | [Pendiente] |
| Deploy | Preparar staging y ejecutar smoke test | [Pendiente] |

**Evidencia 4:** [Insertar captura con las cinco etapas de Jenkins]

## 4. Pruebas realizadas
| Prueba | Resultado esperado | Resultado observado |
|---|---|---|
| GET /hello?name=Gabriela | Hello, Gabriela! | [Completar] |
| GET /hello | Hello, mundo! | [Completar] |
| GET /health | status = ok | [Completar] |
| Documentacion Doxygen | Crear docs/html/index.html | [Completar] |
| GitHub | Ver docs/html publicado | [Completar tras habilitar push] |

**Evidencia 5:** [Insertar captura del Test Report o Console Output]

### 3.5 Monitoreo y notificaciones
[Describe el estado del job, consulta Console Output y, si corresponde,
como configuraste las notificaciones por correo. No afirmes haber enviado
correos si no configuraste SMTP y NOTIFY_EMAIL.]

## 5. Resultados obtenidos
[Escribe cuantos tests pasaron, el estado final de cada etapa y si lograste
registrar y subir la documentacion a GitHub. NO declares exito sin ejecutar.]

## 6. Problemas y soluciones
[Ejemplo de formato: Problema: ... / Causa: ... / Solucion: ...]

## 7. Mejoras propuestas
- Registrar la version de dependencias para mayor reproducibilidad.
- Agregar revision automatizada de seguridad de dependencias.
- Generar alertas cuando falle el pipeline, como solicita el paso 5.
- Usar una rama especifica para cambios de documentacion y un Pull Request.
- Realizar un despliegue persistente si el contexto lo requiere.

## 8. Conclusiones
[Explica que aprendiste sobre documentacion, trazabilidad y cambios controlados.]
