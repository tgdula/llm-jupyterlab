# Augmented DEV

Introducing "Augmented Developer" – the ultimate tool for software developers to enhance their coding prowess. By harnessing advanced AI, it comprehends your project's source code and architecture, instantly offering invaluable insights and answers to your queries and streamlining code reviews. Need to extend your codebase? No problem. "Augmented Developer" will generate code, including tests, seamlessly integrating with your existing project.

While still in its nascent stage, it's been exciting to offer a glimpse into its potential through a set of Jupyter notebooks. These notebooks leverage a variety of cutting-edge Language Model (LLM) technologies integrated with the Retrieval Augmented Generation approach via the Langchain framework.

Currently, the project supports an array of LLM models tailored for code understanding and generation:
* local [Ollama](https://ollama.com/) models, such as `codellama` - see [augmented-dev_v2-ollama.ipynb](notebooks/augmented-dev_v2-ollama.ipynb)
* Azure OpenAI models, such as as `GPT-3.5-turbo` and `GPT-4` - see [augmented-dev_v3-azure-openai.ipynb](notebooks/augmented-dev_v3-azure-openai.ipynb)
* Vertex AI models, such as `code-bison` and `codechat-bison` - see [augmented-dev_v4-vertex-ai.ipynb](notebooks/augmented-dev_v4-vertex-ai.ipynb)

Through these notebooks, developers can explore firsthand how "Augmented Developer" harnesses the power of these LLM models to delve into selected source code, offering insights and even generating code snippets. While our project is in its infancy, these notebooks serve as a promising glimpse into its potential to revolutionize the way developers approach coding tasks.

![Augmented developer (source:ideogram.ai)](resources/images/augmented-dev-001-ideogram.ai.png "Augmented developer (source:ideogram.ai)")


## Installation

setup new conda environment
```bash
conda env create --file environment.yml
```

```bash
conda activate augmented-dev
```


## Requirements

Notebooks in order to run, require 
* certain environment settings / environment variables, such as
  * `OPENAI_API_BASE` and `OPENAI_API_KEY` for Azure notebook
  * `GOOGLE_APPLICATION_CREDENTIALS` for Vertex AI  
  Please refer to the specific notebooks for details
* access to codebase that will be analysed. Paths can be provided in notebooks.



## Launching jupyter notebooks:

```bash
jupyter lab
```

## Special thanks to

The interactive jupyter notebook extension originates from: https://github.com/darinkist/MediumArticle_InteractiveChatGPTSessionsInJupyterNotebook
Many thanks to [darinkist](https://github.com/darinkist) for sharing this 🙏