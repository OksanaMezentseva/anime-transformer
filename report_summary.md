# 🧾 GPT Image 1 – Image Generation Report

## Project Overview

This report summarizes the results of using OpenAI's **GPT Image 1** model to generate images from 10 input files using **two different prompts** per image.

A total of **20 images** were generated and stored, and the **inference time was logged** for each image. The results were then analyzed in terms of speed, cost, and scalability.

---

## ⚙️ Processing Details

- Number of input images: **10**
- Number of output images: **20** (2 per input using 2 prompts)
- Resolution used: **1536 × 1024**
- Quality: **Medium**

---

## 🕒 Performance Summary

- **Average image generation time:** ~30.2 seconds
- **Estimated throughput:**
  - ~2 images per minute
  - ~119 images per hour

> ⚠️ Larger input images took longer to process.  
> For example, `1.png` (1354×903) had longer inference time compared to others (mostly 400×400).  
> GPT Image 1 processes pixel data as tokens — so more pixels = more compute = slower generation.

---

## 💰 Cost Breakdown

- **Medium quality image (1536×1024):** $0.063 per image
- **Total for 20 images:** $1.26

> ⬆️ If high quality was selected instead, the cost would be **$0.25 per image** → **$5.00 total**

---

## 📉 API Rate Limit Impact

Real-world performance is also affected by **OpenAI API rate limits** depending on your **usage Tier**:

| Tier     | Tokens/Minute (TPM) | Image Requests/Minute (IPM) |
|----------|----------------------|------------------------------|
| Tier 1   | 100,000              | 5                            |
| Tier 2   | 250,000              | 20                           |
| Tier 3   | 800,000              | 50                           |
| Tier 4   | 3,000,000            | 150                          |
| Tier 5   | 8,000,000            | 250                          |

Even if model speed allows for 2 images/minute, your **IPM limit may be the bottleneck**, especially in lower tiers.

---

## 📁 Output Files

- `outputs/` — contains all generated images (`1_v1.png`, `1_v2.png`, ..., `10_v2.png`)
- `timing_log.csv` — includes duration of each generation step

---

## 📌 Conclusion

- GPT Image 1 provides high-quality, consistent results
- Processing time is acceptable (~30 sec per image)
- Cost is reasonable at medium quality
- Input image size and API Tier level impact speed and scalability
