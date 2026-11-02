#!/usr/bin/env python3
"""Inicia o agente portfolio_manager no terminal usando o Runner do Google ADK."""

import asyncio

from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai import types

from my_agent.agent import root_agent

APP_NAME = "portfolio_manager"
USER_ID = "usuario_local"
SESSION_ID = "sessao_local"


async def main():
    session_service = InMemorySessionService()
    await session_service.create_session(
        app_name=APP_NAME, user_id=USER_ID, session_id=SESSION_ID
    )
    runner = Runner(agent=root_agent, app_name=APP_NAME, session_service=session_service)

    print(f"{root_agent.name} — {root_agent.description}")
    print("Digite 'sair' para encerrar.\n")

    try:
        while True:
            texto = input("Você: ").strip()
            if texto.lower() in ("sair", "exit", "quit"):
                break
            if not texto:
                continue

            mensagem = types.Content(role="user", parts=[types.Part(text=texto)])
            async for evento in runner.run_async(
                user_id=USER_ID, session_id=SESSION_ID, new_message=mensagem
            ):
                if evento.is_final_response() and evento.content and evento.content.parts:
                    print(f"\nAgente: {evento.content.parts[0].text}\n")
    except KeyboardInterrupt:
        pass
    finally:
        if hasattr(runner, "close"):
            await runner.close()
        print("\nAgente finalizado.")


if __name__ == "__main__":
    asyncio.run(main())
