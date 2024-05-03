import streamlit as st
import pandas as pd
import plotly.express as px
import pyarrow.parquet as pq


# Data loading and caching
@st.cache
def load_data():
    data = pd.read_parquet('final_data.parquet')
    data['Date'] = pd.to_datetime(data['Date'])
    return data


# Main page function
def main_page():
    st.title('Financial Analysis Project')
    st.markdown("""
    ## Name: Hanqing (Peter) Zhao

    ## How to use this webapp:

    Interactivity:

    - This webapp has four pages, and can be navigated to by clicking under Navigation on the left.
        - Main Page(default): Display the project name, student name, explanation and analysis for plots and charts, and 
        conclusion.
        - Project Reflections: Display additional questions from 4-8 with answers. 
        - Data Sources: Descriptions of all data sources used by this webapp, with url and apis respectively. Additionally, 
        a paragraph describing the final parquet file is included as well. 
        - Interactive Data / Analysis / Charts: This page has three tabs on the top, allowing user to navigate to interactive
         data plots, project analysis, and charts. The interactive data tab allow user to utilize the sidebar on the left
         to select data that they are interested in. The analysis tab has the research plan, methods, and results of the 
         project. And finally, the charts tab shows additional line graph and scatter plots to visualize the data.""")
    st.markdown("""----------------------------------------------------------------------------------------------------
    """)

    st.markdown("""  
    Plots & Charts(Brief):
    - Gold Price vs SP500 Price: 
        - The line graph provides illustration of the price trends of Gold and the S&P 500 over approximately two decades, starting from around 2001 up to 2019.
    - SP500 Price vs 10 Year Treasury Note:
        - The scatter plot displaying the relationship between the S&P 500 Price and the 10-Year 
        Treasury Note Yield reveals distinct clusters indicating varying economic conditions.
    - SP500 Price vs Gold Price
        - The scatter plot illustrating the relationship between the S&P 500 Price and Gold Price shows 
        a varied pattern without a straightforward linear correlation.
    - Gold Price vs 10 Year T Note
        - The scatter plot comparing Gold Price and the 10-Year Treasury Note Yield showcases an inverse 
        relationship, highlighted by clusters that suggest varying economic conditions.""")

    st.markdown("""----------------------------------------------------------------------------------------------------
    """)

    st.markdown("""
    Conclusion:

    In the long term, the three data series appear to operate independently of one another. This independence implies 
    that any shocks affecting one of the variables are unlikely to have a permanent or proportional impact on the 
    others over an extended period. Sad :(


    <<<< Full plots/charts, analysis and conclusions are on the last page, note the last page have three tabs at the top! 

    """)

    st.markdown("""----------------------------------------------------------------------------------------------------
    """)

    st.markdown("""

    ## Major “gotchas”
    - The last page have three tabs, but sometimes you have to scroll up to see them. 
    - On the Interactive Data / Analysis / Charts page, only one graph can be displayed at a time. This limitation is largely due to 
    webpage size constrains, better results may be achieved if two plots can be displayed together side by side to help
    comparison. 
    - It is hard to have accurate control over the font size, some texts are not the most convenient for reading. 
    - My ability in using streamlit limits the amount of complex functions that could be achieved on interactive data page.
    For example, it is almost impossible to achieve real time calculation of desired econometric indicators and graph them
    if not stored previously. 
    """)


