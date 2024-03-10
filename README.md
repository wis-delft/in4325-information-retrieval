# IN4325: Information retrieval

This is the repository accompanying the [IN4325 (information retrieval) lecture (2023/2024)](https://studiegids.tudelft.nl/a101_displayCourse.do?course_id=64130) at TU Delft.

Here, we publish any hands-on material (i.e., Jupyter notebooks). The notebooks will be released alongside the lecture, so be sure to keep checking this repository every week!

Found a bug or an error in one of the notebooks? We're happy to accept pull requests!

What you'll find **here**:

- Project material (scaffolding project, final project)
- _Introduction to PyTerrier_ series

What you'll find **[on Brightspace](https://brightspace.tudelft.nl/d2l/home/596319)**:

- Slides
- Assignments
- Announcements
- Any other lecture-related material and discussions

## Content

| #   | File                                              | Title                    |                                                                                                                                                                                                                         |
| --- | ------------------------------------------------- | ------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 00  | `scaffolding/00-task.ipynb`                       | Scaffolding project      |                                                                                                                                                                                                                         |
| 01  | `intro-pyterrier/01-setup.ipynb`                  | Setup                    | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/wis-delft/in4325-information-retrieval/blob/main/intro-pyterrier/01-setup.ipynb)                  |
| 02  | `intro-pyterrier/02-indexing-retrieval.ipynb`     | Indexing & retrieval     | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/wis-delft/in4325-information-retrieval/blob/main/intro-pyterrier/02-indexing-retrieval.ipynb)     |
| 03  | `intro-pyterrier/03-datasets.ipynb`               | Datasets                 | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/wis-delft/in4325-information-retrieval/blob/main/intro-pyterrier/03-datasets.ipynb)               |
| 04  | `intro-pyterrier/04-evaluation-experiments.ipynb` | Evaluation & experiments | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/wis-delft/in4325-information-retrieval/blob/main/intro-pyterrier/04-evaluation-experiments.ipynb) |
| 05  | `intro-pyterrier/05-transformers.ipynb`           | Transformers             | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/wis-delft/in4325-information-retrieval/blob/main/intro-pyterrier/05-transformers.ipynb)           |
| 06  | `intro-pyterrier/06-learning_to_rank.ipynb`       | Learning to rank         | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/wis-delft/in4325-information-retrieval/blob/main/intro-pyterrier/06-learning_to_rank.ipynb)       |
| 07  | `intro-pyterrier/07-neural_models.ipynb`          | Neural ranking models    | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/wis-delft/in4325-information-retrieval/blob/main/intro-pyterrier/07-neural_models.ipynb)          |

## How to run the notebooks

We recommend running the notebooks **locally**. You'll need up-to-date versions of

- [Python](https://www.python.org/downloads/),
- [JDK](https://www.oracle.com/java/technologies/downloads/),
- a notebook viewer, such as [JupyterLab](https://jupyter.org/) or [Visual Studio Code](https://code.visualstudio.com/).

Alternatively, you can use **[Google Colab](https://colab.research.google.com/)** to run the notebooks in the cloud. However, this requires a Google account. **Note that Colab environments are not persistent, i.e., you'll have to download files you don't want to lose.**

## Troubleshooting

We'll collect common issues and respective solutions here.

### UnicodeDecodeError: 'charmap' codec can't decode [...]

This is an issue of `ir_datasets` which seems to happen on Windows only. [There is a fix already](https://github.com/allenai/ir_datasets/issues/208), but it hasn't been merged. A possible workaround is to set Python to use UTF-8 by default.

TL;DR: Set the enrivonment variable `PYTHONUTF8=1`.

#### Step-by-step guide

1. [Open the environment variable settings](img/pythonutf8_1.png).
2. [Create a new user environment variable](img/pythonutf8_2.png).
3. [Use `PYTHONUTF8` as variable name and `1` as value](img/pythonutf8_3.png).

**You have to restart Python (i.e., the notebook server) after this.**

Note that this setting may have unexpected effects on other Python scripts, so it's best to revert this after you're done with the notebooks.
