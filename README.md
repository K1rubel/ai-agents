# ai-agents
== part of the weekly interns' training at iCogLabs-Ethiopia.
## Requirements --
⚠️  Before running the collaborative-code-execution.py file Docker must be installed and running with python3-slim docker image.
📒  Docker is used for the safety of running code that potentially could cause system instability if run using local command line tools.
## Task Description
Use a code execution agent to run a code in autogen's collaborative setting. I have implemented a group chat feature using atuogens GroupChat method that takes, as parameters, a host of agents that specialize on specific tasks.
### Agents
  -- user_proxy -- initiates the chat in the group
  -- coder_agent -- attempts to convert user requests into python programs
  -- reviewer_agent -- reviews the code output of the coder and suggests improvements for the coder to make amendments. Also, the reviewer tracks the output of the executor and communicates the things that need to be improved in the output.
  -- code executor -- upon approval of the coder's output by the reviewer, the executor runs the code and prints the execution result.
### Files
  -- config.json -- configuration file for the llm_config parameter of the agents used in the group chat
  -- collaborative-code-execution.py main file containing implementation of the collaborative code execution using autogens ai agents.
-- chat.txt -- file containing a copy of a run of the code 
  
