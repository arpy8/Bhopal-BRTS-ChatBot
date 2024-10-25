PROJECT_DESC = f"""
{'<br>'*9}
<div class="poppins-light">
    <div class="section">
        <h2>Challenge Background</h2>
        <p>As Bhopal grows, the need for efficient public transportation becomes increasingly critical. The Bus Rapid Transit System (BRTS) is a key component of the city's transit network, providing reliable service through its red buses. Despite its importance, many commuters struggle with the BRTS due to unfamiliarity with routes and language barriers, leading to confusion and inefficiencies.</p>
        <p>Navigating BRTS routes can be complex, especially for those who are not fluent in the local language or new to the city. This challenge affects first-time users, tourists, and non-native speakers who may find it difficult to understand schedules, routes, and ticketing procedures.</p>
        <p>To address these issues, an AI-driven chatbot with natural language processing (NLP) capabilities is proposed. This chatbot will offer real-time, multilingual guidance, including Hindi, to help users navigate the BRTS more effectively. By providing step-by-step navigation, accurate bus schedules, and traffic updates, the chatbot aims to enhance the commuting experience and encourage greater use of public transportation. Ultimately, this solution seeks to improve accessibility, reduce confusion, and support Bhopal's sustainable urban growth.</p>
    </div>
    <div class="section">
        <h2>The Problem</h2>
        <p>Bhopal's rapid urbanization has led to an increasing reliance on its public transportation system, particularly the Bus Rapid Transit System (BRTS), which serves as a critical component in maintaining urban mobility. Despite the BRTS's importance, many commuters struggle to effectively navigate the system. This issue is particularly pronounced among those unfamiliar with the city's layout, non-native speakers, and individuals who are not well-versed in the local language, primarily Hindi.</p>
        <p>The current lack of user-friendly, multilingual navigation support for BRTS users poses a significant challenge. Commuters often face difficulties in understanding bus routes, schedules, and ticketing procedures, leading to confusion, delays, and underutilization of the public transport system. This problem is exacerbated by the absence of real-time guidance, which is crucial for ensuring efficient travel, especially during peak hours or in cases of unexpected traffic conditions.</p>
        <p>Without an accessible, reliable solution, Bhopal's BRTS risks becoming less effective as the city grows, potentially leading to increased traffic congestion and reduced public transportation usage. There is an urgent need for a solution that can guide commuters through the BRTS system in a way that is both comprehensible and convenient, regardless of their familiarity with the city or their language proficiency.</p>
    </div>
    <div class="section">
        <h2>Goal of the Project</h2>
        <p>The goal of this project is to develop an AI-driven chatbot that provides real-time navigation and route guidance for commuters using Bhopal's Bus Rapid Transit System (BRTS). The chatbot will be equipped with natural language processing (NLP) capabilities to support multiple languages, with a primary focus on Hindi, making it accessible to a diverse range of users. By offering step-by-step guidance, real-time bus schedules, and traffic condition updates, the chatbot aims to enhance the user experience, promote greater utilization of the BRTS and contribute to the overall improvement of urban mobility in Bhopal.</p>
    </div>
    <div class="section contact">
        <p>For more information, please reach out to our team at <a href="mailto:omdena@vitbhopal.ac.in">omdena@vitbhopal.ac.in</a> 📧</p>
    </div>
</div>
"""


CSS_STYLING = """
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Poppins:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,100;1,200;1,300;1,400;1,500;1,600;1,700;1,800;1,900&display=swap" rel="stylesheet">         
<style>
.mapboxgl-ctrl-bottom-right, .mapboxgl-ctrl-bottom-left {
    display: none !important;
}
.poppins-light, h2, h3, h4, h5, h6 {
    font-family: "Poppins", sans-serif !important;
    font-weight: 200 !important;
    font-style: normal !important;
}
.poppins-light h1 {
    color: #00ff00 !important;
    font-size: 200px !important;
}
div[data-testid="stMetric"]
{
    background-color: rgba(0, 0, 0, 0.5);
    color: white;
    padding: 10px 0 0 10px;
    border-radius: 5px;
    border-color: #26282e !important;
}
</style>
"""

LANDMARK_COLORS = {
    "SR1": {"hex": "#FF5733", "rgb": [1.0, 0.34, 0.2]},
    "SR2": {"hex": "#33A2FF", "rgb": [0.2, 0.64, 1.0]},
    "SR3": {"hex": "#A833FF", "rgb": [0.66, 0.2, 1.0]},
    "SR4": {"hex": "#33FFBD", "rgb": [0.2, 1.0, 0.74]},
    "SR5": {"hex": "#FF33A8", "rgb": [1.0, 0.2, 0.66]},
    "SR6": {"hex": "#FFD733", "rgb": [1.0, 0.84, 0.2]},
    "SR7": {"hex": "#33FF57", "rgb": [0.2, 1.0, 0.34]},
    "SR8": {"hex": "#FF8C33", "rgb": [1.0, 0.55, 0.2]},
    "TR1": {"hex": "#334FFF", "rgb": [0.2, 0.31, 1.0]},
    "TR2": {"hex": "#FF333F", "rgb": [1.0, 0.2, 0.25]},
    "TR3": {"hex": "#33FF8D", "rgb": [0.2, 1.0, 0.55]},
    "TR4": {"hex": "#B8FF33", "rgb": [0.72, 1.0, 0.2]}
}