# 🤖 AI Engineering Knowledge Assistant

![Python](https://img.shields.io/badge/Python-3.12-blue)
![LangChain](https://img.shields.io/badge/LangChain-Latest-green)
![LangGraph](https://img.shields.io/badge/LangGraph-AI-orange)
![Google Gemini](https://img.shields.io/badge/Google-Gemini-blueviolet)
![FAISS](https://img.shields.io/badge/Vector%20Database-FAISS-red)
![License](https://img.shields.io/badge/License-Educational-lightgrey)

---

# 📌 Descripción

**AI Engineering Knowledge Assistant** es un asistente inteligente basado en la arquitectura **Retrieval-Augmented Generation (RAG)**, desarrollado con **LangChain**, **LangGraph**, **Google Gemini** y **FAISS**.

El sistema permite consultar documentos PDF mediante lenguaje natural, recuperando primero la información más relevante desde una base vectorial antes de generar una respuesta con un modelo de Inteligencia Artificial Generativa.

Este proyecto fue desarrollado como parte del **Challenge AI Engineering de Alura Latam**, aplicando buenas prácticas de ingeniería de software, procesamiento documental y arquitecturas modernas para aplicaciones de IA.

---

# 🎯 Objetivos

* Construir un asistente basado en RAG.
* Procesar documentos PDF automáticamente.
* Implementar búsqueda semántica mediante embeddings.
* Utilizar Google Gemini como modelo generativo.
* Orquestar el flujo con LangGraph.
* Crear una arquitectura modular y escalable.

---

# 🏗️ Arquitectura

```text
                          +----------------------+
                          |      PDF Files       |
                          +----------+-----------+
                                     |
                                     v
                           PyPDFLoader
                                     |
                                     v
                  RecursiveCharacterTextSplitter
                                     |
                                     v
              Google Gemini Embeddings API
                                     |
                                     v
                      FAISS Vector Database
                                     |
                                     v
                            Semantic Retriever
                                     |
                                     v
                           LangGraph Workflow
                                     |
                                     v
                     Google Gemini 3.1 Flash Lite
                                     |
                                     v
                           Intelligent Response
```

---

# 🚀 Características

* Retrieval-Augmented Generation (RAG)
* Procesamiento automático de documentos PDF
* Búsqueda semántica mediante embeddings
* Base vectorial FAISS
* Integración con Google Gemini
* Workflow con LangGraph
* Memoria conversacional
* Arquitectura modular
* Fácil escalabilidad

---

# 🛠️ Tecnologías Utilizadas

| Tecnología                   | Uso                      |
| ---------------------------- | ------------------------ |
| Python 3.12                  | Lenguaje principal       |
| LangChain                    | Orquestación de LLM      |
| LangGraph                    | Flujo del agente         |
| Google Gemini 3.1 Flash Lite | Modelo de IA             |
| Gemini Embeddings            | Embeddings semánticos    |
| FAISS                        | Base de datos vectorial  |
| PyPDFLoader                  | Lectura de PDFs          |
| python-dotenv                | Variables de entorno     |
| Git                          | Control de versiones     |
| GitHub                       | Repositorio del proyecto |

---

# 📂 Estructura del Proyecto

```text
ai-engineering-knowledge-assistant/
│
├── data/
│   └── Documentos PDF
│
├── src/
│   ├── graph.py
│   ├── llm.py
│   ├── retriever.py
│   ├── memory.py
│   ├── tools.py
│   └── prompts/
│       └── template.py
│
├── vector_store/
├── app.py
├── ingest.py
├── config.py
├── requirements.txt
└── README.md
```

---

# ⚙️ Instalación

## 1. Clonar el repositorio

```bash
git clone https://github.com/CesarConstantino/ai-engineering-knowledge-assistant.git
```

## 2. Crear un entorno virtual

```bash
python -m venv .venv
```

## 3. Activar el entorno

### Windows

```bash
.venv\Scripts\activate
```

### Linux / macOS

```bash
source .venv/bin/activate
```

## 4. Instalar dependencias

```bash
pip install -r requirements.txt
```

## 5. Configurar variables de entorno

Crear un archivo llamado `.env`

```env
GOOGLE_API_KEY=TU_API_KEY
```

## 6. Generar la base vectorial

```bash
python ingest.py
```

## 7. Ejecutar la aplicación

```bash
python app.py
```

---

# 🔄 Flujo del Sistema

1. El usuario agrega documentos PDF a la carpeta **data/**.
2. El sistema procesa los documentos.
3. Se generan embeddings con Google Gemini.
4. Los embeddings se almacenan en FAISS.
5. El Retriever recupera el contexto más relevante.
6. LangGraph coordina el flujo del agente.
7. Google Gemini genera la respuesta final.

---

# 💬 Ejemplos de Preguntas

* ¿De qué trata el documento?
* Resume el documento.
* ¿Cuál es la arquitectura del sistema?
* ¿Qué microservicios existen?
* ¿Cómo funciona el API Gateway?
* ¿Cuál es la estrategia de versionado de APIs?
* ¿Qué servicios pertenecen al Squad IA?
* ¿Qué tecnologías utiliza la arquitectura?

---

# 🧠 Ejemplo de Respuesta

**Pregunta**

> ¿De qué trata el documento?

**Respuesta**

> El documento describe la arquitectura de microservicios de la organización, incluyendo el catálogo de servicios, dependencias, estrategia de versionado de APIs, infraestructura en AWS, observabilidad distribuida, políticas de seguridad y organización de los diferentes Squads responsables de cada dominio.

---

# 📸 Capturas de Pantalla

## Aplicación en ejecución

*(Se agregará después del despliegue en Oracle Cloud Infrastructure.)*

---

# ☁️ Despliegue en Oracle Cloud Infrastructure

La aplicación será desplegada en **Oracle Cloud Infrastructure (OCI)**.

Aquí se incluirá:

* URL pública de la aplicación.
* Capturas del despliegue.
* Evidencia de funcionamiento.

---

# 📈 Resultados del Proyecto

Durante el desarrollo se implementaron exitosamente:

* Arquitectura Retrieval-Augmented Generation (RAG)
* Integración con Google Gemini
* Workflow mediante LangGraph
* Procesamiento automático de documentos PDF
* Base vectorial FAISS
* Recuperación semántica de información
* Memoria conversacional
* Arquitectura modular para futuras ampliaciones

---

# 📚 Aprendizajes

Este proyecto permitió fortalecer conocimientos en:

* AI Engineering
* Arquitecturas RAG
* LangChain
* LangGraph
* Vector Databases
* Embeddings
* Ingeniería de Software aplicada a IA
* Integración de modelos generativos
* Gestión de proyectos con Git y GitHub

---

# 🚀 Próximas Mejoras

* Interfaz web con Streamlit.
* Soporte para múltiples documentos.
* Carga dinámica de archivos.
* Historial persistente de conversaciones.
* Integración con bases de conocimiento empresariales.
* Despliegue productivo en OCI.

---

# 👨‍💻 Autor

## César Constantino

**AI Strategist | AI Engineer | Fraud Prevention Architect**

Especialista en Prevención de Fraude, Inteligencia Artificial, Machine Learning y Arquitecturas RAG orientadas al desarrollo de soluciones empresariales.

GitHub:

https://github.com/CesarConstantino

---

# 📄 Licencia

Proyecto desarrollado con fines educativos como parte del **Challenge AI Engineering de Alura Latam**.

Puede utilizarse como referencia para aprendizaje sobre aplicaciones de Inteligencia Artificial Generativa basadas en RAG.
