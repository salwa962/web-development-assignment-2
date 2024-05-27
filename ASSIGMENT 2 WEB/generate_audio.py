import pyttsx3

def save_story_to_audio(story_text, file_name):
    engine = pyttsx3.init()
    engine.save_to_file(story_text, file_name)
    engine.runAndWait()

if __name__ == "__main__":
    stories = {
        "story1": """From Home to Hope

    The sun rose over Gaza, casting its golden rays on the shattered remains of Shuja'iyya. Youssef, twelve years old, watched as his family prepared to leave their home for the last time. Their once vibrant neighborhood was now a landscape of ruins, with the echoes of laughter replaced by the distant sounds of conflict.
    
    Youssef’s father, Ahmed, packed what little they could salvage into a few bags. His mother, Fatima, held his younger sister, Leila, close, trying to mask her fear with a brave smile. “We need to move quickly,” Ahmed urged, his voice tight with urgency and sorrow.
    
    They joined a stream of families heading towards the temporary shelters set up on the outskirts of the city. The journey was perilous, with the constant threat of airstrikes hanging over them. But driven by hope for safety, they pressed on.
    
    After hours of walking, they reached a sprawling camp filled with rows of tents. Aid workers distributed food, water, and blankets. Youssef’s family was assigned a small, olive-green tent at the edge of the camp. The tent, with its thin canvas walls, offered little comfort, but it was their new home.
    
    Days turned into weeks. Ahmed found work with the aid organizations, and Fatima joined other women in cooking communal meals. Youssef and Leila made friends among the other displaced children, playing games and attending makeshift classes organized by volunteers. In these moments, they found brief escapes from the harsh realities around them.
    
    One evening, Youssef sat outside the tent with his father. “Do you think we’ll ever go back home?” he asked.
    
    Ahmed placed a reassuring hand on his son’s shoulder. “One day, Inshallah. Home is not just a building, Youssef. It’s our family, our memories, and our dreams. As long as we have each other, we have hope.”
    
    Youssef nodded, comforted by his father’s words. He looked around the camp and saw families sharing meals, children laughing, and neighbors supporting each other. In the face of adversity, the community had come together, their resilience shining through the darkness.
    
    That night, as he lay on the thin mat inside the tent, Youssef closed his eyes and imagined a future where they would return to Shuja'iyya, rebuild their home, and restore their lives. He held onto that vision tightly, knowing that hope was their greatest strength.
    
    And so, amidst the tents and turmoil, Youssef’s story of resilience and hope continued to unfold, proving that even in the darkest times, the light of human spirit could never be extinguished.
    
    </p>
        A family in Gaza finds hope and resilience in a refugee camp after their home is destroyed, united by their love and the belief in a brighter future.
    </p>""",
        "story2": """ A New Dawn in Aleppo
    The morning light barely pierced through the smoky haze over Aleppo. Thirteen-year-old Noor stood at the window of her family's battered apartment, surveying the rubble-strewn streets of her once-vibrant city. Inside, her father, Khaled, boiled water, while her mother, Layla, patched Noor’s only remaining dress. Her younger brother, Sami, played with a makeshift toy car made from discarded scraps.
    
    “Stay close, Noor. We may need to leave quickly,” Khaled warned. The family lived in constant readiness, always prepared to flee at a moment’s notice due to the relentless bombardments. Noor missed school and the normalcy it brought. Now, her education came from stories and lessons shared by her father, a former teacher.
    
    That day, an unusual calm settled over the city as evening approached. Seizing the opportunity, the family ventured to a nearby aid distribution point. The journey was perilous, every step shadowed by the threat of snipers and sudden attacks. At the center, they received bread, water, and a small first aid kit—barely enough to last a few days, but a lifeline nonetheless.
    
    Returning home, Noor noticed the resilience in the faces of those around her. Despite the hardships, a quiet determination bound them together. Back in their apartment, the family shared a simple meal in silence. After dinner, Khaled told a story of a mythical bird rising from the ashes, symbolizing hope and renewal.
    
    “We will rise again, my dear,” Khaled reassured Noor and Sami. “No matter how hard things get, we will rebuild. We will create a new life from the ruins of the old.”
    
    That night, the family huddled together for warmth. Noor lay awake, her father's words echoing in her mind. Despite the destruction, she felt a flicker of hope. She closed her eyes, dreaming of a future where Aleppo would once again be a city of light and laughter.
    
    In the war-torn city, Noor found strength in her family and hope in the promise of a new dawn. As the first light of morning touched the horizon, she knew that no matter the challenges ahead, they would face them together
</p>
    Amidst the devastation of war in Aleppo, thirteen-year-old Noor finds resilience and hope with her family, dreaming of a new dawn for their city.
    
    </p>
        Amidst the devastation of war in Aleppo, thirteen-year-old Noor finds resilience and hope with her family, dreaming of a new dawn for their city.
    </p>""",
        "story3": """Whispers of Change
 Whispers of Change
    In the streets of Khartoum, Sudan, whispers of change stirred the air. Fatima, a university student, felt the pulse of her nation quicken as protests swelled against decades of oppression. With courage in her heart, she joined the swelling crowds, raising her voice for justice and freedom.
    
    As days stretched into weeks, the protests grew, met with violent resistance from the ruling regime. Tear gas and bullets filled the air, but Fatima and her comrades stood firm, their resolve unyielding. Despite the danger, hope burned bright in their eyes, fueling their fight for a better Sudan.
    
    International support bolstered their cause, shining a spotlight on their struggle. And then, a breakthrough: the dictator fell, toppled by the collective will of the people. In the streets, jubilation erupted as Sudan embraced a new dawn of democracy.
    
    But amidst the celebrations, Fatima knew their journey was far from over. The road to true freedom would be fraught with challenges, but with unity and determination, she believed in a Sudan where justice and equality reigned.
    
    In the heart of Khartoum, Fatima stood as a symbol of resilience, her spirit unbroken, her dreams for a brighter Sudan unwavering.</p>
<p>
    In Sudan's streets, Fatima joins a swelling movement for change, enduring violence and oppression, until their collective resilience topples a dictator, igniting hope for a brighter future.
</p>
</p>
</p>""",
"story4": """
The Lantern of Hope

    In a bustling city in China, amidst the towering skyscrapers and bustling streets, there lived a young artist named Mei. Mei had always been captivated by the beauty of her country's rich cultural heritage, but she also saw the shadows that lurked beneath the surface—shadows of censorship, oppression, and silenced voices.
    
    Despite the risks, Mei used her art as a tool for resistance, painting vibrant murals that depicted the struggles and aspirations of her people. Each stroke of her brush was a defiant act, a silent protest against the tightening grip of authoritarian rule.
    
    One evening, as the city slept under a blanket of stars, Mei ventured into a forgotten alleyway, her heart heavy with a sense of urgency. Armed with cans of paint and a vision of hope, she began to work, transforming the drab walls into a canvas of color and defiance.
    
    Her mural depicted a lone figure holding a lantern aloft, its light piercing the darkness that threatened to engulf the city. Beneath the figure were the words: "Hope is a flame that cannot be extinguished."
    
    As Mei worked, a small crowd began to gather, drawn by the power of her art and the message it conveyed. Some watched in awe, while others whispered words of encouragement. For a brief moment, the alleyway became a sanctuary, a space where dreams could flourish and voices could be heard.
    
    But their sanctuary was short-lived. Soon, the authorities arrived, their faces hidden behind masks, their footsteps heavy with menace. They ordered Mei to stop, threatening her with arrest and imprisonment. But Mei refused to back down, her defiance burning brighter than ever.
    
    In a final act of protest, Mei lit a lantern and placed it at the foot of her mural, its flame dancing in the night. As the authorities moved in to extinguish the light, Mei whispered a silent prayer for the future—a future where freedom and justice would reign supreme.
    
    And though they may have silenced her for now, they could never extinguish the flame of hope that burned within her heart. For Mei knew that as long as there were those willing to stand up and speak out, the light of freedom would continue to shine, casting aside the shadows of oppression and illuminating the path towards a brighter tomorrow.</p>
<p>
    In a Chinese city, artist Mei defiantly paints a mural symbolizing hope, facing threats from authorities but igniting a lantern to represent resilience against oppression.
</p>
</p>
</p>""",
"story5": """
Echoes of the Sakura

    In the ancient city of Kyoto, where the whispers of the past mingle with the promises of tomorrow, there lived a young woman named Hiroko. Hiroko’s days were spent amidst the cherry blossoms, their delicate petals dancing on the breeze like fleeting dreams.
    
    But beneath the serene façade of Kyoto, a storm was brewing. The city’s vibrant culture and traditions were threatened by the relentless march of modernity, as skyscrapers loomed over ancient temples and neon lights pierced the night sky.
    
    Hiroko, a fervent defender of her city’s heritage, found herself torn between tradition and progress. As a tour guide, she shared the stories of Kyoto’s rich history with visitors from around the world, hoping to instill in them a deep appreciation for its timeless beauty.
    
    One spring day, as the cherry blossoms bloomed in a riot of pink and white, Hiroko received news that a developer planned to demolish a historic tea house to make way for a luxury hotel. Fueled by a sense of duty to protect her city’s legacy, Hiroko joined forces with fellow activists to protest the project.
    
    Their efforts were met with resistance from the authorities and indifference from some of Kyoto’s residents, who saw progress as inevitable. But Hiroko refused to back down, organizing petitions, rallies, and cultural events to raise awareness and garner support for their cause.
    
    As the battle raged on, Hiroko found solace in the quiet moments spent beneath the sakura trees, their blossoms a reminder of the resilience of nature and the fleeting beauty of life. She knew that change was inevitable, but she refused to let it come at the cost of Kyoto’s soul.
    
    In the end, their perseverance paid off. Through their tireless efforts and unwavering determination, Hiroko and her fellow activists succeeded in saving the tea house, ensuring that future generations would continue to experience the magic of Kyoto’s storied past.
    
    As Hiroko stood amidst the cherry blossoms, their petals swirling around her like confetti, she felt a sense of peace wash over her. Though the battle had been won, she knew that the fight to preserve Kyoto’s heritage would continue. But as long as there were those willing to stand up and defend it, the echoes of the sakura would never fade.
    
    </p>
<p>
    In Kyoto, Hiroko leads a passionate struggle to preserve her city's heritage amidst the encroaching tide of modernity.
</p>
</p>""",

"story6": """
 Echoes of the Fjords

    In the heart of Norway's rugged landscape, where towering mountains meet the crystal waters of the fjords, lies the picturesque village of Flam. Here, amidst the timeless beauty of nature, lives Lars, a young fisherman whose roots run deep in the soil of his ancestors.
    
    As the first light of dawn kisses the horizon, Lars rises with the tide, ready to embark on another day's journey upon the azure waters that have sustained his family for generations. Yet, beneath the tranquil surface of the fjords, echoes of uncertainty ripple through the air.
    
    In recent years, Lars has witnessed the changing currents of his homeland. The once-abundant fish stocks dwindle with each passing season, as warming waters disrupt the delicate balance of nature. Economic pressures loom large as tourism burgeons, bringing with it both prosperity and the erosion of traditional ways of life.
    
    Despite the challenges, Lars remains steadfast in his commitment to the sea, finding solace in the rhythmic motion of the waves and the salty embrace of the ocean breeze. But as he casts his nets into the depths below, he cannot shake the nagging fear that the fjords he holds dear may soon be forever altered by forces beyond his control.
    
    Yet amidst the uncertainty, Lars finds glimmers of hope in the resilience of his community. Together with his fellow villagers, he works tirelessly to adapt to the changing times, embracing sustainable fishing practices and welcoming tourists with open arms, all while striving to preserve the natural beauty that defines their way of life.
    
    In the quiet moments between the ebb and flow of the tide, Lars reflects on the legacy he hopes to leave for future generations. He dreams of a Norway where the fjords remain a sanctuary for both man and nature, where the traditions of the past are cherished and the promise of tomorrow is embraced with optimism and determination.
    
    As the sun sets on another day in Flam, casting hues of crimson and gold across the horizon, Lars returns home with a weary yet hopeful heart. For amidst the echoes of uncertainty that reverberate through the fjords, he knows that as long as there are those like him who are willing to fight for the preservation of their homeland, the spirit of Norway will endure, strong and unyielding, like the mountains that cradle its shores.</p>
<p>
    In the picturesque village of Flam, Norway, Lars, a young fisherman, grapples with environmental changes and economic pressures while striving to preserve his ancestral way of life amidst the timeless beauty of the fjords.
</p>
</p>""",
    }

    for story_id, story_text in stories.items():
        save_story_to_audio(story_text, story_id + ".mp3")

    