# Additional questions
def qa_page():
    st.title('Project Reflections')
    st.markdown("""
    4. What did you set out to study?

        My milestone 1 was about finding the relationship between pollution and climate change, however, 
        two of the datasource were down for maintenance. Therefore I started this new project, and in this project, 
        I set out to explore the interrelationships 
        between three critical financial indicators: the S&P 500 Price, Gold Price, and the 10-Year Treasury Note Yield. 
        The aim was to identify and analyze potential correlation and causation patterns among these variables to 
        understand how they influence each other across different economic conditions. Through statistical analysis and 
        visual data exploration, the project seeks to uncover insights into how these financial metrics interact.""")
    st.markdown("""----------------------------------------------------------------------------------------------------
    """)

    st.markdown("""    5. What did you Discover/what were your conclusions?

        Throughout this project, I discovered significant insights into the relationships between the S&P 500 Price, 
        Gold Price, and the 10-Year Treasury Note Yield. The correlation tests, such as Spearman and Kendall's rank, 
        revealed that while there is a positive correlation between the S&P 500 and Gold Prices, both tend to show a 
        negative correlation with the 10-Year Treasury Note Yield. This suggests that during periods of economic 
        uncertainty, investors may favor gold and shy away from the stock market, which often correlates with a rise in 
        bond yields. Additionally, the Johansen Cointegration Test indicated no long-term equilibrium relationship among 
        these variables, suggesting that they may react independently to different economic pressures over time. My 
        conclusion is that while these financial indicators often move in response to similar economic events, 
        their long-term behaviors remain largely independent, driven by distinct market forces and investor behaviors.""")
    st.markdown("""----------------------------------------------------------------------------------------------------
    """)

    st.markdown("""   6. What difficulties did you have in completing the project?

        Two parts of the project appears to be very challenging. The first being the statistical analysis, I am not the most
        familiar with quite a few tests and therefore had to learn how and when to use them from square 1. Another challenge
        turns out to be building the webapp. I enjoyed the process of building the webapp piece by piece, however, 
        this joyfulness was soon shattered by countless errors and warnings. This is by far the most complicated project 
        I have every done in the program, since one have to utilize basically everything we've learned in class. 
        The results are worth it though :)
    """)
    st.markdown("""----------------------------------------------------------------------------------------------------
    """)

    st.markdown(""" 7. What skills did you wish you had while you were doing the project?

    First of all I wish I am better at python, which would save me tons of trouble debugging or understanding different
    warnings and how to fix them. Secondly, I wish I know how to code html, which would allow me to scrape from a lot 
    more web pages which were all too hard to scrape right now. Lastly, I wish I have better time management. 
    """)
    st.markdown("""----------------------------------------------------------------------------------------------------
    """)

    st.markdown(""" 8. What would you do "next" to expand or augment the project?

    After successfully running tests on timeseries data, I'm looking forward to expanding the dataset with additional 
    financial data. By doing so, I aim to uncover correlations or significant cause-and-effect relationships between 
    various variables. Moreover, enriching the dataset with data from different perspectives will enable us to explore 
    more interesting functions on the interactive data page.
""")

    st.markdown("""----------------------------------------------------------------------------------------------------
    """)


# Data Source Page
def data_source_page():
    st.title('Data Sources')
    st.markdown("""
    ## Overview of Data Sources
    This project utilizes two types of data sources, one is scrape-able data from web page, and second is API accessed data:

    **1. Source One(Scrape-able):**

    URL: https://sdbullion.com/gold-prices-{} (substitute {} for desired year)

    This website recoded daily gold price from 1968 to 2023, which provides the daily gold price for my analysis. The website only have monthly prices for earlier years,
    therefore I picked 2001 to 2019 which all have recorded daily prices. However, the format of the datetime varied
    from year to year, which added difficulty to scraping. 

    **2. Source Two(Public API):**

    API: https://www.alphavantage.co/query

    Alphavantage api provided free access for most financial market data, and I used it to acquire data for SP500 from 2001 
    to 2019.

    **3. Source Three:**

    Yahoo Finance via yfinance

    Yahoo Finance also provides financial data, therefore I used yfinance package in Pycharm to acquire data for 10 Year T-note
    yield from 2001 to 2019. 


    **Final data file: final_data.parquet**

    This dataset encompasses a comprehensive collection of financial metrics spanning from 2001 to 2019, 
    specifically focusing on gold prices, S&P 500 index values, and 10-year Treasury note yields. 
    The gold price data were meticulously gathered through web scraping techniques, 
    while the S&P 500 data were sourced via the AlphaVantage API, and the data for 10-year 
    Treasury note yields were obtained from yfinance. This diverse dataset was initially consolidated 
    into a CSV file and subsequently converted into a Parquet file format to enhance data handling 
    and performance for analysis purposes. The transformation to Parquet ensures efficient storage and faster processing, 
    facilitating more effective data manipulation and analysis in this study.

    """)
    # Checkbox to control data display
    show_all_data = st.checkbox("Show entire data")
    data1 = pq.read_table('final_data.parquet')

    if show_all_data:
        # Display all data in a dataframe using st.dataframe
        st.dataframe(data1.to_pandas())


