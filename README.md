# Evoice - Text-to-Speech & Translation Tool

Evoice is a versatile text-to-speech application that can convert various forms of text input (PDF, images, camera, custom text) into spoken audio in multiple languages.

## Features

- **Multiple Input Methods**:
  - PDF to speech - Extract and read text from PDF files
  - Image to text - Convert text from images using OCR
  - Camera capture - Take pictures and extract text
  - Custom text - Enter text directly for translation and speech

- **Language Support**:
  - Supports 100+ languages for translation and speech synthesis
  - Uses Google Translate API for accurate translations

- **Output Options**:
  - Listen to the translated text immediately
  - Save the audio as an MP3 file for later use

## Requirements

- Python 3.6+
- Required libraries:
  - pyttsx3
  - PyPDF2
  - gtts (Google Text-to-Speech)
  - googletrans
  - PIL (Pillow)
  - pytesseract
  - OpenCV (cv2)
  - playsound

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/evoice.git
   cd evoice
   ```

2. Install required packages:
   ```
   pip install pyttsx3 PyPDF2 gtts googletrans==4.0.0-rc1 Pillow pytesseract opencv-python playsound
   ```

3. Install Tesseract OCR (required for image recognition):
   - For Windows: Download and install from https://github.com/UB-Mannheim/tesseract/wiki
   - For macOS: `brew install tesseract`
   - For Linux: `sudo apt install tesseract-ocr`

## Usage

Run the main script:
```
python Evoice.py
```

Then follow the on-screen instructions to select:
1. The input method (PDF, image, camera, or custom text)
2. The desired output language
3. Whether to listen to the speech or save it as an MP3 file

## File Descriptions

- `Evoice.py` - Main application file with the user interface
- `camera.py` - Module for camera operations and image capture
- `lang.py` - Contains language dictionaries and selection functionality
- `speak.py` - Text-to-speech conversion utilities
- `save.py` - Functions for saving audio output as MP3
- `pdf_reader.py` - PDF processing utilities
- `pdf-to-img.py` - Conversion from PDF to images
- `img2-to-text2.py` - OCR functionality for extracting text from images