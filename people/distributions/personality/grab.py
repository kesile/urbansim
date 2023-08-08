import random
def coin(): return round(random.randint(1,2))

def flipReturn(val, alt):
    flip = coin()
    if flip == 1: return alt
    else: return val

def rollPersonality():
    energy = flipReturn("E", "I") # Extroverted vs Intuitive
    perception = flipReturn("S", "N") # Sensing vs Intuition
    decision = flipReturn("T", "F") # Thinking vs Feeling
    adaptive = flipReturn("J", "P") # Judging vs Percieving
    # expression = flipReturn("C", "D") # Convergent vs Divergent
    # response = flipReturn("H", "A") # Rock vs Adaptable

    personality = energy + perception + decision + adaptive # + expression + response
    return personality

def translator(name, personality):
    personParagraph = ""
    for trait in personality:
        match trait:
            case "E":
                personParagraph = personParagraph + f"{name} is an extroverted individual, who thrives in social settings and enjoys interacting with people from all walks of life. They get their energy from social situations and are invigorated by the company of others. {name}'s friendly and approachable nature makes it easy for them to initiate conversations and build connections with people effortlessly. Their vibrant energy and enthusiasm are infectious, and they often become the life of the party, bringing joy and laughter wherever they go. {name} is not afraid of being the center of attention and is often sought after for their engaging and charismatic presence. They find great fulfillment in being surrounded by friends and acquaintances, and their wide social circle reflects their ability to connect with people on various levels. {name}'s extroverted nature enables them to excel in roles that involve teamwork, public speaking, and networking."
            case "I": 
                personParagraph = personParagraph + f"{name} is an introverted individual, who, while they enjoy talking to others, finds their energy renewed through solitude and introspection. They often seek out quiet and peaceful environments where they can reflect, recharge, and delve deep into their thoughts and emotions. {name} values meaningful one-on-one connections and prefers to have a few close and trusted friends rather than a large social circle. Their ability to listen attentively and empathize with others makes them great confidants and sources of support. {name} may appear reserved or shy in social situations, but once they feel comfortable, they open up and share their insights and creativity. Their introspective nature allows them to explore their inner world and develop a rich inner life. {name}'s independent and self-reliant nature enables them to pursue personal interests and hobbies in depth, often excelling in areas that require focus and solitary work."
            case "S":
                personParagraph = personParagraph + f" {name} is a sensing individual, who is grounded in the present and pays close attention to their surroundings. They have a keen eye for detail and prefer practical solutions to problems. {name} trusts their senses and relies on tangible evidence when making decisions. They are highly observant and often notice things that others might miss. {name}'s realistic and pragmatic approach makes them reliable and capable in handling day-to-day tasks. They are not easily swayed by abstract concepts or hypothetical scenarios but instead focus on what is happening in the here and now. {name}'s practicality and hands-on skills make them adept at various crafts, and they excel in fields that require attention to detail and precision."
            case "N":
                personParagraph = personParagraph + f" {name} is an intuitive individual, who is imaginative and focused on the big picture. They enjoy exploring abstract ideas and possibilities beyond the realm of the immediate environment. {name} often trusts their gut feelings and instincts when making decisions, relying on their intuition to guide them. They are visionary thinkers who can see potential connections and patterns that others may overlook. {name}'s open-mindedness and curiosity lead them to seek out new experiences and ideas, often gravitating toward creative or intellectual pursuits. They enjoy discussing philosophical and theoretical concepts and are not afraid to challenge conventional thinking. {name}'s visionary outlook makes them well-suited for fields that involve strategic planning, innovative problem-solving, and exploring uncharted territory."
            case "T":
                personParagraph = personParagraph + f" {name} is a thinking individual, who values logical reasoning and objective analysis. They prioritize rationality and accuracy in their decision-making process. {name} is not swayed by emotions but instead relies on data and facts to arrive at conclusions. They are skilled at breaking down complex problems into manageable components and evaluating them objectively. {name}'s ability to remain impartial and make tough choices based on reason makes them effective leaders and problem solvers. While they may come across as reserved or direct in their communication, {name}'s intentions are rooted in seeking the truth and finding the best solutions. Their penchant for critical thinking and logical analysis makes them well-suited for fields such as science, engineering, and law."
            case "F":
                personParagraph = personParagraph + f" {name} is a feeling individual, who values empathy and considers the emotions of others in their decision-making process. They have a deep sense of compassion and are skilled at understanding and relating to people's feelings. {name} often prioritizes harmony and emotional well-being in their relationships and interactions. They are sensitive to the needs of others and often take on a nurturing and supportive role in their social circles. {name}'s emotional intelligence and ability to create meaningful connections make them excellent team players and mediators. They may find fulfillment in creative pursuits or careers that involve helping and making a positive impact on others' lives."
            case "J":
                personParagraph = personParagraph + f" {name} is a judging individual, who prefers structure and organization in their life. They like to plan ahead and set clear goals for themselves. {name} is reliable and committed to meeting deadlines and fulfilling their responsibilities. They have a strong sense of discipline and often thrive in environments where rules and routines are established. 's decision-making process is systematic and methodical, as they carefully consider all options before reaching a conclusion. Their preference for closure and decisiveness makes them effective leaders and managers. {name}'s attention to detail and strong work ethic enable them to excel in fields that require precision and order."
            case "P":
                personParagraph = personParagraph + f" {name} is a perceiving individual, who embraces spontaneity and prefers to keep their options open. They enjoy flexibility and are adaptable to changing circumstances. {name} thrives in environments that allow them to explore different possibilities and ideas. They are curious and open to new experiences, often seeking novelty and excitement. {name}'s ability to think on their feet and adapt quickly makes them resourceful problem solvers. They enjoy living in the present moment and may find planning and structure too restrictive. {name}'s creative and innovative nature makes them well-suited for fields that involve exploration and experimentation."
    
    rudeness = round(random.randint(1,5))
    match rudeness: 
        case 1:
            personParagraph = personParagraph + f" {name} is a very nice person, and talks as such."
        case 2:
            personParagraph = personParagraph + f" {name} is a nice person, but is very occassionally unaware of how their words affect others."
        case 3:
            personParagraph = personParagraph + f" {name} is good at heart, but often says things without thinking about how they'll affect others."
        case 4:
            personParagraph = personParagraph + f" {name} is sometimes nice, but often says mean things, whether on purpose or on accident."
        case 5:
            personParagraph = personParagraph + f" {name} is very mean, and will attempt to say rude things to hurt people often.."
    return personParagraph 

def grabPersonality(name):
    return translator(name, rollPersonality()) 