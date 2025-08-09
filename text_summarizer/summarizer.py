from dotenv import load_dotenv
import os

from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI

information = """
born January 30, 1956) is a Japanese professional race car driver. He is known as the Drift King (ドリキン, Dorikin) for his nontraditional use of drifting in non-drifting racing events and his role in popularizing drifting as a motorsport. In professional racing, he is a two-time 24 Hours of Le Mans class winner and the 2001 All Japan GT Championship runner-up. He is also known for touge driving.
The car he drives, a Toyota AE86 Sprinter Trueno, has become one of the most popular sports cars; the car is also known as "Hachi-Roku" in Japan (hachi-roku meaning "eight-six"); his car is also called "The Little Hachi that could." A 2-part video known as 'The Touge' produced by Pluspy (styled as +P) documents Tsuchiya's touge driving with his AE86.
He was a consultant for the popular manga and anime series, Initial D, in which he makes several cameos. He also served as a stunt coordinator and stuntman on The Fast and the Furious: Tokyo Drift, where he also made a cameo appearance.
Biography
Tsuchiya started his career through the Fuji Freshman series in 1977. Unlike many drivers who came from wealthy families or motorsport backgrounds, he honed his skills from street racing and became noted in the underground scene.
Racing career
National championships
Nissan Skyline GT-R (1992)
He would continue to take part in the Japanese Formula Three Championship, Japanese Touring Car Championship (JTCC), the latter while driving a Cosmo Oil Sierra Cosworth and Nissan Skyline GT-R (Team Taisan) in the Group A championships and later a Honda Civic in the Supertouring car championships.[1]
Le Mans
He went on to score a class win and an 8th place overall at the 1995 24 Hours of Le Mans in a Honda NSX. In the same race in 1999, this time in a Toyota GT-One, during the last hour while co-driver Ukyo Katayama was building up pace to the leading BMW V12 LMR he was forced into the grass by a backmarker privateer's BMW LMR, blowing the tire out. They survived the ordeal and went on to score the fastest lap but were forced to settle for second.
NASCAR
He has raced in NASCAR-sanctioned exhibition races at Suzuka Circuit (Suzuka Thunder 100) and at Twin Ring Motegi Superspeedway for the 1998 NASCAR-sanctioned exhibition and 1999 NASCAR Grand National Division, AutoZone West Series races at the circuit, both named the Coca-Cola 500K.
Drifting career
When Tsuchiya was a freshman in circuit racing, he was about to get his racing license suspended because of the illegal racing he was recording for Pluspy. In the movie series Shuto Kousoku Trial, he advised street racers to leave the illegal racing scene if they want to become involved with professional racing.
After retirement
After his retirement, he was Team Director for both GT500 for one year and GT300 Class of ARTA JGTC Team until the team disbanded their GT300 operation at the end of the 2005 season. He owned the aftermarket company Kei Office until he sold the business in the end of 2005 to form DG-5. After quitting D1 in January 2011, he co-founded amateur drifting series Drift Muscle, where he also worked as judge.
His trademark color is jade green, which appears on his overalls and helmet and is the adopted color of the former company. It was also the colour of the D1 Grand Prix Kei Office and DG-5 S15 Silvia of driver and employee Yasuyuki Kazama who also wears a suit similar in pattern.
He also hosts the video magazine "Best Motoring" which features road tests of new Japanese cars including a special section called "Hot Version" which focuses on performance-modified cars. He is a guest presenter in Video Option alongside fellow racing drivers Manabu Orido and Nobuteru Taniguchi, a monthly video magazine, similar to Hot Version except regularly covers the D1GP and its sister video magazine Drift Tengoku which deals purely with drifting.
He has been an editorial supervisor on the televised anime Initial D and Wangan Midnight. He also appeared in the semi biographical film Shuto Kousoku Trial 2, 3, 4, 5, and 6 was also featured in the Super GT magazine show in Japan. His life in driving is parallel to that of the Initial D main character, Takumi, as both of them started exploring their local touge while doing regular deliveries for their family businesses. He makes a number of cameos in the series: in the First Stage, he briefly converses with Takumi's father, Bunta; in the Third Stage, a motorcycle rider wearing a similar racing suit overtakes Takumi as he was en route to an invitation battle with Ryosuke Takahashi; and in the Final Stage, he meets Takumi in person while the latter spectates a circuit race in the end credits. The color of Tomo's racing suit from the Initial D 4th Stage is jade green and has a similar pattern to Tsuchiya's suit. He also made an appearance opposite Top Gear's Jeremy Clarkson in a Motorworld in Japan special showing drifting competition in the mid 1990s in Japan.
After 1995, he sometimes appeared as a Formula One guest commentator in Japanese Fuji TV.
"""

if __name__ == "__main__":
    load_dotenv()
    print(os.environ['openai_api_key'])


    summary_template = """
    given the information {information} about a person I want you to create:
    1. a short summary
    2. two interesting facts about them 
    """

    summary_prompt_template = PromptTemplate(input_variables="information",template=summary_template)

    llm= ChatOpenAI(temperature=0,model_name="gpt-4.1")

    chain = summary_prompt_template | llm
    res = chain.invoke(input={"information":information})

    print(res)



