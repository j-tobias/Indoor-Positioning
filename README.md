
# Indoor Positioning

The Indoor Positioning project demonstrates the application of machine learning, specifically Random Forest, to solve real-world problems like indoor positioning. By leveraging machine learning algorithms, this project aims to accurately predict the indoor location of a person based on collected data. This README provides an overview of the project, including the data collection process, features used for classification, achieved accuracy, and practical implications and potential applications.

## Key Features

-   **Indoor Positioning:** Utilizes Random Forest algorithm for indoor positioning, predicting the location of a person within a building.
-   **Data Collection:** Describes the process of collecting data for training the model, including the types of sensors used and the data attributes recorded.
-   **Feature Selection:** Discusses the features selected for classification, which play a crucial role in accurately predicting indoor locations.
-   **Accuracy:** Highlights the achieved accuracy of the model and its performance in predicting indoor positions.
-   **Practical Implications:** Discusses the practical implications and potential applications of the Indoor Positioning project.

## Data Collection

The data for the Indoor Positioning project was collected by deploying a network of sensors within the building. The sensors are scanning for Bluetooth Low Energy signals. These sensors captured various data attributes such as received signal strengths, unique identifier and Major/Minor. The data collection process involved walking through different areas of the building while recording sensor data at regular intervals.

The collected data was then labeled with the corresponding ground truth indoor locations to create a supervised learning dataset. The ground truth locations were determined using manual surveys. This labeled dataset was used to train and evaluate the Random Forest model.

## Feature Selection

Feature selection is a critical step in building an accurate indoor positioning model. The following features were considered for classification:

-   **Signal Strength (RSSI):** The strength of Bluetooth signals received by the sensors.

The feature was chosen based on it's ability to differentiate between different locations within the building. Feature engineering techniques were also applied to extract relevant information and improve the model's predictive capabilities.

## Accuracy

The accuracy achieved by the Indoor Positioning model depends on several factors, including the quality of the data, feature selection, model training and number of available Sensors. Extensive evaluation and testing were conducted to assess the model's performance. The achieved accuracy should be reported here, along with any relevant metrics used for evaluation, such as precision, recall, or F1 score.

The accuracy of the model may vary depending on the complexity of the indoor environment, the density of sensors, and the availability of signals. It is important to acknowledge any limitations and potential challenges associated with the accuracy of indoor positioning systems.

## Practical Implications and Potential Applications

The Indoor Positioning project has practical implications and potential applications in various domains, including:

-   **Navigation and Wayfinding:** The ability to accurately predict indoor positions can assist users in navigating complex indoor environments, such as shopping malls, airports, or large office buildings.
-   **Asset Tracking:** Indoor positioning can be used for tracking and managing assets within a facility, optimizing workflows, and improving inventory management.
-   **Location-based Services:** Businesses can leverage indoor positioning to deliver targeted advertisements, personalized recommendations, or location-based notifications to users within their premises.
-   **Security and Emergency Response:** Indoor positioning can enhance security measures and aid emergency response teams by providing real-time location information during critical situations.

By showcasing the Indoor Positioning project, you can demonstrate your ability to apply machine learning techniques to solve real-world problems and highlight the potential impact of indoor positioning in various industries.
