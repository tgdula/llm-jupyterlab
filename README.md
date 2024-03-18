# Augmented DEV

This project simplifies usage and tests of different LLM models for code understanding and developer aid.

Different models are covered in dedicated Jupyter notebooks:
* `augmented-dev_v2-ollama.ipynb` - local models, using [Ollama](https://ollama.com/)
* `augmented-dev_v3-azure-openai.ipynb` - Azure OpenAI models
* `augmented-dev_v4-vertex-ai.ipynb` - Vertex AI models


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