Project Overview: Flame-War LLM-Based Mediation & Comparative Analysis

Anish Kuttetira and Kumar Chaudhary

This repository contains all the samples and LLM outputs for each section of the project, divided into subfolders.

Start by section number:

Dataset_v2 - The original, unaltered dataset that was provided at the start of the project

0 - Preparation

This folder contains Flattened_v2, which contains the input dataset flatenned by chronological order. It also contains the script flattener.py which was used to create Flattened_v2.

1 - llm_mediation

This folder contains step1_output, or the initial mediation outputs (judgement and steering) that were generated using the meta-llama Instruct model. It also contains the .ipynb notebook that was used to generate these mediations.

2 - llm_as_a_judge

This folder contains Output_s2, or the LLM scores for mediations that were generated using the Qwen model. It also contains the .ipynb notebook that was used to generate these scores.

3 - advanced_prompting

This folder contains few_shot, rubric, and multi_agent subfolders, each containing the .ipynb file used to create the judgements and the judgements themselves. They follow the different prompting strategies for each subfolder.

4 - user_simulation

This folder contains Output_s4, which contains the simulated user replies when mediation was inserted midway through a conversation. It also contains the .ipynb notebook that was used to generate this.

5 - comparative_analysis

This folder contains the data and outputs for comparative analysis, as well as the .ipynb notebook to replicate these results. It has .csv data provided, as well as output images and calculated/cleaned results.
