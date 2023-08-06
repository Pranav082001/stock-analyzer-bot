# Stock Analyzer Bot 
An AI Bot that can help you with stock investment by analyzing all the real-time as well as historic stock-related information with the help of LLM

# Motivation

As a retail investor, if you don't have a finance background or the capability to understand all the complicated financial terms makes the stock analysis process really time-consuming. Every time I end up watching some fin-YouTuber's video or some random blog on the internet to avoid manually dealing with all this stuff. This is where thought of making a Langchian and LLM-based bot that can take real-time as well as historic data to make investment analysis 

# How to run 
All the code and experimentation can be found in <code>stock_analyzer_bot.ipynb</code> notebook. 
You need to add openai_api_key in the initial code cell

# Experimentation
Have defined a couple of tools/functions for the agent which scraps and gather real time information related to the input stock. It includes following- 
1. Historic Stock price data. (You can take 1month, 1 year data depending on you models context length)
2. Company's financial statement  
3. Latest company related news  
All these factors seems sufficient for the analysis, it captures historical performance as well as real time market sentiment. If you want further more tools can be added. 

#### Approach 1- Using langchain ReAct agent
- The response and action agent did not turn out to be that good. Sometimes the results were below average
- Zero shot React agent dynamically thinks about the query in runtime and tries to perform action based on the thought
- The agent used to get stuck in infinite loop of thoughts and actions as it was not able to think with that kind of expected level for complicated task like stock analysis
- This approach may work or may not, Further improvements can be made by modifying the prompt

#### Approach 2- Predefine prompt with function calls

- Open ai has introduced function call a month ago, which is really helpful with which we can get structured output as we want in json format from LLM
-In this method stock ticker is extracted with the help of function calls. As most of the future code was dependet on this single argument
-And in the later stages stock data, news, financial statements are simply fetched by inputting ticker symbol
-It is recommended to use this approach for robust and stable analysis

 # Further improvemetns and addition to be done
a) Streamlit Demo \
b) More robust prompting for stable output \
c) Support of other opensource LLMS \
d) Note- Its a fun hobby project, Feel free to add any suggestions/ moodification

