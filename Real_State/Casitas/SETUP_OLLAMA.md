# Ollama Setup Guide for Casitas

This guide explains how to set up Ollama (local LLM) for the Casitas real estate scoring pipeline.

## What is Ollama?

Ollama allows you to run large language models locally on your machine without cloud APIs. For Casitas, we use **Mistral 7B** — a fast, capable open-source model that runs CPU-only or GPU-accelerated.

**Benefits:**
- ✅ No API costs (runs on your hardware)
- ✅ No internet dependency
- ✅ Full privacy (data stays local)
- ✅ Fast on modern laptops
- ⚠️ Slower than cloud APIs without GPU

---

## Installation

### macOS

**Option 1: Homebrew (Recommended)**
```bash
brew install ollama
```

**Option 2: Direct Download**
- Visit https://ollama.ai
- Download `.dmg` file
- Drag to Applications

**Start Ollama (after installation):**
```bash
# Ollama runs as a background service automatically
# Or manually:
ollama serve
```

### Linux (Ubuntu/Debian)

```bash
curl https://ollama.ai/install.sh | sh

# Start daemon
systemctl start ollama
systemctl enable ollama  # Auto-start on boot
```

### Windows

- Download `.exe` from https://ollama.ai
- Run installer
- Ollama starts automatically in background (system tray)

---

## Download Model (First Time Only)

**Mistral 7B** (7 billion parameters) is ideal for Casitas:
- Fast: 8-15s per property on CPU-only
- Good quality: Better than Llama2, competitive with larger models
- Size: ~5GB RAM, ~4.5GB disk

```bash
ollama pull mistral
```

**Alternative Models** (if you prefer):
```bash
ollama pull llama2           # Larger, slower (~13B params)
ollama pull neural-chat      # Smaller, faster (~7B params)
ollama pull dolphin-mixtral  # More capable (~8x7B mixture)
```

---

## Verify Installation

### Test 1: Check Ollama Running
```bash
curl http://localhost:11434/api/tags
```
**Expected:** JSON list of models

### Test 2: Quick Test
```bash
ollama run mistral "What is 2+2?"
```
**Expected:** Response from Mistral model

### Test 3: Python Integration
```python
import ollama

response = ollama.chat(
    model="mistral",
    messages=[{"role": "user", "content": "Hello"}]
)
print(response["message"]["content"])
```

---

## Performance Tuning

### Check Hardware

```bash
# macOS
sysctl -a | grep -i core
# Shows number of CPU cores

# Linux
nproc

# Check GPU
ollama list --verbose
# Shows if GPU acceleration is available
```

### CPU-Only (Default)

```bash
# No additional configuration needed
# Will use all available CPU cores automatically
```

### GPU Acceleration

**NVIDIA (CUDA):**
```bash
# Install CUDA Toolkit first
# https://developer.nvidia.com/cuda-downloads

# Ollama will auto-detect and use GPU
ollama serve  # Should show "Using CUDA device"
```

**Apple Silicon (M1/M2/M3):**
```bash
# Metal acceleration automatic on macOS 12.6+
ollama serve  # Should show "Using Metal"
```

**AMD (ROCm):**
```bash
# Advanced setup required
# See https://github.com/ollama/ollama/blob/main/docs/linux.md
```

### Memory Management

If system runs out of RAM during scoring:

```bash
# Reduce Ollama context window (default 2048)
# Edit ~/.ollama/models/mistral/Modelfile or use:

ollama run mistral --num-ctx 1024
# 1024 token context vs default 2048 (faster but less context)

ollama run mistral --num-gpu 0
# Force CPU-only (if GPU causing issues)
```

---

## Running Casitas Scoring

### Step 1: Ensure Ollama is Running

```bash
# In one terminal, keep running:
ollama serve

# Or verify it's already running:
curl http://localhost:11434/api/tags | grep mistral
```

### Step 2: Run Scoring Script

```bash
cd /path/to/Casitas
python src/scoring.py

# Expected output:
# ✅ Ollama available. Models: ['mistral']
# ✅ Buy Box loaded from config/buy_box_malaga_2026.md
# Archivo cargado: data/processed/activos_20260524_1341.csv
# Propiedades a evaluar: 136
# [1/136] Piso en venta en Centro...
# ✓ Score: 94.0 — oportunidad fuerte
```

