import os
import re
import google.generativeai as genai

model = genai.GenerativeModel("gemini-2.5-flash")

def ask_ai_for_manim_code(user_prompt):
    system_instruction = (
        "You are a strict Manim code generator compiler. Output ONLY valid Python code using the Manim community library. "
        "Do not include any explanations or markdown commentary outside of code blocks. "
        "CRITICAL FONT RULE: Avoid Tex() or MathTex() classes entirely as they cause system dependency crashes. "
        "Use the Text() class exclusively for all textual annotations."
    )
    response = model.generate_content(f"{system_instruction}\n\nUser Request: {user_prompt}")
    return response.text

def extract_python_code(raw_response):
    pattern = rf"{chr(96)}{{3}}(?:python)?\n(.*?)\n{chr(96)}{{3}}"
    match = re.search(pattern, raw_response, re.DOTALL)
    return match.group(1).strip() if match else raw_response.strip()

if __name__ == "__main__":
    print("Generating files...")
    raw_py = ask_ai_for_manim_code("Write a complete Manim scene that visually proves the Pythagorean Theorem. Label sides, shade squares built on each side, and display the identity.")
    with open("pythagoras.py", "w") as f: f.write(extract_python_code(raw_py))
    raw_fourier = ask_ai_for_manim_code("Generate a Manim scene demonstrating how a square wave is built by summing sine harmonics. Show at least 5 terms in different colors, updating step-by-step.")
    with open("fourier_series.py", "w") as f: f.write(extract_python_code(raw_fourier))
    print("Done generating raw files.")
