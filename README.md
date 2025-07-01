# Pokémon Stats Visualizer 🐉📊

![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python&style=flat-square)
![GitHub Repo Size](https://img.shields.io/github/repo-size/yourusername/yourrepo?style=flat-square)
![License: Unlicense](https://img.shields.io/badge/License-Unlicense-blue?style=flat-square)
![Lines of Code](https://img.shields.io/tokei/lines/github/yourusername/yourrepo?style=flat-square)
![Last Commit](https://img.shields.io/github/last-commit/yourusername/yourrepo?style=flat-square)

---

## What’s This?

A simple Python script that fetches Pokémon data from a public CSV, lets you filter Pokémon by type, and then plot two stats against each other for a cool visual comparison.

---

## Features

- Loads Pokémon stats data from a live CSV  
- Filters Pokémon by their **Type1** (e.g., Fire, Water, Grass)  
- Allows you to pick any two stats (Attack, Defense, HP, etc.) to compare visually  
- Displays a scatter plot with matplotlib  
- Fun ASCII art easter egg when you type **"I"** (must be uppercase!)  
- Clears terminal for cleaner UX

---

## How to Use

1. Clone or download the repo  
2. Make sure you have Python 3.x installed  
3. Install dependencies:

```bash
pip install matplotlib pandas
