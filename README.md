# museo-inteligente

SERVER MCP STREAM 

Se levanta un server con el protocolo de MCP para el manejo de tools y/o recurses que puedan conectarse al LLM Realtime y procese la invocacion de las mismas dependiendo de la consulta del cliente.

Devuelve sus respuestas en formato token. 

### Requisitos previos:

- Levantar un entorno virtual.
- Descargar las dependecias: pip install -r requirements.txt


### Levantar Server:

- cd mcp_proyect
- python server_stream_mcp.py


#### Formato Demo

Levantar archivo "main.py" y consultar al endpoint "/get_mcp". Lograremos ver la respuesta del lado del Cliente en formato stream via token.
