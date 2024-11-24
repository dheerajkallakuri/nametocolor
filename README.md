# Name to Color Generator

This project generates a unique color based on a user's name. The color is derived by summing the positions of the letters in the alphabet for each part of the name (first, middle, and last), scaling the values, and mapping them to the RGB and hexadecimal color formats.

Link: https://nametocolor.streamlit.app/

## Features
1. **Name Input**: Accepts the user's first, middle, and last names as input.
2. **Color Generation**: Computes a unique RGB and corresponding hexadecimal color based on the names.
3. **Alphabet-Based Calculation**: Ignores special characters and focuses on the alphabetical characters in the name.
4. **Ensures Valid RGB Values**: The resulting RGB values are always clamped within the valid range of 0-255.

## How It Works
1. **Processing Names**:
   - Each name is converted to lowercase and non-alphabetical characters are removed.
   - The positions of the letters in the alphabet (e.g., `a = 0, z = 25`) are summed for each name.

2. **RGB Value Calculation**:
   - The sums for the first, middle, and last names are multiplied by 4.
   - The resulting values are adjusted using the modulus operator `% 256` to ensure they fall within the range of 0-255.

3. **Color Conversion**:
   - The RGB values are converted into hexadecimal format to represent the color visually.

## Example Usage

For `first_name = "John"`, `middle_name = "Quincy"`, and `last_name = "Doe"`:
```
Hex: #ac4c54
```
<img width="1339" alt="Screenshot 2024-11-23 at 5 33 23 PM" src="https://github.com/user-attachments/assets/d249b5fb-655d-4356-9dde-6767cec2497c">

## Customization
- Modify the scaling factor (currently `4`) to influence the RGB values.
- Enhance the app with additional input validations or features like live color previews using libraries such as Streamlit or Tkinter.

## Use Case
This tool can be used for:
- Visualizing unique name-based colors.
- Generating custom colors for design or personalization purposes.
