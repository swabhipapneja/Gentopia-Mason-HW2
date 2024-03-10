# Gentopia-Mason-HW-G01441441

**IMPORTANT NOTICE: This code repository was adapted from [Gentopia.AI](https://github.com/Gentopia-AI) to support Mason Activities.** 

Author: Ziyu Yao (ziyuyao@gmu.edu)
Copyright and license should go to Gentopia.AI.

## Installation 💻
First, clone this repository:
```
git clone git@github.com:LittleYUYU/Gentopia-Mason.git
cd Gentopia-Mason
```
Next, we will create a virtual environment and install the library:
```
conda create --name gentenv python=3.10
conda activate gentenv
pip install -r requirements.txt
```

Most of the agent construction and execution activities will happen within `GentPool`. For the `gentopia` library to be used within `GentPool`, set up the global environment:
```
export PYTHONPATH="$PWD/Gentopia:$PYTHONPATH"
```
In addition, since we will be using OpenAI's API, we also need to create a `.env` file under `GentPool` and put the API Key inside. The key will be registered as environmental variables at run time.
```
cd GentPool
touch .env
echo "OPENAI_API_KEY=<your_openai_api_key>" >> .env
```
Now you are all set! Let's create your first Gentopia Agent.


## Quick Start: Clone a Vanilla LLM Agent
GentPool has provided multiple template LLM agents. To get started, we will clone the "vanilla agent" from `GentPool/gentpool/pool/vanilla_template` with the following command:
```
./clone_agent vanilla_template <your_agent_name> 
```
This command will initiate an agent template under `./GentPool/gentpool/pool/<your_agent_name>`. The agent configuration can be found in `./GentPool/gentpool/pool/<your_agent_name>/agent.yaml` (note the agent type `vanilla`). The vanilla prompt it uses can be found in the source code of `Gentopia`; see `./Gentopia/gentopia/prompt/vanilla.py`.

You can now run your agent via:
```
python assemble.py <your_agent_name>
```
This vanilla agent simply sends the received user query to the backend LLM and returns its output. Therefore, for many complicated tasks, such as those requiring accessing the latest materials, it will fail. 

## Implement a Scholar LLM Agent with Tool Augmentation
In the second trial, we will create a Scholar agent which is augmented with multiple functions to access Google Scholar in real time.

This is based on the `scholar` agent we have created in the pool. As before, in this demo we simply clone it:
```
./clone_agent scholar <your_agent_name> 
```
Like before, this command created an agent under `./GentPool/gentpool/pool/<your_agent_name>`. Note from its configuration that scholar is an `openai`-type agent. As stated in its [Gentopia's implementation](./Gentopia/gentopia/agent/openai), this type of agent allows for function calling:
> OpenAIFunctionChatAgent class inherited from BaseAgent. Implementing OpenAI function call api as agent.

The available functions to the scholar agent have been listed in its configuration file `./GentPool/gentpool/pool/<your_agent_name>/agent.yaml`, and the implementation of these tools can be found in Gentopia's source code (mostly coming from the [google_scholar.py](./Gentopia/gentopia/tools/google_scholar.py) file, in this example).

Now, you are all set to query this scholar agent for the latest papers by certain authors, the summary of a certain paper, paper citations, etc.


## Remove an Agent
Sometimes an agent can upset you. To wipe it out completely,
```
./delete_agent <your_agent_name> 
```

## PDF Reader
Make sure to install PyPDF2
pip install PyPDF2

sample prompts:
1. read a pdf article on global warming
2. read a pdf on global warming and summarize it

## Bonus Agent - Translation Tool
I built an agent that is a language translation tool. This tool will take input prompt that mentions a language it
has to be converted to. I used the HuggingFace Transformer Library to access a pretrained translation model. The
input prompt is tokenized and then processed by the translation model to result in the translated tokens.

Make sure transformers library is installed, otherwise use the following command:
pip install transformers

Here are few examples of prompts and the responses from the agent:
1. English to French
Prompt: we eat apples in french
my bonus agent: nous mangeons des pommes
2. English to Spanish
Prompt: translate how are you to Spanish
my bonus agent: I have translated ”how are you” to Spanish, which is ”¿C ́omo est ́as?”. If you have any
more translation requests or need assistance with anything else, feel free to let me know!
3. English to German
Prompt: translate see you tomorrow in german
my bonus agent: ”See you tomorrow” translated to German is ”Wir sehen uns morgen.”

## Student Name - Swabhi Papneja
## G No. - G01441441
## NetID - spapneja
