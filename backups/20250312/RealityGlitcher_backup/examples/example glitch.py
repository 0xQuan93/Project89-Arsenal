from modules import sensory_overload, cognitive_dissonance, reality_distortion

# Generate visual noise
sensory_overload.generate_visual_noise(800, 600)

# Generate contradictory statement
belief_system = {
    "belief1": "The world is flat.",
    "belief2": "The Earth is the center of the universe.",
    "belief3": "Humans are inherently evil."
}
contradictory_statement = cognitive_dissonance.generate_contradictory_statements(belief_system)
print(contradictory_statement)

# Distort image
distorted_image = reality_distortion.distort_image("input.jpg", "wave")
cv2.imshow("Distorted Image", distorted_image)
cv2.waitKey(0)
cv2.destroyAllWindows()