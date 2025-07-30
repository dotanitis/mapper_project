# Hex Number Mapper

A Python GUI application that performs linear interpolation mapping of hexadecimal numbers from 8-bit to 10-bit to 16-bit representations.

## Project Description

This application provides a user-friendly interface for:
- Converting hexadecimal numbers between different bit representations (8-bit, 10-bit, 16-bit)
- Performing linear interpolation mapping with configurable ranges
- Real-time updates when values are changed at any step
- Detailed process explanation showing the mathematical calculations

### Features

- **Configurable Ranges**: Set custom min/max values for each bit representation
- **Bidirectional Updates**: Change values at any step (8-bit, 10-bit, or 16-bit) and see automatic updates
- **Dual Input**: Enter values in both hexadecimal and decimal formats
- **Process Visualization**: See the complete linear interpolation formula and calculations
- **Real-time Validation**: Input validation with error handling

### Linear Interpolation Process

The application performs two-stage linear interpolation:
1. **8-bit to 10-bit**: Maps input 8-bit value to 10-bit range using linear interpolation
2. **10-bit to 16-bit**: Maps the resulting 10-bit value to 16-bit range using linear interpolation

Formula: `output = (input - input_min) / (input_max - input_min) * (output_max - output_min) + output_min`

## Setup Instructions

### Prerequisites

- Python 3.6 or higher
- tkinter (usually included with Python)

### Virtual Environment Setup

1. **Create a virtual environment:**
   ```bash
   python -m venv hex_mapper_env
   ```

2. **Activate the virtual environment:**
   
   **On Windows:**
   ```bash
   hex_mapper_env\Scripts\activate
   ```
   
   **On macOS/Linux:**
   ```bash
   source hex_mapper_env/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
   Note: This project uses only built-in Python libraries, so no external packages are required.

### Running the Application

1. **Ensure the virtual environment is activated**

2. **Run the application:**
   ```bash
   python hex_mapper.py
   ```

### Deactivating the Virtual Environment

When you're done using the application:
```bash
deactivate
```

## Usage

1. **Configuration**: 
   - Set the input/output ranges for each bit representation in the Configuration section
   - Default ranges: 8-bit (0-255), 10-bit (0-1023), 16-bit (0-65535)

2. **Input Values**:
   - Enter a hexadecimal value in the 8-bit input field (e.g., "FF", "80", "A0")
   - Or enter a decimal value in the corresponding decimal field
   - Values can also be entered at the 10-bit or 16-bit level

3. **View Results**:
   - See the mapped values update automatically in real-time
   - Review the detailed process explanation at the bottom
   - All calculations and formulas are displayed for transparency

## File Structure

```
mapper_project/
├── hex_mapper.py      # Main GUI application
├── requirements.txt   # Python dependencies (empty - uses built-ins)
└── README.md         # This file
```

## Example

Input: 0x80 (128 decimal) in 8-bit
- Maps to 10-bit: 0x200 (512 decimal) with default ranges
- Maps to 16-bit: 0x8000 (32768 decimal) with default ranges

The process explanation will show the complete mathematical transformation with formulas and intermediate steps.