def app_page():
    # set up three tabs
    # Create a sidebar radio button to select the tab
    selected_tab = st.sidebar.radio("Select Tab", ["Interactive Data", "Analysis", "Charts"])

    if selected_tab == "Interactive Data":
        st.title('Interactive Data')
        data = load_data()
        # set up date for selection
        min_date = data['Date'].min().date()
        max_date = data['Date'].max().date()

        # User selection for commodity
        commodity = st.sidebar.selectbox(
            'Select Commodity',
            ['Gold', 'SP500', '10 Year T Note']
        )

        # User selection for metric type (Price or Return)
        metric_type = st.sidebar.radio("Select Metric Type", ['Price(Yield)', 'Return'])

        # Construct the column name
        if metric_type == 'Return':
            selected_column = f"{commodity} Daily Return"
        else:
            if commodity == '10 Year T Note':
                selected_column = f"{commodity} Yield"
            else:
                selected_column = f"{commodity} Price"

        # User selection for date range
        start_date, end_date = st.sidebar.date_input(
            "Select date range",
            value=[min_date, max_date],
            min_value=min_date,
            max_value=max_date
        )
        st.sidebar.caption("Please make sure to select two dates!")

        # fetch data
        start_date_dt = pd.to_datetime(start_date)
        end_date_dt = pd.to_datetime(end_date)
        filtered_data = data[(data['Date'] >= start_date_dt) & (data['Date'] <= end_date_dt)]

        # Displaying the selected graph
        fig = px.line(filtered_data, x='Date', y=selected_column, title=f'{selected_column} Trend')
        st.plotly_chart(fig)

    elif selected_tab == "Analysis":
        st.markdown(""" 
        ## Analysis

        The goal of this project is to investigate the relationships between S&P500 price, gold price, and 10 year Treasury note.

        Step 1: Use visual inspection or statistical tests to check whether the data series is normally distributed.

        Step 2: Chose correlation test or tests according to normality test results.

        Step 3: Explore potential cause-and-effect relationships between the three data series using Johansen Cointegration Test.

        Step 4: More visualization, draw conclusions about the relationship between the data series from statistical tests. 

        ## Test for Normal Distribution:

        Shapiro-Wilson test was performed on each of the three data series:

            - Gold Price Normality (p-value): 1.8130817924030501e-44
            - SP500 Price Normality (p-value): 5.0869134941937023e-51
            - 10 Year T Note Yield Normality (p-value): 5.148480265824883e-39

        All three data series have extremely low p-values(p-value < 0.05), in this case we can reject the null hypothesis 
        and conclude that all the data series are likely NOT normally distributed. There is no need to plot their 
        histograms since none will follow a symmetrical bell-shaped curve.  

        Next I will conduct non-parametric correlation test(Spearman & Kendall) to assess relationships between the
        variables.

        ## Test for Correlation:

            Spearman's Rank Correlation:

            - Gold Price - SP500 Price: 0.5957593873649222
            - Gold Price - 10 Year T Note Yield: -0.8320977905265164
            - SP500 Price - 10 Year T Note Yield: -0.5516454320480819

            Kendall's Rank Correlation:

            - Gold Price - SP500 Price: 0.4101357525652475
            - Gold Price - 10 Year T Note Yield: -0.6044831658236524
            - SP500 Price - 10 Year T Note Yield: -0.3289082028262134

        Both Spearman's rank (0.5958) and Kendall's rank (0.4101) coefficients are positive for the 
        Gold Price - SP500 Price pair. This indicates a positive monotonic relationship, when the gold price goes up, 
        there's a tendency for the SP500 price to also go up, and vice versa. 

        The coefficients for both Gold Price - 10 Year T Note Yield and SP500 Price - 10 Year T Note Yield are negative. 
        This suggests negative monotonic relationships.  Typically, when the yield of the 10-year Treasury note goes up, 
        it might indicate investors seeking less risky assets. This could lead to a decrease in the price of gold 
        (considered a safe haven asset) and potentially the stock market (reflected by the SP500).

        ## Cause and effect relationships:

            - Eigenvalues: [3.49608761e-03 1.11129871e-03 2.82452942e-05]
            - Trace Statistics: [22.12091955  5.43287361  0.13459073]
            - Critical Values (90%, 95%, 99%): 

                    [[27.0669 29.7961 35.4628]
                    [13.4294 15.4943 19.9349]
                    [ 2.7055  3.8415  6.6349]]

        From the Johansen cointegration test results, it appears that there is no evidence to reject the null hypothesis 
        at conventional significance levels for any number of cointegrating vectors. This suggests that there is no 
        cointegration among the S&P 500 Price, Gold Price, and 10 Year T Note Yield based on the data provided.

        This implies that the variables do not tend to move together in the long run or do not have any long-term 
        equilibrium relationship that consistently brings them back together. Each financial series may react 
        independently to changes in market conditions over the long term.

        ## Conclusion: 

        The investigation into the relationships between the S&P 500 Price, Gold Price, and the 10-Year Treasury Note 
        Yield has provided several insights through both correlation and causation analysis, albeit with findings 
        that reflect both short-term relationships and the absence of long-term equilibrium dynamics.

        Correlation Findings:
        The correlation tests indicated significant relationships among the variables:

        Gold Price and S&P 500 Price: There is a positive monotonic relationship suggesting that movements in the 
        stock market, as represented by the S&P 500, tend to be associated with similar movements in gold prices. 
        This relationship can be attributed to investor behavior, where both assets might be viewed as attractive 
        during certain economic conditions, such as during periods of market confidence or instability, influencing 
        their prices concurrently. Gold Price and 10-Year T Note Yield & S&P 500 Price and 10-Year T Note Yield: The 
        negative correlations suggest that as the yield on long-term U.S. government debt increases, 
        typically indicating rising interest rates or lower bond prices, both gold and S&P 500 prices tend to fall. 
        This could reflect a shift in investor preference towards safer, income-generating assets when yields are 
        higher, moving away from stocks and commodities like gold which do not offer a yield. Causation Analysis: The 
        Johansen cointegration test, aimed at uncovering any long-term equilibrium relationships that might pull 
        these series back into alignment over time, concluded with no evidence of such dynamics. The lack of 
        cointegration suggests that while these financial instruments may exhibit short-term correlations:

        Independent Long-term Behavior: In the long term, they appear to operate independently of one another. This 
        independence implies that any shocks affecting one of the variables are unlikely to have a permanent or 
        proportional impact on the others over an extended period.

        """)

    elif selected_tab == "Charts":
        st.title('Charts')

        image_path = "Time Series Plot of Gold and SP500 Price.png"
        st.image(image_path, width=None, caption="Gold Price vs SP500 Price")
        st.markdown("""The line graph provides illustration of the price trends of Gold and the S&P 500 over 
        approximately two decades, starting from around 2001 up to 2019. During certain periods such as the financial 
        crisis around 2008, gold and S&P 500 trends diverge, where gold prices rose as the S&P 500 fell sharply, 
        supporting gold's status as a safe-haven asset during market downturns. Post-2009, as the S&P 500 recovers 
        and grows, gold prices initially decline, indicating a shift back to riskier assets as market conditions 
        improve. Both asset classes show significant upward trends towards the latter part of the graph (post-2015), 
        possibly indicating broad economic factors influencing asset prices, such as monetary policy changes or 
        global economic conditions. """)
        st.markdown("""""")

        image_path = "scatterplotsp500vs10.png"
        st.image(image_path, width=None, caption="SP500 Price vs 10 Year Treasury Note")
        st.markdown("""The scatter plot displaying the relationship between the S&P 500 Price and the 10-Year 
        Treasury Note Yield reveals distinct clusters indicating varying economic conditions. No clear linear 
        relationship is evident across the entire dataset; however, within specific clusters, trends suggest that 
        higher S&P 500 prices often coincide with moderately increasing yields, likely reflecting periods of economic 
        growth where investors favor equities over bonds. Conversely, other clusters show lower stock prices 
        associated with higher yields, potentially indicating economic downturns where higher bond yields reflect a 
        shift towards safer investments. This pattern underscores the complex interplay between equity markets and 
        bond yields as indicators of investor sentiment and broader economic trends.""")
        st.markdown("""""")

        image_path = "scatterplotsp500vsg.png"
        st.image(image_path, width=None, caption="SP500 Price vs Gold Price")
        st.markdown("""The scatter plot illustrating the relationship between the S&P 500 Price and Gold Price shows 
        a varied pattern without a straightforward linear correlation. Notably, the data points form distinct 
        clusters, suggesting different phases of market behavior or economic conditions. For example, 
        there's a cluster where both gold and S&P 500 prices are lower, possibly reflecting times of economic 
        stability or low inflation expectations. Another prominent cluster occurs at higher gold prices irrespective 
        of moderate variations in S&P 500 prices, which might indicate periods when investors turn to gold as a safe 
        haven amid economic uncertainty or market volatility. This visualization highlights the complex and 
        occasionally inverse relationship between gold and equity markets, reflecting investor sentiment and broader 
        economic indicators during different periods.""")
        st.markdown("""""")

        image_path = "scatterplotgvs10.png"
        st.image(image_path, width=None, caption="Gold Price vs 10 Year T Note")
        st.markdown("""The scatter plot comparing Gold Price and the 10-Year Treasury Note Yield showcases an inverse 
        relationship, highlighted by clusters that suggest varying economic conditions. One notable cluster shows 
        lower gold prices coupled with higher yields, typically indicating strong economic growth and reduced demand 
        for gold as a safe haven. Conversely, another prominent cluster with higher gold prices and lower yields 
        suggests periods of economic uncertainty, where gold is favored as a safe investment and yields on safer 
        assets like Treasury notes decrease. Transition areas between these clusters reflect shifts in investor 
        sentiment or economic policy changes, illustrating the dynamic interplay between these two key financial 
        indicators.""")


# Sidebar navigation setup
def setup_navigation():
    st.sidebar.title("Navigation")
    # Default page
    if 'current_page' not in st.session_state:
        st.session_state.current_page = 'main_page'
    # Navigation buttons
    if st.sidebar.button("Main Page"):
        st.session_state.current_page = 'main_page'
    if st.sidebar.button("Project Reflections"):
        st.session_state.current_page = 'project_reflections_page'
    if st.sidebar.button("Data Sources"):
        st.session_state.current_page = 'data_sources_page'
    if st.sidebar.button("Interactive Data / Analysis / Charts"):
        st.session_state.current_page = 'app_page'

    # Page display based on current_page state
    pages = {
        'main_page': main_page,
        'project_reflections_page': qa_page,
        'data_sources_page': data_source_page,
        'app_page': app_page
    }
    pages[st.session_state.current_page]()


def main():
    setup_navigation()


if __name__ == '__main__':
    main()
