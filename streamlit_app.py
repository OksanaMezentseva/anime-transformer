import os
import base64
import time
from PIL import Image
from dotenv import load_dotenv
import streamlit as st
from openai import OpenAI, RateLimitError
import pandas as pd
from concurrent.futures import ThreadPoolExecutor, as_completed

# Load API key from .env
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# App title
st.title("🎨 Anime Transformer with GPT-Image-1")

# Load prompts
with open("data/prompt.txt", "r", encoding="utf-8") as f:
    prompts = [line.strip() for line in f if line.strip()]

if len(prompts) < 2:
    st.error("You must have at least 2 prompts in prompt.txt.")
    st.stop()

prompt1, prompt2 = prompts[:2]

# Load image files
image_dir = "data"
images = sorted([
    f for f in os.listdir(image_dir)
    if f.lower().endswith((".png", ".jpg", ".jpeg"))
])

# Create output directory
os.makedirs("outputs", exist_ok=True)

# Select image quality
quality = st.selectbox("Select image generation quality:", ["high", "medium", "low", "auto"], index=0)

# Safe OpenAI call with retry on rate limit
def safe_image_edit(img_path, prompt, quality):
    while True:
        try:
            with open(img_path, "rb") as img_file:
                return client.images.edit(
                    model="gpt-image-1",
                    image=[img_file],
                    prompt=prompt,
                    size="auto",
                    quality=quality,
                    n=1
                )
        except RateLimitError:
            wait_time = 60
            st.warning(f"⚠️ Rate limit exceeded. Waiting {wait_time} seconds...")
            time.sleep(wait_time)

# Image processing function
def process_image(img_name, prompt, version, quality):
    img_path = os.path.join(image_dir, img_name)
    start = time.time()

    response = safe_image_edit(img_path, prompt, quality)
    duration = time.time() - start

    # Decode image
    b64_image = response.data[0].b64_json
    img_data = base64.b64decode(b64_image)

    # Save image
    output_filename = f"{os.path.splitext(img_name)[0]}_v{version}.png"
    output_path = os.path.join("outputs", output_filename)
    with open(output_path, "wb") as f:
        f.write(img_data)

    return {
        "filename": output_filename,
        "img_name": img_name,
        "version": version,
        "prompt": prompt[:40],
        "duration": round(duration, 2)
    }

# Main logic
if st.button("🚀 Start Transformation"):
    if not images:
        st.warning("No images found in the 'data/' folder.")
    else:
        start_time = time.time()
        timing_log = []
        futures = []

        progress_bar = st.progress(0, text="Processing...")

        # Use one thread (safe with rate limits)
        with ThreadPoolExecutor(max_workers=1) as executor:
            for img_name in images:
                for i, prompt in enumerate([prompt1, prompt2], start=1):
                    futures.append(executor.submit(process_image, img_name, prompt, i, quality))

            results = []
            for idx, future in enumerate(as_completed(futures), start=1):
                result = future.result()
                results.append(result)

                # Log duration
                timing_log.append({
                    "Image": result["img_name"],
                    "Version": result["version"],
                    "Prompt": result["prompt"],
                    "Duration (sec)": result["duration"]
                })

                progress_bar.progress(idx / len(futures), text=f"{idx} / {len(futures)} completed")

        elapsed = time.time() - start_time
        st.success(f"✅ All done in {elapsed:.2f} seconds!")

        # Show and save timing log
        if timing_log:
            st.subheader("🕓 Timing Log")
            df = pd.DataFrame(timing_log)
            st.dataframe(df)

            csv_path = "outputs/timing_log.csv"
            df.to_csv(csv_path, index=False)
            st.success(f"📝 Timing log saved to: {csv_path}")