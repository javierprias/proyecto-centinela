# 🛡️ PROYECTO CENTINELA GRUPO 2
**Plataforma DevSecOps de Ciclo Completo para Análisis de Desinformación y OSINT**

![Build Status](https://github.com/javierprias/proyecto-centinela/actions/workflows/ci-pipeline.yml/badge.svg)
![Security](https://img.shields.io/badge/Security-Shift--Left-blue)
![Docker](https://img.shields.io/badge/Container-Docker-2496ED)

## 1. Resumen Ejecutivo
El **Proyecto Centinela** es una solución tecnológica diseñada para combatir la desinformación digital mediante la automatización de procesos de vigilancia (OSINT) y análisis de contenido.

El valor central de este proyecto no reside solo en su funcionalidad, sino en su ingeniería: ha sido construido bajo una rigurosa metodología **DevSecOps**. Se ha implementado un ciclo de vida de desarrollo seguro donde la seguridad no es un paso final, sino un componente integrado desde el diseño (Shift-Left Security), utilizando herramientas FOSS para garantizar la integridad, confidencialidad y disponibilidad del sistema.

## 2. Arquitectura del Sistema
La solución sigue una arquitectura de **Microservicios Contenerizados** orquestados con Docker.

## 3. Video

* **Link Video:** https://uniminuto0-my.sharepoint.com/:v:/g/personal/javier_prias_uniminuto_edu_co/IQBbpkb5zFBcS7Tw8wtJOcwDAbAgAYkvDODDxq2TFR6wzOE?nav=eyJyZWZlcnJhbEluZm8iOnsicmVmZXJyYWxBcHAiOiJPbmVEcml2ZUZvckJ1c2luZXNzIiwicmVmZXJyYWxBcHBQbGF0Zm9ybSI6IldlYiIsInJlZmVycmFsTW9kZSI6InZpZXciLCJyZWZlcnJhbFZpZXciOiJNeUZpbGVzTGlua0NvcHkifX0&e=C8KHRN

### Diagrama de Componentes

**Componentes Técnicos**

- Backend (API Gateway): Desarrollado en Python (FastAPI). Recibe datos, ejecuta modelos de NLP (TextBlob) para análisis de sentimiento y sirve de punto de entrada.
- Worker Scraper: Servicio autónomo en Python. Navega periódicamente sitios web objetivo, extrae titulares y los envía al backend. Cuenta con manejo de errores y timeouts para evitar bloqueos.
- Base de Datos: PostgreSQL contenerizado para la persistencia de hallazgos.
- Infraestructura: Todo el stack se despliega mediante docker-compose, garantizando portabilidad absoluta.

```mermaid
graph TD
    User((Usuario/Analista)) -->|HTTP GET /| API[Backend - FastAPI]
    
    subgraph "Red Interna Docker (Aislada)"
        Scraper[Worker Scraper] -->|HTTP POST /analizar| API
        API -->|NLP Analysis| TextBlob[Motor TextBlob]
        API -.->|Persistencia Futura| DB[("PostgreSQL")]
    end
    
    Scraper -->|HTTPS Requests| Web[Internet / Noticias]

