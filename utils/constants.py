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
.poppins-light, p, h2, h3, h4, h5, h6, li {
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

.my-button {
    display: inline-flex;
    -webkit-box-align: center;
    align-items: center;
    -webkit-box-pack: center;
    justify-content: center;
    font-weight: 400;
    padding: 0.25rem 0.75rem;
    border-radius: 0.5rem;
    min-height: 2.5rem;
    margin: 0px;
    line-height: 1.6;
    color: inherit;
    width: auto;
    user-select: none;
    background-color: rgb(19, 23, 32);
    border: 1px solid rgba(250, 250, 250, 0.2);
}
div[data-baseweb="textarea"], button[data-testid="stChatInputSubmitButton"] {
position: absolute !important;
    border-color: #ff000090 !important; 
    top: 15px;
    right: 0px; 
    width: 100%;
}

div[data-baseweb="stChatMessageContent"] {
    font-size: 10px !important;
}

div[data-testid="stMarkdownContainer"] p {
    font-size: 13px;
}

button[data-testid="stChatInputSubmitButton"] {
    right: 15px;
}

p, ol, ul, dl {
    margin: 0px 0px 0.5rem;
}
</style>
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.2/css/all.min.css">
"""

LANDMARK_COLORS = {
    "SR1": {"rgb":[255, 86, 51],  "hex":"#FF5633", "source": [255, 165, 0], "target": [255, 69, 0]},
    "SR2": {"rgb":[51, 163, 255], "hex":"#33A3FF", "source": [0, 128, 128], "target": [0, 206, 209]},
    "SR3": {"rgb":[168, 51, 255], "hex":"#A833FF", "source": [138, 43, 226], "target": [255, 215, 0]},
    "SR4": {"rgb":[51, 255, 188], "hex":"#33FFBC", "source": [255, 140, 0], "target": [255, 99, 71]},
    "SR5": {"rgb":[255, 51, 168], "hex":"#FF33A8", "source": [0, 255, 127], "target": [255, 20, 147]},
    "SR6": {"rgb":[255, 214, 51], "hex":"#FFD633", "source": [34, 139, 34], "target": [60, 179, 113]},
    "SR7": {"rgb":[51, 255, 86],  "hex":"#33FF56", "source": [135, 206, 235], "target": [46, 139, 87]},
    "SR8": {"rgb":[255, 140, 51], "hex":"#FF8C33", "source": [0, 191, 255], "target": [25, 25, 112]},
    "TR1": {"rgb":[51, 79, 255],  "hex":"#334FFF", "source": [255, 99, 71], "target": [178, 34, 34]},
    "TR2": {"rgb":[255, 51, 63],  "hex":"#FF333F", "source": [255, 182, 193], "target": [255, 160, 122]},
    "TR3": {"rgb":[51, 255, 140], "hex":"#33FF8C", "source": [72, 61, 139], "target": [173, 216, 230]},
    "TR4": {"rgb":[183, 255, 51], "hex":"#B7FF33", "source": [255, 255, 0], "target": [255, 140, 0]},
    "All": {"rgb":[183, 255, 51], "hex":"#ff0000", "source": [255, 255, 0], "target": [255, 140, 0]},
    "user": {"rgb":[255, 255, 255], "hex":"#ff0000", "source": [255, 255, 0], "target": [255, 140, 0]}
}

MAPBOX_STYLES = {
    "dark":"mapbox://styles/mapbox/dark-v11",
    "streets":"mapbox://styles/mapbox/streets-v12",
    "outdoors":"mapbox://styles/mapbox/outdoors-v12",
    "light":"mapbox://styles/mapbox/light-v11",
    "satellite":"mapbox://styles/mapbox/satellite-v9",
    "satellite-streets":"mapbox://styles/mapbox/satellite-streets-v12",
    "navigation-day":"mapbox://styles/mapbox/navigation-day-v1",
    "navigation-night":"mapbox://styles/mapbox/navigation-night-v1"
}

AVATAR = {
    "assistant": "./assets/img/assistant.png",
    "user": "./assets/img/user.png"
}


RAG_PROMPT_CONSTANT = """\
You are a helpful and informative bot that answers questions using text from the reference passage included below. \
Be sure to respond in a complete sentence, being comprehensive, including all relevant background information. \
However, you are talking to a non-technical audience, so be sure to break down complicated concepts and \
strike a friendly and converstional tone. \
If the passage is irrelevant to the answer, you may ignore it.

QUESTION: '{query}'
PASSAGE: '{relevant_passage}'

ANSWER:
"""