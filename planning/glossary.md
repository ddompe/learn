# Glossary and terminology decisions

Decisions for the Spanish translation. Add terms as they are introduced.

## General decisions

- Spanish variant: neutral Latin American.
- Register: **tú**.
- Keep English when the term is the one learners will meet in tools, documentation, and
  error messages. Introduce the English term once with a Spanish explanation.

## Terms

| English                         | Spanish                                | Keep English? | Notes                                                                           |
| ------------------------------- | -------------------------------------- | ------------- | ------------------------------------------------------------------------------- |
| file                            | archivo                                | No            |                                                                                 |
| folder                          | carpeta                                | No            | "directorio" mentioned once as a synonym                                        |
| path                            | ruta                                   | No            |                                                                                 |
| terminal                        | terminal                               | —             |                                                                                 |
| command line                    | línea de comandos                      | No            |                                                                                 |
| repository                      | repositorio                            | No            |                                                                                 |
| commit                          | commit                                 | Yes           | verb: "hacer commit"                                                            |
| branch                          | rama                                   | No            | "branch" mentioned once                                                         |
| pull request                    | pull request                           | Yes           |                                                                                 |
| push / pull                     | push / pull                            | Yes           |                                                                                 |
| package                         | paquete                                | No            |                                                                                 |
| virtual environment             | entorno virtual                        | No            |                                                                                 |
| DataFrame                       | DataFrame                              | Yes           |                                                                                 |
| prompt                          | prompt                                 | Yes           | "instrucción" mentioned once                                                    |
| token                           | token                                  | Yes           |                                                                                 |
| encoding                        | codificación                           | No            |                                                                                 |
| bug                             | error / bug                            | Both          |                                                                                 |
| script                          | script                                 | Yes           |                                                                                 |
| notebook                        | notebook                               | Yes           | "cuaderno" mentioned once                                                       |
| API key                         | clave de API                           | No            |                                                                                 |
| AI assistant                    | asistente de IA                        | No            | Chat tool that writes and explains code (0.1)                                   |
| learning path                   | ruta de aprendizaje                    | No            | Not to be confused with file "path" (ruta); consider "itinerario" if it clashes |
| opinionated                     | con criterio propio                    | No            | Course teaches one fixed tool set (0.1)                                         |
| operating system                | sistema operativo                      | No            |                                                                                 |
| application                     | aplicación                             | No            |                                                                                 |
| memory (RAM)                    | memoria (RAM)                          | No            | vs. storage / almacenamiento                                                    |
| storage                         | almacenamiento                         | No            |                                                                                 |
| bit / byte                      | bit / byte                             | Yes           |                                                                                 |
| absolute path                   | ruta absoluta                          | No            |                                                                                 |
| relative path                   | ruta relativa                          | No            |                                                                                 |
| current folder                  | carpeta actual                         | No            |                                                                                 |
| extension                       | extensión                              | No            | file extension                                                                  |
| magic number                    | número mágico                          | No            |                                                                                 |
| text file / binary file         | archivo de texto / binario             | No            |                                                                                 |
| cloud-synced folder             | carpeta sincronizada en la nube        | No            |                                                                                 |
| Unicode / UTF-8                 | Unicode / UTF-8                        | Yes           |                                                                                 |
| mojibake                        | mojibake                               | Yes           | explain once: texto ilegible por codificación                                   |
| float                           | número de punto flotante (float)       | Yes           |                                                                                 |
| Decimal                         | Decimal                                | Yes           | exact decimal type                                                              |
| shell                           | shell / intérprete de comandos         | Yes           |                                                                                 |
| PowerShell / zsh                | PowerShell / zsh                       | Yes           |                                                                                 |
| PATH                            | PATH                                   | Yes           | variable that lists program folders                                             |
| environment variable            | variable de entorno                    | No            |                                                                                 |
| client / server                 | cliente / servidor                     | No            |                                                                                 |
| URL                             | URL                                    | Yes           |                                                                                 |
| HTTP / HTTPS                    | HTTP / HTTPS                           | Yes           |                                                                                 |
| DNS                             | DNS                                    | Yes           |                                                                                 |
| API                             | API                                    | Yes           |                                                                                 |
| revoke (a key)                  | revocar (una clave)                    | No            |                                                                                 |
| LLM (large language model)      | LLM / modelo de lenguaje grande        | Yes           |                                                                                 |
| token                           | token                                  | Yes           |                                                                                 |
| parameters                      | parámetros                             | No            |                                                                                 |
| training / inference            | entrenamiento / inferencia             | No            |                                                                                 |
| knowledge cutoff                | fecha de corte de conocimiento         | No            |                                                                                 |
| context window                  | ventana de contexto                    | No            |                                                                                 |
| vendor / model / product        | proveedor / modelo / producto          | No            |                                                                                 |
| open-weight                     | de pesos abiertos (open-weight)        | Yes           | explain once                                                                    |
| hallucination                   | alucinación                            | No            |                                                                                 |
| personal data                   | datos personales                       | No            |                                                                                 |
| anonymising                     | anonimizar                             | No            |                                                                                 |
| program                         | programa                               | No            |                                                                                 |
| source code                     | código fuente                          | No            |                                                                                 |
| interpreter / compiler          | intérprete / compilador                | No            |                                                                                 |
| variable                        | variable                               | No            |                                                                                 |
| VS Code                         | VS Code                                | Yes           |                                                                                 |
| extension (VS Code)             | extensión                              | No            | distinct from file extension; 1.5 uses the same word                            |
| version control                 | control de versiones                   | No            |                                                                                 |
| snapshot                        | instantánea                            | No            | Git term: commit                                                                |
| history                         | historial                              | No            |                                                                                 |
| Git / GitHub                    | Git / GitHub                           | Yes           |                                                                                 |
| stage / staging area            | preparar (stage) / área de preparación | No            | say stage once                                                                  |
| diff                            | diff                                   | Yes           |                                                                                 |
| remote                          | remoto                                 | No            |                                                                                 |
| branch                          | rama                                   | No            |                                                                                 |
| secret                          | secreto                                | No            |                                                                                 |
| .gitignore / .env               | .gitignore / .env                      | Yes           |                                                                                 |
| package / dependency / registry | paquete / dependencia / registro       | No            |                                                                                 |
| lock file                       | archivo de bloqueo (lock file)         | Yes           | explain once                                                                    |
| typosquatting                   | typosquatting                          | Yes           | explain once                                                                    |
| test (pytest)                   | prueba / pytest                        | No            | pytest stays English                                                            |
| traceback                       | traceback                              | Yes           | explain once: seguimiento de errores                                            |
| debugger / breakpoint           | depurador / punto de interrupción      | No            |                                                                                 |
| string / f-string               | cadena de texto / f-string             | No            | f-string stays English                                                          |
| method                          | método                                 | No            |                                                                                 |
| list / dictionary / tuple / set | lista / diccionario / tupla / conjunto | No            |                                                                                 |
| loop                            | bucle                                  | No            |                                                                                 |
| function / parameter / argument | función / parámetro / argumento        | No            |                                                                                 |
| return                          | devolver (return)                      | Yes           | keyword stays English                                                           |
| exception                       | excepción                              | No            |                                                                                 |
| module                          | módulo                                 | No            |                                                                                 |
| standard library                | biblioteca estándar                    | No            |                                                                                 |
| virtual environment (.venv)     | entorno virtual                        | No            | already listed                                                                  |
| uv                              | uv                                     | Yes           |                                                                                 |
| pyproject.toml / TOML           | pyproject.toml / TOML                  | Yes           |                                                                                 |
| REPL                            | REPL                                   | Yes           | explain once: consola interactiva                                               |
| notebook / cell / kernel        | notebook / celda / kernel              | Yes           | cell: celda                                                                     |
| script                          | script                                 | Yes           | already listed                                                                  |
