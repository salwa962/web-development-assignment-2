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
    
    <p>
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
<p>
    Amidst the devastation of war in Aleppo, thirteen-year-old Noor finds resilience and hope with her family, dreaming of a new dawn for their city.
    
    <p>
        Amidst the devastation of war in Aleppo, thirteen-year-old Noor finds resilience and hope with her family, dreaming of a new dawn for their city.
    </p>""",
        # Add more stories here
    }

    for i, (story_id, story_text) in enumerate(stories.items(), 1):
        file_name = f"story_{i}.mp3"
        save_story_to_audio(story_text, file_name)
        print(f"Saved {file_name}")
