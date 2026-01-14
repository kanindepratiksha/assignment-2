import json
import os
from crew import create_crew


def main():
    user_story = (
        "As a customer, I want to add products to my shopping cart and modify quantities, "
        "so that I can purchase multiple items in a single order."
    )

    crew = create_crew(user_story)
    result = crew.kickoff()

    # Get raw output
    output_data = (
        result.raw if hasattr(result, "raw")
        else result.final_output
    )

    # 🔥 FIX: Convert string → dict if needed
    if isinstance(output_data, str):
        output_data = json.loads(output_data)

    os.makedirs("output", exist_ok=True)

    with open("output/sample_output.json", "w", encoding="utf-8") as f:
        json.dump(output_data, f, indent=2)

    print("✅ sample_output.json written correctly")


if __name__ == "__main__":
    main()
