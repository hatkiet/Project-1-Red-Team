Research question: How did popularity in movie genres shift over three decades ranging from 1990- 2019?
•	How did the revenue total shift over the years? 
•	Did any specific Genres have a more dominant presence than others?
•	What impact did social and economic influences have on movies over 30 years? Did we see a correlation between the revenue and the years economy?

Research expectations:

Over the course of this research, we expect to see changeability in the movie genres over the course of three decades beginning in 1990. While we expect to see an overall consistent growth in revenue over all genres, we also anticipate the data to be a bit volatile due to financial and social influences. 
Our expectation is Action and adventure films will establish a strong grasp on revenue and growth due to potential for blockbuster, high end returns as well as general broad appeal. 
As previously alluded to, we anticipate external factors such as economic constraints and social events to impact revenue over the court of the three decades and contribute to the peaks and valleys we will see in revenue. 


Part 1: Cleaning the data

Over the course of this research, we expect to see changeability in the movie genres over the course of three decades beginning in 1990. While we expect to see an overall consistent growth in revenue over all genres, we also anticipate the data to be a bit volatile due to financial and social influences. 
Our expectation is Action and adventure films will establish a strong grasp on revenue and growth due to potential for blockbuster, high end returns as well as general broad appeal. 
As previously alluded to, we anticipate external factors such as economic constraints and social events to impact revenue over the court of the three decades and contribute to the peaks and valleys we will see in revenue. 


Part 2: Visualization

[1] Revenue Median/Mean by Genres over Three Decades

<img width="1328" alt="Screenshot 2024-02-25 at 12 13 04 PM" src="https://github.com/hatkiet/Project-1-Red-Team/assets/154276115/8b864c2e-7cbd-4f04-93cb-43fdbb821229">

Discussion: ??? 

[2] Box plot of Revenue by Genres

<img width="1080" alt="Screenshot 2024-02-25 at 12 13 23 PM" src="https://github.com/hatkiet/Project-1-Red-Team/assets/154276115/f4985e4f-331b-4265-9536-f25f0ce4a3b3">

Discussion: ???

[3] Movies Distribution by Genres

<img width="865" alt="Screenshot 2024-02-25 at 12 13 32 PM" src="https://github.com/hatkiet/Project-1-Red-Team/assets/154276115/f4646153-4b84-4d44-9f3f-7ca8165c6a05">

Discussion: ???

[4] Revenue over Time for Top Five Genres

<img width="985" alt="Screenshot 2024-02-25 at 12 13 52 PM" src="https://github.com/hatkiet/Project-1-Red-Team/assets/154276115/62a18417-bdd4-487b-a13b-99770cff1b97">

<img width="789" alt="Screenshot 2024-02-25 at 12 14 10 PM" src="https://github.com/hatkiet/Project-1-Red-Team/assets/154276115/fbb49882-e0d3-4632-96b7-ab1446a376c8">

Discussion: Over a period of 30 years, we observed different genres of movies perform in the industry. In the 1990s, Drama genre outperformed all other genres while Comedy had a steady climb in revenue. However, in the 2000s, Drama took a hit and experienced a steep fall off, while Comedy continued to steadily rise. In 2006, we also saw a significant jump in revenue for Action movies. The 2010s marked the beginning of Action movies taking a dominant spot in the genres. Overall, we observed a steady increase in revenue for all genres, from $1-2 billion range in 1990 to $7-10 billion in 2019. 


Part 3: How does disposable personal income influence the popularity of different movie genres? 

The regression analysis sheds light on the connection between disposable personal income (DPI) and the popularity of various movie genres. The correlation coefficients unveil the strength and direction of this connection, with higher values indicating a more robust association between DPI and genre popularity.

Here's a detailed breakdown of the findings:

Correlation Coefficients:

Action: 0.93
Adventure: 0.97
Comedy: 0.97
Thriller: 0.88
Drama: 0.88

These correlation coefficients signify strong positive correlations between DPI and the popularity of Action, Adventure, and Comedy genres, with values nearing 1. Conversely, Thriller and Drama genres also display positive correlations, though slightly weaker. This suggests that consumers with higher disposable incomes are inclined to spend on entertainment, including movie tickets or subscriptions to streaming services offering these genres.

linear regression equations:

Action: y=0.001x+5385838.94
<img width="588" alt="Screenshot 2024-02-25 at 12 23 00 PM" src="https://github.com/hatkiet/Project-1-Red-Team/assets/154276115/99d632b9-9fdd-432f-b19f-e46c0f788cb6">

Adventure: y=0.001x+4565180.12
<img width="586" alt="Screenshot 2024-02-25 at 12 23 13 PM" src="https://github.com/hatkiet/Project-1-Red-Team/assets/154276115/29d00ef2-6b59-4a9e-9a4b-aeb7b5b0c3f8">

Comedy: y=0.001x+3465162.44
<img width="585" alt="Screenshot 2024-02-25 at 12 23 23 PM" src="https://github.com/hatkiet/Project-1-Red-Team/assets/154276115/4e2729b7-2d73-4392-bb3e-3baf38b61053">

Thriller: y=0.001x+5234958.15
<img width="588" alt="Screenshot 2024-02-25 at 12 23 31 PM" src="https://github.com/hatkiet/Project-1-Red-Team/assets/154276115/f5848bd2-80aa-448c-9215-6b9344b6e3d6">

Drama: y=0.001x+066070.52
<img width="588" alt="Screenshot 2024-02-25 at 12 23 39 PM" src="https://github.com/hatkiet/Project-1-Red-Team/assets/154276115/bcc07e1c-d8e5-4c6d-99a3-dd7899214aa0">

Despite the positive correlation, the slope of the regression lines for all genres is extremely close to zero (0.001). This implies that while there's a subtle positive trend, the relationship isn't markedly linear. In essence, changes in DPI have only a minimal direct impact on the revenue generated from each genre. In other words, while a positive relationship exists between DPI and genre popularity, the lack of a significant linear relationship suggests that other regression models or additional factors may better capture this relationship or influence consumer preferences and revenue generation within each genre.

This nuanced understanding underscores the complexity of consumer behavior and the multifaceted nature of the factors influencing entertainment consumption patterns. It emphasizes the importance of comprehensive analysis and consideration of various factors in predicting and adapting to shifts in consumer demand within the film industry. Understanding this relationship can inform strategic decision-making within the film industry, helping stakeholders better anticipate and respond to changes in consumer demand based on economic factors. By aligning their offerings with consumer preferences, filmmakers and industry players can enhance their competitiveness and profitability in the market.

