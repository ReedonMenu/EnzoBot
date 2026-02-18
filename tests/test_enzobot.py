from src.enzobot import EnzoBot


def test_empty_prompt_returns_quick_start() -> None:
    bot = EnzoBot()
    response = bot.respond("   ")
    assert "## Quick Start" in response


def test_code_prompt_uses_engineering_response() -> None:
    bot = EnzoBot()
    response = bot.respond("Help me debug this Python bug")
    assert "## Engineering Response" in response
    assert "Ranked Approach" in response


def test_general_prompt_returns_framework() -> None:
    bot = EnzoBot()
    response = bot.respond("I want to improve team communication")
    assert "## Solution Framework" in response
