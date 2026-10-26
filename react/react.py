max_iterations = 10
iteration = 0
while true(iteration <= max_iterations):
    iteration += 1
    from openai import OpenAI
    openai_client = OpenAI(
        api_key=,
        base_url=
    )
    