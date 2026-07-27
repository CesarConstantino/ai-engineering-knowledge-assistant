# Decisiones Técnicas - AI Engineering Knowledge Assistant

## Objetivo

Documentar las principales decisiones de arquitectura tomadas durante la construcción del sistema.

---

# Arquitectura RAG

## Decisión

Implementar una arquitectura Retrieval-Augmented Generation (RAG).

## Razón

Permite combinar modelos generativos con fuentes externas de conocimiento, reduciendo respuestas sin contexto y permitiendo consultar documentación específica.

---

# Uso de Embeddings

## Decisión

Utilizar embeddings para representar documentos como vectores semánticos.

## Razón

La búsqueda basada en significado permite recuperar información relacionada aunque las palabras exactas no coincidan.

---

# Base Vectorial FAISS

## Decisión

Utilizar FAISS como motor de búsqueda vectorial.

## Razón

FAISS ofrece una solución eficiente para almacenamiento y recuperación de similitud vectorial, adecuada para esta etapa del proyecto.

---

# Google Gemini

## Decisión

Utilizar modelos Gemini para generación de respuestas.

## Razón

Permite integrar capacidades generativas avanzadas manteniendo una arquitectura flexible para futuras evoluciones.

---

# LangChain y LangGraph

## Decisión

Utilizar LangChain y LangGraph como capa de integración y orquestación.

## Razón

Facilitan la construcción de flujos de IA, componentes reutilizables y evolución hacia arquitecturas basadas en agentes.

---

# Consideraciones Futuras

Próximas mejoras técnicas:

- Evaluación automática de calidad RAG.
- Observabilidad del sistema.
- Seguridad y control de acceso.
- Integración con múltiples fuentes de conocimiento.
- Despliegue en nube.

---

# Limitaciones Actuales

- Dependencia de la calidad de los documentos fuente.
- Evaluación avanzada pendiente.
- Sin autenticación empresarial actualmente.

Estas limitaciones forman parte del roadmap de evolución del sistema.
