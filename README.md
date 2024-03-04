# Topic-Modeling-Analysis-on-Tweets

This report presents the findings from a topic modeling analysis performed on a dataset of tweets related to COVID-19. The analysis aimed to uncover the prevalent themes and discussions within the tweets, covering various aspects of the pandemic's impact. The Latent Dirichlet Allocation (LDA) model, implemented via the Gensim library, was employed to identify distinct topics, each represented by a set of keywords.

![image](https://github.com/TaranehAskarzadeh/Topic-Modeling-Analysis-on-Tweets/assets/65934906/5930365d-063d-4251-9872-280be3b209a1)


## Data collection
### Python Library Used:

### Query Construction:
gen_rule_payload: This function from the searchtweets library is used to generate the payload for the search rule, which will be sent to the Twitter API. The payload defines the search query and any additional parameters such as language or excluding retweets.
### Search Query:
The search query (assigned to variable q) is a string that includes a combination of keywords and hashtags related to the COVID-19 pandemic and public transportation. The terms are combined using the logical OR operator, which allows the search to match any tweets containing at least one of the specified terms.
Keywords and hashtags include terms like #covid19, #coronavirus, #pandemic, #covid, #corona, #spread, #virus, #publictransportation, #publictransit, #bike, #bus, #metro, #bikeshare, #scootershare, #masstransit, #subway, #scooter, #uber, #lyft, #flight, #airline, #carpool, #riders.

## Data Preparation
The dataset consisted of tweets collected over several months in 2020. These tweets were preprocessed to remove noise and irrelevant information, such as URLs, mentions, non-alphanumeric characters, and common stopwords. The preprocessing steps included:

- Removal of URLs and mentions to focus on meaningful text content.
- Elimination of non-alphanumeric characters and extra spaces.
- Lowercasing and tokenization of the text.
- Removal of stopwords and short words that are less likely to carry significant meaning.
- 
## Topic Modeling Process
The LDA model was trained with the following hyperparameters, chosen based on preliminary experiments to optimize coherence scores:

An LDA model was trained with the following parameters to best fit the data:

## 1
- Number of Topics: Set to 3 based on preliminary analysis to balance topic specificity and breadth.
- Alpha and Eta: Both set to 0.01 to reflect the assumption that each tweet is likely to exhibit a single topic and a limited set of words.
- Number of Passes: Fixed at 50 to ensure model convergence.

## 2
- Number of Topics: 5, to capture a broad range of discussions without overly diluting thematic distinctions.
- Alpha ('asymmetric'): To allow for variability in topic distribution across documents, considering the diverse nature of tweet content.
- Eta ('auto'): Automatically determined by the model to best capture word-topic distributions.
- Number of Passes: 10, to balance between computational efficiency and model convergence.


## Results
The LDA model yielded a coherence score of 0.3719 (for 3 topic version), indicating a reasonable level of topic coherence and interpretability. The identified topics, along with their descriptions and representative keywords, are as follows:

## 1
### Topic 0: General Transportation and COVID-19
Keywords: co, https, covid, uber, coronavirus, lyft, flight, bus, bike, airline
This topic encapsulates discussions on how the pandemic has affected various modes of transportation, with a focus on ride-sharing services and public transportation.

### Topic 1: Ride-Sharing and Public Health Measures
Keywords: co, https, uber, covid, drivers, bike, coronavirus, lyft, face, masks
This topic highlights conversations around ride-sharing services like Uber and Lyft, particularly focusing on the impact of COVID-19 on drivers and the adoption of health safety measures.

### Topic 2: Aviation Industry and COVID-19
Keywords: co, https, covid, airline, aviation, industry, airport, news, latest, keep
Discussions under this topic revolve around the aviation industry's challenges and responses to the pandemic, including changes in operations and the economic impact.

## 2
### Topic 0: Impact of COVID-19 on the Airline and Aviation Industry
Keywords: covid, airline, flight, pandemic, aviation
Discussion: This topic captures conversations around the significant challenges and responses within the airline and aviation sectors due to the pandemic.

### Topic 1: Ride-Sharing Services and COVID-19 Safety Measures
Keywords: uber, covid, drivers, lyft, mask
Discussion: Discussions in this topic revolve around how ride-sharing services are adapting to COVID-19, focusing on driver and passenger safety measures.

### Topic 2: Governmental and Financial Responses to COVID-19
Keywords: covid, airline, thank, critical, emergency
Discussion: This topic highlights the governmental and financial interventions aimed at mitigating the pandemic's impact, particularly on critical industries.

### Topic 3: Biking and Social Activities During the Pandemic
Keywords: bike, social, ride, free, bicycles
Discussion: Reflecting a shift towards outdoor and socially-distanced activities, this topic emphasizes the increased interest in biking as a form of recreation and commuting.

### Topic 4: Disruptive Technologies and Market Changes Amid COVID-19
Keywords: uber, similar, tesla, market, university
Discussion: This topic explores how the pandemic has accelerated certain technological and market shifts, including the adoption of new business models and services.

## 1  
| Topic   | Description                               | Keywords                                                                                         |
|---------|-------------------------------------------|--------------------------------------------------------------------------------------------------|
| Topic 0 | General Transportation and COVID-19       | co, https, covid, uber, coronavirus, lyft, flight, bus, bike, airline                            |
| Topic 1 | Ride-Sharing and Public Health Measures   | co, https, uber, covid, drivers, bike, coronavirus, lyft, face, masks                            |
| Topic 2 | Aviation Industry and COVID-19            | co, https, covid, airline, aviation, industry, airport, news, latest, keep                       |

## 2

| Topic | Description | Keywords |
| --- | --- | --- |
| Topic 0 | Impact of COVID-19 on the Airline and Aviation Industry | covid, airline, flight, pandemic, aviation |
| Topic 1 | Ride-Sharing Services and COVID-19 Safety Measures | uber, covid, drivers, lyft, mask |
| Topic 2 | Governmental and Financial Responses to COVID-19 | covid, airline, thank, critical, emergency |
| Topic 3 | Biking and Social Activities During the Pandemic | bike, social, ride, free, bicycles |
| Topic 4 | Disruptive Technologies and Market Changes Amid COVID-19 | uber, similar, tesla, market, university |


# Conclusion
The topic modeling analysis of COVID-19 related tweets has revealed a wide array of discussions, from the direct impacts on industries like aviation and ride-sharing to broader societal shifts in response to the pandemic. The identified topics not only reflect the multifaceted nature of the pandemic's effects but also highlight the adaptability and resilience in various sectors and communities. This analysis provides valuable insights into public sentiment and the predominant themes of discourse during a critical period of the pandemic.
