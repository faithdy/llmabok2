from google.adk.agents import SequentialAgent
from .lambda_agent import LambdaAgent
from .while_agent import WhileAgent
from .json_input_agent import JsonInputAgent

root_agent = LambdaAgent(
    name="increase_agent",
    func=lambda x: x + 1,
    input_keys=["number"],
    output_key="number",
)

root_agent = JsonInputAgent(
    name="json_input_agent",
)

# # #

# json_input_agent = JsonInputAgent(
#     name="json_input_agent",
# )

# increase_agent = LambdaAgent(
#     name="increase_agent",
#     func=lambda x: x + 1,
#     input_keys=["number"],
#     output_key="number",
# )

# square_agent = LambdaAgent(
#     name="square_agent",
#     func=lambda x: x * x,
#     input_keys=["number"],
#     output_key="number",
# )

# root_agent = SequentialAgent(
#     name="calc_agent",
#     sub_agents=[json_input_agent, increase_agent, square_agent],
# )


# # #

# increase_agent = LambdaAgent(
#     name="increase_agent",
#     func=lambda x: x + 1,
#     input_keys=["number"],
#     output_key="number",
# )

# square_agent = LambdaAgent(
#     name="square_agent",
#     func=lambda x: x * x,
#     input_keys=["number"],
#     output_key="number",
# )

# root_agent = WhileAgent(
#     name="while_agent",
#     condition="number < 100",
#     sub_agents=[increase_agent, square_agent],
# )

# # #

def fibonacci(f: list[int]) -> list[int]:
    if f is None: f = [0, 1]
    f.append(f[-1] + f[-2])
    return f

json_input_agent = JsonInputAgent(
    name="json_input_agent",
)

fibonacci_while_agent = WhileAgent(
    name="fibonacci_agent",
    condition="len(fib) <= 10",
    sub_agents=[
        LambdaAgent(
            name="fibonacci_step_agent",
            func=fibonacci,
            input_keys=["fib"],
            output_key="fib",
        )
    ],
)

final_output_agent = LambdaAgent(
    name="final_output_agent",
    func=lambda f: f[-1],
    input_keys=["fib"],
    output_key="final_fib",
)

root_agent = SequentialAgent(
    name="fibonacci_workflow_agent",
    sub_agents=[json_input_agent, fibonacci_while_agent, final_output_agent],
)