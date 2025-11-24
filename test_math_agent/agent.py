from google.adk.agents import Agent

def add(a: float, b: float) -> float:
    """
    숫자를 더하여 합계를 반환합니다.

    매개변수:
        a (float): 첫 번째 피연산자.
        b (float): 두 번째 피연산자.

    반환값:
        float: a와 b의 합.

    예시:
        >>> add(1.5, 2.5)
        4.0
    """
    """두 숫자의 합을 반환합니다."""
    return a + b

root_agent = Agent(
    name="test_math_agent",
    model="gemini-2.5-flash",
    instruction="사용자의 간단한 수학 계산 요청을 처리하세요. 덧셈만 지원합니다.",
    tools=[add],
)