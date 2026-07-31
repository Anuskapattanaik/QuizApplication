import os
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'quiz_project.settings')
django.setup()

from quiz_app.models import Question, Option, CATEGORY_CHOICES

quiz_data = {
    'Maths': [
        ('What is 5 + 7?', ['10', '11', '12', '14'], 2),
        ('Solve for x: 2x = 10', ['x = 4', 'x = 5', 'x = 6', 'x = 10'], 1),
        ('What is the square root of 64?', ['6', '7', '8', '9'], 2),
        ('What is 15% of 200?', ['15', '20', '30', '40'], 2),
        ('What is the value of Pi to two decimal places?', ['3.12', '3.14', '3.16', '3.18'], 1),
        ('What is 7 multiplied by 8?', ['54', '56', '62', '64'], 1),
        ('If a triangle has a base of 4 and height of 5, what is its area?', ['10', '15', '20', '25'], 0),
        ('What is the next prime number after 11?', ['12', '13', '15', '17'], 1),
        ('Solve: 12 - 4 * 2', ['16', '12', '8', '4'], 3),
        ('Convert 1/4 to a percentage.', ['15%', '20%', '25%', '30%'], 2)
    ],
    'Physics': [
        ('What is the unit of force?', ['Joule', 'Newton', 'Watt', 'Pascal'], 1),
        ('What is the speed of light in a vacuum?', ['300,000 km/s', '150,000 km/s', '30,000 km/s', '1,000,000 km/s'], 0),
        ('Who developed the theory of relativity?', ['Isaac Newton', 'Galileo Galilei', 'Albert Einstein', 'Nikola Tesla'], 2),
        ('What particles are found in the nucleus of an atom?', ['Electrons only', 'Protons and Neutrons', 'Electrons and Protons', 'Neutrons and Electrons'], 1),
        ('What is the formula for kinetic energy?', ['E=mc^2', 'F=ma', '1/2 mv^2', 'mgh'], 2),
        ('What color of light has the longest wavelength?', ['Violet', 'Green', 'Yellow', 'Red'], 3),
        ('What is the SI unit of electric current?', ['Volt', 'Ohm', 'Ampere', 'Coulomb'], 2),
        ('Which law states that for every action, there is an equal and opposite reaction?', ["Newton's First Law", "Newton's Second Law", "Newton's Third Law", "Law of Gravity"], 2),
        ('What state of matter has a definite volume but no definite shape?', ['Solid', 'Liquid', 'Gas', 'Plasma'], 1),
        ('What instrument is used to measure atmospheric pressure?', ['Thermometer', 'Barometer', 'Hygrometer', 'Anemometer'], 1)
    ],
    'Chemistry': [
        ('What is the chemical symbol for Gold?', ['Go', 'Gd', 'Au', 'Ag'], 2),
        ('What is the most abundant gas in the Earth\'s atmosphere?', ['Oxygen', 'Carbon Dioxide', 'Nitrogen', 'Hydrogen'], 2),
        ('What is the pH value of pure water?', ['0', '5', '7', '14'], 2),
        ('What type of bond involves sharing of electrons?', ['Ionic', 'Covalent', 'Metallic', 'Hydrogen'], 1),
        ('Which element has the atomic number 1?', ['Helium', 'Oxygen', 'Hydrogen', 'Carbon'], 2),
        ('What is the chemical formula for table salt?', ['NaCl', 'KCl', 'NaOH', 'HCl'], 0),
        ('What process turns a liquid into a gas?', ['Condensation', 'Sublimation', 'Evaporation', 'Freezing'], 2),
        ('What is the lightest chemical element?', ['Oxygen', 'Hydrogen', 'Helium', 'Nitrogen'], 1),
        ('Which acid is found in the human stomach?', ['Sulfuric acid', 'Nitric acid', 'Hydrochloric acid', 'Acetic acid'], 2),
        ('What is a substance that speeds up a chemical reaction called?', ['Inhibitor', 'Reactant', 'Product', 'Catalyst'], 3)
    ],
    'Biology': [
        ('What is the powerhouse of the cell?', ['Nucleus', 'Mitochondria', 'Ribosome', 'Endoplasmic Reticulum'], 1),
        ('What molecule carries genetic information?', ['RNA', 'Protein', 'DNA', 'Carbohydrate'], 2),
        ('What process do plants use to make food?', ['Respiration', 'Photosynthesis', 'Digestion', 'Fermentation'], 1),
        ('How many chambers are in the human heart?', ['Two', 'Three', 'Four', 'Five'], 2),
        ('What is the longest bone in the human body?', ['Femur', 'Tibia', 'Fibula', 'Humerus'], 0),
        ('What blood type is considered the universal donor?', ['A+', 'B-', 'AB+', 'O-'], 3),
        ('What gas do humans exhale?', ['Oxygen', 'Carbon Dioxide', 'Nitrogen', 'Helium'], 1),
        ('Which organ is responsible for filtering blood?', ['Heart', 'Liver', 'Kidneys', 'Stomach'], 2),
        ('What part of the plant conducts photosynthesis?', ['Roots', 'Stem', 'Leaves', 'Flower'], 2),
        ('What type of animal is a frog?', ['Reptile', 'Mammal', 'Amphibian', 'Bird'], 2)
    ],
    'Geography': [
        ('What is the largest continent by land area?', ['Africa', 'North America', 'Asia', 'Europe'], 2),
        ('Which river is the longest in the world?', ['Amazon', 'Nile', 'Yangtze', 'Mississippi'], 1),
        ('What is the capital of Australia?', ['Sydney', 'Melbourne', 'Canberra', 'Brisbane'], 2),
        ('Which country has the largest population?', ['India', 'USA', 'China', 'Indonesia'], 2),
        ('What mountain is the highest above sea level?', ['K2', 'Mount Kilimanjaro', 'Mount Everest', 'Mount Fuji'], 2),
        ('Which ocean is the largest?', ['Atlantic Ocean', 'Indian Ocean', 'Pacific Ocean', 'Arctic Ocean'], 2),
        ('What is the capital of Canada?', ['Toronto', 'Vancouver', 'Montreal', 'Ottawa'], 3),
        ('Which continent is also a country?', ['Antarctica', 'Australia', 'Europe', 'South America'], 1),
        ('What desert is the largest hot desert in the world?', ['Gobi', 'Kalahari', 'Sahara', 'Arabian'], 2),
        ('Which country is famous for the Eiffel Tower?', ['Italy', 'Spain', 'Germany', 'France'], 3)
    ],
    'Aptitude': [
        ('If a train travels 60 miles in 1.5 hours, what is its average speed?', ['30 mph', '40 mph', '45 mph', '50 mph'], 1),
        ('If 5 machines make 5 widgets in 5 minutes, how long does it take 100 machines to make 100 widgets?', ['5 minutes', '100 minutes', '50 minutes', '10 minutes'], 0),
        ('Which word does not belong?', ['Apple', 'Banana', 'Carrot', 'Orange'], 2),
        ('Continue the series: 2, 4, 8, 16, ?', ['24', '30', '32', '64'], 2),
        ('If SOME=1234 and MORE=5264, what is ROME?', ['6254', '6234', '5234', '5264'], 1),
        ('A bat and a ball cost $1.10 in total. The bat costs $1.00 more than the ball. How much does the ball cost?', ['10 cents', '5 cents', '15 cents', '20 cents'], 1),
        ('If it takes 3 people 3 days to dig 3 holes, how long does it take 1 person to dig 1 hole?', ['1 day', '3 days', '9 days', '1/3 day'], 1),
        ('Look at this series: 36, 34, 30, 28, 24, ... What number should come next?', ['20', '22', '24', '26'], 1),
        ('Which fraction is larger?', ['3/4', '4/5', '5/6', '6/7'], 3),
        ('How many months have 28 days?', ['1', '2', '6', '12'], 3)
    ],
    'Personality': [
        ('How do you typically recharge your energy?', ['Spending time alone', 'Socializing with groups', 'A mix of both', 'I never run out of energy'], 2),
        ('When making a decision, what do you rely on most?', ['Logic and facts', 'Gut feeling and intuition', 'How it affects others', 'Flipping a coin'], 0),
        ('How do you handle unexpected changes in plans?', ['Get stressed and anxious', 'Adapt easily and go with the flow', 'Try to control the situation', 'Complain but eventually adjust'], 1),
        ('In a group project, what role do you usually take?', ['The Leader', 'The Organizer', 'The Idea Generator', 'The Supporter'], 0),
        ('What describes your ideal weekend?', ['Staying in and reading/gaming', 'Going out to a party or event', 'Outdoor adventure', 'Working on a personal project'], 0),
        ('How do you prefer to communicate important information?', ['Detailed email/text', 'Phone call', 'Face-to-face meeting', 'Quick voice note'], 2),
        ('When conflict arises, you usually:', ['Avoid it entirely', 'Address it head-on immediately', 'Try to find a compromise', 'Let someone else handle it'], 2),
        ('Is your workspace generally:', ['Immaculately organized', 'A bit cluttered but you know where things are', 'Extremely messy', 'Constantly changing'], 1),
        ('Do you prefer to plan your day or be spontaneous?', ['Strict schedule', 'Loose outline', 'Completely spontaneous', 'Depends on the day'], 1),
        ('What motivates you the most?', ['Personal achievement', 'Helping others', 'Financial reward', 'Recognition from peers'], 0)
    ],
    'Current Affairs': [
        ('Which global organization oversees international public health?', ['UN', 'WHO', 'WTO', 'IMF'], 1),
        ('What treaty dictates international action on climate change?', ['Kyoto Protocol', 'Paris Agreement', 'Geneva Convention', 'Montreal Protocol'], 1),
        ('Which country recently hosted the 2024 Summer Olympics?', ['Japan', 'USA', 'France', 'Australia'], 2),
        ('Which technology is currently dominating headlines for its generative capabilities?', ['Blockchain', 'Quantum Computing', 'Artificial Intelligence', '5G'], 2),
        ('What currency is used by the majority of European Union nations?', ['Pound Sterling', 'Franc', 'Euro', 'Lira'], 2),
        ('Which electric vehicle company is led by Elon Musk?', ['Rivian', 'Lucid', 'Tesla', 'Ford'], 2),
        ('What is the name of the international space station program?', ['Mir', 'Skylab', 'ISS', 'Tiangong'], 2),
        ('Which tech company produces the iPhone?', ['Google', 'Samsung', 'Microsoft', 'Apple'], 3),
        ('What social media platform was formerly known as Twitter?', ['Threads', 'Bluesky', 'X', 'Mastodon'], 2),
        ('What global issue involves the rise in Earth\'s average temperature?', ['Deforestation', 'Ozone depletion', 'Global Warming', 'Ocean acidification'], 2)
    ],
    'Computer Science': [
        ('What does CPU stand for?', ['Computer Processing Unit', 'Central Processing Unit', 'Central Process Unit', 'Computer Personal Unit'], 1),
        ('Which of these is a popular programming language?', ['Cobra', 'Python', 'Viper', 'Anaconda'], 1),
        ('What is the main function of an operating system?', ['To run games', 'To manage hardware and software resources', 'To connect to the internet', 'To act as an antivirus'], 1),
        ('What does HTML stand for?', ['Hyper Text Markup Language', 'High Tech Machine Learning', 'Hyperlink and Text Markup Language', 'Home Tool Markup Language'], 0),
        ('What is a bit?', ['A small piece of data', 'A binary digit (0 or 1)', 'A bite of an apple', 'A type of computer bug'], 1),
        ('Which data structure uses LIFO (Last In, First Out)?', ['Queue', 'Linked List', 'Stack', 'Tree'], 2),
        ('What does SQL denote?', ['Standard Query Language', 'Structured Query Language', 'Simple Question Language', 'System Query Logic'], 1),
        ('What is the term for a flaw in a program that causes it to behave incorrectly?', ['Glitch', 'Virus', 'Bug', 'Feature'], 2),
        ('What is commonly considered the brain of the computer?', ['RAM', 'Hard Drive', 'Motherboard', 'CPU'], 3),
        ('Which protocol is used for secure communication over a computer network?', ['HTTP', 'FTP', 'HTTPS', 'SMTP'], 2)
    ],
    'Space': [
        ('What is the closest planet to the Sun?', ['Venus', 'Earth', 'Mercury', 'Mars'], 2),
        ('Which planet is known as the Red Planet?', ['Jupiter', 'Saturn', 'Mars', 'Uranus'], 2),
        ('What is the largest planet in our solar system?', ['Earth', 'Saturn', 'Jupiter', 'Neptune'], 2),
        ('What is the name of our home galaxy?', ['Andromeda', 'Milky Way', 'Sombrero', 'Triangulum'], 1),
        ('What force keeps planets in orbit around the Sun?', ['Magnetism', 'Friction', 'Gravity', 'Centrifugal force'], 2),
        ('Who was the first person to walk on the moon?', ['Buzz Aldrin', 'Yuri Gagarin', 'Neil Armstrong', 'Michael Collins'], 2),
        ('What is a supernova?', ['A new star forming', 'A star exploding', 'A black hole', 'A comet passing by'], 1),
        ('How many moons does Earth have?', ['Zero', 'One', 'Two', 'Three'], 1),
        ('What is the celestial body we orbit called?', ['The Moon', 'The Sun', 'Jupiter', 'Alpha Centauri'], 1),
        ('What is the Great Red Spot on Jupiter?', ['A giant volcano', 'A vast ocean', 'A massive storm', 'A crater'], 2)
    ]
}

def populate_db():
    print("Clearing existing questions...")
    Question.objects.all().delete()
    
    print("Populating database...")
    for category_name, questions in quiz_data.items():
        print(f"Adding questions for {category_name}...")
        for q_text, options_list, correct_idx in questions:
            question = Question.objects.create(category=category_name, text=q_text)
            for idx, opt_text in enumerate(options_list):
                is_curr = (idx == correct_idx)
                Option.objects.create(question=question, text=opt_text, is_correct=is_curr)
                
    print(f"Successfully added {Question.objects.count()} questions across all categories!")

if __name__ == '__main__':
    populate_db()
