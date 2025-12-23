# Imagen Skill Reference

## Setup

### 1. Get a Gemini API Key

1. Go to [Google AI Studio](https://aistudio.google.com/)
2. Click "Get API Key"
3. Create a new API key or use an existing one

### 2. Set Environment Variable

**Windows (PowerShell):**
```powershell
$env:GEMINI_API_KEY = "your-api-key-here"

# To persist across sessions, add to your PowerShell profile:
Add-Content $PROFILE "`n`$env:GEMINI_API_KEY = 'your-api-key-here'"
```

**Windows (CMD):**
```cmd
set GEMINI_API_KEY=your-api-key-here

# To persist, use System Properties > Environment Variables
```

**macOS/Linux:**
```bash
export GEMINI_API_KEY="your-api-key-here"

# Add to ~/.zshrc or ~/.bashrc to persist
echo 'export GEMINI_API_KEY="your-api-key-here"' >> ~/.zshrc
```

## API Reference

### Model

- **Model ID**: `gemini-3-pro-image-preview` (configurable via `--model` flag or `GEMINI_MODEL` env var)
- **Endpoint**: `https://generativelanguage.googleapis.com/v1beta/models/{model}:streamGenerateContent`

### Image Sizes

| Size | Description |
|------|-------------|
| `512` | 512x512 pixels - Fast, good for icons/thumbnails |
| `1K` | 1024x1024 pixels - Default, balanced quality/speed |
| `2K` | 2048x2048 pixels - High resolution, slower |

## Script Parameters

### Python Script (Cross-Platform)

```bash
python scripts/generate_image.py <prompt> [output_path] [--size SIZE]
```

| Parameter | Required | Default | Description |
|-----------|----------|---------|-------------|
| `prompt` | Yes | - | Text description of desired image |
| `output_path` | No | `./generated-image.png` | Where to save the image |
| `--size` | No | `1K` | Image size (512, 1K, or 2K) |

### Environment Variables

| Variable | Required | Default | Description |
|----------|----------|---------|-------------|
| `GEMINI_API_KEY` | Yes | - | Your Google Gemini API key |
| `IMAGE_SIZE` | No | `1K` | Image size (512, 1K, or 2K) |

## Usage Examples

### Basic Generation

```bash
python scripts/generate_image.py "A serene mountain landscape at dawn"
```

### Custom Output Path

```bash
python scripts/generate_image.py "Minimalist logo design" "./assets/logo.png"
```

### High Resolution

```bash
python scripts/generate_image.py --size 2K "Detailed portrait" "./high-res.png"
```

### Small/Fast Generation

```bash
python scripts/generate_image.py --size 512 "Simple icon" "./icon.png"
```

## Prompt Tips

### For Best Results

1. **Be specific**: "A red sports car" vs "A cherry red 1967 Mustang convertible"
2. **Include style**: "in watercolor style", "photorealistic", "minimalist flat design"
3. **Mention lighting**: "golden hour lighting", "soft diffused light", "dramatic shadows"
4. **Specify composition**: "close-up", "wide angle", "from above", "centered"

### Example Prompts by Use Case

**UI/Frontend:**
- "A modern dashboard UI mockup with dark theme, showing analytics charts"
- "Clean minimalist app icon for a task management app, rounded square shape"
- "Hero image for a SaaS landing page, abstract gradient with geometric shapes"

**Documentation:**
- "Simple architecture diagram showing microservices connected by arrows"
- "Flowchart illustrating user authentication process"

**Placeholders:**
- "Professional headshot placeholder, silhouette style, neutral gray background"
- "Product image placeholder, simple box shape with 'Image Coming Soon' text"

**Marketing/Creative:**
- "Isometric illustration of a modern office workspace"
- "Gradient abstract background suitable for presentation slides"

## Troubleshooting

### "GEMINI_API_KEY not set"
Ensure the environment variable is set in your current shell:

**Windows (PowerShell):**
```powershell
echo $env:GEMINI_API_KEY  # Should show your key
```

**macOS/Linux:**
```bash
echo $GEMINI_API_KEY  # Should show your key
```

### "API request failed with HTTP status 400"
- Check your prompt for special characters that may break JSON
- Ensure the prompt isn't empty
- Verify API key is valid

### "API request failed with HTTP status 429"
- Rate limited - wait a moment and retry
- Consider upgrading your API quota

### "No image data found in response"
- The model may have refused the prompt (content policy)
- Try rephrasing the prompt
- Check if the model returned an error message in the response

### Image is corrupted/won't open
- Ensure Python 3.6+ is installed
- Check if the full response was received (network issues)
- Verify output path is writable

### Windows-specific issues
- Make sure Python is in your PATH
- Use forward slashes or escaped backslashes in paths

## API Costs

Check [Google AI pricing](https://ai.google.dev/pricing) for current Gemini API costs. Image generation typically costs more than text generation.

## Limitations

- Maximum prompt length varies by model
- Some content types may be restricted by Google's content policy
- Generated images are subject to Google's terms of service
- Rate limits apply based on your API tier
