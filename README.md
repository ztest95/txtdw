# Text to Desktop Wallpaper

A Python application that converts text into images and automatically sets them as your desktop wallpaper. The application watches for changes to a text file and dynamically generates a new wallpaper image whenever the text is modified.

## Features

- 🖼️ **Real-time text-to-image conversion**: Automatically generates images from text input
- 👀 **File watching**: Monitors `input.txt` for changes and regenerates the image instantly
- 🎨 **Customizable appearance**: Configure colors, fonts, and dimensions through a config file
- 🖥️ **Automatic wallpaper setting**: Sets the generated image as your desktop background (Windows)
- 📝 **Live editing**: Opens Notepad for real-time text editing with instant preview

## Requirements

- Python 3.x
- Windows OS (for automatic wallpaper setting)
- Arial font (typically pre-installed on Windows)

## Installation

1. Clone or download this repository
2. Create a virtual environment:
   ```bash
   python -m venv .venv
   ```
3. Activate the virtual environment:
   ```bash
   .venv\Scripts\activate
   ```
4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Quick Start

1. Run the application:
   double-click `run.bat` for a convenient shortcut or run
   ```bash
   python run.py
   ```

   This will:
   - Start the file watcher
   - Open `input.txt` in Notepad
   - Generate an image from the current text
   - Set it as your wallpaper when you close Notepad

2. Edit the text in Notepad - the wallpaper will update automatically as you save changes

3. Close Notepad when finished - the final image will be set as your wallpaper

## Configuration

Edit `config.txt` to customize the appearance:

```plaintext
desktop_height = 1200      # Output image height
desktop_width = 1920       # Output image width
background_color = black   # Background color (black, white, red, etc.)
text_position = center     # Text position (currently unused)
text_alignment = left      # Text alignment (currently unused)
text_color = white         # Text color
text_size = 64            # Font size in pixels
```

## File Structure

```
txt2img/
├── run.py              # Main application entry point
├── config.txt          # Configuration file
├── input.txt           # Your text input (edit this file)
├── input.sample.txt    # Sample text file
├── output.png          # Generated wallpaper image
├── requirements.txt    # Python dependencies
├── src/
│   ├── to_image.py     # Text-to-image conversion logic
│   └── watcher.py      # File monitoring system
└── README.md          # This file
```

## How It Works

1. **File Monitoring**: The `watcher.py` uses the `watchdog` library to monitor changes to `input.txt`
2. **Image Generation**: When changes are detected, `to_image.py` creates a new image using PIL (Pillow)
3. **Text Rendering**: The text is rendered with the specified font, size, and color onto a background
4. **Wallpaper Setting**: The generated image is automatically set as the desktop wallpaper using Windows API

## Dependencies

- **Pillow (PIL)**: Image processing and text rendering
- **psutil**: Process monitoring and management
- **watchdog**: File system event monitoring

## Limitations

- Currently Windows-only for automatic wallpaper setting
- Requires Arial font to be installed
- Text positioning is currently centered only

## Future Improvements

Based on the todo list:
- [ ] Package the application to run without external dependencies
- [ ] Add support for other operating systems
- [ ] Implement dynamic text sizing based on content length
- [ ] Add more text positioning and alignment options

## Example

1. Write some text in `input.txt`:
   ```
   "Good morning!
   Today is a beautiful day"
   ```

2. The application generates an image with this text and sets it as your wallpaper

3. Edit the text and save - your wallpaper updates instantly!


##

*Guided by vibes and machine suggestions.*
