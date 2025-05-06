from django.shortcuts import render
import plotly.express as px
import plotly.io as pio


def graph_page(request):
    data = {
        'Day': ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'],
        'Hours Played': [2, 1, 1, 2, 3, 3, 2]
    }

    # Create a bar chart using Plotly Express
    fig = px.bar(data, x='Day', y='Hours Played', title='Hours Played on Drums Per Week',
                 labels={'Hours Played': 'Hours Played', 'Day': 'Day of the Week'})

    # Generate the HTML code for the graph
    graph_html = pio.to_html(fig, full_html=False)

    # Pass the graph HTML to the template
    return render(request, 'graph/graph.html', {'graph_html': graph_html})
