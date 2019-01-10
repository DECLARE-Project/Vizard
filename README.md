# Vizard

An automated guide for the configuration and execution of performance analysis.

Running examples can be found on the following pages:
- Specifying performance concerns and generating experiments for JMeter and Locust ([link](http://declare-project.github.io/Vizard/Definition))
- Report generation (and concern refinement, if possible) ([link](http://declare-project.github.io/Vizard/Report))


### What does this tool do?

The idea behind Vizard is to simplify the configuration of analysis tools and the extraction of these results.
In the first step, Vizard guides you through the creation of a user concern.
A user concern can express an interest in a metric of a software system.
This is done in a human language to keep the tool as simple as possible. 
The user concern also servers as the domain model to abstract the technical details from the user. 

In the second step, the tool creates a declarative performance report from the previously generated analysis result.
This report contains graphs and annotation that explain the data.

### Who should use this tool?

Users from any background can use this tool. 
It is useful to have a background in computer science to understand the scope of the project but not necessary.
Experts, as well as inexperienced users in performance analysis have the possibility to express their concerns.
More complex configuration steps are hidden behind a expert mode, which can be activated by the user.

### How can I use this tool?

First you have to [create user concern](http://declare-project.github.io/Vizard/Definition). 
Follow the instructions of the tool and state your interest in a software system.

When you don't have the environment to perform an analysis experiment yourself you can 
skip the last instruction of the analysis and jump directly to the [report generation](http://declare-project.github.io/Vizard/Report).
The report tool provides previously performed analysis experiments with typical user concerns and analysis data.

### Supported Analysis Tools

Vizard currently supports the following analysis tools:

- JMeter
- Locust

### Screenshots

<p align="center">

**Welcome Page**

<img alt="User Concern Definition Welcome" src="https://github.com/DECLARE-Project/Vizard/blob/master/docs/images/def_1.png" width="400px"/>


**Query Definition**

<img alt="User Concern Definition Query" src="https://github.com/DECLARE-Project/Vizard/blob/master/docs/images/def_2.png" width="400px"/>


**Report Summary**

<img alt="User Concern Report Overview" src="https://github.com/DECLARE-Project/Vizard/blob/master/docs/images/rep_1.png" width="400px"/>


**Report Section with Graph**

<img alt="User Concern Report Graph" src="https://github.com/DECLARE-Project/Vizard/blob/master/docs/images/rep_2.png" width="400px"/>
</p>