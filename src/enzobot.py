from __future__ import annotations

from dataclasses import dataclass
import re
from typing import Callable


@dataclass(frozen=True)
class IntentRule:
    """Maps keyword patterns to an intent handler."""

    name: str
    pattern: re.Pattern[str]
    handler: Callable[[str], str]


class EnzoBot:
    """A lightweight, deterministic assistant for local use."""

    def __init__(self) -> None:
        self.rules = (
            IntentRule("greeting", re.compile(r"\b(hi|hello|hey)\b", re.I), self._handle_greeting),
            IntentRule("plan", re.compile(r"\b(plan|roadmap|strategy)\b", re.I), self._handle_plan),
            IntentRule("code", re.compile(r"\b(code|python|bug|refactor|test)\b", re.I), self._handle_code),
        )

    def respond(self, prompt: str) -> str:
        """Return a premium-style, structured response for the user prompt."""
        clean_prompt = prompt.strip()
        if not clean_prompt:
            return self._empty_prompt_response()

        for rule in self.rules:
            if rule.pattern.search(clean_prompt):
                return rule.handler(clean_prompt)

        return self._handle_general(clean_prompt)

    def _empty_prompt_response(self) -> str:
        return (
            "## Quick Start\n"
            "- Share your goal in one sentence.\n"
            "- Add constraints (time, tools, budget).\n"
            "- I will return ranked options with next steps."
        )

    def _handle_greeting(self, _: str) -> str:
        return (
            "## Hello 👋\n"
            "I can help with strategy, coding, and execution planning.\n\n"
            "### Fast Paths\n"
            "- **Build something:** describe the feature and stack.\n"
            "- **Fix an issue:** share error + expected behavior.\n"
            "- **Plan work:** share objective + deadline."
        )

    def _handle_plan(self, prompt: str) -> str:
        return (
            "## Strategic Plan\n"
            f"**Objective:** {prompt}\n\n"
            "### Recommended Sequence\n"
            "1. Define measurable outcome (what success looks like).\n"
            "2. Break into milestones with owners and deadlines.\n"
            "3. Track risks weekly and adjust scope early.\n\n"
            "### Optimization\n"
            "- Prioritize high-impact, low-effort tasks first."
        )

    def _handle_code(self, prompt: str) -> str:
        return (
            "## Engineering Response\n"
            f"**Request:** {prompt}\n\n"
            "### Ranked Approach\n"
            "1. Reproduce the issue with a minimal test case.\n"
            "2. Implement the smallest safe fix.\n"
            "3. Add tests for regression prevention.\n"
            "4. Refactor only after tests pass.\n\n"
            "### Deliverables\n"
            "- Patch diff\n"
            "- Test evidence\n"
            "- Follow-up hardening ideas"
        )

    def _handle_general(self, prompt: str) -> str:
        return (
            "## Solution Framework\n"
            f"**Input:** {prompt}\n\n"
            "### Option Ranking\n"
            "1. **Direct path:** fastest to execution.\n"
            "2. **Balanced path:** speed + robustness.\n"
            "3. **High-upside path:** innovation-focused.\n\n"
            "### Next Action\n"
            "- Reply with constraints and I will produce an implementation plan."
        )


def main() -> None:
    bot = EnzoBot()
    print("EnzoBot CLI ready. Type 'exit' to quit.")
    while True:
        user_input = input("You> ").strip()
        if user_input.lower() in {"exit", "quit"}:
            print("EnzoBot> Goodbye.")
            break
        print("EnzoBot>")
        print(bot.respond(user_input))


if __name__ == "__main__":
    main()
