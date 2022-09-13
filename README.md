# scholarprofile-scraper
A simple tool to scrape google scholar profiles using beautifulsoup and requests

The output will be a .txt file with the name of the scholar with all publications listed in order of most to least recent. The publications will be listed with the information listed below (with example), a single-line blank will be between each publication.

**Title**: Designing Conversational Robots with Children during the Pandemic <br />
**Authors**: T Beelen, E Velner, R Ordelman, KP Truong, V Evers, T Huibers <br />
**Journal, Year**: arXiv preprint arXiv:2205.11300, 2022 <br />
**Year**: 2022

# main.py
**main.py** can be run directly with python

# ui.py
**scrapper.py** and **frames.py** is accessed by **ui2.0.py** allowing a simple user interface using tkinter and customtkinter

# Requiremenets
beautifulsoup4==4.11.1 <br />
customtkinter==4.5.10 <br />
lxml==4.9.1 <br />
requests==2.28.1 <br />
tk==0.1.0 <br />
auto-py-to-exe==2.22.0