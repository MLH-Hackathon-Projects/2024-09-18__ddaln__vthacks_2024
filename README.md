# DispatchIQ
## VTHax 2024
### Team:
- Daniel Hollberg
- Alex Urbina
- Aidan Walters 
- Aneesh Tummeti

## Inspiration

In emergency situations, dispatchers are often inundated with a high volume of calls, many of which are waiting in a FIFO (First-In, First-Out) queue to connect with a dispatcher. Compounding this challenge is the fact that approximately 20% of the U.S. population speaks a language other than English as their first language, which can further complicate communication and delay response times. DispatchIQ is designed to assist dispatchers by automating the triage process for these queued calls. 

DispatchIQ ensures a seamless and effective solution for managing emergency call prioritization and enhances dispatcher efficiency by utilizing:
- Google Kubernetes Engine for orchestration and deployment which ensures availability
- Azure AI Speech Service for real-time speech-to-text conversion
- XGBoost (Extreme Gradient Boosting) for developing models to predict severity scores
- MongoDB Atlas integration for data management
- Gemini large language model (LLM) for real-time summarization and analysis
- Flask and React for front-end
- Python for back-end support

## What it Does

DispatchIQ is an AI-powered call triage and prioritization system designed to assist 911 dispatchers by:
- Automatically transcribing calls in real-time.
- Supporting multiple languages with automatic language translation.
- Assigning a severity score to each case.
- Ranking emergencies based on urgency to optimize resource allocation.
- Prompting dispatchers with follow-up questions to gather missing information.

## How We Built It

1. **Speech-to-Text Conversion**: Leveraged Azure's Speech-to-Text API to transcribe live audio recordings of emergency calls that are in the dispatch queue.
2. **Severity Scoring**: Developed a machine learning algorithm using gradient boosted trees to assign severity scores based on features pulled from transcribed calls, incorporating crucial details such as location, nature of the emergency, and immediate risks.
3. **Priority Ranking**: Implemented a system to rank emergencies and help dispatchers focus on the highest-priority cases first.
4. **Database Integration**: Utilized MongoDB Atlas to store call data and transcripts, and developed a query system to summarize key points and update severity scores in real-time.
5. **Technology Stack**: Built the system using Google Kubernetes Engine for orchestration, Azure AI Speech Service for transcription, and integrated with large language models like Gemini. The frontend and backend are developed using React and Flask with Python, respectively.

## Challenges We Ran Into

- **Accuracy of Transcriptions**: Ensuring high accuracy of speech-to-text conversion in noisy environments and with non-native English speakers.
- **Severity Scoring**: Developing an algorithm that can reliably assess the severity of a situation from sometimes ambiguous or incomplete information.
- **Real-Time Processing**: Handling the high volume of incoming calls and processing data quickly enough to be actionable in urgent situations.

## Accomplishments That We're Proud Of

- **Efficient Triage**: Successfully reduced dispatcher workload by automating the initial triage process and prioritizing calls effectively.
- **Real-Time Updates**: Enabled dynamic updates to severity scores, ensuring that dispatchers have the most current information.
- **Improved Dispatcher Focus**: Helped dispatchers focus on critical cases by providing an AI-generated priority list and reducing manual effort.

## What We Learned [TODO]

- **Importance of Accuracy**: High accuracy in speech-to-text conversion is crucial for effective triage and prioritization.
- **Need for Dynamic Systems**: Real-time updates and dynamic severity scoring are essential for handling evolving emergency situations.
- **Human-AI Collaboration**: AI can significantly enhance human decision-making but should work in tandem with human judgment rather than replace it.

## What's Next for DispatchIQ

- **Integration with Additional Services**: Explore opportunities to integrate DispatchIQ with other public health and emergency response services to broaden its impact.
- **Continual Improvement**: Enhance the AI's ability to handle diverse languages and accents, and refine severity scoring algorithms based on real-world feedback.
- **Expansion of Features**: Develop new features such as automated follow-ups for ambiguous cases and more advanced analytics for emergency response optimization.
- **AI Prompts**: Integrate AI-driven prompts to gather additional information from distressed callers and fill in gaps that might be missed during high call volumes.