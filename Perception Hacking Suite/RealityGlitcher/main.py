from modules import sensory_overload, cognitive_dissonance, reality_distortion

def induce_glitch(screen_width, screen_height, belief_system, image_path, distortion_type):
    """Induces a glitch by combining sensory overload, cognitive dissonance, and reality distortion."""
    sensory_overload.generate_visual_noise(screen_width, screen_height)
    contradictory_statement = cognitive_dissonance.generate_contradictory_statements(belief_system)
    print(contradictory_statement)
    distorted_image = reality_distortion.distort_image(image_path, distortion_type)
    cv2.imshow("Distorted Image", distorted_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def main():
    screen_width = 800
    screen_height = 600
    belief_system = {
        "belief1": "The world is flat.",
        "belief2": "The Earth is the center of the universe.",
        "belief3": "Humans are inherently evil."
    }
    image_path = "input.jpg"
    distortion_type = "wave"
    induce_glitch(screen_width, screen_height, belief_system, image_path, distortion_type)

if __name__ == "__main__":
    main()