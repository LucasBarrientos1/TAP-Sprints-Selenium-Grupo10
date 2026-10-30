# Proyecto Final — Automatización Cross-Browser con Selenium WebDriver y CI/CD
**Grupo 10** — Barrientos, Lucas · Sandoval, Thiago · Pereyra, Dario · Zelaya, Alexis
Técnicas Avanzadas de Programación (TAP) — Ciclo 2026 — Instituto IES Alfredo Coviello

## 1. Qué es este repositorio
Este repositorio contiene el artefacto técnico final del proyecto de especialización en herramientas de testing (Sprints 1 a 4). La solución implementa una suite de pruebas automatizadas End-to-End (E2E) utilizando **Python**, **Selenium WebDriver** y **pytest**, con parametrización *cross-browser* y un pipeline de Integración Continua (CI/CD) completamente automatizado en **GitHub Actions**.

## 2. Sistema Bajo Prueba (SUT)
**ParaBank** (`https://parabank.parasoft.com/parabank`), una plataforma de banca en línea simulada provista por Parasoft como entorno de prácticas autorizado para ingeniería de calidad. El sistema permite validar flujos críticos como autenticación, alta de usuarios, transferencias y apertura de cuentas.

## 3. Estructura del Repositorio
```
TAP-Sprints-Selenium-Grupo10/
├── .github/
│   └── workflows/
│       └── tests.yml          # Pipeline de Integración Continua (CI/CD) en GitHub Actions
├── tests/
│   ├── test_login.py          # Casos de prueba de autenticación y registros (TC01 a TC06)
│   └── test_transfer_y_cuentas.py # Casos de transferencia y cuentas (TC07 a TC10)
├── reportes/                  # Directorio para reportes HTML y capturas ante fallos
├── conftest.py                # Fixture cross-browser centralizado y gestión de datos dinámicos
├── requirements.txt           # Dependencias oficiales del proyecto (pytest, selenium, pytest-html, etc.)
├── pytest.ini                 # Configuración general de ejecución de pytest
└── README.md                  # Documentación oficial del proyecto
```

## 4. Requisitos Previos
- Python 3.9 o superior instalado.
- Google Chrome, Mozilla Firefox o Microsoft Edge instalados localmente.
- **Selenium Manager** (incorporado nativamente desde Selenium 4.6+) se encarga de resolver y gestionar los drivers de forma transparente sin requerir descargas manuales de terceros.

## 5. Instalación Local
```bash
# 1. Clonar el repositorio
git clone https://github.com/LucasBarrientos1/TAP-Sprints-Selenium-Grupo10.git
cd TAP-Sprints-Selenium-Grupo10

# 2. Crear y activar el entorno virtual
python3 -m venv .venv
source .venv/bin/activate         # En Windows: .venv\Scripts\activate

# 3. Instalar las dependencias del proyecto
pip install -r requirements.txt
```

## 6. Comandos de Ejecución Local
```bash
# Ejecutar toda la suite en Chrome (por defecto)
pytest

# Ejecutar la suite en un navegador específico
pytest --browser=chrome
pytest --browser=firefox

# Ejecutar en modo sin ventana (headless)
pytest --browser=chrome --headless

# Generar un reporte HTML formal de la ejecución
pytest --html=reportes/report.html --self-contained-html -v
```

## 7. Matriz de Casos de Prueba Automatizados
| Archivo | Caso | Qué verifica | Estado |
|---|---|---|---|
| `test_login.py` | TC01 - TC03 | Autenticación, login exitoso, usuario inexistente y contraseña vacía. | ✅ Ejecutado, PASSED |
| `test_login.py` | TC04 - TC06 | Registro de usuario válido, campos vacíos y colisión de username duplicado. | ✅ Ejecutado, PASSED |
| `test_transfer_y_cuentas.py` | TC07 - TC10 | Transferencias entre cuentas, montos límite y apertura de cuentas nuevas. | ✅ Ejecutado / Integrado en suite |

## 8. Integración Continua y Pipeline CI/CD (GitHub Actions)
El workflow configurado en `.github/workflows/tests.yml` orquesta la ejecución desatendida de la suite:
* **Matriz Multi-navegador:** Ejecución paralela en contenedores Linux (`ubuntu-latest`) para **Google Chrome** y **Mozilla Firefox**.
* **Historial de Ejecuciones:** Tras una fase de estabilización de infraestructura, el pipeline consolidó un historial de 23 corridas, alcanzando un **100% de éxito en verde (All checks passed)** en la **Corrida #23**.
* **Artefactos Automáticos:** Cada ejecución genera y almacena reportes en formato HTML, XML y capturas de pantalla (*screenshots*) descargables desde la pestaña *Actions* de GitHub.

### Comandos de ejecución en CI/CD (equivalentes locales):
```bash
pytest --browser=chrome --headless -n 2 --html=reportes/report.html --self-contained-html
```

## 9. Enlaces y Recursos de Interés
* **Repositorio Oficial en GitHub:** [TAP-Sprints-Selenium-Grupo10](https://github.com/LucasBarrientos1/TAP-Sprints-Selenium-Grupo10)
* **Sistema Bajo Prueba (ParaBank):** [https://parabank.parasoft.com/parabank](https://parabank.parasoft.com/parabank)
* **Evidencias y Videos de Demostración:** [Carpeta Compartida en Google Drive](https://drive.google.com/drive/folders/1V_x-wwkhoI9YKYVzqY0wXnFoj3Kgy-6V?usp=sharing)