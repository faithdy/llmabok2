from google.adk.agents import Agent
MODEL = "gemini-2.0-flash"

# 초기 시놉시스 작성자: 사용자가 입력한 한 줄 로그라인에서 출발해 간결한 초기 시놉시스를 만든다.
initial_writer_agent = Agent(
    name="initial_writer_agent",
    model=MODEL,
    description="An agent that composes an initial synopsis from a single-line logline input.",
    output_key="synopsis",
    instruction=(
        "사용자가 제공한 1줄 로그라인(한 문장)을 받아, 한국어로 간결하고 명확한 초기 시놉시스를 작성하라. "
        "시놉시스는 3~6문장 내외로 구성하고, 반드시 다음을 포함하라: 주인공(또는 관점인물), 핵심 목표/갈등, 주요 전개(중요한 전환점), 예상되는 결말 또는 후속 방향. "
        "톤은 대중적이고 매력적으로 유지하되, 과도한 세부 묘사 대신 아이디어의 신선함과 매력을 우선시하라."
    ),
)

critic_agent = Agent(
    name="critic_agent",
    model=MODEL,
    description="An agent that critiques a short synopsis and gives concrete, prioritized suggestions for improvement.",
    output_key="critique",
    instruction=(
        "다음 입력값 {synopsis}를 비평하라. 비평은 구체적이고 건설적이어야 하며, 반드시 아래 형식을 따르라.\n"
        "1) 한 문장 요약: 시놉시스의 핵심 아이디어를 1문장으로 정리\n"
        "2) 항목별 점수(1-10) 및 한 줄 코멘트: 각 항목에 대해 1-10 점수와 한 줄 설명을 적어라:\n"
        "   - 대중성(대중에게 어필할 가능성)\n"
        "   - 매력(캐릭터/후킹 요소의 끌림)\n"
        "   - 아이디어(신선함/재미/독창성)\n"
        "   - 적시성(시기적·문화적 적합성)\n"
        "3) 강점(최대 3개): 무엇이 잘 작동하는지 구체 근거와 함께\n"
        "4) 약점(최대 3개): 중요한 문제와 이유(예: 아이디어 부족, 모티브 불명확, 페이싱 문제 등)\n"
        "5) 우선순위가 매겨진 구체적 개선안: 각 약점에 대해 실행 가능한 수정 제안(문장 대체 예시 포함 가능), 우선순위를 명시할 것\n"
        "6) 최종 평가(1-10) 및 한 줄 권고: 개선의 핵심 포인트 한 줄로 정리\n"
        "응답은 간결하게 항목별로 명확히 구분해서 작성하되, 시놉시스 원문을 불필요하게 다시 쓰지 말고 핵심 개선점을 중심으로 제시하라."
    ),
)

reviser_agent = Agent(
    name="reviser_agent",
    model=MODEL,
    description="An agent that revises the synopsis based on the critic's prioritized feedback.",
    output_key="synopsis",
    instruction=(
        "state의 {synopsis}와 {critique}를 참고하여, 비평에서 우선순위로 지적된 약점들을 반영해 개선된 시놉시스를 작성하라. "
        "수정 시 원작(초기 시놉시스)의 핵심 아이디어는 유지하되, 대중성·매력·아이디어·적시성 관점에서 구체적으로 보완하라. "
        "각 변경사항 옆에 간단한 한 문장 주석(# 수정 이유: ...)으로 어떤 문제가 해결되었는지 표기하고, 변경된 문장 또는 새로 추가된 문장은 '<<추가/수정>>' 같은 표식으로 표시하라. "
        "최종 출력은 통합된 완성본 시놉시스이어야 하며, 가능한 한 간결하고 상업적·창작적으로 매력적인 표현을 우선적으로 반영하라."
    ),
)

