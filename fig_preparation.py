import plotly.express as px


def generate_figures(df):

    # ----------------------------------------------------
    csat_pie = px.pie(
        df.groupby(['satisfaction']).agg(csat=('ticket_number', 'count')).reset_index(),
        values='csat',
        names='satisfaction',
        hole=.3,
    )

    # horizontal bar with time progression of CSAT
    month_key = {5: 'May', 6: 'June', 7: 'July', 8: 'August'}

    df['month'] = df.ticketcreationdate.dt.month

    csat_month = df.groupby(['month'])['satisfaction'].value_counts(normalize=True).rename('proportion_tickets').mul(100).round().reset_index()

    csat_month['month'] = csat_month.month.map(month_key)

    monthly_bar = px.bar(
        csat_month,
        x="proportion_tickets", 
        y="month", 
        color='satisfaction', 
        orientation='h',
        height=400,
        labels={
            'proportion_tickets': "Percentage of Tickets (%)",
            'month': '',
            'satisfaction': ''
            },
    )


    # ----------------------------------------------------
    replytime_bar = px.bar(
        df.groupby(['satisfaction']).agg(avg_replytime=('replytime', 'mean')).reset_index(), 
        x="satisfaction",
        y="avg_replytime",
        color='satisfaction',
        labels={
            'avg_replytime': "Average Reply Time (min)",
            'satisfaction': 'Customer Satisfaction'
            },
        color_discrete_map={
        'Good': '#636EFA',
        'Bad': '#EF553B'
        }
        )
    replytime_bar.update_layout(showlegend=False)

    replytime_hist = px.histogram(
        df[df.satisfaction.isin(['Good', 'Bad'])],
        x="replytime",
        color="satisfaction",
        marginal="rug",
        hover_data=df.columns,
        barmode="overlay",
        labels={
            'replytime': "Reply Time (min)",
            'count': 'Number of Tickets'
            }
        )


    # ----------------------------------------------------
    fullresolutiontime_bar = px.bar(
        df.groupby(['satisfaction']).agg(avg_fullresolutiontime=('fullresolutiontime', 'mean')).reset_index(),
        x="satisfaction",
        y="avg_fullresolutiontime",
        color='satisfaction',
        labels={
            'satisfaction': 'Customer Satisfaction',
            'avg_fullresolutiontime': 'Average Full Resolution Time (days)'
            }, 
        color_discrete_map={
        'Good': '#636EFA',
        'Bad': '#EF553B'
        }
        )
    
    fullresolutiontime_bar.update_layout(showlegend=False)

    fullresolutiontime_hist = px.histogram(
        df[df.satisfaction.isin(['Good', 'Bad'])],
        x="fullresolutiontime",
        color="satisfaction",
        marginal="rug",
        hover_data=df.columns,
        barmode="overlay",
        labels={
            'satisfaction': 'Customer Satisfaction',
            'fullresolutiontime': 'Full Resolution Time (days)'
            }
        )

    # ----------------------------------------------------
    # 

    cpc_hist = px.histogram(
        df[df.satisfaction.isin(['Good', 'Bad'])],
        x="cpc",
        color="satisfaction",
        marginal="rug",
        hover_data=df.columns,
        barmode="overlay",
        labels={
            'satisfaction': '',
            'cpc': 'Number of Contacts per Case'
            }
        )

    firstcontact_df = (df[df.satisfaction.isin(['Good', 'Bad'])].groupby('satisfaction')['firstcontactresolution']
                                                .value_counts(normalize=True)
                                                .mul(100).round(2)
                                                .rename('percent')
                                                .reset_index())

    firstcontact_df.firstcontactresolution = firstcontact_df.firstcontactresolution.map({0: 'No', 1: 'Yes'})                                          

    firstcontactresolution_bar = px.bar(
        firstcontact_df,
        x="firstcontactresolution",
        y="percent",
        color='satisfaction',
        barmode='group',
        labels={
            'satisfaction': '',
            'percent': 'Percentage of tickets (%)',
            'firstcontactresolution': 'First Contact Resolution'
            }, 
        color_discrete_map={
        'Good': '#636EFA',
        'Bad': '#EF553B'
        }
        )
    firstcontactresolution_bar.update_layout(showlegend=False)

    figures = dict(
        csat_pie=csat_pie,
        monthly_bar=monthly_bar,
        replytime_bar=replytime_bar,
        replytime_hist=replytime_hist,
        fullresolutiontime_bar=fullresolutiontime_bar,
        fullresolutiontime_hist=fullresolutiontime_hist,
        cpc_hist=cpc_hist,
        firstcontactresolution_bar=firstcontactresolution_bar
    )



    return figures