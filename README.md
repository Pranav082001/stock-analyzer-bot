# Stock Analyzer Bot 
An AI Bot that can help you with stock investment by analyzing all the real-time as well as historic stock-related information with the help of LLM

# Motivation

As a retail investor, if you don't have a finance background or the capability to understand all the complicated financial terms, makes the stock analysis process really time-consuming. Every time I end up watching some fin-YouTuber's video or some random blog on the internet to avoid manually dealing with all this stuff. This is where i thought of making a Langchian and LLM-based bot that can take real-time as well as historic data to make investment analysis 
<!--
# How to run 
All the code and experimentation can be found in <code>stock_analyzer_bot.ipynb</code> notebook. 
You need to add openai_api_key in the initial code cell
+-->
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
- In this method stock ticker is extracted with the help of function calls. As most of the future code was dependet on this single argument
- And in the later stages stock data, news, financial statements are simply fetched by inputting ticker symbol. Further analyzed by openai llm
- It is recommended to use this approach for robust and stable analysis

# Example - 
Input- \
```Anazlyze_stock("Is it a good time to invest in Yes Bank?") ```

Output- 

```
'Query': 'Is it a good time to invest in Yes Bank?', 'Company_name': 'Yes Bank', 'Ticker': 'YESBANK'
Analyzing.....
Investment Thesis for Yes Bank:
1. Financial Performance: Yes Bank has shown improvement in its financials over the past three years. The net debt has increased, indicating higher borrowing, but the tangible book value and common stock equity have also increased, suggesting a stronger financial position.
2. Total Capitalization: The total capitalization of Yes Bank has been consistently increasing, indicating a growing investor base and potential for future growth. This can be seen as a positive sign for investors considering investing in the bank.
3. Total Assets: Yes Bank's total assets have also been increasing steadily, indicating the bank's ability to attract and manage a larger pool of assets. This growth in assets can contribute to the bank's profitability and potential for future expansion.
4. Stock News: Recent news about Yes Bank suggests that the stock has seen a marginal increase in price and has been holding steady. This stability in the stock price can be seen as a positive sign for investors, indicating a potential for future growth.
5. Weak Underlying Business: However, it is important to note that there are concerns about the bank's weak underlying business, as indicated by the soft quarter expected in Q1. This may lead to a decline in profitability, which could impact the stock price in the short term.
6. Overall Market Conditions: It is also important to consider the overall market conditions and the banking sector as a whole before making an investment decision. Factors such as economic conditions, regulatory changes, and competition can significantly impact the performance of Yes Bank and its stock price.
Based on the available data and information, it can be concluded that investing in Yes Bank at this time carries both positive and negative factors. The positive factors include the bank's improving financials, increasing total capitalization, and steady stock price. However, the concerns about the weak underlying business and potential decline in profitability should also be taken into consideration. Therefore, investors should carefully evaluate their risk tolerance and conduct further research and analysis before making an investment decision in Yes Bank.
```


 # Further improvemetns and addition to be done
a) Streamlit Demo \
b) More tools can be added. Fo eg. math tool to perform complex technical analysis \
b) More robust prompting for stable output \
c) Support of other opensource LLMS \
d) Note- Its a fun hobby project, Feel free to add any suggestions/ moodification

