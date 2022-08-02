[![build](https://github.com/SarnadAbhilash/textsummary-github-actions/actions/workflows/actions.yml/badge.svg)](https://github.com/SarnadAbhilash/textsummary-github-actions/actions/workflows/actions.yml)
# Text summarizer
This is a CLI tool that generates a summary for any article using pre trained transformer models from Hugging face.

## Overview
1. Supply the tool with the article required to be summarized using the command line
2. Load the model and the tokenizer
3. Generate summary

## Getting started
Create a virtual environment.

`python3 -m venv venv`

Activate the virtual environment
`source venv/bin/activate`

Then run the make file
`make all`

## Usage
To generate a summary, Add the contents of an article in the article.txt file and then run the follwing command

`python main.py <<path to article.txt>>`