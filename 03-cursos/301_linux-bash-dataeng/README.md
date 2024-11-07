# Course Plan: Linux and Bash for Data Engineering

**Course Overview:** This course provides a comprehensive foundation in Linux and Bash, equipping learners with the skills needed to build data engineering solutions. Through hands-on labs, readings, videos, and assignments, students will develop technical expertise in Linux and Bash commands, file management, shell scripting, and configuration, preparing them for real-world data engineering challenges.

**Course Goals:**
Develop proficiency in Linux and Bash to solve data engineering tasks.
Understand and apply shell scripting to automate processes.
Explore file management, data processing, and text manipulation in a Linux environment.
Gain hands-on experience with tools like SSH, Git, and command-line utilities.
Course Structure:
The course is organized into four modules, each building on the last to deepen learners' understanding of Linux and Bash. Each module includes video lectures, readings, hands-on labs, quizzes, and assignments to reinforce learning outcomes.

## Module 1: Using Linux
Objective: Gain familiarity with the Linux environment and explore core commands, tools, and configurations that are essential for data engineering.

**Topics Covered:**

Introduction to Linux and the Shell Environment
Accessing Linux Systems and Shell Environments
Working with GitHub Codespaces
Basic Linux Commands (e.g., ls, cd, cp, mv, rm)
Shell Piping (| and >)
Introduction to SSH for remote connectivity

**Topics Covered:**

Videos: Overview of Linux concepts, shell commands, SSH
Readings: Key terms, secure connection setup, CodeWhisperer CLI
Assignments: Quizzes on basic Linux usage, shell piping, and SSH
Labs: Practice common commands, shell piping, creating SSH keys, and using shell pipelines.
Total Time Commitment: ~18 hours

## Module 2: Using Bash
Objective: Master the Bash shell to configure development environments and control standard input and output streams for data processing.

**Topics Covered:**

Bash Shell Configuration (e.g., .bashrc, .zshrc)
Shell Variables and Environmental Configuration
Standard Streams (stdin, stdout, stderr)
Manipulating shell environment variables in interactive and scripting modes

**Topics Covered:**

Videos: Configuring the shell environment, understanding variables and streams
Readings: Key terms, reflections on shell configuration and variable management
Assignments: Quizzes on shell configuration, variables, and streams
Labs: Practice configuring the shell, sourcing variables, and using streams in Bash scripts
Total Time Commitment: ~16 hours

## Module 3: Building Bash Scripts
Objective: Learn to write complex Bash scripts with logic and control flow to automate repetitive tasks and build command-line tools for data engineering.

**Topics Covered:**

Shell Logic and Control Flow (e.g., if, for, while statements)
Data Manipulation and Filtering in Bash
Command-Line Tool Creation in Bash
Introduction to Bash Functions, Makefiles, and Dockerfiles

**Learning Activities:**

Videos: Building Bash scripts, using loops and control flow, data manipulation
Readings: Key terms, script-building techniques, reflections
Assignments: Quizzes on control flow, data manipulation, and command-line tools
Labs: Writing loops in Bash, truncating data files, building a data-processing CLI, working with functions
Total Time Commitment: ~19 hours

## Module 4: Composing File and Data Solutions
Objective: Apply advanced Linux techniques to manage files, directories, permissions, and text-based data for data engineering solutions.

**Topics Covered:**

File and Directory Management (e.g., find, locate, chmod, chown)
Searching and Modifying Filesystem Content
Data Processing Commands (grep, cut, sort, uniq)
Text Manipulation with awk, sed, and regex

**Learning Activities:**

Videos: Filesystem searching, modifying files and permissions, text processing
Readings: Key terms, reflections on file management and text processing
Assignments: Quizzes on filesystem searches, permissions, and text processing
Labs: Search commands in Bash, practicing shell permissions, advanced text searching, and a final phrase-repeating challenge.
Total Time Commitment: ~19 hours

## Summary
The course introduces key concepts essential for Bash CLI proficiency, including the efficiency of command-line interface (CLI) use, scripting basics, configuration files, environment variables, and search tools. For data scientists, engineers, and machine learning practitioners, Bash provides a fast and efficient way to execute commands and automate tasks.

## Key Concepts

### 1. Bash CLI (Command Line Interface)

Bash CLI offers a direct, efficient path for executing commands, critical for data and machine learning engineers needing quick access to system resources.
Importance: It minimizes time to task completion, allowing direct execution of operations without the overhead of graphical interfaces.

### 2. Scripting Basics
Shebang Line: A special line in scripts (e.g., `#!/bin/bash`) that specifies the interpreter, ensuring that the correct programming language executes the code.
Example: `#!/usr/bin/env python3` would run the script in Python.
Chmod: This command (`chmod +x`) changes file permissions to make scripts executable.
Example: `chmod +x script.sh` allows the script to be run by typing `./script.sh`.

### 3. Configuration Files and Variables
`.bashrc` File: Runs every time a new terminal session is opened, allowing customization of the terminal environment with commands, aliases, and variable definitions.
Example: An alias (`alias mycmd='cd /project/dir && source env/bin/activate'`) can simplify repetitive tasks.
Environment Variables: Store sensitive information (e.g., API keys) in `.bashrc` to prevent accidental exposure in version control.
`.profile` File: Executes only upon login, suitable for initial setups that don’t need to run in every new session.

### 4. Search Utilities
`find`: Performs real-time, exhaustive searches by scanning the entire filesystem based on user-defined patterns.
Example: `find . -name "*.txt"` locates all .txt files in the current directory and subdirectories.
`locate`: Uses a pre-built index for faster, metadata-based searches, ideal for large filesystems where find would be slower.
Trade-off: `find` offers thorough searches; `locate` provides speed.

### Summary of Key Points
Efficiency: Bash CLI minimizes task completion time.
Customization: `.bashrc` and `.profile` enhance the terminal environment.
Search Flexibility: Use `find` for thoroughness and `locate` for speed.