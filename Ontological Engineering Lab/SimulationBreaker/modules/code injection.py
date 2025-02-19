def inject_code(target_system, code_snippet):
    """Injects code into the target system."""
    print(f"Injecting code into {target_system}: {code_snippet}")

if __name__ == "__main__":
    # Example usage
    target_system = "traffic_lights"
    code_snippet = "for light in lights: light.turn_green()"
    inject_code(target_system, code_snippet)