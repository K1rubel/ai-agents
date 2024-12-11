import os, pathlib

from pathlib import Path
from autogen import ConversableAgent, GroupChat, GroupChatManager
from autogen.coding import DockerCommandLineCodeExecutor
import autogen

config_list = autogen.config_list_from_json(
   "config.json"
)
llm_config =  {"config_list" : config_list,  "timeout": 120}
user_proxy = autogen.UserProxyAgent(
    name="User",
    human_input_mode="TERMINATE",
    function_map=None,

)
coder_agent_system_message = '''
You are a Python programmer tasked with solving problems using Python programming.

Focus on producing syntactically correct code. It's alright if there are a few mistakes.

Avoid detailed explanations. Brief comments within the code will suffice.

Do not include example execution of the code.

If the Reviewer Agent provides feedback, make the necessary adjustments accordingly.
'''
coder_agent = ConversableAgent(
    name="Coder Agent",
    system_message=coder_agent_system_message,
    llm_config=llm_config,
)
reviewer_agent_system_message = '''
You are a highly skilled Python program debugger. Your task is to review the code written by the Coder Agent.

Do not print out the original or corrected code. Use your comments to guide the coder in improving the code.

If no code is produced by the Coder Agent, instruct it to write the code using Python.

If the code meets the requirements of the specific task, reply with 'Code Approved' and instruct the Executor to execute the code with arguments of its choice and print the result.
'''
reviewer_agent = ConversableAgent(
    name="Review Agent",
    system_message=reviewer_agent_system_message,
    llm_config=llm_config,
)

# Executor

work_dir = Path("coding")
work_dir.mkdir(exist_ok=True)
executor = DockerCommandLineCodeExecutor(work_dir=work_dir)

executor_agent_system_message = '''
Execute the code approved by the reviewer and print out the result using a sample argument.

Important: Print out the sample argument and the result.
'''
executor_agent = ConversableAgent(
    name="Executor",
    system_message=executor_agent_system_message,
    # description=coder_system_message,
    llm_config=llm_config,
    code_execution_config={"executor": executor},
    human_input_mode="NEVER",
)


group_chat = GroupChat(
    agents=[user_proxy ,coder_agent, reviewer_agent, executor_agent],
    messages=[],
    send_introductions=True,
    max_round=6,
)

group_chat_manager = GroupChatManager(
    groupchat=group_chat,
    llm_config=llm_config,
)

chat_result = user_proxy.initiate_chat(
    group_chat_manager,
    message="Write a python code that calculates the factorial of a number.",
    summary_method="reflection_with_llm",
)