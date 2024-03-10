import random
import string
from user_db_functions import *

# Function to generate a paragraph of text for specialties
def generate_specialties_paragraph():
    specialties = [
        "Experienced in cybersecurity and implementing secure practices.",
        "Proficient in data analysis and machine learning techniques.",
        "Skilled in front-end development with expertise in JavaScript frameworks.",
        "Experienced in cloud computing and deploying scalable solutions.",
        "Knowledgeable in database management and optimizing query performance.",
        "Expertise in mobile app development for both iOS and Android platforms.",
        "Familiar with agile methodologies and project management tools.",
        "Experienced in network administration and troubleshooting.",
        "Proficient in DevOps practices and continuous integration/continuous deployment (CI/CD).",
        "Skilled in UI/UX design and creating engaging user experiences.",
        "Specializes in mentoring BIPOC individuals and providing support for underrepresented groups.",
        "Passionate about helping LGBTQ+ individuals navigate the tech industry and providing a safe space for all identities.",
        "Dedicated to supporting first-generation college students in their career development and academic journey.",
        "Experienced in mentoring individuals with disabilities and advocating for inclusive practices in tech.",
        "Skilled in guiding veterans transitioning into the tech industry and providing resources for a successful career change."
    ]
    return random.choice(specialties)


# Function to generate a paragraph of text for interests
def generate_interests_paragraph():
    interests = [
        "Passionate about exploring new technologies and their applications.",
        "Interested in cybersecurity and learning about the latest threats and defenses.",
        "Eager to learn more about data science and its real-world applications.",
        "Curious about new developments in artificial intelligence and machine learning.",
        "Excited about the possibilities of blockchain technology and its impact on industries.",
        "Interested in web development and creating dynamic and responsive websites.",
        "Keen on learning about cloud computing and its role in modern IT infrastructure.",
        "Interested in mobile app development and creating innovative mobile solutions.",
        "Curious about the Internet of Things (IoT) and its potential to transform industries.",
        "Passionate about cybersecurity and securing digital assets."
    ]
    return random.choice(interests)





# Function to generate a random string for passwords
def generate_random_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for i in range(length))

# Function to generate a random first name
def generate_random_first_name():
    first_names = [
        "John", "Emma", "Michael", "Sophia", "William", "Olivia", "James", "Ava", "Alexander", "Isabella"
    ]
    return random.choice(first_names)

# Function to generate a random last name
def generate_random_last_name():
    last_names = [
        "Smith", "Johnson", "Brown", "Jones", "Garcia", "Martinez", "Davis", "Rodriguez", "Miller", "Taylor"
    ]
    return random.choice(last_names)

# Function to generate a random location
def generate_random_location():
    states = [
        "California", "Texas", "Florida", "New York", "Illinois", "Pennsylvania", "Ohio", "Georgia", "North Carolina", "Michigan"
    ]
    countries = [
        "USA", "Canada", "UK", "Australia", "Germany", "France", "Japan", "China", "Brazil", "India"
    ]
    state = random.choice(states)
    country = random.choice(countries)
    return f"{state}, {country}"

def generate_self_identifications():
    identifications = [
        "BIPOC", "LGBTQ+", "Disabled", "First-generation college student", "Non-binary", "Transgender", "Veteran", "Single parent", "Caregiver"
    ]
    num_identifications = random.randint(1, 3)  # Generate a random number of identifications (1 to 3)
    return random.sample(identifications, num_identifications)  # Randomly select identifications from the list

# Function to generate a dataset
def generate_users_dataset(num_users):
    dataset = []
    for i in range(num_users):
        user_id_email = f"user_{i}@example.com"
        password = generate_random_password(random.randint(8, 12))
        first_name = generate_random_first_name()
        last_name = generate_random_last_name()
        profile_pic = f"profile_pic_{i}.jpg"
        location = generate_random_location()
        social_media_links = ["facebook.com/johndoe", "twitter.com/johndoe"]
        specialties = generate_specialties_paragraph() if random.random() > 0.5 else None
        interests = generate_interests_paragraph() if random.random() > 0.5 else None
        self_identifications = generate_self_identifications() if random.random() > 0.5 else []
        
        user_data = (user_id_email, [password, first_name, last_name, profile_pic, location, social_media_links, specialties, interests, self_identifications])
        dataset.append(user_data)
    return dataset

# Function to generate a list of self-identifications
def generate_self_identifications():
    identities = ["BIPOC", "LGBTQ+", "First-generation college student", "Individual with disabilities", "Veteran"]
    num_identities = random.randint(1, len(identities))
    return random.sample(identities, num_identities)

# Generate a dataset of users
num_users = 10
users_dataset = generate_users_dataset(num_users)

# Print the dataset
for user_data in users_dataset:
    print(user_data)

if __name__ == "__main__":
    user_db = UserDB()
    my_db = user_db.getDb()
    my_db.drop_collection("users")

    for user_data in users_dataset:
        user_id_email, data = user_data
        password, first_name, last_name, profile_pic, location, social_media_links, specialties, interests, self_identifications = data
        name = f"{first_name} {last_name}"
        email = user_id_email
        user_db.add_user(name, email, password)
        if specialties:
            user_db.make_mentor_profile(user_db.get_id(email), specialties)
        if interests:
            user_db.make_mentee_profile(user_db.get_id(email), interests)
        if self_identifications:
            user_db.update_self_identification(user_db.get_id(email), self_identifications)

