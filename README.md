La idea de este repositorio fue instanciar un server MCP para poder manejar Tools hacia cualquier agente LLM que acepte tools. 

Tiene funciones simples de calculos de matematica y trae nombres de una lista local.

Funciona mediante una api, para poder interactuar de forma mas simple

Para arrancarlo localmente, uvicorn main:app --reload

La ruta para poder iniciar la conversacion es: http://127.0.0.1:8000/api/chat_model

Durante el desarrollo del proyecto en Windows, me encontré con un error relacionado con la ejecución de subprocesos asincrónicos utilizando `asyncio.create_subprocess_exec`,
lo cual arrojaba una excepción `NotImplementedError`. Este problema se debe a que, por defecto, Windows utiliza el `WindowsProactorEventLoopPolicy`, el cual no implementa correctamente el transporte para subprocesos.
A pesar de intentar forzar el uso del `WindowsSelectorEventLoopPolicy` (que sí lo soporta), continuaban los conflictos. Para resolverlo de forma efectiva, opté por correr el entorno en WSL (Windows Subsystem for Linux),
donde el soporte para `asyncio` y subprocesos es completo y nativo, eliminando completamente el error y permitiendo la ejecución del cliente stdio sin inconvenientes.