### Step 3: Monitor Performance

```bash
# In another terminal, check memory usage:
watch -n 1 "ps aux | grep ollama"

# Check CPU load:
top  # or Activity Monitor on macOS
```

---

## Troubleshooting

### Issue: "Connection refused" (Ollama not running)

```
Error: failed to connect to http://localhost:11434
```

**Solution:**
```bash
# Start Ollama in foreground to see errors
ollama serve

# If stuck, try:
killall ollama
ollama serve
```

### Issue: "Model not found"

```
Error: model "mistral" not found
```

**Solution:**
```bash
ollama pull mistral
ollama list  # Verify it downloaded
```

### Issue: Out of Memory

```
CUDA Error: out of memory
# or
OOM (system swap overloaded)
```

**Solution:**
```bash
# Reduce model quantization (use smaller version)
ollama pull mistral:7b-q4  # Quantized version (more compression)

# Or reduce context window
ollama run mistral --num-ctx 512
```

### Issue: Very Slow Scoring (>30s per property)

**Diagnosis:**
- Is GPU being used? Check `ollama serve` output
- How many CPU cores? `nproc` or sysctl
- Is system doing other work? Check Activity Monitor / top

**Solutions:**
```bash
# 1. Force CPU-only (disable GPU debugging)
export CUDA_VISIBLE_DEVICES=""
ollama serve

# 2. Use smaller model
ollama pull mistral:7b-q4
# Edit src/scoring.py: MODEL_NAME = "mistral:7b-q4"

# 3. Use faster model
ollama pull neural-chat
# Edit src/scoring.py: MODEL_NAME = "neural-chat"

# 4. Check for background processes
# Close browsers, IDEs, etc. consuming CPU
```

### Issue: JSON Parse Errors

```
ValueError: No JSON object found in model response
```

**Solution (Rare):**
```bash
# Mistral occasionally returns non-JSON
# Script has retry logic, but if persistent:

# Try a different model
ollama pull neural-chat
# Edit src/scoring.py: MODEL_NAME = "neural-chat"

# Re-run scoring
python src/scoring.py
```

---

## Expected Scoring Times

| Setup | Time per Property | Total for 136 | Hardware |
|-------|-------------------|---------------|----------|
| CPU-only (4 cores) | 15-20s | 35-45 min | MacBook Air M1 |
| CPU (8 cores) | 10-15s | 23-35 min | Intel i7/i9 |
| NVIDIA GPU | 3-5s | 7-12 min | RTX 4060+ |
| Apple Metal (M1/M2) | 5-8s | 12-18 min | MacBook Pro M1/M2 |

**Your first run:** Slightly slower (OS caching). Subsequent runs faster.

---

## Production Tips

### Automate Scoring

**On macOS (cron):**
```bash
# Add to crontab
crontab -e

# Run scoring every Sunday at 2 AM
0 2 * * 0 cd /path/to/Casitas && python src/scoring.py >> data/output/scoring.log 2>&1
```

**Keep Ollama Running:**
```bash
# macOS (LaunchAgent)
# Create ~/Library/LaunchAgents/com.ollama.plist with:
<?xml version="1.0" encoding="UTF-8"?>
<plist version="1.0">
<dict>
  <key>Label</key>
  <string>com.ollama</string>
  <key>ProgramArguments</key>
  <array>
    <string>/usr/local/bin/ollama</string>
    <string>serve</string>
  </array>
  <key>RunAtLoad</key>
  <true/>
</dict>
</plist>

# Load it:
launchctl load ~/Library/LaunchAgents/com.ollama.plist
```

### Monitor Scoring

```bash
# Watch progress in real-time
tail -f data/output/ranking_final_*.csv

# Check for errors
tail -f data/output/scoring_errors_*.csv
```

### Clean Ollama Cache (if space-constrained)

```bash
# Remove downloaded models
ollama rm mistral

# Verify
ollama list

# Re-download only what you need
ollama pull mistral
```

---

## References

- **Ollama Docs:** https://github.com/ollama/ollama
- **Mistral Model:** https://mistral.ai/
- **Model Performance:** https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard
- **Quantization Guide:** https://github.com/ggerganov/llama.cpp/wiki/Quantization

---

**Last Updated:** 2026-07-24  
**Casitas Version:** 1.1
