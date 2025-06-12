# GPT Image 1 – Prompt-based Image Transformation

This project demonstrates the use of **OpenAI's GPT Image 1** model to generate new images from existing ones using two distinct prompts.

## 📌 Overview

- ✅ Input: 10 original images
- 🔁 Process: Each image processed with **2 different prompts**
- 🖼️ Output: 20 AI-generated images (2 per input)
- 🕒 Logged: Inference time per image
- 📊 Analyzed: 
  - Average processing time
  - Estimated throughput (images per minute/hour)
  - Cost per image and total project cost
  - Impact of input image size on speed

## 📂 Files

- `/outputs/` — folder with all generated images (`*_v1.png`, `*_v2.png`)
- `timing_log.csv` — duration of each inference
- `report_summary.txt` — summary of findings (speed, cost, scaling limits)

## 💡 Key Findings

- Average image generation time: **~30.2 seconds**
- Estimated throughput: **~2 images/min or 119 images/hour**
- Cost per image (medium quality, 1536×1024): **$0.063**
- Total cost for 20 images: **$1.26**
- Input image size affects processing speed
- API Tier level (IPM limit) may throttle real-world performance

## 🛠️ Tech Stack

- `OpenAI GPT Image 1 API`
- `Python (PIL, pandas)`
- `Streamlit` (planned for frontend demo)

## 📎 Report & Results

- 📄 report_summary.md
- 📁 [Output folder with images & logs]
